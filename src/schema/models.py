"""Minimal Pydantic models for AvivClassified v3.1 / AvivImmo v2.1.

Hand-written subset scoped to what the transforms actually emit. AVIV's
minor versions add fields silently and our models tolerate unknown keys
(``model_config = ConfigDict(extra="allow")``) — both the inbound side
(``ClassifiedStatusDocument``) and the outbound side (``Classified``).

If you need the full machine-generated tree, run ``datamodel-codegen``
against ``context/aviv-classified-api-v4.json`` and use the result instead
of these models — the field names match.
"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


# Loose base: tolerate unknown fields from minor-version drift.
class _Permissive(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


# ---------------------------------------------------------------------------
# Inputs (outbound) — what we POST/PUT to AVIV
# ---------------------------------------------------------------------------
class Source(_Permissive):
    sourceSystem: str
    sourceSystemVersion: str | None = None
    offererId: str
    offererEstateId: str
    offererEstateNamespace: str | None = None


class MetaData(_Permissive):
    source: Source


class Location(_Permissive):
    street: str | None = None
    houseNumber: str | None = None
    postalCode: str
    city: str
    country: str  # ISO 3166-1 alpha-2
    latitude: float | None = None
    longitude: float | None = None


class Amount(_Permissive):
    amount: float
    currency: str = "EUR"


class BuyPrices(_Permissive):
    price: Amount | None = None


class RentPrices(_Permissive):
    baseRent: Amount | None = None
    countrySpecific: dict[str, Any] | None = None


class Prices(_Permissive):
    buy: BuyPrices | None = None
    rent: RentPrices | None = None


class Space(_Permissive):
    livingSurface: float | None = None
    totalSurface: float | None = None
    roomCount: int | None = None
    bedroomCount: int | None = None
    bathroomCount: int | None = None


class EnergyClass(_Permissive):
    label: str | None = None         # "A".."G"
    value: float | None = None       # kWh/m²/yr (or kgCO2/m²/yr for GHG)
    type: str | None = None          # "DPE" / "GES"


class Energy(_Permissive):
    dpe: EnergyClass | None = None
    ghg: EnergyClass | None = None


class RealEstateData(_Permissive):
    estateType: str
    estateSubType: str | None = None
    distributionType: str  # "BUY" / "RENT"
    location: Location
    prices: Prices | None = None
    space: Space | None = None
    energy: Energy | None = None
    description: str | None = None
    metaData: MetaData


# Media
MediaType = Literal["PICTURE", "VIRTUAL_TOUR", "PANORAMA", "VIDEO"]


class Media(_Permissive):
    url: str
    mediaType: MediaType
    category: str  # one of 34 documented categories; left as str so additions don't break us
    title: str | None = None
    tags: list[str] = Field(default_factory=list)


class Classified(_Permissive):
    """The full payload sent to ``POST /classifieds`` and ``PUT /classifieds/{id}``."""

    portals: list[str]
    data: RealEstateData
    media: list[Media] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Outputs (inbound) — what AVIV returns on /classifieds/{id}/statuses
# ---------------------------------------------------------------------------
class MediaStatus(_Permissive):
    url: str
    status: str  # e.g. DOWNLOADED, DOWNLOADING_FAILED


class PortalStatus(_Permissive):
    portal: str
    status: str
    statusDetails: dict[str, Any] | None = None


class ClassifiedStatus(_Permissive):
    classifiedId: str
    status: str
    portalStatuses: list[PortalStatus] = Field(default_factory=list)
    mediaStatuses: list[MediaStatus] = Field(default_factory=list)
