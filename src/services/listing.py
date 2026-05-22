"""Listing service — orchestrates fetch → transform → validate → submit.

The handlers in ``src/handlers/*`` call into ``ListingService`` rather than
talking to AVIV directly. Putting the orchestration here lets the unit
tests cover the publish / update / archive / delete flows without spinning
up a Flask app, and keeps the handlers thin enough to read in one screen.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..clients.aviv import AvivClient
from ..clients.odoo import OdooClient
from ..core.exceptions import (
    AvivAPIError,
    DuplicatedClassified,
    PreconditionFailed,
    ValidationError,
)
from ..core.tenant import Tenant
from ..schema import Classified
from ..transforms import build_classified
from .attachment import fetch_attachments
from .validation import ValidationIssue, validate


# Subset of product.template columns we read for every operation. Keeping
# this explicit lets us add fields without surprising the network footprint.
TEMPLATE_FIELDS: tuple[str, ...] = (
    "id",
    "name",
    "description_sale",
    "list_price",
    "currency_id",
    "x_is_properties",
    "x_status",
    "x_distribution_type",
    "x_property_type",
    "x_street",
    "x_house_number",
    "x_postal_code",
    "x_city",
    "x_country_code",
    "x_living_surface",
    "x_total_surface",
    "x_room_count",
    "x_bedroom_count",
    "x_bathroom_count",
    "x_dpe_class",
    "x_ges_class",
    "x_aviv_listing_id",
    "x_is_published_seloger",
)


@dataclass
class PublishOutcome:
    """Result returned by every state-changing operation.

    The handler turns this into the JSON body of the webhook response and
    into the Odoo chatter message. ``issues`` carries pre-flight validation
    failures (no AVIV call was made); ``aviv_error`` carries a failure
    returned by AVIV itself.
    """

    classified_id: str = ""
    traceparent: str = ""
    issues: list[ValidationIssue] | None = None
    aviv_error: AvivAPIError | None = None
    duplicate: bool = False  # POST hit Duplicated Classified and fell back to PUT
    etag: str = ""


@dataclass
class ListingService:
    tenant: Tenant
    odoo: OdooClient
    aviv: AvivClient
    public_base_url: str         # Odoo URL exposed for attachment fetch
    source_system: str = "SelogerConnector"
    source_system_version: str = "0.1.0"

    # ------------------------------------------------------------------
    # State-changing flows
    # ------------------------------------------------------------------
    def publish(self, template_id: int) -> PublishOutcome:
        classified = self._build_payload(template_id)
        issues = validate(classified, self.tenant.aviv.portals)
        if issues:
            return PublishOutcome(issues=issues)

        payload = classified.model_dump(exclude_none=True)
        try:
            classified_id, traceparent = self.aviv.post_classified(payload)
        except DuplicatedClassified as exc:
            # Idempotency contract from context/api-overview.md: POST against
            # an existing offererEstateId falls back to GET → PUT.
            existing_id = exc.existing_classified_id or self._find_existing_id(template_id)
            if not existing_id:
                return PublishOutcome(aviv_error=exc, traceparent=exc.traceparent)
            outcome = self._update(existing_id, classified)
            outcome.duplicate = True
            return outcome
        except AvivAPIError as exc:
            return PublishOutcome(aviv_error=exc, traceparent=exc.traceparent)

        self._stash_listing_id(template_id, classified_id, published=True)
        return PublishOutcome(classified_id=classified_id, traceparent=traceparent)

    def update(self, template_id: int) -> PublishOutcome:
        classified = self._build_payload(template_id)
        issues = validate(classified, self.tenant.aviv.portals)
        if issues:
            return PublishOutcome(issues=issues)

        classified_id = self._require_listing_id(template_id)
        return self._update(classified_id, classified)

    def archive(self, template_id: int) -> PublishOutcome:
        """Soft-disable a listing by switching availability to OFF_MARKET and PUT-ing."""

        classified_id = self._require_listing_id(template_id)
        classified = self._build_payload(template_id)
        # Force-flip the management block to OFF_MARKET regardless of the
        # current Odoo status — archive means "take it off the portals."
        classified.data.management = {"availability": "OFF_MARKET"}  # type: ignore[attr-defined]
        outcome = self._update(classified_id, classified)
        if not outcome.aviv_error:
            self.odoo.write_template(template_id, {"x_is_published_seloger": False})
        return outcome

    def delete(self, template_id: int) -> PublishOutcome:
        classified_id = self._require_listing_id(template_id)
        try:
            # Best-effort: try to fetch the current ETag for the optional
            # If-Match header. Some AVIV deployments accept DELETE without it.
            etag = ""
            try:
                _, etag, _ = self.aviv.get_classified(classified_id)
            except AvivAPIError:
                pass
            traceparent = self.aviv.delete_classified(classified_id, etag=etag)
        except AvivAPIError as exc:
            return PublishOutcome(aviv_error=exc, traceparent=exc.traceparent)
        self.odoo.write_template(template_id, {
            "x_is_published_seloger": False,
            "x_aviv_listing_id": False,
        })
        return PublishOutcome(classified_id=classified_id, traceparent=traceparent)

    # ------------------------------------------------------------------
    # Read-only flows
    # ------------------------------------------------------------------
    def fetch_status(self, template_id: int) -> tuple[dict[str, Any], str]:
        classified_id = self._require_listing_id(template_id)
        body, traceparent = self.aviv.get_statuses(classified_id)
        return body, traceparent

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------
    def _build_payload(self, template_id: int) -> Classified:
        template = self.odoo.read_template(template_id, list(TEMPLATE_FIELDS))
        attachments = fetch_attachments(self.odoo, template_id=template_id)
        try:
            return build_classified(
                template,
                attachments,
                self.tenant,
                public_base_url=self.public_base_url,
                source_system=self.source_system,
                source_system_version=self.source_system_version,
            )
        except ValueError as exc:
            raise ValidationError(str(exc)) from exc

    def _update(self, classified_id: str, classified: Classified) -> PublishOutcome:
        """GET → PUT with If-Match, retrying once on 412."""

        payload = classified.model_dump(exclude_none=True)
        for attempt in (1, 2):
            try:
                _, etag, _ = self.aviv.get_classified(classified_id)
            except AvivAPIError as exc:
                return PublishOutcome(aviv_error=exc, traceparent=exc.traceparent,
                                       classified_id=classified_id)
            try:
                traceparent = self.aviv.put_classified(classified_id, payload, etag)
                return PublishOutcome(classified_id=classified_id,
                                       traceparent=traceparent, etag=etag)
            except PreconditionFailed as exc:
                if attempt == 2:
                    return PublishOutcome(aviv_error=exc, traceparent=exc.traceparent,
                                           classified_id=classified_id)
                # else: refetch the ETag and retry once.
                continue
            except AvivAPIError as exc:
                return PublishOutcome(aviv_error=exc, traceparent=exc.traceparent,
                                       classified_id=classified_id)

        # Unreachable — kept for type-checker satisfaction.
        return PublishOutcome(classified_id=classified_id)

    def _require_listing_id(self, template_id: int) -> str:
        template = self.odoo.read_template(template_id, ["x_aviv_listing_id"])
        existing = template.get("x_aviv_listing_id") or ""
        if not existing:
            raise ValidationError(
                "Listing has no AVIV id yet — publish it before updating/archiving/deleting."
            )
        return str(existing)

    def _find_existing_id(self, template_id: int) -> str | None:
        template = self.odoo.read_template(template_id, ["x_aviv_listing_id"])
        return template.get("x_aviv_listing_id") or None

    def _stash_listing_id(self, template_id: int, classified_id: str, *,
                          published: bool) -> None:
        self.odoo.write_template(template_id, {
            "x_aviv_listing_id": classified_id,
            "x_is_published_seloger": published,
        })
