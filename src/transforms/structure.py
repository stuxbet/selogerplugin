"""Odoo -> AVIV ``structure`` block (rooms / kitchen / parking lots).

Placeholder: the starter field set doesn't capture these concepts yet. Add
Odoo fields (e.g. ``x_kitchen_type``, ``x_parking_lot_count``) and a
``build_structure`` body when they exist. The orchestrator skips ``None``
returns, so this stays out of the payload until then.
"""

from __future__ import annotations

from typing import Any


def build_structure(template: dict[str, Any]) -> dict[str, Any] | None:
    return None
