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
