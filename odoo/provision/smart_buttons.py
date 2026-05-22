"""Smart-button provisioning for seloger.

Installs four webhook-type server actions on ``product.template`` and injects
a button block into the base ``product.template`` form view. Clicking a
button fires an HTTP POST to the configured webhook URL, which is handled by
the seloger Flask server in ``seloger/src/app.py``.

Marker convention: the injected XML is wrapped in
``<!-- SELOGER_BUTTONS_START -->`` / ``<!-- SELOGER_BUTTONS_END -->`` so
reruns can locate and replace the block without disturbing other edits to
the same view.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlencode, urlsplit, urlunsplit

from .client import OdooClient
from .views import ensure_inherited_view, find_view_id


# ---------------------------------------------------------------------------
# Server-action specs
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class ServerActionSpec:
    """A webhook-backed server action that drives one smart button."""

    name: str        # ir.actions.server.name (stable identifier on reruns)
    label: str       # button caption shown in the form view
    path: str        # path appended to the webhook base URL (e.g. "/post")


SERVER_ACTION_SPECS: tuple[ServerActionSpec, ...] = (
    ServerActionSpec(name="Seloger: Post Listing",    label="Post Listing",    path="/post"),
    ServerActionSpec(name="Seloger: Update Listing",  label="Update Listing",  path="/update"),
    ServerActionSpec(name="Seloger: Archive Listing", label="Archive Listing", path="/archive"),
    ServerActionSpec(name="Seloger: Delete Listing",  label="Delete Listing",  path="/delete"),
)

# Fields sent in the webhook payload (Odoo populates these from the record).
WEBHOOK_FIELD_NAMES: tuple[str, ...] = ("id", "name")


# ---------------------------------------------------------------------------
# Form-view button block
# ---------------------------------------------------------------------------
BUTTON_BLOCK_MARKER_START = "<!-- SELOGER_BUTTONS_START -->"
BUTTON_BLOCK_MARKER_END = "<!-- SELOGER_BUTTONS_END -->"
BUTTON_BLOCK_RE = re.compile(
    r"\s*<!-- SELOGER_BUTTONS_START -->.*?<!-- SELOGER_BUTTONS_END -->",
    flags=re.DOTALL,
)
INHERITED_VIEW_KEY = "seloger.product_template.smart_buttons"
INHERITED_VIEW_NAME = "Seloger: product.template smart buttons"


# ---------------------------------------------------------------------------
# Webhook URL builder
# ---------------------------------------------------------------------------
_WEBHOOK_SUFFIXES = ("/post", "/update", "/archive", "/delete")


def _normalize_webhook_base(url: str | None) -> str:
    """Return the app base URL even if WEBHOOK_URL already points at /post."""

    if not url:
        return ""
    parts = urlsplit(url)
    normalized = urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip("/"), "", ""))
    for suffix in _WEBHOOK_SUFFIXES:
        if normalized.endswith(suffix):
            return normalized[: -len(suffix)]
    return normalized


def _build_webhook_url(base_url: str, path: str, identifier: str | None) -> str:
    cleaned = _normalize_webhook_base(base_url).rstrip("/")
    if not cleaned:
        return ""
    query = urlencode({"identifier": identifier}) if identifier else ""
    return urlunsplit(("", "", f"{cleaned}/{path.lstrip('/')}", query, ""))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _resolve_field_ids(client: OdooClient, model: str, field_names: tuple[str, ...]) -> list[int]:
    rows = client.search_read(
        "ir.model.fields",
        [("model", "=", model), ("name", "in", list(field_names))],
        ["id", "name"], limit=0,
    )
    by_name = {row["name"]: row["id"] for row in rows}
    missing = [name for name in field_names if name not in by_name]
    if missing:
        raise RuntimeError(
            f"webhook payload references unknown product.template fields: {missing}. "
            "Make sure bootstrap_properties_app and the rest of provisioning ran first."
        )
    return [by_name[name] for name in field_names]


def ensure_server_actions(client: OdooClient, *, model_id: int, webhook_base_url: str,
                          webhook_identifier: str | None) -> dict[str, int]:
    """Create/update the four webhook server actions. Returns name → id."""

    field_ids = _resolve_field_ids(client, "product.template", WEBHOOK_FIELD_NAMES)
    names = [spec.name for spec in SERVER_ACTION_SPECS]
    existing = client.search_read(
        "ir.actions.server",
        [("name", "in", names)],
        ["id", "name", "state", "binding_type", "webhook_url", "webhook_field_ids", "model_id"],
        limit=0,
    )
    by_name = {row["name"]: row for row in existing}
    action_ids: dict[str, int] = {}

    for spec in SERVER_ACTION_SPECS:
        webhook_url = _build_webhook_url(webhook_base_url, spec.path, webhook_identifier)
        desired: dict[str, Any] = {
            "name": spec.name,
            "model_id": model_id,
            "binding_model_id": model_id,
            "binding_type": "action",
            "state": "webhook",
            "webhook_url": webhook_url,
            "webhook_field_ids": [[6, 0, field_ids]],
        }
        row = by_name.get(spec.name)
        if not row:
            action_id = client.create("ir.actions.server", desired)
            print(f"  CREATE action {spec.name!r} id={action_id}")
            print(f"           URL: {webhook_url}")
            action_ids[spec.name] = action_id
            continue

        action_id = row["id"]
        action_ids[spec.name] = action_id
        delta: dict[str, Any] = {}
        if row.get("state") != "webhook":
            delta["state"] = "webhook"
        if row.get("binding_type") != "action":
            delta["binding_type"] = "action"
        if row.get("webhook_url") != webhook_url:
            delta["webhook_url"] = webhook_url
        live_model = row.get("model_id")
        live_model_id = live_model[0] if isinstance(live_model, list) else live_model
        if live_model_id != model_id:
            delta["model_id"] = model_id
            delta["binding_model_id"] = model_id
        live_fields = sorted(row.get("webhook_field_ids") or [])
        if live_fields != sorted(field_ids):
            delta["webhook_field_ids"] = [[6, 0, field_ids]]
        if delta:
            client.write("ir.actions.server", [action_id], delta)
            print(f"  UPDATE action {spec.name!r} {list(delta)}")
        else:
            print(f"  OK     action {spec.name!r}")
    return action_ids


def _render_button_block(action_ids_by_name: dict[str, int]) -> str:
    lines = [f"            {BUTTON_BLOCK_MARKER_START}"]
    for spec in SERVER_ACTION_SPECS:
        action_id = action_ids_by_name[spec.name]
        lines.append(
            f'            <button string="{spec.label}" type="action" name="{action_id}"/>'
        )
    lines.append(f"            {BUTTON_BLOCK_MARKER_END}")
    return "\n".join(lines)


def ensure_button_block_view(client: OdooClient, *, parent_view_id: int,
                              action_ids_by_name: dict[str, int]) -> int:
    """Inject the button block into the product.template form via an inherited view."""

    block_xml = _render_button_block(action_ids_by_name)
    arch = (
        "<data>\n"
        "    <xpath expr=\"//sheet\" position=\"before\">\n"
        "        <header>\n"
        f"{block_xml}\n"
        "        </header>\n"
        "    </xpath>\n"
        "</data>"
    )
    return ensure_inherited_view(
        client,
        key=INHERITED_VIEW_KEY,
        name=INHERITED_VIEW_NAME,
        model="product.template",
        view_type="form",
        parent_view_id=parent_view_id,
        arch=arch,
        priority=20,
    )


def ensure_smart_buttons(client: OdooClient, *, webhook_base_url: str,
                         webhook_identifier: str | None) -> dict[str, int]:
    """High-level entry point used by ``provision_database.py``.

    Creates the four webhook server actions, looks up the base
    ``product.template`` form view, and installs the inherited view that
    injects the button block above the sheet header.
    """

    print(f"\n--- Smart-button server actions ---")
    if not webhook_base_url:
        print("  WARN  WEBHOOK_URL is empty; actions will be created with no URL.")
    model_id = client.get_model_id("product.template")
    action_ids = ensure_server_actions(
        client,
        model_id=model_id,
        webhook_base_url=webhook_base_url,
        webhook_identifier=webhook_identifier,
    )

    print(f"\n--- Form button block ---")
    parent_view_id = find_view_id(client, "product.template", "form",
                                  name="product.template.product.form")
    if parent_view_id is None:
        parent_view_id = find_view_id(client, "product.template", "form")
    if parent_view_id is None:
        raise RuntimeError("No product.template form view found to inherit from.")
    ensure_button_block_view(client, parent_view_id=parent_view_id,
                             action_ids_by_name=action_ids)
    return action_ids
