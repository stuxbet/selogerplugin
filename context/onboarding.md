# SeLoger / AVIV APIs — Onboarding Path

Source: https://www.developers.aviv-group.com/guides/how-to-onboard-on-aviv-apis/onboarding-path-french-apis-seloger-services

## Initial contact

- **Email: `partners@groupeseloger.com`** (the "Connect Success Team")
- Note: this is the **correct contact for partner onboarding** — different from `support-caas@groupeseloger.com` which is the API-team support address listed in the OpenAPI spec
- Connect Success Team validates eligibility, provides initial docs, sets up communication channels (including a dedicated **Slack** channel)

## The 7-phase onboarding (GTM framework)

### Phase 1 — Information & Scoping
- Kick-off meeting to align on objectives
- Receive technical documentation and sandbox access
- **Share the list of clients/agencies ("RCUs")** to be migrated or integrated
- → This is presumably where `intermediary_id` provisioning per agency happens: you supply the list, AVIV assigns the IDs

### Phase 2 — Technical Setup & Credentials
- Provisioning of `client_id` and `client_secret`
- Sandbox URL provided
- Invitation to a dedicated Slack channel
- Recurring sync calls scheduled
- You begin architectural design + automated test prep

### Phase 3 — Integration & Development
- Active coding against AVIV APIs
- Data field mapping verification (internal listing structure → AVIV format)
- Weekly sync meetings for technical blockers

### Phase 4 — Functional Testing & QA
- Sandbox validation: test cases for listings + media processing
- Final logic review with AVIV engineers

### Phase 5 — Pre-Production & Load Testing
- Final Go/No-Go decision
- Performance validation against expected volume
- Selection of pilot agencies

### Phase 6 — Pilot Launch
- **1–3 clients** moved to production
- Intensive monitoring + feedback loop for real-world edge cases

### Phase 7 — Full Deployment
- Communication plan execution
- **Progressive roll-out in waves** (e.g. 10 → 30 → 50+ RCUs)
- Handover to standard support + ongoing monitoring

## Glossary

- **RCU** — AVIV's term for an agency customer (likely "Référence Client Unique" or similar). Each agency you onboard counts as one RCU.
- **Connect Success Team** — AVIV's partner onboarding team (`partners@groupeseloger.com`)

## What this changes for our plan

1. **Use `partners@groupeseloger.com`** for the initial outreach, not `support-caas@…`. The API-spec contact is for post-onboarding technical questions.
2. **Expect a structured partner relationship**, not a self-serve API key handout: kickoff meeting, Slack channel, weekly syncs, multi-phase reviews.
3. **Bring the list of target agencies** to the initial conversation — Phase 1 explicitly asks for the RCU list during scoping. Even a rough list of "who we expect to onboard in the first 6 months" should be useful.
4. **Volume estimate matters early** — Phase 5 sizes load against expected volume. Have a rough "X listings × Y daily updates × Z agencies" estimate ready.
5. **Pilot is 1–3 clients, then waves of 10/30/50+** — match this to our own rollout plan. Identify which 1–3 friendly agencies will pilot.
