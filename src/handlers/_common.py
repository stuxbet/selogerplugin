"""Shared helpers used by every webhook handler.

The handler files (publish.py, update.py, archive.py, delete.py) stay thin
on purpose — the heavy lifting lives in ``ListingService``. Cross-cutting
glue (template-id parsing, chatter writing, response building) lives here
so the per-action files read in one screen.
"""

from __future__ import annotations

from typing import Any

from flask import Response, jsonify, request

from ..chatter import (
    format_aviv_error,
    format_publish_success,
    format_validation_failure,
)
from ..clients.aviv import AvivClient
from ..clients.odoo import OdooClient
from ..core.auth import AvivCredentials, TokenCache
from ..core.exceptions import (
    AvivAPIError,
    TenantNotFound,
    ValidationError,
)
from ..core.tenant import Tenant, TenantRegistry
from ..services.listing import ListingService, PublishOutcome


def extract_template_id(payload: dict[str, Any] | None) -> int:
    """Pull the product.template id out of the webhook body.

    Odoo's ``ir.actions.server`` webhook posts a JSON list of "records",
    each with at least an ``id``. Some Odoo versions wrap it under
    ``params.records``; tolerate both shapes.
    """

    if not payload:
        raise ValidationError("missing webhook payload")
    records = payload.get("records")
    if not records and "params" in payload:
        records = (payload.get("params") or {}).get("records")
    if not records or not isinstance(records, list):
        raise ValidationError("webhook payload missing 'records' list")
    first = records[0]
    if not isinstance(first, dict) or "id" not in first:
        raise ValidationError("webhook payload first record has no id")
    try:
        return int(first["id"])
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"non-integer record id: {first['id']!r}") from exc


def resolve_tenant_from_request() -> Tenant:
    """Resolve the tenant from the ``?identifier=`` query param.

    Uses the app-injected ``TENANT_REGISTRY`` so tests can wire a stub
    registry without monkey-patching the module-level singleton.
    """

    from flask import current_app
    identifier = request.args.get("identifier")
    if not identifier:
        raise TenantNotFound("missing 'identifier' query parameter")
    registry: TenantRegistry = current_app.config["TENANT_REGISTRY"]
    return registry.get(identifier)


def build_listing_service(*, tenant: Tenant, credentials: AvivCredentials,
                          token_cache: TokenCache, public_base_url: str,
                          aviv_base_url: str) -> ListingService:
    odoo = OdooClient.for_tenant(tenant.odoo)
    aviv = AvivClient.for_intermediary(
        credentials=credentials,
        intermediary_id=tenant.aviv.intermediary_id,
        base_url=aviv_base_url,
        token_cache=token_cache,
    )
    return ListingService(
        tenant=tenant,
        odoo=odoo,
        aviv=aviv,
        public_base_url=public_base_url,
    )


def write_chatter_for_outcome(svc: ListingService, *, template_id: int,
                               outcome: PublishOutcome,
                               success_title_overrides: dict[str, str] | None = None) -> None:
    """Post a single chatter message reflecting an outcome."""

    if outcome.issues:
        body = format_validation_failure(outcome.issues)
    elif outcome.aviv_error:
        body = format_aviv_error(outcome.aviv_error)
    else:
        body = format_publish_success(
            classified_id=outcome.classified_id,
            traceparent=outcome.traceparent,
            etag=outcome.etag,
            deduplicated=outcome.duplicate,
        )
    try:
        svc.odoo.post_message(template_id, body)
    except Exception:  # pragma: no cover — chatter is best-effort
        # The webhook response still tells the user something useful even
        # if Odoo refuses the chatter (e.g. permission issue).
        pass


def outcome_response(outcome: PublishOutcome) -> Response:
    """Translate an outcome into the JSON webhook response."""

    if outcome.issues:
        payload = {
            "status": "validation_error",
            "issues": [
                {"portal": i.portal, "code": i.code, "message": i.message}
                for i in outcome.issues
            ],
        }
        return jsonify(payload), 422

    if outcome.aviv_error:
        err = outcome.aviv_error
        payload = {
            "status": "aviv_error",
            "aviv_status": err.status_code,
            "title": err.title,
            "detail": err.detail,
            "errors": err.errors,
            "traceparent": err.traceparent or err.instance,
        }
        return jsonify(payload), 502

    return jsonify({
        "status": "ok",
        "classified_id": outcome.classified_id,
        "traceparent": outcome.traceparent,
        "etag": outcome.etag,
        "deduplicated": outcome.duplicate,
    }), 200
