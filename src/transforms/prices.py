"""Odoo -> AVIV ``prices`` block.

The seloger Properties app stores the headline price in
``product.template.list_price``; ``x_distribution_type`` decides whether the
amount belongs in ``buy.price`` or ``rent.baseRent``. BUCOM also needs
``rent.countrySpecific.fr.leaseRight`` ("prix de la cession"); we surface a
helper here so the BUCOM transform can opt in without each handler having
to know about FR-specifics.
"""

from __future__ import annotations

from typing import Any

from ..schema import Amount, BuyPrices, Prices, RentPrices


DEFAULT_CURRENCY = "EUR"


def build_prices(template: dict[str, Any]) -> Prices | None:
    """Return the ``Prices`` block.

    ``None`` when neither a buy nor a rent amount is present (so the calling
    transform can omit the field rather than send an empty object).
    """

    distribution = (template.get("x_distribution_type") or "").upper()
    headline = _amount(template.get("list_price"), template.get("currency_code"))
    if headline is None:
        return None

    if distribution == "RENT":
        return Prices(rent=RentPrices(baseRent=headline))

    # Treat BUY (and anything else) as a sale price by default; the per-portal
    # validator will reject the listing if the distribution type is wrong.
    return Prices(buy=BuyPrices(price=headline))


def attach_lease_right(prices: Prices | None, lease_right_amount: float | None,
                       currency: str = DEFAULT_CURRENCY) -> Prices | None:
    """Stamp ``rent.countrySpecific.fr.leaseRight`` onto an existing block.

    Used by the BUCOM-specific handler. Idempotent — overwrites any existing
    ``leaseRight`` value.
    """

    if lease_right_amount is None:
        return prices
    prices = prices or Prices(rent=RentPrices())
    rent = prices.rent or RentPrices()
    country_specific = dict(rent.countrySpecific or {})
    fr_block = dict(country_specific.get("fr") or {})
    fr_block["leaseRight"] = {"amount": float(lease_right_amount), "currency": currency}
    country_specific["fr"] = fr_block
    rent.countrySpecific = country_specific
    prices.rent = rent
    return prices


def _amount(value: Any, currency: Any) -> Amount | None:
    if value in (None, False, "", 0, 0.0):
        return None
    try:
        amount = float(value)
    except (TypeError, ValueError):
        return None
    if amount <= 0:
        return None
    return Amount(amount=amount, currency=str(currency or DEFAULT_CURRENCY))
