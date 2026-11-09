# PROMPT 19 — Deep links, sharing, anti-abuse and Nagpur launch readiness

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Implement Android verified app links/deep links for profile/post/club/Pool/event/venue with safe fallback pages. Native share actions and UTM-like aggregate attribution without tracking private people. Add onboarding from shared links (after login returns to target), invitation capacity checks, event referrals. Implement real content/admin moderation operating procedure, abuse rate limits, anti-bot guardrails and deletion/export lifecycle, app support center, privacy policy/terms links, map/location consent and partner consent. Build a local Nagpur pilot with explicit admin-created verified partners, no fake content; prepare seed script solely for dev/test data, and tools to import partner data only with permission. Set analytics event naming and consent-aware aggregation, error logging without sensitive information. Check actual Google Play policies and target SDK again.

## Required acceptance criteria
External shared URL opens corresponding object safely, gated object doesn't leak restricted info, account deletion/logout/blocked flows work, pilot setup does not assume partner authorization.

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
6. **Next prompt** (`20` if not final) and why this step is ready.
