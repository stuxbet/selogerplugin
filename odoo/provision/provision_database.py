"""CLI entry point: provision a blank Odoo database for the seloger connector.

Run order (each step idempotent):

1. ``ensure_properties_app`` — the same step ``bootstrap_properties_app.py``
   runs standalone. Re-running here is a no-op if the app is already in
   place.
2. Create seloger custom fields on ``product.template`` from
   ``field_specs.ALL_FIELD_GROUPS``.
3. Inject the "Seloger" notebook page into the base product.template form
   so the new fields are visible to users.
4. Create the four webhook server actions (Post / Update / Archive /
   Delete) and inject the smart-button block into the form header.

Environment variables (typically loaded from ``seloger/.env``):

* ``ODOO_BASE_URL``, ``ODOO_API_KEY``, ``ODOO_DATABASE`` — Odoo connection
* ``WEBHOOK_URL`` — base URL of the seloger webhook server (the script
  trims trailing ``/post`` etc. before appending each action's path)
* ``WEBHOOK_IDENTIFIER`` — optional tenant token forwarded as
  ``?identifier=…`` on every webhook URL

Run with: ``python -m seloger.odoo.provision.provision_database``.
"""

from __future__ import annotations

import argparse
import sys

from .client import OdooClient
from .env import odoo_env
from .fields import ensure_field_with_options
from .field_specs import ALL_FIELD_GROUPS, all_fields
from .notebook_page import ensure_notebook_page
from .properties_app import ensure_properties_app
from .smart_buttons import ensure_smart_buttons
from .views import find_view_id


def _ensure_seloger_fields(client: OdooClient) -> None:
    print("\n--- Seloger fields ---")
    model_id = client.get_model_id("product.template")
    for label, specs in ALL_FIELD_GROUPS:
        if not specs:
            continue
        group_name = label.get("en_US") if isinstance(label, dict) else label
        print(f"  group: {group_name} ({len(specs)} field(s))")
        for spec in specs:
            ensure_field_with_options(client, "product.template", spec, model_id)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Provision the seloger connector on a target Odoo database."
    )
    parser.add_argument(
        "--skip-properties-app",
        action="store_true",
        help="Assume bootstrap_properties_app has already been run; skip the "
             "Properties menu/action/view step.",
    )
    parser.add_argument(
        "--skip-smart-buttons",
        action="store_true",
        help="Do not create or update the webhook server actions and their "
             "form-view block. Useful when WEBHOOK_URL is not yet known.",
    )
    args = parser.parse_args(argv)

    env = odoo_env()
    print(f"Provisioning seloger on {env.database} @ {env.base_url}")
    print(f"  WEBHOOK_URL = {env.webhook_url or '(unset)'}")
    if env.webhook_identifier:
        print(f"  WEBHOOK_IDENTIFIER = {env.webhook_identifier[:6]}…")
    print()

    client = OdooClient(env)

    if not args.skip_properties_app:
        print("=== Step 1: Properties app ===")
        ensure_properties_app(client)

    print("\n=== Step 2: Seloger fields ===")
    _ensure_seloger_fields(client)

    print("\n=== Step 3: Notebook page ===")
    parent_form_id = find_view_id(
        client, "product.template", "form",
        name="product.template.product.form",
    ) or find_view_id(client, "product.template", "form")
    if parent_form_id is None:
        print("  ERROR: no product.template form view found.")
        return 1
    ensure_notebook_page(client, parent_view_id=parent_form_id)

    if not args.skip_smart_buttons:
        print("\n=== Step 4: Smart buttons ===")
        if not env.webhook_url:
            print("  WARN  WEBHOOK_URL is empty — actions will be created with an empty URL.")
        ensure_smart_buttons(
            client,
            webhook_base_url=env.webhook_url,
            webhook_identifier=env.webhook_identifier or None,
        )

    print(f"\nDone. Provisioned {len(all_fields())} seloger field(s) "
          f"plus the Properties app.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
