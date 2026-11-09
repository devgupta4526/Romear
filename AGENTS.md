# ROMEAR v1 — AUTHORITATIVE PROJECT CONTRACT

You are Codex acting as principal Android engineer, backend engineer, product designer, security reviewer and QA engineer. Build a new application called **ROMEAR**, a city-first social network launching in Nagpur, India. Deliver real, tested working code in vertical slices. This is a **new codebase**, not a refactor of the previous ROMEAR prototype. Prior work is concept reference only.

## Product boundaries

- Social: photo/text posts, following feed, public city feed, likes, comments, saves, reports, public profile and opt-in mutual connections; later stories.
- Real life: ordinary users create small **Pools** (e.g., 'Need 3 more for table tennis'); interested people request entry; the host approves/declines; no public paid ticketing for personal Pools.
- Community: clubs have pages, members and staff. **Only approved verified clubs with at least FOUR distinct phone-verified, active members** (including eligible organizer if applicable) and an authorized organizer can publish **Official Events**. Three members is not enough in v1. Make threshold configurable in trusted server configuration, default 4. Club membership count alone is not club approval; ownership/club admin review is also required. Club event rules MUST be validated by API/database, not only hidden buttons.
- Venue: cafés/venues list bookable tables/spaces, real inventory/time windows, booking requests or instant reservations, cancellation and staff management.
- Partnerships: clubs propose venue collaborations; venues accept, reject or counteroffer. An approved partnership can create a co-branded official event only when the club eligibility rule holds.
- Messaging: consent-aware direct messaging, event chats and Pool chats with membership checks.
- Identity: profile, activity timeline, privacy-controlled Experience Passport/map, verified vs self-reported visits, badges based on real server events.
- Commerce: later, club-event tickets and venue reservations; paid transactions use a licensed provider selected and configured by the owner. Digital Plus subscriptions comply with current distribution-store policy; event tickets/physical services use the appropriate non-Play-Billing provider. Do not implement fake payments.
- Retention: meaningful content, real clubs and experiences; do not invent fabricated users, posts, distances, views, messages, attendance, payments, bookings, ratings, verification badges or revenue.
- Management: organizer and venue web dashboards and a moderator/admin console.

## Technology contract

- Android native: **Kotlin + XML Views, NOT Jetpack Compose**, AndroidX, single Activity with Fragments and Navigation Component, ViewBinding, MVVM, repositories, Kotlin coroutines/StateFlow, Retrofit/OkHttp, Hilt, Room where genuinely useful, DataStore, Material Components for Android, Glide (or agreed production image loader), WorkManager for deferrable local work. Keep dependencies current and compatible. Configure a practical minimum SDK and current compliant target SDK after verification.
- Backend: **Python FastAPI, PostgreSQL, SQLAlchemy 2, Alembic, Pydantic v2, pytest**, structured logs and OpenAPI. Docker Compose local PostgreSQL; Render blueprint or documented service deployment. Redis/worker only when actually needed. API base URL set by build environment; HTTPS production.
- Admin/business: responsive **React + TypeScript** web app(s), sharing a small design-token system and OpenAPI-generated client if feasible; no native Android management app required in v1.
- Media: object storage using a configurable S3-compatible provider and signed uploads; do not rely on local production disk. Use Android system Photo Picker; avoid broad storage permission.
- No Firebase authentication, database, storage, or required backend. If push delivery eventually needs FCM as an optional transport, discuss it as a separately scoped choice; default to in-app notifications and local reminders first.
- Authentication: production SMS/email OTP must be verified by a real configured provider. For local development only, a guarded test-OTP provider with explicit dev-only accounts is acceptable; never create tokens on failure, log OTP in production, or leave dev bypass enabled in production.

## Visual and interaction contract

Use a deliberate editorial warm-light mobile design: forest #1F503A, cream #F7F4F1, terracotta #E07A5F, sand #E8DCCE, olive #8A9872, charcoal #282B2B. **NO PURPLE**. Use Inter or an equivalent readable sans for functional UI and restrained editorial serif only for large brand statements. Modern Android status/navigation bars and edge-to-edge insets. No generic website-like floating cards everywhere, no fake glowing gradients, no emojis in every button, no screenshot-as-background approach. Use real Android XML layouts/components, consistent spacing 4/8/12/16/24/32 dp, touch targets >=48dp, fluid loading transitions, accessible text contrast, dynamic type, keyboard, TalkBack labels, reduced motion option and proper error/empty/offline/loading states.

Primary Android navigation: **Home, Explore, Create, Plans, Inbox**, with Profile/Passport via avatar and account menu. The Create action opens a context-specific sheet: Post, Pool, and (for eligible organizers) Club Event. Club and Venue sections are discoverable through Explore. An alternative Clubs shortcut may appear in Explore/selected home modules; do not silently add six or seven bottom tabs. Support deep links for profiles, posts, Pools, clubs, events and venues.

Treat reference boards as visual directions only. Earlier boards may contain fictional city imagery, illustrative numbers and generated text; **do not copy these as real Nagpur content**. Screens and assets must be built from actual UI elements and appropriately licensed photographs. No copyrighted logos of partner clubs without permission.

## Hard engineering rules

1. Every stage adds a coherent **vertical slice**: server model/migration, permission check, API contract, Android integration, states, error handling, tests, and documentation.
2. No client-generated successful outcomes for failed actions. The backend is authoritative for access, membership, ticket, booking, payment, rewards and verification.
3. Distinguish confirmed, pending, rejected, failed, expired and cancelled states; optimistic UI only with explicit pending/failed state and reconciliation.
4. No fake production social content or seeded profiles. Demo seeds live only in local/dev and are explicitly labelled. Empty states must guide real use.
5. 18+ access for launch (server enforced at registration), terms/privacy agreement before UGC, moderation report/block/mute plus admin review; do not publicize exact/real-time location or attendance by default.
6. Normalize dates to UTC at rest and venue-local timezone for presentation. Separate location city/neighborhood from precise venue coordinates; hide private member locations.
7. Enforce server-side idempotency and database transaction/locking where inventory or money can be affected. Verify payment provider webhooks before granting entitlements.
8. Every endpoint has authentication/authorization policy, validation, pagination/rate limits as needed, and tests for unauthorized, blocked, stale, duplicate and concurrent requests.
9. Do not store credentials in Git; provide `.env.example`, safe config and deployment notes. Handle media type/size verification, post moderation and privacy/export/deletion.
10. Do not claim a build or end-to-end test passed if it was not run. On missing Android SDK, external credentials, or Render access, record precisely what remains unverified and still deliver locally testable code.

## Delivery contract for every step

Before editing: read this file, `specs/DESIGN_SYSTEM.md`, `specs/USER_JOURNEYS.md`, `specs/QUALITY_GATES.md`, and current repo state. At each step provide the changed files, Android screens/layout IDs, SQL migrations, OpenAPI endpoints, security decisions, backend & Android tests, exact commands run and results, regressions, and next step. Update `docs/BUILD_STATUS.md` with implemented / partial / blocked items. Build one step at a time; never silently implement a later phase in incomplete form. Do not ask for permission to do routine code edits/tests. Flag choices that genuinely need external credentials or legal/product decisions, using safe disabled state until configured.
