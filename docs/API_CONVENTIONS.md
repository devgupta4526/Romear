# API, schema and security conventions

Stage 00 exposes only these public read-only endpoints; authentication is deliberately
absent because no accounts or business actions exist:

| Method/path | Success | Failure | Policy |
| --- | --- | --- | --- |
| GET `/health` | `200 {"status":"ok"}` after lifespan startup | 503 before startup | Public liveness; does not imply DB readiness |
| GET `/ready` | `200 {"status":"ready"}` | 503 on DB outage, missing/stale migration | Public, no DB connection details returned |
| GET `/v1` | `200 {"service":"romear-api","api_version":"v1","stage":"00"}` | Standard errors | Public static API metadata |
| GET `/v1/openapi.json` | OpenAPI schema | Standard errors | Public machine contract |
| GET `/v1/docs` | Swagger UI in dev/staging | 404 in prod | Documentation only |

Readiness verifies `SELECT 1` and Alembic revision `0001_infrastructure`. It never
mutates records. Missing DB and errors are real failures, never demo fallbacks.
Connection, pool and statement timeouts bound database waits; callers have 10-second
timeouts and make checks only on explicit action. Production ingress must rate-limit
diagnostics and protect against volumetric abuse before internet exposure.

Examples:

```http
GET /ready
Accept: application/json
```

```json
{"error":{"code":"database_unavailable","message":"Database is not ready","request_id":"server-generated-uuid"}}
```

All errors use `error.code`, a safe human `message`, and generated `request_id`.
`X-Request-ID` matches that value. Unknown endpoints and wrong HTTP methods receive
404/405 envelopes. Validation errors use 422; unexpected server errors use a generic
500. No SQL, stack traces, request bodies, URLs, OTPs or credentials are logged.
Structured request records include only generated ID, method, status and duration.
Responses use `Cache-Control: no-store`. CORS is an explicit origin allowlist with
no credentials or wildcard; CORS does not replace authorization.

Future `/v1` business routes must require validated server-issued bearer credentials
by default, explicitly list their roles, and query resource ownership/membership,
blocks, privacy, revocation and account eligibility on the server. Missing/invalid
credentials: 401; denied role/access: 403 or privacy-preserving 404; conflicting stale
state/duplicate action: 409; abuse limits: 429 with Retry-After. Never grant access
from client flags or failed provider operations. Stage 00 does not mint tokens or
implement an OTP bypass. Age, consent, moderator access and privacy rules must be
tested when registration/UGC is introduced, not represented as completed here.

Database names use snake_case; API fields use snake_case. Future resources use
opaque server-generated identifiers, UTC-aware `timestamptz` at rest and ISO 8601
UTC strings (`Z`) over HTTP. User presentation uses an IANA venue timezone, initially
`Asia/Kolkata`. Never interpret naive local timestamps as UTC. Location city and
neighborhood remain distinct from private coordinates/attendance.

Future list endpoints use keyset/cursor pagination with stable unique ordering:

```json
{"items":[],"next_cursor":null,"has_more":false}
```

`limit` defaults to 20, range 1–100; opaque cursor length <=512. No list endpoint is
introduced in Stage 00. Inventory/payment writes will require server-side idempotency,
transactions/locking and race tests at the relevant stage; none exists here.

Export schema from `backend`: `.venv/Scripts/python.exe scripts/export_openapi.py`.
Then from `business-web`: `npm run api:generate`. CI rejects schema/type drift.
Android DTO tests verify the actual `/ready` contract and malformed/failed responses.
