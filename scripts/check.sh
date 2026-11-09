#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
(
  cd backend
  .venv/bin/python -m ruff check .
  .venv/bin/python -m ruff format --check .
  .venv/bin/python -m mypy app
  .venv/bin/python -m pytest -q
  .venv/bin/python scripts/export_openapi.py
)
(
  cd business-web
  npm run api:generate
  npm run typecheck
  npm test
  npm run build
)
(
  cd android
  ./gradlew :app:assembleDebug :app:testDebugUnitTest :app:lintDebug
)
