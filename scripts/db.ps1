$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
docker compose up -d --wait postgres
if ($LASTEXITCODE) { throw 'PostgreSQL startup failed' }
Push-Location backend
try {
    & .venv/Scripts/python.exe -m alembic upgrade head
    if ($LASTEXITCODE) { throw 'Migration failed' }
} finally { Pop-Location }
