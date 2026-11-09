$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
if (!(Test-Path .env)) { Copy-Item .env.example .env }
python -m venv backend/.venv
if ($LASTEXITCODE) { throw 'Python venv failed' }
& backend/.venv/Scripts/python.exe -m pip install -r backend/requirements.lock
if ($LASTEXITCODE) { throw 'Backend dependency installation failed' }
& backend/.venv/Scripts/python.exe -m pip install --no-deps -e backend
if ($LASTEXITCODE) { throw 'Backend installation failed' }
Push-Location business-web
try {
    npm ci
    if ($LASTEXITCODE) { throw 'Web dependency installation failed' }
} finally { Pop-Location }
Write-Output 'Dependencies installed. Start Docker, then run scripts/db.ps1 and scripts/check.ps1.'
