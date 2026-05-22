"""GET /health — liveness probe."""

from __future__ import annotations

from flask import Response, current_app, jsonify

from ..core.tenant import registry


def handle_health() -> Response:
    try:
        tenant_count = len(registry().all())
    except Exception as exc:  # pragma: no cover — startup-only failure
        return jsonify({"status": "degraded", "detail": str(exc)}), 503
    return jsonify({
        "status": "ok",
        "tenants": tenant_count,
        "aviv_base_url": current_app.config.get("AVIV_BASE_URL"),
    }), 200
