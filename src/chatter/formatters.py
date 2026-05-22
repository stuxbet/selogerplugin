"""HTML chatter formatters.

All formatters return a single string of HTML that Odoo's ``message_post``
accepts. Keep the markup minimal — chatter sanitizes aggressively and any
``<style>`` blocks are stripped.

The trace-parent value is included on every formatter because AVIV's
support runbook (``context/api-overview.md``) directs us to quote it when
opening a ticket; surfacing it inline in the chatter makes it one click
away from the user.
"""

from __future__ import annotations

from html import escape
from typing import Iterable

from ..core.exceptions import AvivAPIError
from ..schema import ClassifiedStatus
from ..services.validation import ValidationIssue


def format_publish_success(*, classified_id: str, traceparent: str,
                            etag: str = "", deduplicated: bool = False) -> str:
    suffix = (
        '<p><em>Existing AVIV listing matched — switched to update.</em></p>'
        if deduplicated else ""
    )
    return _wrap(
        title="✅ SeLoger publish acknowledged",
        rows=[
            ("AVIV Classified ID", classified_id),
            ("Traceparent", traceparent),
            ("ETag", etag),
        ],
        extra=suffix,
    )


def format_validation_failure(issues: Iterable[ValidationIssue]) -> str:
    items = "".join(
        f"<li><strong>[{escape(issue.portal)}] {escape(issue.code)}</strong>: "
        f"{escape(issue.message)}</li>"
        for issue in issues
    )
    return _wrap(
        title="⚠️ SeLoger validation failed",
        rows=[],
        extra=f"<ul>{items}</ul>",
    )


def format_aviv_error(error: AvivAPIError) -> str:
    items = "".join(
        f"<li><code>{escape(str(err.get('name', '')))}</code>: "
        f"{escape(str(err.get('reason', '')))}</li>"
        for err in (error.errors or [])
    )
    error_block = f"<ul>{items}</ul>" if items else ""
    return _wrap(
        title=f"❌ SeLoger publish failed (HTTP {error.status_code})",
        rows=[
            ("Title", error.title),
            ("Detail", error.detail),
            ("Source", error.error_source),
            ("Traceparent", error.traceparent or error.instance),
        ],
        extra=error_block,
    )


def format_status_update(status: ClassifiedStatus, *, traceparent: str = "") -> str:
    rows: list[tuple[str, str]] = [
        ("AVIV Classified ID", status.classifiedId),
        ("Status", status.status),
        ("Traceparent", traceparent),
    ]
    portal_lines = "".join(
        f"<li><strong>{escape(p.portal)}</strong>: {escape(p.status)}</li>"
        for p in status.portalStatuses
    )
    media_failures = [
        m for m in status.mediaStatuses if str(m.status).upper() == "DOWNLOADING_FAILED"
    ]
    extra_blocks: list[str] = []
    if portal_lines:
        extra_blocks.append(f"<p><strong>Portals</strong></p><ul>{portal_lines}</ul>")
    if media_failures:
        bullets = "".join(
            f"<li><code>{escape(m.url)}</code></li>" for m in media_failures
        )
        extra_blocks.append(
            "<p><strong>⚠️ Media downloads failed.</strong> Fix the URL(s) "
            "below and then <em>contact AVIV Customer Care</em> — they need "
            "to reprocess these manually; re-submitting is not enough.</p>"
            f"<ul>{bullets}</ul>"
        )
    return _wrap(
        title="ℹ️ SeLoger status update",
        rows=rows,
        extra="".join(extra_blocks),
    )


# ---- shared building block ------------------------------------------------
def _wrap(*, title: str, rows: Iterable[tuple[str, str]], extra: str = "") -> str:
    body_rows = "".join(
        f"<tr><td><strong>{escape(label)}</strong></td>"
        f"<td><code>{escape(value)}</code></td></tr>"
        for label, value in rows if value
    )
    table = f"<table>{body_rows}</table>" if body_rows else ""
    return f"<p><strong>{escape(title)}</strong></p>{table}{extra}"
