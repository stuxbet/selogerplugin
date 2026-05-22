# Operations Runbook

## Health and liveness

`GET /health` returns:

```json
{
  "status": "ok",
  "tenants": <int>,
  "aviv_base_url": "https://api.aviv-group.com/sandbox/caas/v4"
}
```

A non-200 response means the tenant registry couldn't load — usually a
malformed `tenants.json`. Check the most recent app log line; the
`ConfigError` message names the offending entry.

## Log inspection

Every AVIV response carries a `traceparent` header. The connector logs it
into the Odoo chatter on every action and surfaces it in the JSON webhook
response (`"traceparent": "..."`). When opening a ticket with AVIV
(`support-caas@groupeseloger.com`), paste that value verbatim — it
shortcut-resolves their server-side search.

Log lines worth grepping:

* `seloger.status_poller` — periodic poll loop, drops + requeues
* `seloger.app` — startup, request 5xx
* `flask.app` — Flask's own request log

## Forcing a token refresh

If AVIV revokes or rotates credentials, the in-memory cache will continue
serving the old token until expiry. To force a refresh without restarting:

```python
# inside a Python shell on the host
from seloger.src.core.tenant import registry
from flask import current_app

cache = current_app.config["AVIV_TOKEN_CACHE"]
for tenant in registry().all():
    cache.invalidate(intermediary_id=tenant.aviv.intermediary_id,
                     audience=current_app.config["AVIV_BASE_URL"])
```

Or simply restart the Flask process — the cache is process-local.

## Handling `DOWNLOADING_FAILED` media

AVIV reports `DOWNLOADING_FAILED` in the per-media status array when their
crawler can't fetch an attachment URL. The chatter formatter surfaces the
list of failed URLs with a banner: **re-submitting the listing alone will
not fix this.** Steps:

1. Fix the URL in Odoo (re-upload, mark public, double-check ACLs).
2. The next update will produce a new `?ts=` query param, which makes the
   URL distinct.
3. Open a ticket with AVIV Customer Care
   (`support-caas@groupeseloger.com`) quoting the `traceparent`. They have
   to manually flush the failed media before AVIV will retry.

## Rate-limit recovery

The AVIV client honors `Retry-After` on 429 responses (capped at 30 s).
For sustained 429s, back off the sending tenant — extend
`STATUS_POLL_INTERVAL_SECONDS`, throttle bulk publishes through the
webhook layer, or temporarily disable a noisy tenant via `tenants.json`.

## Tenant rotation / decommissioning

1. `ops/add_tenant.py` registers a new tenant and prints the new key.
2. Update the Odoo smart buttons for the agency to use the new
   `?identifier=` value (see `odoo/provision/smart_buttons.py`).
3. To retire a tenant, delete its block from `tenants.json` and redeploy.
   The token cache entry will eventually expire on its own.

## Promoting sandbox → production

* Set `AVIV_AUDIENCE` and `AVIV_API_BASE_URL` to the prod URLs
  (`https://api.aviv-group.com/caas/v4` for both).
* Update the smart-button URLs to point at the prod Flask deployment.
* AVIV runs a manual review at this point (see `context/use-cases.md`
  Phase 1) — be ready to demo idempotent publish + update + archive.

## Disaster recovery

* The connector is stateless apart from the in-memory token cache and the
  status-poller queue. Both rebuild from Odoo + `tenants.json` after a
  restart.
* `x_aviv_listing_id` on each `product.template` is the authoritative
  link to AVIV — losing the connector temporarily doesn't lose the mapping.
