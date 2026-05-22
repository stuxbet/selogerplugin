from __future__ import annotations

from seloger.src.transforms import build_classified


def test_full_pipeline_emits_valid_payload(base_template, base_attachments, tenant):
    classified = build_classified(
        base_template,
        base_attachments,
        tenant,
        public_base_url="https://example.odoo.com",
    )
    dumped = classified.model_dump(exclude_none=True)
    assert dumped["portals"] == ["SL"]
    assert dumped["data"]["distributionType"] == "BUY"
    assert dumped["data"]["location"]["postalCode"] == "75001"
    assert dumped["data"]["metaData"]["source"]["offererEstateId"] == "42"
    assert dumped["data"]["prices"]["buy"]["price"]["amount"] == 850000.0
    assert dumped["media"][0]["category"] == "COVER_PICTURE"


def test_missing_address_raises(base_template, base_attachments, tenant):
    base_template["x_postal_code"] = ""
    import pytest
    with pytest.raises(ValueError):
        build_classified(base_template, base_attachments, tenant,
                          public_base_url="https://example.odoo.com")
