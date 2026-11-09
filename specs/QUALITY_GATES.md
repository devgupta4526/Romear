# QUALITY GATES — MUST PASS BEFORE NEXT PROMPT

At every stage: (a) Android debug build assembles, (b) backend typecheck/lint/tests and migrations run on clean PostgreSQL, (c) API client and schema agree, (d) no demo fallbacks in release, (e) no unhandled crashes, (f) correct loading/empty/error/offline/permission denied states, (g) authz and abuse/edge tests, (h) real emulator UI screenshot reviewed where possible, (i) all new screens reachable/back stack correct, (j) documentation updated.

Security scenarios: unauthorized access, wrong role, blocked user, revoked token, OTP abuse/expiry, age gating, metadata-only media injection, oversized file, edit/delete other person's post, leaked group messages, exact location exposure, repeated payment callback, duplicate QR, 2 users booking last seat concurrently, host approval races, club losing verified status, venue owner spoofing.

Payments: never confirm paid ticket or subscription from client success alone; verify backend provider webhook/signature, idempotency key, order price/currency, transaction state, and refund; no generated valid QR until server has confirmed eligible entitlement. Digital vs physical/live ticket billing comply with current Play requirements (verify before release).

Content: enforce report/block/mute on social feed, profiles, comments and chat; require terms before upload; moderator review state and audit events; rate limit spam/harassment; effective non-consensual sharing controls.

Accessibility: large text and TalkBack labels, 48dp targets, touch/keyboard/back behavior, reduced motion, color contrast, empty and error placeholders, responsive narrow Android phone, no overflow.

Performance: paginate feeds, thumbnails, immutable cache policies, upload compression, image decode sizing, safe background/foreground behavior, no unbounded polling, database indices, logs without secrets.

Do not mark a stage COMPLETE in `docs/BUILD_STATUS.md` when any of these criteria is unverified; use PARTIAL/BLOCKED with honest notes.
