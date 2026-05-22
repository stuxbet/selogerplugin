"""POST /update — push an Odoo edit into an existing AVIV classified."""

from __future__ import annotations

from flask import Response, current_app, jsonify, request

from ..core.exceptions import ConfigError, TenantNotFound, ValidationError
from ._common import (
    build_listing_service,
    extract_template_id,
    outcome_response,
    resolve_tenant_from_request,
    write_chatter_for_outcome,
)


def handle_update() -> Response:
    try:
        tenant = resolve_tenant_from_request()
        template_id = extract_template_id(request.get_json(silent=True))
    except TenantNotFound as exc:
        return jsonify({"status": "tenant_not_found", "detail": str(exc)}), 404
    except ValidationError as exc:
        return jsonify({"status": "bad_request", "detail": str(exc)}), 400

    try:
        svc = build_listing_service(
            tenant=tenant,
            credentials=current_app.config["AVIV_CREDENTIALS"],
            token_cache=current_app.config["AVIV_TOKEN_CACHE"],
            public_base_url=tenant.odoo.base_url,
            aviv_base_url=current_app.config["AVIV_BASE_URL"],
        )
        outcome = svc.update(template_id)
    except ConfigError as exc:
        return jsonify({"status": "config_error", "detail": str(exc)}), 503
    except ValidationError as exc:
        return jsonify({"status": "validation_error", "detail": str(exc)}), 422

    write_chatter_for_outcome(svc, template_id=template_id, outcome=outcome)
    return outcome_response(outcome)
