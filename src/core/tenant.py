"""Tenant configuration loader.

``tenants.json`` is the source of truth for who can call the webhook server.
Each tenant carries its Odoo connection details, the AVIV-issued
``intermediary_id`` / ``offerer_id``, and the list of portals it publishes
to. The file is read once on app startup; ``reload()`` swaps the cache
atomically.
"""

from __future__ import annotations

import json
import os
import threading
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .exceptions import ConfigError, TenantNotFound


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_TENANTS_PATH = REPO_ROOT / "seloger" / "tenants.json"


@dataclass(frozen=True)
class OdooConfig:
    base_url: str
    api_key: str
    database: str


@dataclass(frozen=True)
class AvivConfig:
    """Per-tenant AVIV identity. Client id/secret stay in env vars (one set
    per integrator); ``intermediary_id`` and ``offerer_id`` are the
    agency-scoped values issued by AVIV during onboarding."""

    intermediary_id: str
    offerer_id: str
    portals: tuple[str, ...]


@dataclass(frozen=True)
class Tenant:
    key: str
    name: str
    odoo: OdooConfig
    aviv: AvivConfig


class TenantRegistry:
    """Thread-safe in-memory cache of tenants. Atomic ``reload()``."""

    def __init__(self, path: Path | str | None = None):
        self.path = Path(path) if path else DEFAULT_TENANTS_PATH
        self._lock = threading.Lock()
        self._tenants: dict[str, Tenant] = {}

    def load(self) -> None:
        if not self.path.is_file():
            raise ConfigError(f"tenants file not found: {self.path}")
        try:
            payload = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ConfigError(f"tenants file is not valid JSON: {exc}") from exc

        raw = payload.get("tenants", {})
        if not isinstance(raw, dict):
            raise ConfigError("tenants.json must contain a top-level 'tenants' object")

        new_cache: dict[str, Tenant] = {}
        for key, body in raw.items():
            new_cache[key] = _build_tenant(key, body)
        with self._lock:
            self._tenants = new_cache

    def reload(self) -> None:
        self.load()

    def get(self, key: str) -> Tenant:
        with self._lock:
            tenant = self._tenants.get(key)
        if tenant is None:
            raise TenantNotFound(f"no tenant registered for key {key!r}")
        return tenant

    def all(self) -> tuple[Tenant, ...]:
        with self._lock:
            return tuple(self._tenants.values())


def _build_tenant(key: str, body: dict[str, Any]) -> Tenant:
    if not isinstance(body, dict):
        raise ConfigError(f"tenant {key!r}: payload must be an object")

    name = str(body.get("name", "")).strip()
    odoo_raw = body.get("odoo") or {}
    aviv_raw = body.get("aviv") or {}

    try:
        odoo = OdooConfig(
            base_url=str(odoo_raw["base_url"]).rstrip("/"),
            api_key=str(odoo_raw["api_key"]),
            database=str(odoo_raw["database"]),
        )
    except KeyError as exc:
        raise ConfigError(f"tenant {key!r}: missing odoo.{exc.args[0]}") from exc

    portals = aviv_raw.get("portals") or ()
    if not isinstance(portals, (list, tuple)):
        raise ConfigError(f"tenant {key!r}: aviv.portals must be a list")
    try:
        aviv = AvivConfig(
            intermediary_id=str(aviv_raw["intermediary_id"]),
            offerer_id=str(aviv_raw["offerer_id"]),
            portals=tuple(str(p) for p in portals),
        )
    except KeyError as exc:
        raise ConfigError(f"tenant {key!r}: missing aviv.{exc.args[0]}") from exc

    return Tenant(key=key, name=name, odoo=odoo, aviv=aviv)


_REGISTRY: TenantRegistry | None = None


def registry() -> TenantRegistry:
    """Process-wide singleton, lazily loaded from ``TENANTS_PATH`` env or default."""

    global _REGISTRY
    if _REGISTRY is None:
        path_env = os.environ.get("TENANTS_PATH")
        _REGISTRY = TenantRegistry(path_env or DEFAULT_TENANTS_PATH)
        _REGISTRY.load()
    return _REGISTRY


def resolve(identifier: str | None) -> Tenant:
    """Translate a webhook ``identifier`` query param into a Tenant."""

    if not identifier:
        raise TenantNotFound("missing 'identifier' query parameter")
    return registry().get(identifier)
