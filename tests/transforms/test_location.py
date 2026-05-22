from __future__ import annotations

from seloger.src.transforms.location import build_location


def test_full_address_round_trips(base_template):
    location = build_location(base_template)
    assert location is not None
    assert location.postalCode == "75001"
    assert location.city == "Paris"
    assert location.country == "FR"
    assert location.street == "Rue de Rivoli"
    assert location.houseNumber == "12"


def test_returns_none_when_required_fields_missing(base_template):
    base_template["x_city"] = ""
    assert build_location(base_template) is None


def test_country_code_normalized_to_upper(base_template):
    base_template["x_country_code"] = "fr"
    assert build_location(base_template).country == "FR"
