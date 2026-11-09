# PROMPT 08 — Ordinary-user Pools: create, request to join, host approval, capacity and chat

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Build Pools as casual user activities independent of official club events. Any eligible 18+ user creates a Pool: title/activity, description, public place/meeting instructions, local date/time & timezone, optional ability level, capacity_total including creator, approval policy (default request-only), expiry/cancellation policy. Example table tennis Pool 4 total = 1 organizer + 3 openings. Android: Pools Explore, Create Pool wizard, Pool Detail, Request to Join note, My Pools (hosting/joined/pending), Host Approval Queue, accepted group chat and participant list. Backend: pools, membership requests, audit history, transactional capacity reservations, approve/decline/cancel/leave/remove, publish only when valid; membership grants chat access. No tickets or paid event tiers for ordinary Pools. Default location displayed only after approval if sensitive; public venue summary remains approximate. Race conditions and duplicate requests must be tested.

## Required acceptance criteria
With 4 capacity, host + exactly 3 approved, fourth concurrent approval blocked (409), pending != joined; rejected/cancelled cannot message; host actions survive refresh and different devices.

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
6. **Next prompt** (`09` if not final) and why this step is ready.
