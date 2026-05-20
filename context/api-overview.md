# AVIV Classified API v4 — Overview & Operational Semantics

Source: https://www.developers.aviv-group.com/apis/classifieds-management-v4-4-0-2/versions/3e7a2390-1a4f-42db-9739-3276f69841ff/

Companion to [aviv-classified-api-v4.json](aviv-classified-api-v4.json) (OpenAPI spec). This doc captures the prose/operational rules that aren't in the OpenAPI file.

---

## Base URL

`https://api.aviv-group.com/caas/v4`

Sandbox: `https://api.aviv-group.com/sandbox/caas/v4`

V4 release date: **2025-11-05**. Complies with AvivClassified v3.1 and AvivImmo v2.1.

## Versioning policy

- Major version (`v4`) increments only on breaking changes
- Minor versions ship silently as backward-compatible additions (new optional params, new fields, new endpoints, field reordering)
- Plan accordingly: schemas should tolerate unknown fields

## Async processing model

Listings are processed asynchronously (milliseconds to minutes). POST/PUT/DELETE return an acknowledgement + URL to poll for status. Use the `/classifieds/{id}/statuses` endpoint or subscribe via webhook.

## traceparent header

Every response includes a `traceparent` header (W3C Trace Context). **When contacting AVIV support about a specific request, include this value** for fastest resolution. The connector should log the traceparent on every response.

## ETag / If-Match — optimistic concurrency

Updates use HTTP ETag for concurrent-write protection.

1. `GET /classifieds/{id}` returns the resource with an `ETag` response header
2. `PUT /classifieds/{id}` with header `If-Match: <etag>` will only apply if the ETag still matches server-side
3. If another writer modified the resource in between, the PUT returns **412 Precondition Failed**

This means **single-record updates need a read-before-write** if you want to be safe against concurrent writers (e.g. two Odoo users editing the same property at once). The connector should either always GET→PUT, or accept that 412 means "refetch and retry."

## Pagination

`GET /classifieds` is paginated:
- Default page size: **250**
- Override with `?limit=N`
- Continue with `?nextToken=<token>` (opaque base64 cursor returned by previous response)

## Authentication

OAuth 2.0 `client_credentials`. Full details in [m2m-authentication.md](m2m-authentication.md). Scopes:

| Scope | Grants |
|---|---|
| `caas:*` | All operations |
| `caas:classifieds:*` | All classified endpoints |
| `caas:classifieds:read` | GET `/classifieds`, GET `/classifieds/{id}` |
| `caas:classifieds:create` | POST `/classifieds` |
| `caas:classifieds:update` | PUT `/classifieds/{id}` |
| `caas:classifieds:delete` | DELETE `/classifieds/{id}` |

Scopes are case sensitive.

## Errors

Follow **RFC 7807 (Problem Details for HTTP APIs)** with two AVIV extensions: `errors` and `errorSource`.

```json
{
  "type": "https://caas-api-documentation.kugawana.eu/.../Validation-Error",
  "title": "Bad request",
  "detail": "Your request has not been validated",
  "instance": "00-652039077ca790cc11d3a80cc29dbeb9-ca5243f0e6c43195-00",
  "errors": [
    {"name": "/space", "reason": "must NOT have additional properties: space."}
  ],
  "errorSource": "body",
  "status": 400
}
```

| Field | Meaning |
|---|---|
| `errors[].name` | JSON pointer into the request body (e.g. `/data/estateSubTypes/trading`) |
| `errors[].reason` | Human-readable validation failure |
| `errorSource` | One of `body`, `requestParameter`, `header`, `contentType` |
| `instance` | Same value as the response `traceparent` header — use for support |

### Named error types (so far documented)

1. **Validation Error (400)** — schema/format issue. See above.
2. **Duplicated Classified (400)** — `offererEstateId` already used. Each listing must have a unique `offererEstateId` per offerer. Response includes the existing `classifiedId`.
3. **Duplicated Media (400)** — same media `url` already attached to another media on another classified.
4. **Colliding Contacts (400)** — you may not set both `data.contact.*` and `specific.gsl.contact.*` simultaneously. Pick one mechanism.

Notable: contact information has **two routing options** — generic (`data.contact.*`) and SeLoger-specific (`specific.gsl.contact.*`). They're mutually exclusive. The v3 deprecation notes say generic is the preferred path going forward (contact entities are created via the separate "Aviv Contact API").

## Identity model

Three IDs to keep straight:

| ID | Lives in | Meaning |
|---|---|---|
| `client_id` / `client_secret` | OAuth credentials | Your application's identity (one per integrator) |
| `intermediary_id` | OAuth token request body | Which agency you're acting on behalf of |
| `offererEstateId` | `data.metaData.source.offererEstateId` | Your stable identifier for one specific listing |
| `classifiedId` | Server-assigned, returned on POST | AVIV's UUID for the listing — used in all subsequent URLs |

## Media

From the v4 changelog (release 2025-11-05):

- `media` is an array on `AvivClassified`, siblings of `portals` and `data`
- Each item has: `url`, `mediaType`, `title`, `category`, `tags[]`
- **MediaType enum (4):** `PICTURE`, `VIRTUAL_TOUR`, `PANORAMA`, `VIDEO`
- **MediaCategory enum (34):** BALCONY, BASEMENT, BATHROOM, BEDROOM, CHILDREN_ROOM, CORRIDOR, COVER_PICTURE, ENERGY_CERTIFICATE, ENTRY_HALL, FLOOR_PLAN, GARAGE, GARDEN, HOUSE_VIEW, INDOOR, KITCHEN, LIVING_ROOM, LOGO, MAP, MISC, OUTDOOR, OUTDOOR_BUILDING, OUTDOOR_HOUSE, OUTSIDE_VIEW, POOL, PROPERTY_INFORMATION, SCHEMA, SITE_PLAN, STAIRS, STORAGE_ROOM, SURROUNDING, TERRACE, TOILETS, VERANDA, VIEW_FROM_PROPERTY, WORK_ROOM
- V4 removed per-media endpoints (`POST/PATCH/DELETE /classifieds/{id}/media/{mediaId}`) and per-media status endpoint. Media is now fully managed via the parent classified payload.
- Media status is reported within the parent `ClassifiedStatus.mediaStatuses` array.

## V3 → V4 breaking changes (summary)

- Removed all per-media endpoints (see above)
- Removed `PATCH /classifieds/{id}` — only PUT remains
- Media must be sent inline in the classified payload

No header or auth changes between v3 and v4.

## Portal SLC and SLN history

- `SLC` (SeLoger Construire) added in v3.5 — January 2025
- `SLN` (SeLoger Neuf) added in v3.6 — February 2025

If a customer needs Logic-Immo (LI) or Lux-Residence (LR), V4 doesn't support them — fall back to V3.

## Notes for the Odoo connector

- **`offererEstateId` mapping:** use Odoo `product.template.id` as a string — guaranteed unique per tenant, stable across edits.
- **Idempotency:** AVIV deduplicates by `offererEstateId` (returns Duplicated Classified). Our POST handler should catch this 400 and follow up with a GET → PUT instead.
- **412 retry loop:** if concurrent edits happen, retry with fresh ETag once before failing.
- **Cache token per `intermediary_id`** with TTL just shy of 24h (e.g. 23h) — token-reuse is a hard AVIV requirement.
- **Always log `traceparent`** from every response into the Odoo chatter — makes support tickets one-shot.
