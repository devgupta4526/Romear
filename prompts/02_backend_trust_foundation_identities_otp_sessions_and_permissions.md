# PROMPT 02 — Backend trust foundation, identities, OTP, sessions and permissions

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Define users, auth identities, OTP challenges, sessions, verification flags, device sessions, terms acceptance, moderation reports, blocks, audit log, base role memberships. Build strict OTP request/verify/refresh/logout/session revoke endpoints, rate limits, TTL, retry limits, replay protection, hashed refresh token rotation and CSRF/security considerations where applicable. Integrate real provider adapter with disabled production mode until credentials supplied; explicit local-only fixed test accounts and OTP hook gated by ENV=development. 18+ eligibility uses DOB on backend (date only, encrypted/sensitive handling appropriate). Add Pydantic schemas, error codes (401/403/409/422/429), permission tests, migrations and safe session persistence contract for Android. No client-owned claims of verification. Establish moderation admin auth roles.

## Required acceptance criteria
Invalid/expired OTP never returns token; no fake successful auth on network error; token revocation test, rate limit test, underage test, new migration on clean DB and login API integration tests all pass.

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
6. **Next prompt** (`03` if not final) and why this step is ready.
