# PROMPT 10 — Club-only official events, RSVPs, waitlists and organizer event tools

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Implement event draft/publish/cancel/close under approved club only, enforce 4-member rule on creation/publish (document draft policy), owners/admins with organizer permission only. Events: details, capacity, public venue/partner, time zone, tiers marked FREE initially, attendee RSVP, waitlist, duplicate prevention, organizer approval where configured, organizer attendance list/check-in. Android: Events listing, event detail, free RSVP, QR/attendance pass tied to server signed token, My Plans link and event group chat (only valid members). Business web initially Club Event editor, attendee approvals/check-in and list using same API. Use atomic last-seat assignment, cancellation policy and reminders. Paid ticket tiers remain DISABLED until payments phase, never fake checkout success. Server handles eligibility change and existing confirmed events predictably; audit logs for state changes.

## Required acceptance criteria
A normal account's POST /v1/events returns 403; verified 3-member club fails; verified 4-member authorized club succeeds; no overbooking, no duplicate RSVP, check-in verifiable server-side.

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
6. **Next prompt** (`11` if not final) and why this step is ready.
