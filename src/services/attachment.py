"""Attachment service — fetch the public, ordered image list for a template.

The real work happens inside ``transforms.media.build_media``; this service
exists to keep the Odoo I/O out of the transform itself so the transform
remains a pure function over already-fetched data.
"""

from __future__ import annotations

from typing import Any

from ..clients.odoo import OdooClient


def fetch_attachments(client: OdooClient, *, template_id: int) -> list[dict[str, Any]]:
    """Return ir.attachment rows for a product.template, ordered for AVIV.

    Ordering rule: by ``id`` ascending. Odoo's website module stores its
    gallery order in a related ``product.image`` model when available, but
    the starter Properties app doesn't enable that — so we fall back to
    insertion order, which is what the user implicitly expects from "first
    image becomes cover."
    """

    rows = client.read_attachments(res_id=template_id)
    rows.sort(key=lambda row: row.get("id", 0))
    return rows
