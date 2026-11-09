# Deployment boundary (not deployed)

Stage 00 provides a backend Dockerfile and documented Render path; no infrastructure
or paid service has been created. Build context is `backend/`. The image runs as a
non-root user. Configure a Render web service with root directory `backend`, build
`pip install -r requirements.lock && pip install --no-deps .`, start
`uvicorn app.main:create_app --factory --host 0.0.0.0 --port $PORT --no-access-log`.
Use managed PostgreSQL, never a local production SQLite file or local media disk.

Set `PYTHON_VERSION=3.14.3` for the native service to match the tested runtime.
The start command follows [Render's FastAPI deployment guidance](https://render.com/docs/deploy-fastapi),
adapted to this repository's application factory.

Set `ROMEAR_ENV=staging` or `prod`, `ROMEAR_ALLOW_TEST_DATA=false`, and an explicit
`ROMEAR_DATABASE_URL=postgresql+psycopg://<user>:<password>@<host>:5432/<database>?sslmode=require`.
Set JSON `ROMEAR_CORS_ORIGINS` to the exact HTTPS
dashboard origins. The app rejects dev credentials, non-TLS DB and unsafe CORS outside
dev. Store secrets in provider settings, never repository files. Run `alembic upgrade
head` as a separate pre-deploy command using authorized migration credentials.
Configure readiness path `/ready`; `/health` only proves the process started.

Public HTTPS, rate limits, managed backups, restore drills, monitoring, secrets
rotation and release signing remain deployment gates. No production domain is owned
or assumed by this starter. Android staging/release default to reserved `.invalid`
hosts; supply `-PSTAGING_API_URL=https://<configured-host>/` or
`-PPROD_API_URL=https://<configured-host>/`. Configure release signing outside Git.
Unsigned builds are validation artifacts, not publishable releases.

Dashboard: `npm ci`, set `VITE_API_BASE_URL` to the HTTPS API, then `npm run build`.
Host `dist/` as static content. Vite environment values are public; never put secrets
in them. No account or management function is enabled in this foundation.

Rollback: deploy the previous compatible application build. Do not automatically
downgrade production data. The Stage 00 migration has a tested downgrade path for
disposable/local databases; later migrations need their own data-safe procedures.
