from __future__ import annotations

from seloger.src.transforms.prices import attach_lease_right, build_prices


def test_buy_distribution_emits_buy_price(base_template):
    prices = build_prices(base_template)
    assert prices.buy is not None
    assert prices.buy.price.amount == 850000.0
    assert prices.rent is None


def test_rent_distribution_emits_base_rent(base_template):
    base_template["x_distribution_type"] = "RENT"
    base_template["list_price"] = 1500
    prices = build_prices(base_template)
    assert prices.rent is not None
    assert prices.rent.baseRent.amount == 1500
    assert prices.buy is None


def test_zero_price_returns_none(base_template):
    base_template["list_price"] = 0
    assert build_prices(base_template) is None


def test_lease_right_attaches_under_country_specific(base_template):
    prices = build_prices(base_template)
    updated = attach_lease_right(prices, 25000.0)
    assert updated.rent.countrySpecific["fr"]["leaseRight"]["amount"] == 25000.0
