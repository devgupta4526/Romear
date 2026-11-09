# ADR 001: Native clients and an authoritative PostgreSQL API

Status: accepted for Stage 00, 10 November 2026.

ROMEAR begins as a monorepo: `android/`, `backend/`, `business-web/`. The supplied
project contract and specifications remain authoritative. No prior prototype code
or social seed data is imported.

Android uses Kotlin, XML Views, a single Activity, Fragments, Navigation Component,
ViewBinding, Hilt, a ViewModel/StateFlow, repository and Retrofit/OkHttp. Minimum SDK
26 keeps native APIs practical; compile/target SDK 36 meets the verified Play target
requirement. AGP 8.13.2, Gradle 8.13 and Kotlin 2.2.10 form a compatible explicit
toolchain. Java 21 runs Gradle; application bytecode targets Java 17. No Compose.
Room, DataStore, media loading and WorkManager arrive only with actual persisted
or deferred work. They are not needed for a stateless readiness check.

Debug is dev (`app.romear.dev`), staging is a non-debuggable optimized build
(`app.romear.staging`), release is prod (`app.romear`). Staging/prod require HTTPS;
unconfigured hosts use `.invalid` and cannot fabricate a successful connection.
No signing keys are included. Every build has `ALLOW_TEST_DATA=false`; any future
preview data must be in debug/tests, never a repository fallback. Runtime guard
also rejects enabling test data in non-dev/non-debug builds.

FastAPI/Pydantic v2, SQLAlchemy 2 and Alembic use PostgreSQL exclusively. Sessions
roll back uncommitted work on close. Migrations are explicit deployment actions;
API startup never auto-creates or seeds a schema. Liveness is separate from schema
and database readiness. The initial revision creates an empty infrastructure table
and Alembic version record, with no users, memberships, tokens or privileges.
Python 3.14 and exact dependency lock match the available runtime and CI.

React/TypeScript/Vite provides one responsive foundation route. Its API types are
generated from the checked-in OpenAPI artifact. No authentication or management
controls are represented as implemented.

No Firebase, payment, OTP, storage or deployment provider is contacted. Render
deployment is documented, not provisioned. PostgreSQL is locally bound to loopback.
Server-side configurable club threshold defaults to 4 and cannot go below 4 in v1;
membership and authorization enforcement belong to their future domain stages.

Tradeoff: Stage 00 has only an empty shell and diagnostic action. Full five-item
navigation, reusable product components and visual refinement remain Stage 01.
Stateless infrastructure endpoints are public. There are no business writes or
role-specific resources to expose. Authentication defaults and future permission
requirements are specified in `API_CONVENTIONS.md` before implementing them.

Sources checked during implementation:

- [Play target SDK requirements](https://developer.android.com/google/play/requirements/target-sdk)
- [AGP releases and compatibility](https://developer.android.com/build/releases/about-agp)
- [FastAPI lifespan and tests](https://fastapi.tiangolo.com/advanced/testing-events/)
