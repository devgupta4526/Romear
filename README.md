# ROMEAR

A city-first social network starting in Nagpur. **Stage 00 only:** a native Android
empty shell, an authoritative API/database foundation and one business web placeholder.
There are no accounts, social records, bookings, payments or management features yet.

See [build evidence and blockers](docs/BUILD_STATUS.md), [architecture decision](docs/ADR_001_FOUNDATION.md),
[API conventions](docs/API_CONVENTIONS.md) and [deployment boundary](docs/DEPLOYMENT.md).
Device validation is handed to the owner in [Android manual QA](docs/ANDROID_MANUAL_QA.md).
The project contract is [AGENTS.md](AGENTS.md); implementation stops after prompt 00.

## Requirements

- Windows PowerShell 7 (commands below), Git, Python **3.14**, Node **24**, npm.
- Docker Desktop with Linux containers running; local PostgreSQL 17 is also supported.
- JDK 21, Android SDK platform 36/build-tools 36.0.0 and platform-tools. Set `JAVA_HOME`
  and `ANDROID_HOME` or create ignored `android/local.properties` with `sdk.dir`.
- Free disk space for Gradle dependencies, Docker and an optional emulator. The default
  caches and AVDs use C: on Windows even when the repository is on E:.

## Install and migrate

From the repository root:

```powershell
./scripts/bootstrap.ps1
./scripts/db.ps1
```

Bootstrap creates `.env` from `.env.example` only when missing, a local Python venv,
installs the exact Python lock and runs `npm ci`. It never starts business actions
or seeds data. `db.ps1` starts PostgreSQL and explicitly applies Alembic migrations.
The example DB password is for loopback local development only. Do not deploy it.

Manual equivalent:

```powershell
Copy-Item .env.example .env # only if .env does not already exist
python -m venv backend/.venv
backend/.venv/Scripts/python.exe -m pip install -r backend/requirements.lock
backend/.venv/Scripts/python.exe -m pip install --no-deps -e backend
docker compose up -d --wait postgres
cd backend
.venv/Scripts/python.exe -m alembic upgrade head
.venv/Scripts/python.exe -m alembic current
```

Start API from `backend/`, in its own terminal:

```powershell
.venv/Scripts/python.exe -m uvicorn app.main:create_app --factory --host 0.0.0.0 --port 8000 --log-level info --no-access-log
```

Binding all interfaces is for emulator access on a trusted development network; for
host-only work use `--host 127.0.0.1`. The app emits redacted structured logs instead
of URL-bearing access logs. Open [Swagger](http://localhost:8000/v1/docs),
[health](http://localhost:8000/health), [readiness](http://localhost:8000/ready) or
[schema](http://localhost:8000/v1/openapi.json). A running API with a missing/stale DB
returns healthy liveness and **503 readiness**. That is expected until migrations pass.

## Android

From `android/`:

```powershell
./gradlew.bat :app:assembleDebug :app:testDebugUnitTest :app:lintDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n app.romear.dev/app.romear.MainActivity
```

Open `android/` in Android Studio, select a device, and Run also works. The single
`shellFragment` shows the branded empty state. **Check connection** calls the actual
API `/ready`; it does not create content or pretend registration exists.
Default emulator URL: `http://10.0.2.2:8000/`. For USB devices:

```powershell
adb reverse tcp:8000 tcp:8000
./gradlew.bat :app:assembleDebug -PDEV_API_URL=http://127.0.0.1:8000/
```

Variants: `assembleDebug` = dev, `assembleStaging` = staging, `assembleRelease` = prod.
Override endpoints with `-PDEV_API_URL=.../`, `-PSTAGING_API_URL=https://.../`,
`-PPROD_API_URL=https://.../`. Non-dev defaults intentionally use reserved `.invalid`
domains; configure real HTTPS before deployment. No production signing credentials
are supplied; staging/release build validation produces unsigned artifacts.

## Business web

In a separate terminal from the root:

```powershell
cd business-web
npm ci
Copy-Item .env.example .env.local # only if missing
npm run dev
```

Open [local dashboard foundation](http://localhost:5173). The `/` placeholder contains
one real readiness action, no invented counts or enabled business operations.
`npm run typecheck`, `npm test` and `npm run build` validate this starter.

## Checks and PostgreSQL integration

```powershell
./scripts/check.ps1
```

Without `ROMEAR_TEST_DATABASE_URL`, PostgreSQL integration is explicitly **skipped**;
unit tests do not imply migrations passed. To run the integration suite, create a
new empty disposable DB whose name ends in `_test` (never your real application DB):

```powershell
docker compose exec postgres sh -c 'createdb -U "$POSTGRES_USER" romear_test'
$env:ROMEAR_TEST_DATABASE_URL = 'postgresql+psycopg://romear_local:local_development_only@localhost:5432/romear_test'
./scripts/check.ps1 -Integration
```

The integration test requires a blank DB and exercises upgrade, repeat upgrade,
metadata agreement, real readiness, UTC, rollback, downgrade and re-upgrade. It
leaves that test schema migrated. Use a new empty DB for each later invocation, or
deliberately drop/recreate **only that disposable test DB** yourself. Do not delete
Docker volumes containing wanted data. `docker compose down` preserves the local DB.
For connected-device tests: `./scripts/check.ps1 -Device`. No emulator screenshots
are claimed unless a device actually ran the current build.

On macOS/Linux use `.venv/bin/python`, create the venv/install dependencies manually,
and run `bash scripts/check.sh`. The committed Gradle wrapper supports `./gradlew`.
CI checks backend/PostgreSQL, generated schema consistency, web and Android builds.

If C: is full, move **this task's new caches** to available workspace storage before
running commands; do not delete unrelated files:

```powershell
New-Item -ItemType Directory -Force artifacts/tmp | Out-Null
$env:TEMP = "$PWD/artifacts/tmp"
$env:TMP = $env:TEMP
$env:GRADLE_USER_HOME = "$PWD/.gradle"
$env:npm_config_cache = "$PWD/artifacts/npm-cache"
```

Regenerate schema: from `backend`, run `.venv/Scripts/python.exe scripts/export_openapi.py`;
from `business-web`, run `npm run api:generate`. Recheck/commit both artifacts together.
Dependency updates are intentional: regenerate the Python lock with
`backend/scripts/lock_dependencies.py` in the tested venv and rerun all checks.
No external OTP, media or payment integration is configured at this stage.
