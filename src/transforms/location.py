"""Odoo -> AVIV ``location`` block."""

from __future__ import annotations

from typing import Any

from ..core.country_codes import odoo_to_aviv_country
from ..schema import Location


def build_location(template: dict[str, Any]) -> Location | None:
    """Return an AVIV ``Location`` from a product.template row.

    Returns ``None`` when none of the mandatory address fields are populated;
    the per-portal validator will reject the listing later with a clearer
    message than a Pydantic schema error.
    """

    postal = (template.get("x_postal_code") or "").strip()
    city = (template.get("x_city") or "").strip()
    country = odoo_to_aviv_country(template.get("x_country_code"))
    if not (postal and city and country):
        return None
    return Location(
        street=_nonempty(template.get("x_street")),
        houseNumber=_nonempty(template.get("x_house_number")),
        postalCode=postal,
        city=city,
        country=country,
    )


def _nonempty(value: Any) -> str | None:
    if value is None or value is False:
        return None
    s = str(value).strip()
    return s or None
