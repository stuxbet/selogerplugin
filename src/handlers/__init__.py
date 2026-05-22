"""HTTP webhook handlers — thin Flask views over the service layer."""

from .archive import handle_archive
from .delete import handle_delete
from .health import handle_health
from .publish import handle_post
from .update import handle_update

__all__ = [
    "handle_archive",
    "handle_delete",
    "handle_health",
    "handle_post",
    "handle_update",
]
