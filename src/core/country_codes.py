"""Mapping between the Odoo ``x_country_code`` selection keys (ISO 3166-1
alpha-2) and the AVIV-accepted country codes.

AVIV's OpenAPI accepts ISO 3166-1 alpha-2 for ``location.country``, so the
mapping is currently the identity — but the function exists as a clear seam
for future remapping (e.g. if AVIV switches to alpha-3).
"""

from __future__ import annotations

# Countries the seloger Properties app currently lets the user pick (see
# ``odoo/provision/field_specs.py``). Used both for validation (reject
# unknown ISO codes) and to surface a stable allow-list to the transforms.
SUPPORTED_COUNTRIES: frozenset[str] = frozenset({"FR", "BE", "LU", "CH", "MC"})


def odoo_to_aviv_country(code: str | None) -> str | None:
    """Normalize an Odoo country code into the AVIV-accepted form.

    Returns ``None`` if the input is empty so the calling transform can decide
    whether to leave the field unset or raise a validation error.
    """

    if not code:
        return None
    normalized = code.strip().upper()
    return normalized or None
