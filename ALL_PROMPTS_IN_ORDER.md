# ROMEAR — ALL 21 SEQUENTIAL CODEX PROMPTS

Read `AGENTS.md`, `specs/` before each stage. Paste exactly one numbered prompt at a time into Codex. Do not ask Codex to execute all 21 in one run.

# PROMPT 00 — Repository bootstrap, delivery discipline and local development

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Set up a brand-new monorepo with `/android`, `/backend`, `/business-web`, `/docs`, `AGENTS.md`, Git ignore, `.editorconfig`, `.env.example`, README and reproducible scripts. Android Kotlin/XML starter app launches to a branded, accessible empty shell; backend FastAPI serves `/health`, `/ready` and `/v1` OpenAPI; Postgres local Docker Compose; SQLAlchemy session, initial Alembic revision and pytest. Business web gets a clean React+TypeScript bootstrapped placeholder route, not fake dashboard data. Establish CI for backend tests and Android build where environment supports it. Create `docs/BUILD_STATUS.md`, ADR 001 and API/schema convention, auth/error envelope, pagination envelope and UTC/timezone rules. No business features. Start by inspecting installed tools, Java, Gradle, Android SDK and Python rather than assuming paths. Ensure Gradle Kotlin DSL and version catalog are consistent. Configure dev/staging/prod variants and strict debug-only test data rules.

## Required acceptance criteria
`./gradlew :app:assembleDebug` succeeds when SDK present, `pytest` passes, local DB migrates from blank, `/health` reflects healthy startup, `.env.example` has no secrets, repo commands documented; no invented backend responses.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`01` if not final) and why this step is ready.


---

# PROMPT 01 — Visual language, reusable XML components and navigation shell

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Implement forest/cream/terracotta design tokens as Android resource colors, dimensions, type styles, shapes, themes/day-night. Build reusable avatar, event/Pool/club/venue/post list cards, error/empty/offline/loading states, chips, buttons, headers, skeletons and confirmation state. Android single-activity plus ViewBinding Fragments: Home, Explore, Plans, Inbox, Profile reached via avatar; Create center action opens sheet with only authorized actions. Set up nested navigation graphs, deep link parser (placeholder routes safe until features exist), correct back/keyboard/insets. Use original screen XML components not screenshot images. Use design boards as references only; no production seeded cards. Create debug-only Android preview gallery with labeled mock data, isolated from app repositories. Validate tap targets, screen reader, font scaling and emulator layouts.

## Required acceptance criteria
Bottom navigation and create sheet function, screen states have source-of-truth models, screen preview gallery only in debug, dark/large-text supported, CI Android build passes.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`02` if not final) and why this step is ready.


---

# PROMPT 02 — Backend trust foundation, identities, OTP, sessions and permissions

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Define users, auth identities, OTP challenges, sessions, verification flags, device sessions, terms acceptance, moderation reports, blocks, audit log, base role memberships. Build strict OTP request/verify/refresh/logout/session revoke endpoints, rate limits, TTL, retry limits, replay protection, hashed refresh token rotation and CSRF/security considerations where applicable. Integrate real provider adapter with disabled production mode until credentials supplied; explicit local-only fixed test accounts and OTP hook gated by ENV=development. 18+ eligibility uses DOB on backend (date only, encrypted/sensitive handling appropriate). Add Pydantic schemas, error codes (401/403/409/422/429), permission tests, migrations and safe session persistence contract for Android. No client-owned claims of verification. Establish moderation admin auth roles.

## Required acceptance criteria
Invalid/expired OTP never returns token; no fake successful auth on network error; token revocation test, rate limit test, underage test, new migration on clean DB and login API integration tests all pass.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`03` if not final) and why this step is ready.


---

# PROMPT 03 — First-launch onboarding and return-user session flow

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Implement splash → welcome → phone entry → six-digit OTP → DOB/18+ → city and optional neighborhood selection → interest selection (3 to 8) → minimal profile username/name/photo optional → terms/guidelines → optional notification/location permission education → Home. Returning user skips completed steps based on server account state only. Avoid hard-failing if precise location declined; manual Nagpur selection is first-class. Android OTP auto-fill if available without reading SMS permission; resend cooldown, loading, wrong OTP, account suspended, network failure, retry and session restoration. HTTP DTOs from OpenAPI, Hilt repositories, encrypted token storage (best practices), DataStore for nonsecrets; Photo Picker for avatar. Backend profile onboarding endpoints + state transitions. Consent version tracking and privacy defaults.

## Required acceptance criteria
New and returning flows persist across restart; permission denial works; failed OTP cannot enter app; no active tokens when server denies; screenshots for each onboarding screen.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`04` if not final) and why this step is ready.


---

# PROMPT 04 — User profiles, interests, follows, mutual connections and safety

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Develop edit profile, public profile, private visibility defaults, photo gallery, usernames, interests, social following/unfollowing, mutual connection request/accept/decline, counters based on DB, blocked-users management, profile moderation report, privacy settings. Screens: My Profile, Edit Profile, Public Profile, Followers/Following, Incoming Requests, Interests, privacy controls. API: GET/PUT /v1/me, GET /v1/users/{id}, follow endpoints, connection requests and blocks. Filter sensitive fields based on visibility; server checks blocked relationships on all later social queries and chat. Include realistic empty states and no invented follower counts. Support basic share profile link.

## Required acceptance criteria
Two-account tests: blocked user sees appropriate restricted view and cannot connect/message; follow counts reconcile on refresh; all UI fields from server with correct privacy; photo removal works.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`05` if not final) and why this step is ready.


---

# PROMPT 05 — Inbox and real, permission-gated messaging foundation

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Implement server conversation/message models, conversation membership roles, direct connection chat eligibility, group conversation keyed to purpose (pool_id,event_id), message send/list/unread/mark-read, ordering/pagination, safe attachments hook, message delivery states. Android inbox list, direct chat, group chat, composer, failure/retry, unread badges, attachments disabled until implemented. Prefer WebSockets with authenticated session + reconnect and bounded fallback polling, or initially efficient paginated refresh with explicit lifecycle; make architecture extensible. Backend membership checked on every read/send, block enforcement, revoked access on leave/remove, moderation report and rate limit. No canned replies or demo-id special cases.

## Required acceptance criteria
Messages persist across reinstall and second device; rejected message visibly fails; unauthorized conversations return 403; blocking prevents messages; chat list updates correctly.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`06` if not final) and why this step is ready.


---

# PROMPT 06 — Core social feed: create posts, media, reactions, comments and saves

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Add posts with text/photographs, author, created_at, visibility, moderation status, optional linked venue/club/event/pool and voluntary coarse city tag. Image upload via signed URLs/object store; validate MIME/type/size and stripping of sensitive metadata. Backend endpoints for create/edit/delete posts, paginated Following and For You (simple relevance, transparent rules, no fake popularity), comments and reactions/saves, report content and author, disable/mute. Android Home with feed selector For You/Following/Nearby (privacy-safe city only), rich post card, full post detail/comment screen, composer with preview and Photo Picker, saved collection list, upload progress and retry. Seed local sample posts only in explicit debug preview. Report/block controls accessible for every post.

## Required acceptance criteria
User A post visible to authorized User B; blocked/deleted/moderated content removed; correct pagination; uploading fails cleanly without ghost post; no real data assumed for empty feed.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`07` if not final) and why this step is ready.


---

# PROMPT 07 — Explore unified discovery, search, filters, and relevant recommendations

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Search public posts, eligible people, real clubs, Pools, club events and venues with debounced query, paginated backend results, common filters (city/Nagpur, topic, type, date, open spots, interests), and privacy-safe people discovery. Android Explore landing with useful category tiles and recent/saved searches, list/card templates and filtering bottom sheets, empty states. Use relational indexed search initially (Postgres FTS/trigrams as justified); implement ranking that explains why people/events shown without bogus numerical match %. Do not expose contact info or exact nearby personal coordinates. Allow cross-linking from a post to linked Pool, club, event and café only when real server-backed object exists.

## Required acceptance criteria
Search results reconcile with real server state; age/privacy/block/visibility filters hold; unsupported categories show true empty/coming-later states not fabricated items.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`08` if not final) and why this step is ready.


---

# PROMPT 08 — Ordinary-user Pools: create, request to join, host approval, capacity and chat

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Build Pools as casual user activities independent of official club events. Any eligible 18+ user creates a Pool: title/activity, description, public place/meeting instructions, local date/time & timezone, optional ability level, capacity_total including creator, approval policy (default request-only), expiry/cancellation policy. Example table tennis Pool 4 total = 1 organizer + 3 openings. Android: Pools Explore, Create Pool wizard, Pool Detail, Request to Join note, My Pools (hosting/joined/pending), Host Approval Queue, accepted group chat and participant list. Backend: pools, membership requests, audit history, transactional capacity reservations, approve/decline/cancel/leave/remove, publish only when valid; membership grants chat access. No tickets or paid event tiers for ordinary Pools. Default location displayed only after approval if sensitive; public venue summary remains approximate. Race conditions and duplicate requests must be tested.

## Required acceptance criteria
With 4 capacity, host + exactly 3 approved, fourth concurrent approval blocked (409), pending != joined; rejected/cancelled cannot message; host actions survive refresh and different devices.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`09` if not final) and why this step is ready.


---

# PROMPT 09 — Clubs: pages, memberships, organizer roles and verification gate

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Allow any adult user to request/create a club profile with name, about, category, logo, city, rules, ownership evidence and staff. Status DRAFT → PENDING_REVIEW → APPROVED/REJECTED/SUSPENDED; platform admin reviews identity/ownership (no fake verified badge). Users follow public clubs; request to join / leave; admins approve. Roles OWNER, ADMIN, MODERATOR, MEMBER; staff assignment audit. Event eligibility only when approved and >=4 distinct active phone-verified club members; configurable server threshold default 4. Implement club directory, detail with Posts/Members/Events tabs, join/follow and manage club (mobile minimal), club-admin verification queue in admin. API has explicit eligibility state and reasons but backend blocks publish regardless of client. Handle leaving/disabled verification, duplicate accounts, suspended users, moderators cannot escalate to owner.

## Required acceptance criteria
Three eligible members cannot publish; fourth makes eligible if club approved and organizer authorized; suspended club cannot publish; verification badges only server-approved; membership admin access tested.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`10` if not final) and why this step is ready.


---

# PROMPT 10 — Club-only official events, RSVPs, waitlists and organizer event tools

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Implement event draft/publish/cancel/close under approved club only, enforce 4-member rule on creation/publish (document draft policy), owners/admins with organizer permission only. Events: details, capacity, public venue/partner, time zone, tiers marked FREE initially, attendee RSVP, waitlist, duplicate prevention, organizer approval where configured, organizer attendance list/check-in. Android: Events listing, event detail, free RSVP, QR/attendance pass tied to server signed token, My Plans link and event group chat (only valid members). Business web initially Club Event editor, attendee approvals/check-in and list using same API. Use atomic last-seat assignment, cancellation policy and reminders. Paid ticket tiers remain DISABLED until payments phase, never fake checkout success. Server handles eligibility change and existing confirmed events predictably; audit logs for state changes.

## Required acceptance criteria
A normal account's POST /v1/events returns 403; verified 3-member club fails; verified 4-member authorized club succeeds; no overbooking, no duplicate RSVP, check-in verifiable server-side.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`11` if not final) and why this step is ready.


---

# PROMPT 11 — Cafés and venues: business claims, real inventory and reservation flows

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Create venue claim/onboarding & platform admin approval, business profile with photos, facilities, public address, location, policies, staff roles, table capacities, reservable event spaces, opening hours, blackout dates, and venue-local time slots. Android: Places directory, venue detail, table vs group booking selection, date/party/time chooser, request/hold/confirm/cancel states, booking details in Plans, messages/support. Backend venues/inventory/availability/rules/bookings with transaction-safe holds and expiration, optional venue approval queue; no phantom slots or guaranteed instant confirmation without live capacity. Web Venue Hub: basic staff sign-in, listing editor, availability calendar, request approval queue. Hold expiry and conflicting reservations must be explicit; payment-required reservations remain pending until provider is configured later.

## Required acceptance criteria
Two users racing for last table cannot both confirm; timezone/overnight hours tested; owner alone can edit availability; failed API never creates a confirmed Android reservation.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`12` if not final) and why this step is ready.


---

# PROMPT 12 — Club–venue partnerships and co-branded collaborative events

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Build partner search by real venue facilities and availability, club collaboration requests with proposed date/time, turnout estimate, venue needs, food offer/cost terms, booking scope, attachments, status REQUESTED → COUNTEROFFERED → ACCEPTED/DECLINED/CANCELLED/EXPIRED; each party's authorized staff may sign off. Club organizer web and Venue Hub show request inbox, proposals, counteroffers and final agreement record, change notifications and audit. On ACCEPTED let eligible club organizer create co-branded event linked to approved venue reservation and partnership; recheck verified club eligibility before publishing. Members can discover venue/club through linked event; preserve separate agreement, event, and booking ownership. No showing projected café revenue as realized revenue; measure check-ins/redemptions separately.

## Required acceptance criteria
Agreement needs both sides' acceptance, conflicting venue window rejected, roles scoped, club under four verified members cannot publish co-branded Event, confirmed partnership persists on both dashboards.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`13` if not final) and why this step is ready.


---

# PROMPT 13 — Unified Plans, activity notifications and reminders

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Plans screen consolidates upcoming/pending/completed/cancelled: self-created Pool and approvals, joined Pool, club event RSVPs and tickets, café table/space bookings, meetup suggestions. Provide calendar/list, date grouping, linked chat, directions only to official public venues, cancellation policy, check-in and support. Backend creates durable in-app notifications for join requests, replies, approvals, club posts, booking changes and event updates; user notification preferences, read/unread/pagination; Android bell & inbox notifications. WorkManager for local reminders based on real server-confirmed plans; do not rely on background location. Add basic RSVP reminders and event rescheduling propagation; no spam notifications or fake urgent prompts.

## Required acceptance criteria
One user with a Pool, free Event and café booking sees all three correctly with real status; cancelling any reflects on refresh, correct notifications issued once, denied notification permission doesn't break Plans.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`14` if not final) and why this step is ready.


---

# PROMPT 14 — Experience Passport, voluntary history, privacy-safe map and achievements

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Build profile tabs Posts / Experiences / Map / Clubs, an Experience Passport record of server-verified attended club events/pool attendance (only when a legitimate host check-in supports it) and venue redemptions vs self-recorded visits. Immutable verification source and audit evidence; no farming fake QR/levels. Level/XP rules from distinct verified participation with anti-duplicate caps; achievement badges and monthly recap. Android: Passport cover, timeline, map filtered to PUBLIC VOLUNTARILY SHARED locations only, badges, collections, monthly recap, visibility settings. Server privacy default = private for exact location and attendance; allow public/followers/connections/private separately per content type, manual suppression, delayed sharing, delete. Map SDK/provider optional config; list representation must work without map API key. Never store/show continuous GPS tracks by default.

## Required acceptance criteria
Manual check-in explicitly unverified; server check-in verified; map hidden by default; changing visibility immediately affects other clients; duplicate check-in cannot inflate XP.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`15` if not final) and why this step is ready.


---

# PROMPT 15 — Stories, daily activity updates and shared media memories

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Add 24h ephemeral Stories and quick daily activity updates with upload/multi-image/text controls, optional tagged club/event/venue, mention consent, view/reply privacy rules, expiry and cleanup, report/block, moderation. Share a completed experience into feed/story via explicit user action; don't auto-publicize a meeting attendance. Android story tray, full-screen viewer with progress/pause/accessibility, add story, media selection, activity-share composer, simple collaborative album only with per-user photo permissions. Backend schedule cleanup job, rate limits, media access control. Feature flag video until real processing/moderation infrastructure is ready; do not implement fake short-video processing.

## Required acceptance criteria
Story expires on server, private story inaccessible to others, blocked user cannot view/reply, no leak of tagged person's exact venue/activity without consent.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`16` if not final) and why this step is ready.


---

# PROMPT 16 — Real payments: paid event tickets, deposits, QR validation and refunds

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Add paid ticket tiers for eligible club Events and optional venue deposits only after payment provider selection and credentials; implement provider interface and sandbox first. Order model separate from booking/RSVP; quote server-side, inventory holds, idempotent checkout, payment webhook verification, transaction/receipt, QR issued only after success, single-use or attendance-state check-in validation, cancellation/refund request and status. Android: event ticket tier/quantity chooser, checkout, pending/failure/confirmed, My Tickets, ticket QR, refund help. Backend database transactions and consistent refunds; no payment amount trusted from Android; handle duplicate callbacks and abandoned checkouts. Keep paid functions disabled with clear UI until real PSP configured. Review applicable India payments/tax obligations before launch.

## Required acceptance criteria
Sandbox successful transaction creates confirmed ticket only after verified webhook; payment failure/timeout never creates confirmed pass; duplicate webhook idempotent; no overselling and cancellation/refund states tested.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`17` if not final) and why this step is ready.


---

# PROMPT 17 — Freemium ROMEAR Plus and promoted content with clear labeling

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Implement free tier preserving basic social interactions, club follow, Pool creation, community discovery, safety, messaging, and basic Passport. Plus optional personal experience recaps, collections, design customizations and advanced filters; check paid entitlements on backend, store receipts or verification via Play Billing where required for Play-distributed digital services; no paywall for block/report/privacy or essential connection functions. Build clear pricing/restore/manage subscription screens; no invented plans/prices in production. Business promotions: verified clubs/venues may submit labeled sponsored event campaigns, budgets/audiences within allowed privacy rules, manual moderation approval, reporting of impressions/clicks/verified bookings; enable billing only when safe commercial setup exists. Android Sponsored labels, hide/mute/report ads; business web campaign creation and metrics. Never sell exact personal location or expose private club membership in targeting.

## Required acceptance criteria
Expired subscription loses only premium extras; free features remain; every ad labelled Sponsored; campaigns cannot target private data; no live charge without configured compliant billing.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`18` if not final) and why this step is ready.


---

# PROMPT 18 — Organizer, Venue and platform-admin web dashboards

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Complete responsive React+TypeScript business portal. Club Hub modules: club identity, verification progress, role invitations, members/approvals, events/attendees/check-in, venue proposals, posts, audience metrics (true data), moderation/report escalations. Venue Hub: claim, profile, tables/spaces, availability, booking approvals/cancellations, partner proposals, offers, aggregate check-ins/redemptions without revealing personal contact data, campaign metrics. Admin console: verify clubs/venues, suspicious/abusive accounts, content reports, financial disputes, seat/booking audit, entitlements, roles, event/pool safety controls. Shared role-based server API and granular scope; clean responsive UI desktop first. Use real empty states, no sample-revenue graph in production. Add audit log for moderator actions.

## Required acceptance criteria
Club admin cannot read venue business secrets, venue owner cannot access unrelated clubs, moderator actions auditable, dashboards work on real records and still render with zero records.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`19` if not final) and why this step is ready.


---

# PROMPT 19 — Deep links, sharing, anti-abuse and Nagpur launch readiness

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Implement Android verified app links/deep links for profile/post/club/Pool/event/venue with safe fallback pages. Native share actions and UTM-like aggregate attribution without tracking private people. Add onboarding from shared links (after login returns to target), invitation capacity checks, event referrals. Implement real content/admin moderation operating procedure, abuse rate limits, anti-bot guardrails and deletion/export lifecycle, app support center, privacy policy/terms links, map/location consent and partner consent. Build a local Nagpur pilot with explicit admin-created verified partners, no fake content; prepare seed script solely for dev/test data, and tools to import partner data only with permission. Set analytics event naming and consent-aware aggregation, error logging without sensitive information. Check actual Google Play policies and target SDK again.

## Required acceptance criteria
External shared URL opens corresponding object safely, gated object doesn't leak restricted info, account deletion/logout/blocked flows work, pilot setup does not assume partner authorization.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`20` if not final) and why this step is ready.


---

# PROMPT 20 — Whole-app audit, release verification, performance and rollout

Paste this complete prompt into Codex **after** the previous stage has passed its quality gate. The repository must contain `AGENTS.md` and the `specs/` folder from this kit.

## Your task
Implement the following end-to-end in the new ROMEAR repository, editing real code rather than only describing a plan.

Run a full dependency/migration audit, Android unit/UI/instrumented tests, backend integration/permission/concurrency tests, business-web tests, basic security review, release build with obfuscation and signing configuration (never include secret signing keys), staging deploy on Render, database migration strategy, backup/restore, rate limits, monitoring, alerting and rollback docs. Exercise end-to-end test journeys for new user→post→follow→message; Pool host→three approvals→full→group chat; three-to-four club verification threshold→event RSVP; café booking→venue approval; partnership→co-branded event; real ticket payment sandbox/QR; Passport privacy; moderation block/report. Generate runbook, known gaps and launch checklist. Evaluate retention measures but don't claim actual user metrics. Produce final API docs and Play Store readiness checklist, marking blocked merchant/SMS/media/map/push credentials precisely.

## Required acceptance criteria
Release candidate builds with all configured services; every critical scenario passes in staging; any untested external operation explicitly BLOCKED; no fake success paths remain.

### NON-NEGOTIABLE INSTRUCTIONS FOR THIS STEP
- Read `AGENTS.md` and all `specs/*.md`, inspect actual repo state and the prior steps' implementation before coding. Do not replace existing working features or drift the product rules.
- Implement **both backend and Android** of this vertical slice, plus business-web only where described. Create migrations, enforce role/privacy rules server-side, document API with request/response examples and errors, and connect every UI action to real behavior.
- Use XML Views + Kotlin, not Compose; the warm forest/cream/terracotta system; real loading/empty/error/offline/pending/success states; fully reachable navigation/back behavior. New assets must be licensed/local or own original vector assets. No purple theme or screenshot-as-UI.
- Add unit/integration tests for happy path, denial, stale state, duplicates and failure; test concurrency for inventory, chat membership, verification gate and payment when relevant.
- No local fabricated success. Dev mock data only in clearly segregated preview/tests and never as a repository fallback. If external service credentials aren't available, implement a clean provider boundary and show honest disabled/unavailable states, not fake confirmations.
- Run builds/tests where toolchain permits; report exact commands/results and missing capabilities. Update `docs/BUILD_STATUS.md`. Do not proceed to a later stage unless this step is working or explicitly flagged PARTIAL with a blocker.

### End-of-step response format
1. **What changed** (Android screen routes/layout files, FastAPI models/migrations/endpoints, web routes)
2. **How to run locally** (commands, environment dependencies)
3. **Evidence of quality** (actual tests and emulator screenshots if available; exact failures if not)
4. **Security and abuse coverage** (what roles, failures, races were tested)
5. **Gaps / blocked external integrations** (be explicit)
6. **Next prompt** (`21` if not final) and why this step is ready.


---

