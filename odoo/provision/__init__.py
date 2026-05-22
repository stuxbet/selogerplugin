"""Idempotent Odoo provisioning for the seloger connector.

Modules in this package configure a target Odoo database so it is ready to
host product.template records that the seloger webhook server can publish to
AVIV's CaaS API. Two entry points sit at the top:

* ``bootstrap_properties_app.py`` — pre-provisioning: creates the top-level
  Properties menu, its window action, and the kanban/list/search views.
* ``provision_database.py`` — full provisioning: ensures the Properties app
  is in place, then creates the seloger-specific custom fields, places them
  on the product.template form, and wires the Post/Update/Archive/Delete
  smart buttons.

Both entry points are safe to run repeatedly against the same database; each
step compares the live record to the desired state and only writes when a
delta is detected.
"""
