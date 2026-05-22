"""Compose per-section transforms into a complete AVIV ``Classified`` payload."""

from __future__ import annotations

from typing import Any

from ..core.tenant import Tenant
from ..schema import (
    Classified,
    MetaData,
    RealEstateData,
    Source,
)
from .building_property import build_building_property
from .country_specific_fr import build_country_specific_fr
from .energy import build_energy
from .features import build_features
from .location import build_location
from .management import build_management
from .media import build_media
from .prices import attach_lease_right, build_prices
from .spaces import build_space
from .structure import build_structure
from .texts import build_description


SOURCE_SYSTEM_DEFAULT = "SelogerConnector"
SOURCE_SYSTEM_VERSION_DEFAULT = "0.1.0"


def build_classified(
    template: dict[str, Any],
    attachments: list[dict[str, Any]],
    tenant: Tenant,
    *,
    public_base_url: str,
    source_system: str = SOURCE_SYSTEM_DEFAULT,
    source_system_version: str = SOURCE_SYSTEM_VERSION_DEFAULT,
) -> Classified:
    """Turn an Odoo product.template + its attachments into an AVIV payload.

    The result is what the publish handler POSTs (or PUTs) directly. Sections
    that don't have data on this template simply aren't included — AVIV's
    schema treats them as optional unless the per-portal validator says
    otherwise.
    """

    location = build_location(template)
    if location is None:
        # Pydantic requires a Location to build RealEstateData. Surface a
        # cleaner error than a schema validation failure: the listing-service
        # validator will catch this before we reach this point in production.
        raise ValueError(
            "Cannot build AVIV payload: missing required address fields "
            "(x_postal_code / x_city / x_country_code)."
        )

    metadata = MetaData(
        source=Source(
            sourceSystem=source_system,
            sourceSystemVersion=source_system_version,
            offererId=tenant.aviv.offerer_id,
            offererEstateId=str(template["id"]),
            offererEstateNamespace=tenant.odoo.database,
        )
    )

    real_estate = RealEstateData(
        estateType=_estate_type(template),
        estateSubType=template.get("x_estate_subtype") or None,
        distributionType=(template.get("x_distribution_type") or "BUY").upper(),
        location=location,
        prices=build_prices(template),
        space=build_space(template),
        energy=build_energy(template),
        description=build_description(template),
        metaData=metadata,
    )

    # Optional blocks — set as ``extra`` keys via attribute assignment because
    # Pydantic's ``extra="allow"`` mirrors them onto ``model_dump()``.
    for attr, value in (
        ("structure", build_structure(template)),
        ("features", build_features(template)),
        ("management", build_management(template)),
        ("buildingProperty", build_building_property(template)),
        ("countrySpecificFr", build_country_specific_fr(template)),
    ):
        if value is not None:
            setattr(real_estate, attr, value)

    media = build_media(attachments, public_base_url=public_base_url)
    classified = Classified(
        portals=list(tenant.aviv.portals),
        data=real_estate,
        media=media,
    )
    return classified


def attach_bucom_lease_right(classified: Classified, lease_right_amount: float) -> Classified:
    """Stamp ``data.prices.rent.countrySpecific.fr.leaseRight`` (BUCOM)."""

    classified.data.prices = attach_lease_right(classified.data.prices, lease_right_amount)
    return classified


# ---- helpers -------------------------------------------------------------
def _estate_type(template: dict[str, Any]) -> str:
    """Derive AVIV ``estateType`` from the property-type selection.

    AVIV's estate types are coarser than the Odoo selection; HOUSE/APARTMENT
    map to ``RESIDENTIAL`` for resale/rental flows, OFFICE/TRADING map to
    their own buckets. Keep this minimal — the per-portal validator does the
    hard work of rejecting unsupported combinations.
    """

    property_type = (template.get("x_property_type") or "").upper()
    return {
        "HOUSE": "HOUSE",
        "APARTMENT": "APARTMENT",
        "OFFICE": "OFFICE",
        "PARKING": "PARKING",
        "LAND": "LAND",
    }.get(property_type, "HOUSE")


__all__ = [
    "attach_bucom_lease_right",
    "build_classified",
    "build_building_property",
    "build_country_specific_fr",
    "build_description",
    "build_energy",
    "build_features",
    "build_location",
    "build_management",
    "build_media",
    "build_prices",
    "build_space",
    "build_structure",
]
