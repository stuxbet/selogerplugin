"""Odoo -> AVIV ``management`` block (availability, sold/rented state).

The seloger Properties app stores listing state in ``x_status``; map it to
AVIV's availability enum so portals reflect the right "Available / Sold /
Rented / Off market" badge.
"""

from __future__ import annotations

from typing import Any


# Odoo x_status -> AVIV availability code. AVIV only documents these in the
# prose use-cases doc — extend the table as we encounter more states.
_STATUS_MAP = {
    "available":  "AVAILABLE",
    "rented":     "RENTED",
    "sold":       "SOLD",
    "off_market": "OFF_MARKET",
}


def build_management(template: dict[str, Any]) -> dict[str, Any] | None:
    status = (template.get("x_status") or "").strip().lower()
    aviv_status = _STATUS_MAP.get(status)
    if not aviv_status:
        return None
    return {"availability": aviv_status}
