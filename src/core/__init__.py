"""Core primitives shared by every layer of the connector."""

from .exceptions import (
    AvivAPIError,
    CollidingContacts,
    ConfigError,
    ConnectorError,
    DuplicatedClassified,
    PreconditionFailed,
    TenantNotFound,
    TooManyRequests,
    ValidationError,
)
from .auth import (
    AvivCredentials,
    CachedToken,
    TokenCache,
    request_token,
)
from .tenant import (
    AvivConfig,
    OdooConfig,
    Tenant,
    TenantRegistry,
    registry,
    resolve,
)

__all__ = [
    "AvivAPIError",
    "AvivConfig",
    "AvivCredentials",
    "CachedToken",
    "CollidingContacts",
    "ConfigError",
    "ConnectorError",
    "DuplicatedClassified",
    "OdooConfig",
    "PreconditionFailed",
    "Tenant",
    "TenantNotFound",
    "TenantRegistry",
    "TokenCache",
    "TooManyRequests",
    "ValidationError",
    "registry",
    "request_token",
    "resolve",
]
