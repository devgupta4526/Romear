# ROMEAR build progress

Stage 00 implementation and verification, 10 November 2026 (Asia/Kolkata).

| Stage | Status | Verified checks | Issues/next action |
|---|---|---|---|
| 00 | PARTIAL — implementation and local build checks finished | Android debug/staging/release/test APK builds; 3 Android unit tests; lint 0 errors; backend lint/typecheck/13 tests including PostgreSQL; web typecheck/5 tests/build; live API readiness | Device testing delegated to owner; Docker engine unavailable; remote CI result unverified |
| 01 onward | NOT STARTED | None | Requires explicit owner approval; no later-stage business implementation |

## Implemented scope

- Android native Kotlin/XML single-Activity shell, `shellFragment` in `main_nav.xml`,
  `activity_main.xml`, `fragment_shell.xml`; original vector icon and warm tokens.
  Hilt/ViewModel/StateFlow/repository/Retrofit; real `/ready` check with empty,
  checking, ready, unavailable and network failure states. Edge-to-edge insets,
  scrollable large text, 48dp button and polite status announcements.
- Debug/dev, staging and release/prod configurations; HTTPS/non-debug constraints
  and disabled test data in all variants. Version catalog and checksum-pinned wrapper.
- FastAPI `/health`, `/ready`, `/v1`, `/v1/openapi.json` and dev/staging `/v1/docs`.
  No accounts, sessions, auth bypass, social or business endpoints.
- PostgreSQL SQLAlchemy sessions; `0001_infrastructure` creates empty
  `infrastructure_metadata` with UTC-aware timestamp and Alembic version record.
  Readiness checks real connectivity and exact revision. No data seeding.
- React/TypeScript `/` business foundation with real readiness action and generated
  OpenAPI types. No business counters, transactions or management controls.
- Loopback Docker Compose, backend Dockerfile, CI, exact dependency locks, setup/check
  scripts, ADR 001, API/security/timezone/pagination and deployment documentation.

## Security boundaries

Public diagnostics are read-only; unsupported mutation methods and unknown domain
routes are denied. Test coverage includes missing startup, DB outage, stale schema,
repeated health checks, failed/unexpected responses, private exception redaction,
untrusted CORS, pagination bounds and non-dev test-data/unsafe-config rejection.
Real PostgreSQL verifies migration idempotency and uncommitted transaction rollback.
Role, blocked-user, token, inventory, membership and payment races are not applicable
to Stage 00 because those resources do not exist; they remain gates of future stages.
No Firebase, Compose, payment, OTP, object storage or fabricated provider successes.

Production deployment, signing, public domains, OTP/media/payment provider credentials
are not configured or claimed. Rate limiting at ingress and production operations
are deployment gates described in DEPLOYMENT.md.

## Evidence so far

Commands are relative to the repository root unless a working directory is listed.

| Working directory | Exact command | Actual result |
|---|---|---|
| root | `java -version` | Temurin 21.0.11 |
| root | `python --version` | Python 3.14.3 |
| root | `node --version`; `npm --version` | Node 24.14.0; npm 11.9.0 |
| root | `docker version` / `docker info` | Client 29.2.1; daemon pipe missing |
| root | `adb devices -l` | Initially empty; isolated E: emulator later connected |
| root | `python -m venv backend/.venv` | Passed |
| root | `backend/.venv/Scripts/python.exe -m pip install -e './backend[dev]'` | Passed; exact versions recorded in requirements.lock |
| backend | `.venv/Scripts/python.exe -m ruff check .` | Passed |
| backend | `.venv/Scripts/python.exe -m ruff format --check .` | Passed |
| backend | `.venv/Scripts/python.exe -m mypy app` | Passed, 5 source files |
| backend | `.venv/Scripts/python.exe -m pytest -q` | Final run: 13 passed with real PostgreSQL test URL; previous unconfigured run explicitly skipped integration |
| backend | `.venv/Scripts/python.exe -m alembic upgrade head --sql` | Passed; PostgreSQL DDL generated, not counted as DB execution |
| backend | `.venv/Scripts/python.exe -m alembic upgrade head` | Passed on blank local PostgreSQL 17.6 DB |
| backend | `.venv/Scripts/python.exe -m alembic current` | `0001_infrastructure (head)` |
| backend | `.venv/Scripts/python.exe -m alembic check` | No new upgrade operations detected |
| backend | `.venv/Scripts/python.exe scripts/export_openapi.py` | Generated docs/openapi.json |
| root | `backend/.venv/Scripts/python.exe -m pip check` | No broken requirements |
| business-web | `npm install` | Installed 121 packages, audit 0 vulnerabilities |
| business-web | `npm run api:generate` | Generated src/api/schema.d.ts from backend artifact |
| business-web | `npm run typecheck` | Passed |
| business-web | `npm test` | 5 passed; one concurrent retry hit host `spawn UNKNOWN`, subsequent standalone run passed |
| business-web | `npm run build` | Passed, 30 modules transformed |
| root | `docker compose config --quiet` | Passed after creating ignored .env from example; initial missing-env failure expected |
| root | `Invoke-RestMethod http://localhost:8000/health` | Actual HTTP success: status ok |
| root | `Invoke-RestMethod http://localhost:8000/ready` | Actual HTTP success: status ready after migrations |
| root | `Invoke-RestMethod http://localhost:8000/v1` | Actual service/API/stage metadata |
| android | `./gradlew.bat :app:assembleDebug :app:testDebugUnitTest :app:lintDebug` | Initial wrapper extraction failed: C: full; second run reached kapt then JVM native out-of-memory |
| android | `./gradlew.bat --no-daemon :app:assembleDebug :app:testDebugUnitTest :app:lintDebug :app:assembleDebugAndroidTest :app:assembleStaging :app:assembleRelease` | BUILD SUCCESSFUL in 4m 57s; 204 tasks (135 executed/69 up-to-date); all variants, 3 unit tests and lint (0 errors/30 warnings) passed |
| root | `docker compose up -d --wait postgres` | Failed: Docker Desktop Linux engine named pipe missing |
| root | `C:/Program Files/Git/bin/bash.exe -n scripts/check.sh` | Passed syntax validation |
| root | PowerShell `Language.Parser.ParseFile` for scripts/*.ps1 | All 3 scripts passed syntax validation |
| root | `git diff --cached --check -- android backend business-web docs scripts .github README.md compose.yaml .env.example .editorconfig .gitattributes .gitignore` | Passed for Stage 00 implementation; untouched supplied ALL_PROMPTS_IN_ORDER.md has a pre-existing blank EOF line |

Local DB verification used official EDB PostgreSQL 17.6 Windows binaries under ignored
`artifacts/postgres/`, initialized under `artifacts/pgdata/`, bound **only** to
127.0.0.1:55432, without installing a system service. This isolated diagnostic cluster
uses local trust authentication, not the deployable configuration. Commands:

```powershell
./artifacts/postgres/pgsql/bin/initdb.exe -D ./artifacts/pgdata -U romear_local -A trust --encoding=UTF8 --locale=C
./artifacts/postgres/pgsql/bin/pg_ctl.exe -D ./artifacts/pgdata -l ./artifacts/postgres.log -o '-h 127.0.0.1 -p 55432' start
./artifacts/postgres/pgsql/bin/createdb.exe -h 127.0.0.1 -p 55432 -U romear_local romear_stage00_test
./artifacts/postgres/pgsql/bin/createdb.exe -h 127.0.0.1 -p 55432 -U romear_local romear
$env:ROMEAR_TEST_DATABASE_URL = 'postgresql+psycopg://romear_local@127.0.0.1:55432/romear_stage00_test'
$env:ROMEAR_DATABASE_URL = 'postgresql+psycopg://romear_local@127.0.0.1:55432/romear'
```

After adding a credential-redaction regression test, the final 13-test run used a
fresh empty `romear_final_test` database created with the same `createdb` command.
The only remaining backend warning is upstream Starlette's deprecation of its httpx
test adapter; tests actually pass. Alembic's path separator warning was fixed.

Android unit checks cover real HTTP success/503/401, missing and malformed JSON,
network IOException, duplicate checking, failure state and successful retry.
An initial test exposed malformed JSON being classified as offline; the repository
now catches malformed JSON before IOException and the regression tests pass.
Lint also caught an API-27-only navigation-bar theme item at minSdk 26; it was
removed because the edge-to-edge helper already handles navigation-bar appearance.
Remaining lint warnings are unsuppressed: newer dependency/toolchain versions,
target newer-than-36 advice (36 meets the verified current Play requirement), unused
foundation palette/spacing tokens, old-API accessibility-heading handling, backup
configuration advice and background overdraw. They are recorded rather than hidden
by a lint baseline. No claim of zero warnings or production release readiness.

**Owner instruction:** emulator/device tests are skipped at the owner's explicit
request. The existing emulator was stopped before final builds. An isolated AVD
connected during environment troubleshooting, but no app installation, instrumented
test run or screenshot review was performed. See ANDROID_MANUAL_QA.md for handoff.

The regular supported local path is Docker Compose and scripts/db.ps1. Docker Desktop
launch plus `docker desktop start` did not expose an engine, so container startup and
Docker image build are unverified. CI is defined but no remote CI pass is claimed.

Host constraints: initial C: free space was under 200MB. This task's Gradle cache,
temp directory, npm cache and new AVD were placed under ignored E: workspace folders.
Existing user AVDs/data were not moved or removed. The first Gradle compile crash
reported exhausted native memory/pagefile; retry uses 1536MB heap, two workers,
in-process Kotlin and no persistent daemon with emulator paused.

Build outputs (ignored in Git):

- `android/app/build/outputs/apk/debug/app-debug.apk` — install this for owner QA.
- `android/app/build/outputs/apk/staging/app-staging-unsigned.apk`.
- `android/app/build/outputs/apk/release/app-release-unsigned.apk`.
- `android/app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk` — compiled,
  **not run** on a device.
- `android/app/build/reports/tests/testDebugUnitTest/index.html` and
  `android/app/build/reports/lint-results-debug.html` — actual local reports.
- `business-web/dist/` — actual production web bundle.

See STAGE_00_FILES.md for the exact implementation file inventory. The supplied
contract/specs/prompt kit and design reference boards were preserved. Git excludes
local .env, SDK paths, venv/node_modules, caches, private keys and build/crash outputs;
staged source was checked for common private-key/token patterns without a match.

## Next step

Owner: run ANDROID_MANUAL_QA.md and verify Docker Compose startup after restoring
Docker Desktop. Review remote CI in GitHub. Do not start Stage 01 until the owner
explicitly approves. No previous working code existed, so no existing
feature regression is claimed; future UI/auth/business functionality is absent.
