# Use Cases — AVIV Classified API v4

Source pages on https://www.developers.aviv-group.com/apis/classifieds-management-v4-4-0-2/docs/use-cases/

Three use-case docs cover the operational flow:

- `manage-classifieds` — overall publish lifecycle + per-portal required fields
- `manage-medias` — media submission rules, diffing model
- `switch-from-v3-to-v4` — migration runbook (relevant if you have V3 customers; not for greenfield builds)

---

## 1. Manage classifieds — required fields per portal

The most important content on this page. Each AVIV portal has its own mandatory-field set on top of the OpenAPI schema's required fields.

### Resale (portal `SL`)
- `estateType`, `estateSubType`, `distributionType`
- `location.postalCode`, `location.city`, `location.country`
- `prices.buy.price.amount`
- `metaData.source` + sub-attributes

### Rental (portal `SL`)
- `estateType`, `estateSubType`, `distributionType`
- `location.postalCode`, `location.city`, `location.country`
- `prices.rent.baseRent.amount`
- `metaData.source` + sub-attributes

### Luxury (portal `BD` — Belles Demeures)
- `estateType`, `estateSubType`, `distributionType`
- `location.postalCode`, `location.city`, `location.country`
- Prices must meet portal thresholds based on resale/rental type and location (contact customer care for current thresholds)
- All prices accepted for `estateSubType` in `CASTLE`, `MANOR_HOUSE`, `MANSION`
- **≥ 1 picture required**
- Surface (when provided) must be **≥ 20 m²**
- Description **≥ 160 characters**
- `metaData.source` + sub-attributes
- Some classified types forbidden on BD — contact customer care

### Bureaux & Commerces (portal `BUCOM`)
- Only available for classifieds with `estateType = TRADING`
- `data.prices.rent.countrySpecific.fr.leaseRight` (French: *prix de la cession*)
- Same data otherwise as resale/rental

### SeLoger Neuf (`SLN`) and SeLoger Construire (`SLC`)
- Spec says "refer to New Builds & New Homes Use cases" — those pages may exist but aren't in the nav we've seen.

### Workflow (all portals)
1. **POST** `/classifieds` with `portals` array — classified is acknowledged with 202
2. **PUT** `/classifieds/{id}` with the full payload to update (no PATCH in v4)
3. **DELETE** `/classifieds/{id}` to stop publication
4. Status reported async via `/classifieds/{id}/statuses` or webhook

### Operational guidance
- "If nothing has changed then retain from sending us an update" — AVIV detects no-op updates and skips them, but they ask you not to send them in the first place
- "Send us a unique API call that will sum up all these changes at once" — consolidate user edits before pushing, don't fire one PUT per field

---

## 2. Manage media — submission and diffing rules

### Submission model
- Media is sent inline in the classified payload (POST or PUT) — there are no separate media endpoints in v4
- `media` is an ordered array; **display order on portals = array order** (no separate `displayOrder` field)
- Only the **first** `VIRTUAL_TOUR` is displayed
- Only the **first** `VIDEO` is displayed
- Pictures, virtual tours, and videos are displayed in separate areas on the portals

### URL timestamp convention
AVIV diffs media by URL string. To force a re-download of a changed image, **append a timestamp query param**:

```
http://a.com/a.jpg?timestamp=2026-02-13T09:25:57
```

- Same URL on next update → AVIV does **not** re-download
- Different URL (e.g. different timestamp) → AVIV downloads
- Removed from list → media removed from classified
- Added to list → media downloaded

This dictates how the Odoo attachment URL builder needs to work: encode the Odoo attachment's `write_date` into the URL so AVIV refetches when an image is replaced. Immoweb-test does something similar with SHA256 hashes.

### Reference payload

```json
{
  "media": [
    {
      "category": "LIVING_ROOM",
      "mediaType": "PICTURE",
      "tags": ["LIVING_ROOM"],
      "title": "Double living room",
      "url": "http://a.com/a.jpg?timestamp=2026-02-13T09:25:57"
    },
    {
      "category": "COVER_PICTURE",
      "mediaType": "PICTURE",
      "tags": ["COVER_PICTURE"],
      "title": "Cover",
      "url": "http://a.com/a.jpg?timestamp=2026-02-13T09:25:57"
    }
  ]
}
```

### Sad-path

| Status | Meaning | Fix |
|---|---|---|
| `CREATED_WITH_MEDIA_ERROR` (classified-level) | Classified created but one or more media had issues | Fix each media issue; PUT classified again |
| `DOWNLOADING_FAILED` (media-level) | AVIV could not download the media URL | After the URL is fixed and accessible, **contact Customer Care** so they reprocess it (re-submitting alone is not enough) |

The need to contact Customer Care for `DOWNLOADING_FAILED` is operationally significant — surface this in the Odoo chatter so the agency knows to file a support ticket.

---

## 3. V3 → V4 migration runbook

Only relevant if you have existing V3 customers; greenfield builds skip this. Three phases:

### Phase 1 — Dev + Sandbox
- Build against V4
- Test on V4 sandbox
- Validation: AVIV + you both sign off (e.g. "adding, removing, ordering media works", "an update can mix description + media changes")

### Phase 2 — Pilot
- Pick pilot customers
- Switch them to V4
- Stop sending V3 calls for them
- Send V4 updates for all active classifieds of these pilots at once
- **AVIV verifies:** all classifieds have same media count, all received a V4 update
- AVIV revokes V3 authorization for pilots
- 1-week observation period before proceeding

### Phase 3 — Full cutover
- Same milestones as Phase 2, applied to the rest of the customer base

This confirms: **AVIV runs a manual review at each phase**. Production access is not self-serve.

---

## Resource link

The pages reference "French API V4" as the full API reference — same OpenAPI spec we already have at [aviv-classified-api-v4.json](aviv-classified-api-v4.json).
