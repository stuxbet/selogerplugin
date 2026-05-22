"""External-service clients used by the seloger connector."""

from .aviv import AvivClient, PROD_BASE_URL, SANDBOX_BASE_URL
from .odoo import OdooClient, OdooClientError

__all__ = [
    "AvivClient",
    "OdooClient",
    "OdooClientError",
    "PROD_BASE_URL",
    "SANDBOX_BASE_URL",
]
