# PROMPT 15 — Stories, daily activity updates and shared media memories

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Add 24h ephemeral Stories and quick daily activity updates with upload/multi-image/text controls, optional tagged club/event/venue, mention consent, view/reply privacy rules, expiry and cleanup, report/block, moderation. Share a completed experience into feed/story via explicit user action; don't auto-publicize a meeting attendance. Android story tray, full-screen viewer with progress/pause/accessibility, add story, media selection, activity-share composer, simple collaborative album only with per-user photo permissions. Backend schedule cleanup job, rate limits, media access control. Feature flag video until real processing/moderation infrastructure is ready; do not implement fake short-video processing.

## Required acceptance criteria
Story expires on server, private story inaccessible to others, blocked user cannot view/reply, no leak of tagged person's exact venue/activity without consent.

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
6. **Next prompt** (`16` if not final) and why this step is ready.
