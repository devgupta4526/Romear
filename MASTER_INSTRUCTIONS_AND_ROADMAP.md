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


---

# ROMEAR BUILD SEQUENCE — START HERE

**Start from a blank repository**. Copy `AGENTS.md` and the `specs/` folder to the repository root. Put the reference boards in `design_reference/` (optional). Give Codex `prompts/00_....md` (or paste its contents), wait for an actual implementation and test results, then give `01`, etc. **Do NOT give it the full kit as one huge task.**

All prompts are also concatenated in `ALL_PROMPTS_IN_ORDER.md` for offline reading. The individual files are canonical and easier to execute.

## Build timeline (dependency order)

| Step | Deliverable | Product unlocked |
|---|---|---|
| 00 | Repository bootstrap, delivery discipline and local development | Foundation |
| 01 | Visual language, reusable XML components and navigation shell | Foundation |
| 02 | Backend trust foundation, identities, OTP, sessions and permissions | Foundation |
| 03 | First-launch onboarding and return-user session flow | Foundation |
| 04 | User profiles, interests, follows, mutual connections and safety | Core social |
| 05 | Inbox and real, permission-gated messaging foundation | Core social |
| 06 | Core social feed: create posts, media, reactions, comments and saves | Core social |
| 07 | Explore unified discovery, search, filters, and relevant recommendations | Core social |
| 08 | Ordinary-user Pools: create, request to join, host approval, capacity and chat | Pools |
| 09 | Clubs: pages, memberships, organizer roles and verification gate | Clubs and Events |
| 10 | Club-only official events, RSVPs, waitlists and organizer event tools | Clubs and Events |
| 11 | Cafés and venues: business claims, real inventory and reservation flows | Venues/Partnerships |
| 12 | Club–venue partnerships and co-branded collaborative events | Venues/Partnerships |
| 13 | Unified Plans, activity notifications and reminders | Plans/Passport |
| 14 | Experience Passport, voluntary history, privacy-safe map and achievements | Plans/Passport |
| 15 | Stories, daily activity updates and shared media memories | Media/Commerce |
| 16 | Real payments: paid event tickets, deposits, QR validation and refunds | Media/Commerce |
| 17 | Freemium ROMEAR Plus and promoted content with clear labeling | Media/Commerce |
| 18 | Organizer, Venue and platform-admin web dashboards | Operations/Launch |
| 19 | Deep links, sharing, anti-abuse and Nagpur launch readiness | Operations/Launch |
| 20 | Whole-app audit, release verification, performance and rollout | Operations/Launch |

## What to paste first into Codex

```text
You are building a BRAND-NEW ROMEAR monorepo from scratch. Read AGENTS.md, specs/DESIGN_SYSTEM.md, specs/USER_JOURNEYS.md and specs/QUALITY_GATES.md first. Then implement the entire contents of prompts/00_repository_bootstrap_delivery_discipline_and_local_development.md. Do not start Phase 01 until Phase 00 builds and its acceptance criteria are verified. Deliver real working code, not a plan or an imitation screen. Use Kotlin+XML Android, FastAPI+Postgres, Render deployability, no Firebase auth/database/storage, and warm cream/forest/terracotta UI. At the end list files changed, commands run, tests and issues.
```

If that exact file name differs, use the 00-prefixed path shown in `prompts/`.

## The permanent Codex instruction for every next turn

```text
Continue the ROMEAR from-scratch implementation. Read AGENTS.md and the current repo first. Confirm the previous step's quality gates and outstanding blockers. Implement only the next numbered prompt completely as a vertical slice (Android XML + backend + migrations + tests, web admin if specified). Do not fabricate any successful auth, booking, chat, join, payment, verification or attendance. Preserve all prior functionality. Report tested results, not guesses. Update docs/BUILD_STATUS.md.
```

## Product rules Codex MUST preserve
- **Posts** by real users, **Pools** by eligible individual users, **official Events** by eligible verified clubs only.
- **Club event gate:** approved club + authorized organizer + **four** distinct, active phone-verified members; no event if only three.
- **Pool request:** creator included in total capacity, host approves; never a public ticketed event.
- **Cafés:** authentic venue availability with owner-authorized inventory; request or confirmation is not a payment.
- **Passport:** private by default; verified vs self-reported activity separate.
- **Subscriptions and ads:** later; keep core social and safety tools free; clearly label sponsored media.
- **No purple**; Android Kotlin XML; backend Render-deployable, no Firebase backend.

## Recommended working cadence
Use one Codex session per stage, check diffs and test results, commit the result, launch on emulator, and only then run the next stage. If Codex is overwhelmed within a stage, ask it to first finish the **backend and API tests** and then the **Android UI wiring** without marking the stage complete until both exist.

## Design boards
Reference screenshots are mood/structure examples, not Android assets to paste as backgrounds. Some earlier illustrative boards show non-Nagpur imagery or nonsensical AI-generated microcopy: use correct brand, Nagpur-focused city representation where authorized, and real data. Refer to `specs/DESIGN_SYSTEM.md` and `design_reference/README.md`.
