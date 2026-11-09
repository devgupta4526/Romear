param([switch]$Integration, [switch]$Device)
$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
function Invoke-Checked([scriptblock]$Command) {
    & $Command
    if ($LASTEXITCODE) { throw "Check failed: $Command" }
}
Push-Location backend
try {
    Invoke-Checked { .venv/Scripts/python.exe -m ruff check . }
    Invoke-Checked { .venv/Scripts/python.exe -m ruff format --check . }
    Invoke-Checked { .venv/Scripts/python.exe -m mypy app }
    if ($Integration -and !$env:ROMEAR_TEST_DATABASE_URL) {
        throw 'Integration requires ROMEAR_TEST_DATABASE_URL pointing to a blank database ending in _test'
    }
    Invoke-Checked { .venv/Scripts/python.exe -m pytest -q }
    Invoke-Checked { .venv/Scripts/python.exe scripts/export_openapi.py }
} finally { Pop-Location }
Push-Location business-web
try {
    Invoke-Checked { npm run api:generate }
    Invoke-Checked { npm run typecheck }
    Invoke-Checked { npm test }
    Invoke-Checked { npm run build }
} finally { Pop-Location }
Push-Location android
try {
    Invoke-Checked { ./gradlew.bat :app:assembleDebug :app:testDebugUnitTest :app:lintDebug }
    if ($Device) { Invoke-Checked { ./gradlew.bat :app:connectedDebugAndroidTest } }
} finally { Pop-Location }
