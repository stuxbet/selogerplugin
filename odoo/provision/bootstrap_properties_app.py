"""CLI entry point: pre-provisioning — install the Properties app.

This script is the first thing to run against a clean Odoo database. It
mirrors the layout of the seloger dev database: a top-level "Properties"
menu that opens a product.template window action filtered by
``x_is_properties``, plus the kanban / list / search views that drive it.

The follow-up step (``provision_database.py``) adds the seloger-specific
fields, notebook tab, and smart buttons.

Connection details come from environment variables (read from
``seloger/.env`` if present): ``ODOO_BASE_URL``, ``ODOO_API_KEY``,
``ODOO_DATABASE``. Safe to run repeatedly; every step compares the live
record to the desired state and writes only when needed.

Run with: ``python -m seloger.odoo.provision.bootstrap_properties_app``.
"""

from __future__ import annotations

import argparse
import sys

from .client import OdooClient
from .env import odoo_env
from .properties_app import ensure_properties_app


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Bootstrap the Properties app on the target Odoo database "
                    "(menu, window action, kanban/list/search views, app fields)."
    )
    parser.add_argument(
        "--action-label",
        default="Properties",
        help='Display name for the window action (default: "Properties").',
    )
    parser.add_argument(
        "--menu-label",
        default="Properties",
        help='Display name for the top-level menu (default: "Properties").',
    )
    args = parser.parse_args(argv)

    env = odoo_env()
    print(f"Bootstrapping Properties app on {env.database} @ {env.base_url}\n")

    client = OdooClient(env)
    ensure_properties_app(client, action_label=args.action_label, menu_label=args.menu_label)
    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
