# PROMPT 00 — Repository bootstrap, delivery discipline and local development

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Set up a brand-new monorepo with `/android`, `/backend`, `/business-web`, `/docs`, `AGENTS.md`, Git ignore, `.editorconfig`, `.env.example`, README and reproducible scripts. Android Kotlin/XML starter app launches to a branded, accessible empty shell; backend FastAPI serves `/health`, `/ready` and `/v1` OpenAPI; Postgres local Docker Compose; SQLAlchemy session, initial Alembic revision and pytest. Business web gets a clean React+TypeScript bootstrapped placeholder route, not fake dashboard data. Establish CI for backend tests and Android build where environment supports it. Create `docs/BUILD_STATUS.md`, ADR 001 and API/schema convention, auth/error envelope, pagination envelope and UTC/timezone rules. No business features. Start by inspecting installed tools, Java, Gradle, Android SDK and Python rather than assuming paths. Ensure Gradle Kotlin DSL and version catalog are consistent. Configure dev/staging/prod variants and strict debug-only test data rules.

## Required acceptance criteria
`./gradlew :app:assembleDebug` succeeds when SDK present, `pytest` passes, local DB migrates from blank, `/health` reflects healthy startup, `.env.example` has no secrets, repo commands documented; no invented backend responses.

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
6. **Next prompt** (`01` if not final) and why this step is ready.
