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


def _materialize_tenants_json() -> None:
    """If ``TENANTS_JSON`` is set, write it to a tmpfile and point the loader at it.

    Lets Azure App Settings carry the JSON blob without ever touching the
    filesystem from git. ``TENANTS_PATH`` is respected if explicitly set —
    that wins.
    """

    if os.environ.get("TENANTS_PATH"):
        return
    raw = os.environ.get("TENANTS_JSON")
    if not raw:
        return
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
