"""Flask app factory and routing for the seloger connector.

The factory keeps every dependency injectable so unit tests build their own
``app`` without touching the filesystem. ``main()`` is the prod entry point —
it loads ``.env``, builds the app, and starts the status-poller background
thread.
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Any

from flask import Flask, Response, current_app, jsonify, request

from .chatter import format_status_update
from .clients.aviv import AvivClient, PROD_BASE_URL, SANDBOX_BASE_URL
from .clients.odoo import OdooClient
from .core.auth import AvivCredentials, TokenCache
from .core.exceptions import ConfigError
from .core.tenant import TenantRegistry, Tenant, registry
from .handlers import (
    handle_archive,
    handle_delete,
    handle_health,
    handle_post,
    handle_update,
)
from .schema import ClassifiedStatus
from .services.status_poller import StatusPoller


log = logging.getLogger("seloger.app")


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ENV_PATH = REPO_ROOT / "seloger" / ".env"


# ---------------------------------------------------------------------------
# Environment + factory
# ---------------------------------------------------------------------------
def load_dotenv(path: Path | None = None) -> None:
    target = path or DEFAULT_ENV_PATH
    if not target.is_file():
        return
    for raw in target.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def _resolve_aviv_base_url() -> str:
    explicit = os.environ.get("AVIV_API_BASE_URL", "").strip().rstrip("/")
    if explicit:
        return explicit
    audience = os.environ.get("AVIV_AUDIENCE", "").strip().rstrip("/")
    if audience:
        return audience
    return SANDBOX_BASE_URL


def _credentials_from_env() -> AvivCredentials:
    return AvivCredentials(
        client_id=os.environ.get("AVIV_CLIENT_ID", ""),
        client_secret=os.environ.get("AVIV_CLIENT_SECRET", ""),
        audience=os.environ.get("AVIV_AUDIENCE", _resolve_aviv_base_url()),
        user_agent=os.environ.get("AVIV_USER_AGENT", "SelogerConnector/0.1.0 Python/3.11"),
    )


def create_app(*, credentials: AvivCredentials | None = None,
                tenant_registry: TenantRegistry | None = None,
                aviv_base_url: str | None = None,
                token_cache: TokenCache | None = None,
                poller: StatusPoller | None = None) -> Flask:
    """Build a configured Flask app. All deps are injectable for tests."""

    app = Flask("seloger-connector")
    app.url_map.strict_slashes = False
    logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))

    # Tenant registry — load now so config errors fail fast on startup.
    if tenant_registry is None:
        try:
            tenant_registry = registry()
        except ConfigError as exc:
            log.error("failed to load tenants: %s", exc)
            raise

    # Config keys consumed by the handler module.
    app.config["TENANT_REGISTRY"] = tenant_registry
    app.config["AVIV_CREDENTIALS"] = credentials or _credentials_from_env()
    app.config["AVIV_BASE_URL"] = aviv_base_url or _resolve_aviv_base_url()
    app.config["AVIV_TOKEN_CACHE"] = token_cache or TokenCache()
    app.config["STATUS_POLLER"] = poller

    _register_routes(app)
    return app


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
def _register_routes(app: Flask) -> None:
    app.add_url_rule("/health",  view_func=handle_health,  methods=["GET"])
    app.add_url_rule("/post",    view_func=handle_post,    methods=["POST"])
    app.add_url_rule("/update",  view_func=handle_update,  methods=["POST"])
    app.add_url_rule("/archive", view_func=handle_archive, methods=["POST"])
    app.add_url_rule("/delete",  view_func=handle_delete,  methods=["POST"])
    app.add_url_rule("/aviv/status", view_func=handle_aviv_status_webhook,
                     methods=["POST"])


def handle_aviv_status_webhook() -> Response:
    """Receive AVIV's outbound status callbacks.

    Signature verification is left as a TODO until AVIV documents the
    mechanism (see ``context/README.md`` open question 5). For now we trust
    the source and rely on the network boundary + an obscure URL path.
    """

    payload = request.get_json(silent=True) or {}
    try:
        status_doc = ClassifiedStatus.model_validate(payload)
    except Exception as exc:
        return jsonify({"status": "invalid_payload", "detail": str(exc)}), 400

    tenant_key = request.args.get("identifier")
    if not tenant_key:
        return jsonify({"status": "missing_identifier"}), 400
    try:
        tenant = current_app.config["TENANT_REGISTRY"].get(tenant_key)
    except Exception:
        return jsonify({"status": "unknown_tenant"}), 404

    template_id = _resolve_template_for_classified(tenant, status_doc.classifiedId)
    if not template_id:
        return jsonify({"status": "no_matching_template"}), 200  # benign no-op

    odoo = OdooClient.for_tenant(tenant.odoo)
    body = format_status_update(status_doc, traceparent=request.headers.get("traceparent", ""))
    try:
        odoo.post_message(template_id, body)
    except Exception as exc:  # pragma: no cover — chatter is best-effort
        log.warning("status webhook: chatter post failed: %s", exc)

    return jsonify({"status": "ok"}), 200


def _resolve_template_for_classified(tenant: Tenant, classified_id: str) -> int | None:
    """Find the product.template id that owns ``classified_id``."""

    odoo = OdooClient.for_tenant(tenant.odoo)
    rows = odoo.search_read(
        "product.template",
        [("x_aviv_listing_id", "=", classified_id)],
        ["id"],
        limit=1,
    )
    return rows[0]["id"] if rows else None


# ---------------------------------------------------------------------------
# Prod entry point
# ---------------------------------------------------------------------------
def main() -> None:
    load_dotenv()
    poller = _build_poller()
    app = create_app(poller=poller)
    if poller:
        poller.start()
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)


def _build_poller() -> StatusPoller | None:
    """Wire a status poller if the feature flag is enabled."""

    if os.environ.get("ENABLE_STATUS_POLLER", "true").lower() != "true":
        return None
    credentials = _credentials_from_env()
    base_url = _resolve_aviv_base_url()
    cache = TokenCache()

    def aviv_factory(t: Tenant) -> AvivClient:
        return AvivClient.for_intermediary(
            credentials=credentials,
            intermediary_id=t.aviv.intermediary_id,
            base_url=base_url,
            token_cache=cache,
        )

    def odoo_factory(t: Tenant) -> OdooClient:
        return OdooClient.for_tenant(t.odoo)

    def notify(t: Tenant, odoo: OdooClient, template_id: int,
               status: ClassifiedStatus) -> None:
        body = format_status_update(status)
        odoo.post_message(template_id, body)

    return StatusPoller(
        aviv_factory=aviv_factory,
        odoo_factory=odoo_factory,
        notify=notify,
        poll_interval_seconds=float(os.environ.get("STATUS_POLL_INTERVAL_SECONDS", "30")),
    )


if __name__ == "__main__":  # pragma: no cover
    main()
