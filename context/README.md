# SeLoger connector — reference docs

All external documentation we have for the SeLoger / AVIV CaaS integration. Captured 2026-05-20.

## What to build against

**AVIV Classified API v4** — modern REST API, OAuth 2.0, real-time CRUD. Publishes to SeLoger and 4 sister portals (BUCOM, BD, SLC, SLN). This is the primary target.

The Belgian Immoweb portal is **not** reachable from v4 even though the `specific.iwt` namespace stub exists — keep using [../../immoweb-test/](../../immoweb-test/) for Immoweb publishing.

## File index

### Primary references — AVIV Classified API v4

| File | Source | What's in it |
|---|---|---|
| [aviv-classified-api-v4.json](aviv-classified-api-v4.json) | Dev portal export | OpenAPI 3.0.3 spec, v4.0.2 (456 KB). 8 endpoints + 36 schemas. The authoritative API contract. |
| [m2m-authentication.md](m2m-authentication.md) | [/docs/m2m-authentication](https://www.developers.aviv-group.com/apis/classifieds-management-v4-4-0-2/docs/m2m-authentication) | OAuth 2.0 `client_credentials` flow: token endpoint, request body, mandatory User-Agent + token-caching rules |
| [api-overview.md](api-overview.md) | [/versions/3e7a2390-…](https://www.developers.aviv-group.com/apis/classifieds-management-v4-4-0-2/versions/3e7a2390-1a4f-42db-9739-3276f69841ff/) | Operational semantics not in the OpenAPI spec: ETag/If-Match concurrency, traceparent, RFC 7807 errors, pagination, identity model, changelog |
| [use-cases.md](use-cases.md) | [/docs/use-cases/*](https://www.developers.aviv-group.com/apis/classifieds-management-v4-4-0-2/docs/use-cases/manage-classifieds) | Per-portal required fields (Resale, Rental, BD Luxury, BUCOM), media diffing rules (URL timestamp trick), V3→V4 migration runbook |
| [onboarding.md](onboarding.md) | [/guides/.../onboarding-path-french-apis-seloger-services](https://www.developers.aviv-group.com/guides/how-to-onboard-on-aviv-apis/onboarding-path-french-apis-seloger-services) | 7-phase partner onboarding flow. **Correct contact email: `partners@groupeseloger.com`** (not the API support address) |

### Secondary references

| File | Source | What's in it |
|---|---|---|
| [aviv-classified-api-v3.json](aviv-classified-api-v3.json) | Dev portal export | OpenAPI 3.0.3 spec, v3.1.3 of the same API (legacy). Useful because it inlines enum values (EstateType=12, MediaCategory=35, CurrencyCodes=180, MultiLingualText=184) that v4 hides behind refs. Also v3 supports 7 portals — adds `LI` (Logic-Immo) and `LR` (Lux-Residence) which v4 dropped. |
| [legacy/seloger-transferts-4.08-v6.pdf](legacy/seloger-transferts-4.08-v6.pdf) | [gedeon.im mirror](https://gedeon.im/docs/TransfertsSeloger408v6.pdf) | "Spécifications Techniques d'Exportation" — SeLoger's pre-API CSV-over-FTP feed format. Fallback option if the modern API isn't viable. |
| [legacy/seloger-transferts-4.08-007.pdf](legacy/seloger-transferts-4.08-007.pdf) | [chronotech.fr mirror](https://www.chronotech.fr/_media/immobilier-passerelle/TransfertsSeloger.4.08.007.pdf) | Different mirror of the same spec series (revision 007). Keep both — third-party hosts can disappear. |

## Open questions (to ask AVIV support)

Not in any doc above; requires emailing `support-caas@groupeseloger.com`:

1. Rate limits on `/classifieds` endpoints
2. Media file constraints (formats, max size, max dimensions, max count)
3. `intermediary_id` provisioning per agency customer
4. `metaData.source.sourceSystem` registration requirements
5. Webhook delivery retry policy + signing mechanism
6. Belles Demeures luxury pricing thresholds
7. Sandbox→production review criteria (beyond token-caching)
8. Listing auto-expiry / lifecycle policies
9. Whether a dry-run / validation-only endpoint exists
10. "New Builds & New Homes" use-case page referenced for SLN/SLC but not located on the dev portal

## Production endpoints

- API: `https://api.aviv-group.com/caas/v4`
- Sandbox API: `https://api.aviv-group.com/sandbox/caas/v4`
- OAuth token: `https://auth.api.aviv-group.com/oauth/token` (same host for both envs; switch via `audience` claim)
- Dev portal: https://www.developers.aviv-group.com/apis/classifieds-management-v4-4-0-2/

## Sister project reference

Compare to [../../immoweb-test/context/](../../immoweb-test/context/) for the existing Immoweb integration — same connector pattern, much of the field model and transformer logic carries over since AVIV/Immoweb share the underlying data spec (AvivClassified v3.0.0 + AvivImmo v2.1).
