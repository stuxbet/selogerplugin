"""Place seloger fields on the product.template form via a 'Seloger' tab.

The tab is injected through an inherited view (so the base form's Studio /
core layout stays untouched) and groups fields by the categories defined in
``field_specs.ALL_FIELD_GROUPS``.
"""

from __future__ import annotations

from collections.abc import Mapping
from xml.sax.saxutils import escape

from .client import OdooClient
from .field_specs import ALL_FIELD_GROUPS
from .views import ensure_inherited_view


INHERITED_VIEW_KEY = "seloger.product_template.notebook_page"
INHERITED_VIEW_NAME = "Seloger: product.template notebook page"
NOTEBOOK_PAGE_NAME = "seloger"
NOTEBOOK_PAGE_STRING = "Seloger"


def _group_string(label: str | Mapping[str, str]) -> str:
    # Group strings in inherited views are not stored as JSONB in the same way
    # field labels are — we render the English variant here and Odoo will pick
    # up the per-locale value from view translations once the user enables them
    # via the standard "Translate" UI.
    if isinstance(label, Mapping):
        return label.get("en_US") or next(iter(label.values()), "")
    return label or ""


def _render_group(label: str | Mapping[str, str], field_names: tuple[str, ...]) -> str:
    if not field_names:
        return ""
    lines = [f'                <group string="{escape(_group_string(label))}">']
    for name in field_names:
        lines.append(f'                    <field name="{escape(name)}"/>')
    lines.append("                </group>")
    return "\n".join(lines)


def _render_arch() -> str:
    group_xml: list[str] = []
    for label, specs in ALL_FIELD_GROUPS:
        names = tuple(spec.name for spec in specs)
        rendered = _render_group(label, names)
        if rendered:
            group_xml.append(rendered)
    body = "\n".join(group_xml) if group_xml else (
        '                <group/>  <!-- no seloger fields configured yet -->'
    )
    return (
        "<data>\n"
        '    <xpath expr="//sheet//notebook" position="inside">\n'
        f'        <page string="{escape(NOTEBOOK_PAGE_STRING)}" name="{NOTEBOOK_PAGE_NAME}">\n'
        f"{body}\n"
        "        </page>\n"
        "    </xpath>\n"
        "</data>"
    )


def ensure_notebook_page(client: OdooClient, *, parent_view_id: int) -> int:
    arch = _render_arch()
    return ensure_inherited_view(
        client,
        key=INHERITED_VIEW_KEY,
        name=INHERITED_VIEW_NAME,
        model="product.template",
        view_type="form",
        parent_view_id=parent_view_id,
        arch=arch,
        priority=18,
    )
