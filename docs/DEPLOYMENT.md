# Deployed backend: Render + Neon

Deployed on 10 November 2026 (Asia/Kolkata). Stage 00 only.

- API: https://romear-api.onrender.com
- Readiness: https://romear-api.onrender.com/ready
- OpenAPI: https://romear-api.onrender.com/v1/openapi.json
- Render dashboard: https://dashboard.render.com/web/srv-dbp2153rjlhs73d64vfg
- Confirmed workspace: My Workspace.
- Neon project: romear / twilight-tree-62576717, PostgreSQL 17, Singapore,
  production branch, database romear.
- Render service: romear-api / srv-dbp2153rjlhs73d64vfg, Singapore, free compute.
- Source: https://github.com/devgupta4526/Romear, main, auto-deploy enabled.

Native Python runtime: 3.14.3. Build command:

```sh
pip install -r backend/requirements.lock && pip install --no-deps ./backend
```

Start command:

```sh
cd backend && exec uvicorn app.main:create_app --factory --host 0.0.0.0 --port $PORT --no-access-log
```

Environment source of truth is Render's service settings: PYTHON_VERSION=3.14.3,
ROMEAR_ENV=prod, ROMEAR_ALLOW_TEST_DATA=false, ROMEAR_CORS_ORIGINS=[] and secret
ROMEAR_DATABASE_URL. The latter uses postgresql+psycopg and the direct Neon endpoint
with required TLS. No database password or connection string is in Git or Android.
A bounded SQLAlchemy connection pool supports this single-instance foundation.
Direct connections support the existing session timezone/timeout settings; review
these before switching to a transaction-mode pooler.

Migration 0001_infrastructure was applied explicitly to this NEW Neon database
using Alembic and a process-only environment variable. No existing user database
was modified and no domain data was seeded. Migrations do not run at startup.
Apply reviewed future migrations explicitly before rollout; free Render services
have no pre-deploy command. Never put migrations in the build command.

The MCP creation surface uses Render's default TCP health check. HTTP /ready was
verified independently. Set /ready as the Dashboard health-check path before a
production launch. The deployed service is a Stage 00 foundation only.

All Android variants default to the verified HTTPS API. DEV_API_URL can override
this for local development. Staging currently shares the Stage 00 database;
provision isolated environments before adding user data. The business web starter
still uses its local API by default. Add an actual HTTPS dashboard CORS origin
when one is deployed; native Android does not require CORS.

Free Render services and Neon idle compute can cold-start. If the first connection
check times out, retry after wake-up; no local success fallback exists. Release
signing is not configured. Emulator testing remains with the owner as requested.

Rollback does not reverse database changes: deploy a compatible earlier app build
and verify readiness. Local Compose and the Dockerfile remain available; the local
Docker engine blocker does not prevent this verified native-runtime deployment.
