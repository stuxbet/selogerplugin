"""Per-portal validation rules.

Each portal in :data:`PORTAL_VALIDATORS` is a callable
``(classified) -> list[ValidationIssue]``. The orchestrator runs validators
for every portal the tenant subscribes to and aggregates the results; if
any portal fails, the publish/update handler short-circuits before touching
the AVIV API.

Rules sourced from ``context/use-cases.md``:

* ``SL`` resale/rental: address + price + metaData.source (covered by the
  Pydantic schema; we only repeat the price rule because it's
  distribution-type-dependent).
* ``BD``: ≥1 picture, surface ≥20 m² (when present), description ≥160 chars.
* ``BUCOM``: requires ``data.prices.rent.countrySpecific.fr.leaseRight`` and
  ``estateType=TRADING``.
* ``SLN`` / ``SLC``: rules not yet documented — pass-through.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

from ..schema import Classified


@dataclass(frozen=True)
class ValidationIssue:
    """One human-readable rejection reason.

    Surfaced verbatim into the Odoo chatter and the webhook response body.
    """

    portal: str
    code: str
    message: str


# ---------------------------------------------------------------------------
# Portal validators
# ---------------------------------------------------------------------------
def _validate_sl(classified: Classified) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    distribution = (classified.data.distributionType or "").upper()
    prices = classified.data.prices

    if distribution == "BUY":
        amount = getattr(getattr(prices, "buy", None), "price", None)
        if amount is None or amount.amount <= 0:
            issues.append(_issue("SL", "MISSING_BUY_PRICE",
                "Resale listings require a positive sale price (prices.buy.price.amount)."))
    elif distribution == "RENT":
        amount = getattr(getattr(prices, "rent", None), "baseRent", None)
        if amount is None or amount.amount <= 0:
            issues.append(_issue("SL", "MISSING_RENT_AMOUNT",
                "Rental listings require a positive base rent (prices.rent.baseRent.amount)."))
    else:
        issues.append(_issue("SL", "UNKNOWN_DISTRIBUTION",
            f"Unsupported distributionType={distribution!r}; expected BUY or RENT."))
    return issues


def _validate_bd(classified: Classified) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if not classified.media:
        issues.append(_issue("BD", "MISSING_PICTURE",
            "Belles Demeures requires at least one picture."))

    space = classified.data.space
    if space and space.livingSurface is not None and space.livingSurface < 20:
        issues.append(_issue("BD", "SURFACE_TOO_SMALL",
            "Belles Demeures rejects listings with livingSurface < 20 m²."))

    description = (classified.data.description or "").strip()
    if len(description) < 160:
        issues.append(_issue("BD", "DESCRIPTION_TOO_SHORT",
            "Belles Demeures requires a description of at least 160 characters."))
    return issues


def _validate_bucom(classified: Classified) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if classified.data.estateType != "TRADING":
        issues.append(_issue("BUCOM", "WRONG_ESTATE_TYPE",
            "Bureaux & Commerces accepts only estateType=TRADING."))

    rent = getattr(classified.data.prices, "rent", None) if classified.data.prices else None
    country_specific = getattr(rent, "countrySpecific", None) if rent else None
    fr_block = (country_specific or {}).get("fr") if country_specific else None
    if not (fr_block and fr_block.get("leaseRight")):
        issues.append(_issue("BUCOM", "MISSING_LEASE_RIGHT",
            "BUCOM listings require data.prices.rent.countrySpecific.fr.leaseRight (prix de la cession)."))
    return issues


def _validate_pass_through(_: Classified) -> list[ValidationIssue]:
    return []


PORTAL_VALIDATORS: dict[str, Callable[[Classified], list[ValidationIssue]]] = {
    "SL":    _validate_sl,
    "BD":    _validate_bd,
    "BUCOM": _validate_bucom,
    "SLN":   _validate_pass_through,  # docs missing
    "SLC":   _validate_pass_through,  # docs missing
}


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------
def validate(classified: Classified, portals: Iterable[str]) -> list[ValidationIssue]:
    """Run every portal validator the tenant subscribes to.

    Returns a flat list of issues across all portals; an empty list means
    the listing is ready to send.
    """

    issues: list[ValidationIssue] = []
    for portal in portals:
        validator = PORTAL_VALIDATORS.get(portal, _validate_pass_through)
        issues.extend(validator(classified))
    return issues


# ---- internals ---------------------------------------------------------
def _issue(portal: str, code: str, message: str) -> ValidationIssue:
    return ValidationIssue(portal=portal, code=code, message=message)
