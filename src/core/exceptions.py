"""Exception hierarchy used across the seloger connector.

The split mirrors the failure modes we surface to chatter and to webhook
callers: configuration errors are programmer-facing, validation errors are
listing-author-facing, and ``AvivAPIError`` carries the RFC 7807 payload
AVIV returns so we can serialize it verbatim into the Odoo log message.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


class ConnectorError(Exception):
    """Base class for every connector-raised exception."""


class ConfigError(ConnectorError):
    """Missing or malformed env var / tenants.json entry."""


class TenantNotFound(ConnectorError):
    """The webhook ``identifier`` does not resolve to a known tenant."""


class ValidationError(ConnectorError):
    """A pre-flight validation rule (Pydantic or per-portal) rejected the listing."""

    def __init__(self, message: str, errors: list[dict[str, Any]] | None = None):
        super().__init__(message)
        self.errors = errors or []


@dataclass
class AvivAPIError(ConnectorError):
    """Raised when AVIV returns a 4xx/5xx response.

    Carries the RFC 7807 payload (``type``/``title``/``detail``/``errors``)
    and the W3C ``traceparent`` so the chatter formatter can include the
    support reference.
    """

    status_code: int
    title: str = ""
    detail: str = ""
    instance: str = ""             # AVIV mirrors traceparent here
    traceparent: str = ""          # response header value
    errors: list[dict[str, Any]] = field(default_factory=list)
    error_source: str = ""
    raw_body: str = ""

    def __str__(self) -> str:  # pragma: no cover — debugging aid
        parts = [f"AVIV {self.status_code}"]
        if self.title:
            parts.append(self.title)
        if self.detail:
            parts.append(self.detail)
        if self.errors:
            parts.append(f"({len(self.errors)} validation error(s))")
        return " | ".join(parts)


class DuplicatedClassified(AvivAPIError):
    """``offererEstateId`` already used; the existing ``classifiedId`` is in ``existing_classified_id``."""

    existing_classified_id: str | None = None


class PreconditionFailed(AvivAPIError):
    """PUT with stale ``If-Match`` — caller should refetch the ETag and retry."""


class CollidingContacts(AvivAPIError):
    """Both generic and SeLoger-specific contact blocks were sent."""


class TooManyRequests(AvivAPIError):
    """429 — back off and retry. ``retry_after_seconds`` is populated when present."""

    retry_after_seconds: float | None = None
