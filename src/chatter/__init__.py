"""HTML chatter formatters for the seloger connector.

Each function returns ready-to-post HTML for the Odoo ``message_post`` call.
Keep the markup minimal and self-contained — chatter renders inside a
restricted iframe and rejects ``<style>`` blocks.
"""

from .formatters import (
    format_aviv_error,
    format_publish_success,
    format_status_update,
    format_validation_failure,
)

__all__ = [
    "format_aviv_error",
    "format_publish_success",
    "format_status_update",
    "format_validation_failure",
]
