# PROMPT 03 — First-launch onboarding and return-user session flow

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Implement splash → welcome → phone entry → six-digit OTP → DOB/18+ → city and optional neighborhood selection → interest selection (3 to 8) → minimal profile username/name/photo optional → terms/guidelines → optional notification/location permission education → Home. Returning user skips completed steps based on server account state only. Avoid hard-failing if precise location declined; manual Nagpur selection is first-class. Android OTP auto-fill if available without reading SMS permission; resend cooldown, loading, wrong OTP, account suspended, network failure, retry and session restoration. HTTP DTOs from OpenAPI, Hilt repositories, encrypted token storage (best practices), DataStore for nonsecrets; Photo Picker for avatar. Backend profile onboarding endpoints + state transitions. Consent version tracking and privacy defaults.

## Required acceptance criteria
New and returning flows persist across restart; permission denial works; failed OTP cannot enter app; no active tokens when server denies; screenshots for each onboarding screen.

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
6. **Next prompt** (`04` if not final) and why this step is ready.
