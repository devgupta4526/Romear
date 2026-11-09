# PROMPT 17 — Freemium ROMEAR Plus and promoted content with clear labeling

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Implement free tier preserving basic social interactions, club follow, Pool creation, community discovery, safety, messaging, and basic Passport. Plus optional personal experience recaps, collections, design customizations and advanced filters; check paid entitlements on backend, store receipts or verification via Play Billing where required for Play-distributed digital services; no paywall for block/report/privacy or essential connection functions. Build clear pricing/restore/manage subscription screens; no invented plans/prices in production. Business promotions: verified clubs/venues may submit labeled sponsored event campaigns, budgets/audiences within allowed privacy rules, manual moderation approval, reporting of impressions/clicks/verified bookings; enable billing only when safe commercial setup exists. Android Sponsored labels, hide/mute/report ads; business web campaign creation and metrics. Never sell exact personal location or expose private club membership in targeting.

## Required acceptance criteria
Expired subscription loses only premium extras; free features remain; every ad labelled Sponsored; campaigns cannot target private data; no live charge without configured compliant billing.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`18` if not final) and why this step is ready.
