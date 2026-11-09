# PROMPT 16 — Real payments: paid event tickets, deposits, QR validation and refunds

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Add paid ticket tiers for eligible club Events and optional venue deposits only after payment provider selection and credentials; implement provider interface and sandbox first. Order model separate from booking/RSVP; quote server-side, inventory holds, idempotent checkout, payment webhook verification, transaction/receipt, QR issued only after success, single-use or attendance-state check-in validation, cancellation/refund request and status. Android: event ticket tier/quantity chooser, checkout, pending/failure/confirmed, My Tickets, ticket QR, refund help. Backend database transactions and consistent refunds; no payment amount trusted from Android; handle duplicate callbacks and abandoned checkouts. Keep paid functions disabled with clear UI until real PSP configured. Review applicable India payments/tax obligations before launch.

## Required acceptance criteria
Sandbox successful transaction creates confirmed ticket only after verified webhook; payment failure/timeout never creates confirmed pass; duplicate webhook idempotent; no overselling and cancellation/refund states tested.

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
6. **Next prompt** (`17` if not final) and why this step is ready.
