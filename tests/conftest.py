"""Shared pytest fixtures (mocked clients, tenants, fake Odoo records)."""

from __future__ import annotations

import pytest

from seloger.src.core.auth import AvivCredentials, TokenCache
from seloger.src.core.tenant import AvivConfig, OdooConfig, Tenant


@pytest.fixture
def tenant() -> Tenant:
    return Tenant(
        key="tk_test",
        name="Test Agency",
        odoo=OdooConfig(
            base_url="https://example.odoo.com",
            api_key="test-key",
            database="example",
        ),
        aviv=AvivConfig(
            intermediary_id="intermed-1",
            offerer_id="offerer-1",
            portals=("SL",),
        ),
    )


@pytest.fixture
def credentials() -> AvivCredentials:
    return AvivCredentials(
        client_id="cid",
        client_secret="csec",
        audience="https://api.aviv-group.com/sandbox/caas/v4",
        user_agent="SelogerConnector/test",
    )


@pytest.fixture
def token_cache() -> TokenCache:
    return TokenCache()


@pytest.fixture
def base_template() -> dict:
    """A product.template row with all fields the transforms care about."""

    return {
        "id": 42,
        "name": "Charming 3-bedroom apartment in central Paris",
        "list_price": 850000.0,
        "currency_id": [1, "EUR"],
        "x_is_properties": True,
        "x_status": "available",
        "x_distribution_type": "BUY",
        "x_property_type": "APARTMENT",
        "x_street": "Rue de Rivoli",
        "x_house_number": "12",
        "x_postal_code": "75001",
        "x_city": "Paris",
        "x_country_code": "FR",
        "x_living_surface": 78.5,
        "x_total_surface": 82.0,
        "x_room_count": 3,
        "x_bedroom_count": 2,
        "x_bathroom_count": 1,
        "x_dpe_class": "C",
        "x_ges_class": "D",
        "x_aviv_listing_id": False,
        "description_sale": "A bright apartment renovated in 2024. " * 12,
    }


@pytest.fixture
def base_attachments() -> list[dict]:
    return [
        {
            "id": 1, "name": "front.jpg", "mimetype": "image/jpeg",
            "checksum": "abc", "write_date": "2026-04-10 09:00:00",
            "public": True, "url": False,
        },
        {
            "id": 2, "name": "kitchen.jpg", "mimetype": "image/jpeg",
            "checksum": "def", "write_date": "2026-04-10 09:05:00",
            "public": True, "url": False,
        },
    ]
