"""Odoo -> AVIV ``countrySpecific.fr`` block.

The BUCOM-required ``leaseRight`` is already handled in
``transforms.prices.attach_lease_right``; this module hosts the other
France-specific keys (risks, ``commercial.specialOffer``, copropriété
metadata) when those columns are introduced.
"""

from __future__ import annotations

from typing import Any


def build_country_specific_fr(template: dict[str, Any]) -> dict[str, Any] | None:
    return None
