# Connector Architecture

## Runtime model

A single Flask process exposes five POST routes (`/post`, `/update`, `/archive`,
`/delete`, `/aviv/status`) plus a `/health` liveness probe. Each state-changing
route is invoked by an Odoo smart-button webhook; the body identifies which
`product.template` record to operate on. A background `StatusPoller` thread
periodically calls `GET /classifieds/{id}/statuses` on AVIV for listings that
haven't reached a terminal state yet, mirroring the result into the Odoo chatter.

```
+---------+        +-------------+        +-----------------+
|  Odoo   | --POST | Flask /post |--HTTP->| AVIV /classifieds|
+---------+        +-------------+        +-----------------+
     ^                    |                       |
     | chatter            | status webhook (later)|
     +----------------------------------+         |
                                        |         |
                              +----------+        |
                              | /aviv/status <----+
                              +----------+
```

## Module map

| Path | Responsibility |
|---|---|
| `src/core/` | exceptions, OAuth token cache, tenant loader, country mapping |
| `src/clients/aviv.py` | AVIV REST client: 6 endpoints, ETag handling, RFC 7807 error decoding |
| `src/clients/odoo.py` | Tenant-scoped Odoo JSON/2 client (read/write product.template, chatter) |
| `src/schema/` | Minimal Pydantic models (Classified, RealEstateData, ClassifiedStatus, …) |
| `src/transforms/` | One module per AVIV block (`location`, `prices`, `media`, …) + a composer |
| `src/services/validation.py` | Per-portal rules (SL / BD / BUCOM / SLN / SLC) |
| `src/services/listing.py` | `ListingService` — publish / update / archive / delete orchestration |
| `src/services/status_poller.py` | Single-thread background poller, in-memory queue |
| `src/chatter/` | HTML chatter formatters (success / validation / AVIV-error / status) |
| `src/handlers/` | Thin Flask views per endpoint |
| `src/app.py` | App factory, env loader, route registration, prod entry point |
| `odoo/provision/` | Idempotent DB provisioning (Properties app, fields, smart buttons) |
| `odoo/server_actions/` | Reference docs describing each smart button |
| `ops/add_tenant.py` | CLI to register a new tenant in `tenants.json` |

## Multi-tenancy

* `tenants.json` is the source of truth. Each tenant carries Odoo
  credentials + AVIV `intermediary_id` / `offerer_id` + the portal list.
* The OAuth token cache (`src/core/auth.py::TokenCache`) is keyed by
  `(intermediary_id, audience)` with a ~23h TTL — token reuse is mandated by
  AVIV (see [m2m-authentication.md](../context/m2m-authentication.md)).
* Webhook URLs carry the tenant key via `?identifier=<key>`. The handler
  resolves the tenant via the app-injected `TenantRegistry`, so tests can
  stub it without monkey-patching globals.

## Validation strategy

1. **Pydantic schema** (`src/schema/models.py`) — catches type / required
   errors; tolerant of unknown fields (`extra="allow"`) so AVIV minor-
   version drift doesn't break us.
2. **Per-portal rules** (`src/services/validation.py`) — run for every
   portal the tenant subscribes to. Documented in
   [use-cases.md](../context/use-cases.md): SL (price), BD (≥1 picture,
   ≥20 m², ≥160-char description), BUCOM (lease right, estate type), SLN/SLC
   pass-through pending docs.

## Media diff

AVIV decides whether to re-download media by URL equality. The
`build_media` transform appends `?ts=<write_date>` to every Odoo attachment
URL: same `write_date` → same URL → AVIV reuses the cached asset; replaced
file → new `write_date` → new URL → AVIV fetches the new asset. Removing an
attachment from the list removes the media from the classified.

## AVIV integration quirks

* **`User-Agent` header is mandatory.** AVIV's firewall drops requests
  without one (`AVIV_USER_AGENT` env var).
* **Token reuse is mandated.** The token cache holds tokens for ~23h.
* **`traceparent` everywhere.** Every AVIV response carries a W3C
  trace-parent; the chatter formatter surfaces it so support tickets are
  one-shot.
* **ETag / If-Match on PUT.** `ListingService._update` does GET → PUT with
  one 412 retry.
* **Duplicated Classified fallback.** A POST that collides on
  `offererEstateId` is automatically converted into GET → PUT in
  `ListingService.publish`.
* **`offererEstateId` = `product.template.id` as string.** Stable, unique
  per tenant.

## Deployment topology

* One Flask process per environment (sandbox vs prod selected via
  `AVIV_AUDIENCE` / `AVIV_API_BASE_URL`).
* `WEBHOOK_URL` must be the externally-reachable base URL — each
  smart-button URL appends `/post`, `/update`, etc. with the tenant key
  query param.
* The status poller runs in a daemon thread inside the Flask process; for
  high-volume tenants, lift it into a sidecar later.
* `tenants.json` is mounted as a deployment secret (see
  `ops/sync_tenants_secret.sh`).

## Open questions

Tracked in [../context/README.md](../context/README.md). Highlights:

1. Webhook signing — we currently trust the `identifier` query param; AVIV
   has yet to publish signature semantics.
2. SLN / SLC portal rules — placeholders pass-through until use-case docs
   land.
3. Rate limits / 429 budget — best-effort `Retry-After` honored, but
   per-tenant quotas need to be measured in sandbox.
