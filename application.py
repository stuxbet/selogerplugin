"""WSGI entry point for Azure App Service.

Azure's Oryx Python builder looks for ``application:app`` (or ``app:app``)
by default. We expose ``app`` here so the gunicorn invocation can be a
plain ``gunicorn --bind=0.0.0.0:8000 application:app`` with no custom
startup command.

This module also materializes ``tenants.json`` from the ``TENANTS_JSON``
environment variable when present, so the prod deployment can keep the
tenant directory out of git and inject it via Azure App Settings instead.
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path


EMPTY_TENANTS = '{"tenants": {}}'


def _materialize_tenants_json() -> None:
    """Make sure a ``tenants.json`` exists somewhere the loader can find it.

    Resolution order:

    * ``TENANTS_PATH`` set → use it as-is (caller is responsible for the file).
    * ``TENANTS_JSON`` set → write the JSON blob to a tmpfile and point
      ``TENANTS_PATH`` at it. This is how Azure App Settings deliver the
      tenant directory without a file mount.
    * Neither set → write an *empty* tenants file (``{"tenants": {}}``) so
      the Flask app still boots and ``/health`` works as a smoke check.
      The operator then provisions real tenants by setting ``TENANTS_JSON``
      and restarting.
    """

    if os.environ.get("TENANTS_PATH"):
        return
    raw = os.environ.get("TENANTS_JSON", EMPTY_TENANTS)
    try:
        json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"TENANTS_JSON env var is not valid JSON: {exc}") from exc
    fd, path = tempfile.mkstemp(prefix="tenants-", suffix=".json")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(raw)
    os.environ["TENANTS_PATH"] = path


_materialize_tenants_json()

# Importing app last so ``TENANTS_PATH`` is set before the registry loads.
# Use the in-tree import path (no ``seloger.`` prefix) — this module sits at
# the seloger/ repo root, so ``src`` is a sibling package.
from src.app import create_app  # noqa: E402

app = create_app()
