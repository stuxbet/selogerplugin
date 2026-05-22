"""Idempotent ``ir.ui.view`` helpers.

These helpers manage two view-related concerns the provisioning scripts care
about:

* Standalone "primary" views (no ``inherit_id``) — used for the Properties
  app's custom kanban / list / search.
* Inherited views (with ``inherit_id``) — used to inject the Custom-fields
  notebook page and the smart-button block into the existing
  ``product.template`` form.

Each view is identified by its ``name``; on rerun we detect drift via the
``arch_db`` payload and rewrite only when needed.
"""

from __future__ import annotations

from typing import Any

from .client import OdooClient


def ensure_primary_view(client: OdooClient, *, name: str, model: str, view_type: str,
                        arch: str, priority: int = 50) -> int:
    """Create or update a standalone view by ``name``.

    The view's ``arch_db`` is compared to ``arch`` and only rewritten on
    drift. Returns the view id.
    """

    existing = client.search_read(
        "ir.ui.view",
        [("name", "=", name), ("model", "=", model), ("inherit_id", "=", False)],
        ["id", "type", "priority", "arch_db"],
        limit=1,
    )
    if not existing:
        view_id = client.create("ir.ui.view", {
            "name": name,
            "model": model,
            "type": view_type,
            "priority": priority,
            "arch_db": arch,
        })
        print(f"  CREATE view {name!r} id={view_id} type={view_type}")
        return view_id

    row = existing[0]
    delta: dict[str, Any] = {}
    if row.get("priority") != priority:
        delta["priority"] = priority
    if (row.get("arch_db") or "").strip() != arch.strip():
        delta["arch_db"] = arch
    if delta:
        client.write("ir.ui.view", [row["id"]], delta)
        print(f"  UPDATE view {name!r} {list(delta)}")
    else:
        print(f"  OK     view {name!r}")
    return row["id"]


def ensure_inherited_view(client: OdooClient, *, key: str, model: str, view_type: str,
                          parent_view_id: int, arch: str, name: str | None = None,
                          priority: int = 16) -> int:
    """Create or update an inherited view, keyed by its ``key``.

    ``key`` (the dotted XML id-style key, not a regular XML id) is the stable
    identifier we use to find the row on reruns. ``parent_view_id`` is the
    target view's id (e.g. the base ``product.template`` form).
    """

    existing = client.search_read(
        "ir.ui.view",
        [("key", "=", key)],
        ["id", "name", "model", "type", "priority", "inherit_id", "arch_db"],
        limit=1,
    )
    if not existing:
        view_id = client.create("ir.ui.view", {
            "name": name or key,
            "model": model,
            "type": view_type,
            "key": key,
            "priority": priority,
            "inherit_id": parent_view_id,
            "arch_db": arch,
        })
        print(f"  CREATE inherited view {key!r} id={view_id}")
        return view_id

    row = existing[0]
    delta: dict[str, Any] = {}
    if name and row.get("name") != name:
        delta["name"] = name
    if row.get("priority") != priority:
        delta["priority"] = priority
    inherit_id = row.get("inherit_id")
    current_parent = inherit_id[0] if isinstance(inherit_id, list) else inherit_id
    if current_parent != parent_view_id:
        delta["inherit_id"] = parent_view_id
    if (row.get("arch_db") or "").strip() != arch.strip():
        delta["arch_db"] = arch
    if delta:
        client.write("ir.ui.view", [row["id"]], delta)
        print(f"  UPDATE inherited view {key!r} {list(delta)}")
    else:
        print(f"  OK     inherited view {key!r}")
    return row["id"]


def find_view_id(client: OdooClient, model: str, view_type: str,
                 name: str | None = None) -> int | None:
    """Locate a base view (no inherit_id) by model + type and optionally name."""

    domain: list = [
        ("model", "=", model),
        ("type", "=", view_type),
        ("inherit_id", "=", False),
    ]
    if name:
        domain.append(("name", "=", name))
    rows = client.search_read("ir.ui.view", domain, ["id", "name", "priority"],
                              limit=1 if name else 0)
    if not rows:
        return None
    if name:
        return rows[0]["id"]
    # Without an explicit name, pick the lowest-priority (most generic) match.
    rows.sort(key=lambda r: (r.get("priority", 100), r["id"]))
    return rows[0]["id"]
