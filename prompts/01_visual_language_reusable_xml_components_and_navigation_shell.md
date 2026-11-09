# PROMPT 01 — Visual language, reusable XML components and navigation shell

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Implement forest/cream/terracotta design tokens as Android resource colors, dimensions, type styles, shapes, themes/day-night. Build reusable avatar, event/Pool/club/venue/post list cards, error/empty/offline/loading states, chips, buttons, headers, skeletons and confirmation state. Android single-activity plus ViewBinding Fragments: Home, Explore, Plans, Inbox, Profile reached via avatar; Create center action opens sheet with only authorized actions. Set up nested navigation graphs, deep link parser (placeholder routes safe until features exist), correct back/keyboard/insets. Use original screen XML components not screenshot images. Use design boards as references only; no production seeded cards. Create debug-only Android preview gallery with labeled mock data, isolated from app repositories. Validate tap targets, screen reader, font scaling and emulator layouts.

## Required acceptance criteria
Bottom navigation and create sheet function, screen states have source-of-truth models, screen preview gallery only in debug, dark/large-text supported, CI Android build passes.

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
6. **Next prompt** (`02` if not final) and why this step is ready.
