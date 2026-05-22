"""Odoo gallery -> AVIV ``media`` array.

The diff contract (``context/use-cases.md``): AVIV decides whether to
re-download by URL equality. We therefore bake the Odoo attachment's
``write_date`` into a ``?ts=`` query parameter so the URL changes if and
only if the underlying image was replaced. Removing an attachment from
Odoo removes the URL from the ``media`` array; adding one inserts a new
URL.

Display rules captured here:

* ``media`` is ordered — first picture becomes the cover on the portals.
* Only the first ``VIRTUAL_TOUR`` is displayed.
* Only the first ``VIDEO`` is displayed.

The Odoo gallery doesn't carry per-image category metadata yet, so we
default everything to ``PICTURE`` / ``INDOOR`` and mark the first picture
as ``COVER_PICTURE``. Refine by extending the per-attachment metadata in
Odoo (e.g. a Studio ``x_media_category`` selection on ir.attachment) and
plumbing it through here.
"""

from __future__ import annotations

import re
from datetime import datetime
from typing import Any
from urllib.parse import urlencode, urlsplit, urlunsplit

from ..schema import Media


PICTURE_MIME_RE = re.compile(r"^image/")
DEFAULT_CATEGORY = "INDOOR"
COVER_CATEGORY = "COVER_PICTURE"


def build_media(attachments: list[dict[str, Any]], *, public_base_url: str) -> list[Media]:
    """Convert ir.attachment rows into AVIV ``Media`` records.

    ``public_base_url`` is the externally reachable base URL of the Odoo
    instance (e.g. ``https://acme.odoo.com``). We can't use the API URL
    because AVIV's media fetcher has no credentials; the attachments must be
    served publicly. The caller is responsible for ensuring the relevant
    attachments are ``public=True``.
    """

    media: list[Media] = []
    cover_assigned = False
    for row in attachments:
        if not _is_image(row):
            continue
        url = _resolve_url(row, public_base_url=public_base_url)
        if not url:
            continue
        category = DEFAULT_CATEGORY
        tags = [DEFAULT_CATEGORY]
        if not cover_assigned:
            category = COVER_CATEGORY
            tags = [COVER_CATEGORY]
            cover_assigned = True
        media.append(Media(
            url=url,
            mediaType="PICTURE",
            category=category,
            title=str(row.get("name") or "").strip() or None,
            tags=tags,
        ))
    return media


# ---- internals ---------------------------------------------------------
def _is_image(row: dict[str, Any]) -> bool:
    mimetype = (row.get("mimetype") or "").lower()
    return bool(PICTURE_MIME_RE.match(mimetype))


def _resolve_url(row: dict[str, Any], *, public_base_url: str) -> str | None:
    """Return a fully-qualified public URL with a ``?ts=`` cache-buster."""

    raw_url = (row.get("url") or "").strip()
    if raw_url:
        base = raw_url
    else:
        attachment_id = row.get("id")
        if not attachment_id:
            return None
        base = f"{public_base_url.rstrip('/')}/web/image/{attachment_id}"
    timestamp = _ts(row.get("write_date") or row.get("create_date"))
    parts = urlsplit(base)
    query = parts.query
    sep_query = urlencode({"ts": timestamp}) if timestamp else ""
    if query and sep_query:
        new_query = f"{query}&{sep_query}"
    else:
        new_query = query or sep_query
    return urlunsplit((parts.scheme, parts.netloc, parts.path, new_query, parts.fragment))


def _ts(value: Any) -> str:
    if not value:
        return ""
    # Odoo returns "YYYY-MM-DD HH:MM:SS". Normalize to ISO 8601.
    raw = str(value).strip().replace(" ", "T")
    try:
        # Validate it parses; fall back to the raw string if not.
        datetime.fromisoformat(raw)
    except ValueError:
        return raw
    return raw
