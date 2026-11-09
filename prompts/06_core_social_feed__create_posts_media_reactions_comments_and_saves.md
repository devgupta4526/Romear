# PROMPT 06 — Core social feed: create posts, media, reactions, comments and saves

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Add posts with text/photographs, author, created_at, visibility, moderation status, optional linked venue/club/event/pool and voluntary coarse city tag. Image upload via signed URLs/object store; validate MIME/type/size and stripping of sensitive metadata. Backend endpoints for create/edit/delete posts, paginated Following and For You (simple relevance, transparent rules, no fake popularity), comments and reactions/saves, report content and author, disable/mute. Android Home with feed selector For You/Following/Nearby (privacy-safe city only), rich post card, full post detail/comment screen, composer with preview and Photo Picker, saved collection list, upload progress and retry. Seed local sample posts only in explicit debug preview. Report/block controls accessible for every post.

## Required acceptance criteria
User A post visible to authorized User B; blocked/deleted/moderated content removed; correct pagination; uploading fails cleanly without ghost post; no real data assumed for empty feed.

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
6. **Next prompt** (`07` if not final) and why this step is ready.
