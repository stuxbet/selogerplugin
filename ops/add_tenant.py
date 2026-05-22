"""Interactive bootstrap: register a new tenant in ``tenants.json``.

Usage:
    python -m seloger.ops.add_tenant

The script reads the existing tenants file (creates one if missing), asks
for the new tenant's Odoo + AVIV details, mints a fresh tenant key, and
writes the result back. Existing tenants are left untouched.
"""

from __future__ import annotations

import json
import os
import secrets
from pathlib import Path
from typing import Any

from seloger.src.core.tenant import DEFAULT_TENANTS_PATH


def _ask(prompt: str, *, default: str = "", required: bool = True) -> str:
    while True:
        suffix = f" [{default}]" if default else ""
        value = input(f"{prompt}{suffix}: ").strip()
        if not value and default:
            value = default
        if value or not required:
            return value
        print("  (required) — please answer.")


def _ask_list(prompt: str, *, default: tuple[str, ...]) -> list[str]:
    suggestion = ",".join(default)
    raw = input(f"{prompt} [{suggestion}]: ").strip()
    if not raw:
        return list(default)
    return [item.strip() for item in raw.split(",") if item.strip()]


def _mint_key(existing: dict[str, Any]) -> str:
    while True:
        key = "tk_" + secrets.token_hex(32)
        if key not in existing:
            return key


def _load(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {"tenants": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def _save(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")


def main() -> int:
    target = Path(os.environ.get("TENANTS_PATH") or DEFAULT_TENANTS_PATH)
    state = _load(target)
    tenants = state.setdefault("tenants", {})
    print(f"Adding a tenant to {target} (current count: {len(tenants)})\n")

    name = _ask("Tenant name (display only)")
    odoo_url = _ask("Odoo base URL", default="https://example.odoo.com")
    odoo_db = _ask("Odoo database")
    odoo_key = _ask("Odoo API key")
    intermediary_id = _ask("AVIV intermediary_id")
    offerer_id = _ask("AVIV offerer_id")
    portals = _ask_list("Portals (comma-separated)", default=("SL",))

    key = _mint_key(tenants)
    tenants[key] = {
        "name": name,
        "odoo": {
            "base_url": odoo_url.rstrip("/"),
            "api_key": odoo_key,
            "database": odoo_db,
        },
        "aviv": {
            "intermediary_id": intermediary_id,
            "offerer_id": offerer_id,
            "portals": portals,
        },
    }
    _save(target, state)

    print()
    print(f"Registered tenant {name!r} at key:\n\n  {key}\n")
    print("Configure the seloger smart buttons in Odoo so each webhook URL")
    print(f"appends ?identifier={key}.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
