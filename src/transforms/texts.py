"""Odoo -> AVIV headline / description block.

For now this maps:

* product.template.name → AVIV ``data.description`` headline (one-liner)
* product.template.description_sale → AVIV long description, when present

AvivClassified v3.1 also accepts a multilingual ``texts`` block with per-
language headline + description; introduce that here when the seloger
schema starts capturing translated copy.
"""

from __future__ import annotations

from typing import Any


def build_description(template: dict[str, Any]) -> str | None:
    """Compose a description string from the available product.template text fields."""

    parts: list[str] = []
    long_form = (template.get("description_sale")
                 or template.get("description_ecommerce")
                 or template.get("description")
                 or "")
    long_form = str(long_form).strip()
    if long_form:
        parts.append(long_form)

    headline = str(template.get("name") or "").strip()
    if headline and headline not in long_form:
        parts.insert(0, headline)

    if not parts:
        return None
    return "\n\n".join(parts)
