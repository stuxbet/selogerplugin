# Client Onboarding Runbook

AVIV-side partner onboarding (the 7-phase GTM flow) is documented in
[../context/onboarding.md](../context/onboarding.md). The steps below are
the connector-side cutover for one new agency once AVIV has issued the
`intermediary_id` + `offerer_id`.

## Prerequisites

| You need | From |
|---|---|
| Odoo base URL, DB name, API key | the agency |
| `intermediary_id` | AVIV (Phase 1) |
| `offerer_id` | AVIV (Phase 1) |
| Portal list (subset of SL / BD / BUCOM / SLC / SLN) | the agency × AVIV-approved set |
| Publicly reachable Odoo base URL (for AVIV's media fetcher) | the agency |

## 1. Provision the Odoo database

```bash
# Run as the agency's Odoo admin user
export ODOO_BASE_URL=https://acme.odoo.com
export ODOO_API_KEY=<paste>
export ODOO_DATABASE=acme

python -m seloger.odoo.provision.bootstrap_properties_app
python -m seloger.odoo.provision.provision_database
```

Both scripts are idempotent (see [../odoo/provision/](../odoo/provision/)):

* Pre-provision creates the Properties menu, window action, kanban/list/
  search views, and the four "app" fields (`x_is_properties`, `x_status`,
  `x_owner_id`, `x_acheteur_id`).
* Main provision creates the seloger fields, the "Seloger" notebook page,
  and the four smart buttons (Post / Update / Archive / Delete Listing).

`WEBHOOK_URL` in the env file is used as the base of every smart-button URL.

## 2. Register the tenant

```bash
python -m seloger.ops.add_tenant
```

Answer the prompts. The script mints a fresh `tk_<hex>` key and writes it
into `seloger/tenants.json`. **Copy the key** — you'll need it for the
smart-button identifier query param.

## 3. Point the smart buttons at the right tenant

The smart buttons created in step 1 default to no `?identifier=` query
param. Set the per-tenant identifier so each agency's webhook calls
resolve to their own tenant:

```bash
WEBHOOK_IDENTIFIER=<tk_…> \
ODOO_BASE_URL=... ODOO_API_KEY=... ODOO_DATABASE=... \
python -m seloger.odoo.provision.provision_database --skip-properties-app
```

(The provision script re-checks the action URLs and updates them in place.)

## 4. Sync tenants.json to the deployment secret

```bash
seloger/ops/sync_tenants_secret.sh
```

(Or whatever the agency's secret-mgmt flow is — Azure Key Vault, AWS Secrets
Manager, etc. The deployment loads `tenants.json` via the `TENANTS_PATH`
env var.)

## 5. Smoke test against sandbox

1. Open a Property in the agency's Odoo.
2. Fill in the AVIV-required fields (address + price + property type +
   distribution type).
3. Click **Post Listing**.
4. Confirm the chatter shows the green "publish acknowledged" note with a
   non-empty `traceparent` and AVIV `classifiedId`.
5. Edit the price → **Update Listing** → confirm a new chatter note.
6. **Archive Listing** → confirm `x_is_published_seloger` flips to False.
7. **Delete Listing** → confirm `x_aviv_listing_id` is cleared.

If any step fails, the chatter notes carry the exact error code +
`traceparent` AVIV returned — quote that when escalating.

## 6. Production cutover checklist

* [ ] AVIV has signed off on the sandbox phase (Phase 1 review).
* [ ] `AVIV_AUDIENCE` and `AVIV_API_BASE_URL` flipped to prod URLs.
* [ ] Smart-button `WEBHOOK_URL` points at the prod Flask deployment.
* [ ] `tenants.json` synced to the prod secret store.
* [ ] AVIV cuts the prod token (only after Phase 1 review passes).
* [ ] First five listings published in prod and verified visible on the
      portals.
* [ ] Customer Success runs a 1-week observation period before scaling to
      the next wave of agencies.

## Quick reference

* AVIV partner team: `partners@groupeseloger.com`
* AVIV tech support: `support-caas@groupeseloger.com`
* OpenAPI: [../context/aviv-classified-api-v4.json](../context/aviv-classified-api-v4.json)
* AVIV operational notes: [../context/api-overview.md](../context/api-overview.md)
* Use-case + per-portal rules: [../context/use-cases.md](../context/use-cases.md)
