from __future__ import annotations

from seloger.src.services.validation import validate
from seloger.src.transforms import build_classified


def _build(tmpl, attachments, tenant):
    return build_classified(tmpl, attachments, tenant,
                             public_base_url="https://example.odoo.com")


def test_sl_resale_happy_path(base_template, base_attachments, tenant):
    classified = _build(base_template, base_attachments, tenant)
    assert validate(classified, ["SL"]) == []


def test_sl_rejects_zero_buy_price(base_template, base_attachments, tenant):
    classified = _build(base_template, base_attachments, tenant)
    classified.data.prices.buy.price.amount = 0
    issues = validate(classified, ["SL"])
    assert any(i.code == "MISSING_BUY_PRICE" for i in issues)


def test_bd_rejects_when_no_media(base_template, tenant):
    classified = _build(base_template, [], tenant)
    issues = validate(classified, ["BD"])
    assert any(i.code == "MISSING_PICTURE" for i in issues)


def test_bd_rejects_short_description(base_template, base_attachments, tenant):
    base_template["description_sale"] = "too short"
    classified = _build(base_template, base_attachments, tenant)
    issues = validate(classified, ["BD"])
    assert any(i.code == "DESCRIPTION_TOO_SHORT" for i in issues)


def test_bucom_requires_lease_right(base_template, base_attachments, tenant):
    classified = _build(base_template, base_attachments, tenant)
    issues = validate(classified, ["BUCOM"])
    # estate type wrong AND lease right missing
    codes = {i.code for i in issues}
    assert "WRONG_ESTATE_TYPE" in codes
    assert "MISSING_LEASE_RIGHT" in codes
