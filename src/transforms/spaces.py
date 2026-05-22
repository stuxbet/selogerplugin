"""Odoo -> AVIV ``space`` block (surfaces and room counts).

Anything the user left at 0 or blank in Odoo is omitted from the payload —
sending ``livingSurface=0`` would be a real claim, and AVIV's portal-level
validators (BD's 20 m² floor) react badly to it.
"""

from __future__ import annotations

from typing import Any

from ..schema import Space


def build_space(template: dict[str, Any]) -> Space | None:
    living = _pos_float(template.get("x_living_surface"))
    total = _pos_float(template.get("x_total_surface"))
    rooms = _pos_int(template.get("x_room_count"))
    bedrooms = _pos_int(template.get("x_bedroom_count"))
    bathrooms = _pos_int(template.get("x_bathroom_count"))

    if not any((living, total, rooms, bedrooms, bathrooms)):
        return None

    return Space(
        livingSurface=living,
        totalSurface=total,
        roomCount=rooms,
        bedroomCount=bedrooms,
        bathroomCount=bathrooms,
    )


def _pos_float(value: Any) -> float | None:
    if value in (None, False, ""):
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if result > 0 else None


def _pos_int(value: Any) -> int | None:
    if value in (None, False, ""):
        return None
    try:
        result = int(value)
    except (TypeError, ValueError):
        return None
    return result if result > 0 else None
