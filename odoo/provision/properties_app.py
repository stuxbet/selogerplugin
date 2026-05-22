"""Idempotent provisioning of the Properties app on ``product.template``.

What this module installs (mirrors the layout of the seloger dev database):

* Manual product.template fields used by the app: ``x_is_properties``,
  ``x_status``, ``x_owner_id``, ``x_acheteur_id``.
* Three standalone views — kanban / list / search — keyed by the same
  ``product.template.properties.{kanban,list,search}`` names used in dev.
* An ``ir.actions.act_window`` titled per ``ACTION_LABEL`` (defaults to
  "Properties") that filters product.template by ``x_is_properties``.
* The window-action's three view-binding rows (kanban → list → form).
* A top-level menu entry that opens the action.

Every step is keyed by name + model so reruns reconcile rather than
duplicate. The form view is left as Odoo's default product.template form;
the smart-button block (and any custom-fields notebook page) is added by
``provision_database.py`` later.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from .client import OdooClient
from .fields import FieldSpec, SelectionOption, ensure_field_with_options
from .views import ensure_primary_view


# ---------------------------------------------------------------------------
# Field definitions used by the Properties app's views and action defaults.
# ---------------------------------------------------------------------------
def _t(en: str, fr: str) -> dict[str, str]:
    return {"en_US": en, "fr_FR": fr}


PROPERTIES_APP_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name="x_is_properties",
        ttype="boolean",
        label=_t("Is a Property", "Est un bien immobilier"),
        help=_t(
            "Flags this product.template as a real-estate listing, so it shows up "
            "in the Properties app instead of the default product catalogue.",
            "Marque ce product.template comme une annonce immobilière, afin qu'il "
            "apparaisse dans l'application Properties plutôt que dans le catalogue produit.",
        ),
    ),
    FieldSpec(
        name="x_status",
        ttype="selection",
        label=_t("Status", "Statut"),
        selection=(
            SelectionOption("available",  _t("Available",   "Disponible"),  0),
            SelectionOption("rented",     _t("Rented",      "Loué"),        1),
            SelectionOption("sold",       _t("Sold",        "Vendu"),       2),
            SelectionOption("off_market", _t("Off Market",  "Hors marché"), 3),
        ),
    ),
    FieldSpec(
        name="x_owner_id",
        ttype="many2one",
        label=_t("Owner", "Propriétaire"),
        relation="res.partner",
    ),
    FieldSpec(
        name="x_acheteur_id",
        ttype="many2one",
        label=_t("Buyer", "Acheteur"),
        relation="res.partner",
    ),
)


# ---------------------------------------------------------------------------
# View arches (verbatim ports of the dev database).
# ---------------------------------------------------------------------------
KANBAN_VIEW_NAME = "product.template.properties.kanban"
LIST_VIEW_NAME = "product.template.properties.list"
SEARCH_VIEW_NAME = "product.template.properties.search"

KANBAN_ARCH = """<kanban>
    <templates>
        <t t-name="card">
            <div class="d-flex justify-content-between align-items-start">
                <strong><field name="name"/></strong>
                <field name="x_status" widget="label_selection" options="{'classes': {'available': 'success', 'rented': 'warning', 'sold': 'info', 'off_market': 'secondary'}}"/>
            </div>
            <div class="text-muted small mt-1">
                </div>
            <div class="mt-2">
                <strong><field name="list_price" widget="monetary"/></strong>
            </div>
        </t>
    </templates>
</kanban>"""

LIST_ARCH = """<list string="Properties" decoration-success="x_status == 'available'" decoration-warning="x_status == 'rented'" decoration-muted="x_status == 'off_market'" decoration-info="x_status == 'sold'">
    <field name="name"/>
    <field name="x_owner_id"/>
    <field name="list_price"/>
    <field name="x_status" widget="badge" decoration-success="x_status == 'available'" decoration-warning="x_status == 'rented'" decoration-info="x_status == 'sold'" decoration-muted="x_status == 'off_market'"/>
</list>"""

SEARCH_ARCH = """<search>
    <field name="name"/>
    <field name="x_owner_id"/>
    <filter name="filter_available" string="Disponibles" domain="[('x_status','=','available')]"/>
    <filter name="filter_rented" string="Loués" domain="[('x_status','=','rented')]"/>
    <filter name="filter_sold" string="Vendus" domain="[('x_status','=','sold')]"/>
    <filter name="filter_off_market" string="Hors marché" domain="[('x_status','=','off_market')]"/>
    <separator/>
    <filter name="group_status" string="Statut" context="{'group_by': 'x_status'}"/>
    <filter name="group_owner" string="Propriétaire" context="{'group_by': 'x_owner_id'}"/>
</search>"""


# ---------------------------------------------------------------------------
# Action + menu
# ---------------------------------------------------------------------------
ACTION_LABEL = "Properties"
MENU_LABEL = "Properties"
ACTION_DOMAIN = "[('x_is_properties', '=', True)]"
ACTION_CONTEXT = {
    "default_x_is_properties": True,
    "default_x_status": "available",
}
ACTION_HELP = (
    '<p class="o_view_nocontent_smiling_face">Ajoutez votre premier bien immobilier</p>'
    "<p>Créez et gérez vos biens immobiliers depuis cet espace.</p>"
)
ACTION_VIEW_MODE = "kanban,list,form"
MENU_SEQUENCE = 2


@dataclass
class PropertiesAppIds:
    field_ids: dict[str, int]
    kanban_view_id: int
    list_view_id: int
    search_view_id: int
    action_id: int
    menu_id: int


def _ensure_act_window(client: OdooClient, *, label: str, kanban_view_id: int,
                       list_view_id: int, search_view_id: int) -> int:
    """Create or update the Properties window action."""

    existing = client.search_read(
        "ir.actions.act_window",
        [("res_model", "=", "product.template"), ("name", "=", label)],
        ["id", "view_mode", "domain", "context", "help", "search_view_id"],
        limit=1,
    )
    desired: dict[str, Any] = {
        "name": label,
        "res_model": "product.template",
        "view_mode": ACTION_VIEW_MODE,
        "domain": ACTION_DOMAIN,
        "context": json.dumps(ACTION_CONTEXT).replace('"', "'"),
        "help": ACTION_HELP,
        "search_view_id": search_view_id,
    }
    if not existing:
        action_id = client.create("ir.actions.act_window", desired)
        print(f"  CREATE action {label!r} id={action_id}")
    else:
        row = existing[0]
        action_id = row["id"]
        delta: dict[str, Any] = {}
        for key in ("view_mode", "domain", "help"):
            if row.get(key) != desired[key]:
                delta[key] = desired[key]
        # search_view_id comes back as [id, name]
        current_search = row.get("search_view_id")
        current_search_id = current_search[0] if isinstance(current_search, list) else current_search
        if current_search_id != search_view_id:
            delta["search_view_id"] = search_view_id
        # The context round-trips through Odoo and we don't always control quoting;
        # treat both forms as equivalent.
        live_ctx = (row.get("context") or "").replace('"', "'").strip()
        if live_ctx != desired["context"].strip():
            delta["context"] = desired["context"]
        if delta:
            client.write("ir.actions.act_window", [action_id], delta)
            print(f"  UPDATE action {label!r} {list(delta)}")
        else:
            print(f"  OK     action {label!r}")

    # Reconcile the explicit view bindings (act_window.view rows).
    _ensure_action_view_bindings(client, action_id, kanban_view_id, list_view_id)
    return action_id


def _ensure_action_view_bindings(client: OdooClient, action_id: int,
                                 kanban_view_id: int, list_view_id: int) -> None:
    """Ensure kanban→1, list→2, form→3 view-mode rows are bound to the action."""

    existing = client.search_read(
        "ir.actions.act_window.view",
        [("act_window_id", "=", action_id)],
        ["id", "view_id", "view_mode", "sequence"],
        limit=0,
    )
    desired_rows = [
        {"view_mode": "kanban", "view_id": kanban_view_id, "sequence": 1},
        {"view_mode": "list",   "view_id": list_view_id,   "sequence": 2},
        {"view_mode": "form",   "view_id": False,          "sequence": 3},
    ]
    by_mode = {row["view_mode"]: row for row in existing}
    for desired in desired_rows:
        live = by_mode.pop(desired["view_mode"], None)
        if not live:
            client.create("ir.actions.act_window.view", {
                "act_window_id": action_id,
                "view_mode": desired["view_mode"],
                "view_id": desired["view_id"],
                "sequence": desired["sequence"],
            })
            print(f"    CREATE binding view_mode={desired['view_mode']}")
            continue
        delta: dict[str, Any] = {}
        live_view = live.get("view_id")
        live_view_id = live_view[0] if isinstance(live_view, list) else live_view
        if (live_view_id or False) != (desired["view_id"] or False):
            delta["view_id"] = desired["view_id"]
        if live.get("sequence") != desired["sequence"]:
            delta["sequence"] = desired["sequence"]
        if delta:
            client.write("ir.actions.act_window.view", [live["id"]], delta)
            print(f"    UPDATE binding view_mode={desired['view_mode']} {list(delta)}")
    if by_mode:
        client.unlink("ir.actions.act_window.view", [row["id"] for row in by_mode.values()])
        print(f"    DELETE {len(by_mode)} stale view-binding(s)")


def _ensure_menu(client: OdooClient, *, label: str, action_id: int) -> int:
    """Create or update a root-level menu that opens the Properties action."""

    existing = client.search_read(
        "ir.ui.menu",
        [("name", "=", label), ("parent_id", "=", False)],
        ["id", "action", "sequence", "active"],
        limit=1,
    )
    desired_action_ref = f"ir.actions.act_window,{action_id}"
    if not existing:
        menu_id = client.create("ir.ui.menu", {
            "name": label,
            "parent_id": False,
            "action": desired_action_ref,
            "sequence": MENU_SEQUENCE,
            "active": True,
        })
        print(f"  CREATE menu {label!r} id={menu_id}")
        return menu_id

    row = existing[0]
    delta: dict[str, Any] = {}
    if row.get("action") != desired_action_ref:
        delta["action"] = desired_action_ref
    if row.get("sequence") != MENU_SEQUENCE:
        delta["sequence"] = MENU_SEQUENCE
    if not row.get("active"):
        delta["active"] = True
    if delta:
        client.write("ir.ui.menu", [row["id"]], delta)
        print(f"  UPDATE menu {label!r} {list(delta)}")
    else:
        print(f"  OK     menu {label!r}")
    return row["id"]


def ensure_properties_app(client: OdooClient, *, action_label: str = ACTION_LABEL,
                          menu_label: str = MENU_LABEL) -> PropertiesAppIds:
    """Idempotently install the Properties app. Returns the touched ids."""

    print(f"Target: product.template @ {client.env.base_url}")
    print()
    print("--- App fields ---")
    model_id = client.get_model_id("product.template")
    field_ids: dict[str, int] = {}
    for spec in PROPERTIES_APP_FIELDS:
        field_ids[spec.name] = ensure_field_with_options(
            client, "product.template", spec, model_id
        )

    print("\n--- Views ---")
    kanban_id = ensure_primary_view(client, name=KANBAN_VIEW_NAME,
                                    model="product.template", view_type="kanban",
                                    arch=KANBAN_ARCH)
    list_id = ensure_primary_view(client, name=LIST_VIEW_NAME,
                                  model="product.template", view_type="list",
                                  arch=LIST_ARCH)
    search_id = ensure_primary_view(client, name=SEARCH_VIEW_NAME,
                                    model="product.template", view_type="search",
                                    arch=SEARCH_ARCH)

    print("\n--- Window action ---")
    action_id = _ensure_act_window(client, label=action_label,
                                   kanban_view_id=kanban_id, list_view_id=list_id,
                                   search_view_id=search_id)

    print("\n--- Menu ---")
    menu_id = _ensure_menu(client, label=menu_label, action_id=action_id)

    return PropertiesAppIds(
        field_ids=field_ids,
        kanban_view_id=kanban_id,
        list_view_id=list_id,
        search_view_id=search_id,
        action_id=action_id,
        menu_id=menu_id,
    )
