# PROMPT 20 — Whole-app audit, release verification, performance and rollout

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Run a full dependency/migration audit, Android unit/UI/instrumented tests, backend integration/permission/concurrency tests, business-web tests, basic security review, release build with obfuscation and signing configuration (never include secret signing keys), staging deploy on Render, database migration strategy, backup/restore, rate limits, monitoring, alerting and rollback docs. Exercise end-to-end test journeys for new user→post→follow→message; Pool host→three approvals→full→group chat; three-to-four club verification threshold→event RSVP; café booking→venue approval; partnership→co-branded event; real ticket payment sandbox/QR; Passport privacy; moderation block/report. Generate runbook, known gaps and launch checklist. Evaluate retention measures but don't claim actual user metrics. Produce final API docs and Play Store readiness checklist, marking blocked merchant/SMS/media/map/push credentials precisely.

## Required acceptance criteria
Release candidate builds with all configured services; every critical scenario passes in staging; any untested external operation explicitly BLOCKED; no fake success paths remain.

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
6. **Next prompt** (`21` if not final) and why this step is ready.
