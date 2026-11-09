# PROMPT 07 — Explore unified discovery, search, filters, and relevant recommendations

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Search public posts, eligible people, real clubs, Pools, club events and venues with debounced query, paginated backend results, common filters (city/Nagpur, topic, type, date, open spots, interests), and privacy-safe people discovery. Android Explore landing with useful category tiles and recent/saved searches, list/card templates and filtering bottom sheets, empty states. Use relational indexed search initially (Postgres FTS/trigrams as justified); implement ranking that explains why people/events shown without bogus numerical match %. Do not expose contact info or exact nearby personal coordinates. Allow cross-linking from a post to linked Pool, club, event and café only when real server-backed object exists.

## Required acceptance criteria
Search results reconcile with real server state; age/privacy/block/visibility filters hold; unsupported categories show true empty/coming-later states not fabricated items.

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
6. **Next prompt** (`08` if not final) and why this step is ready.
