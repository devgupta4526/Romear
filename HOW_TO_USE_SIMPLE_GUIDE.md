# ROMEAR: HOW TO USE THIS KIT (WINDOWS + CODEX)

## What is inside

- `AGENTS.md` — permanent rules Codex should follow.
- `specs/` — product flow, visual system, and passing conditions.
- `prompts/` — exactly **21 prompts** numbered **00 to 20**.
- `design_reference/` — nine broad UI design boards for consistent look; **not** production assets and not individually validated screen implementations.
- `docs/BUILD_STATUS.md` — stage log that Codex updates.
- `START_HERE.md` and `MASTER_INSTRUCTIONS_AND_ROADMAP.md` — other guidance.

## 1. Setup once

1. Install Android Studio (includes Android SDK/emulator), VS Code with Codex or your normal Codex environment, Git, Python, Docker Desktop (for PostgreSQL), and a JDK compatible with the Android Gradle project. If running Windows Docker Desktop with WSL 2, enable that integration.
2. Create an **empty** folder, e.g. `C:\Projects\ROMEAR`.
3. Extract the contents of **this ZIP directly into that folder**. Confirm `C:\Projects\ROMEAR\AGENTS.md` and `C:\Projects\ROMEAR\prompts\00_...md` exist. Do **not** leave files nested two folders deep.
4. Open the `ROMEAR` folder in your code editor (not just a Markdown file). Start Codex with the workspace set to this project.
5. Confirm Codex can read `AGENTS.md` and `specs/`. The boards are in `design_reference/`.

## 2. Run Prompt 00 first

Paste the text in `COPY_TO_CODEX_START.txt` into Codex. Codex should create real project files in the same workspace, run relevant checks, and produce a status summary.

It may require an installed Android SDK, Docker daemon, or API credentials for some stages. For stage 00 no paid service credentials are required. Dev-only test OTP is allowed in stages 02-03 if clearly guarded, but production sign-in must use a real verified provider.

## 3. After **every** prompt: verify, fix, save, then continue

- **Read Codex's summary:** Which files changed? What did it actually test? What remains blocked?
- **Run it yourself:** start backend+Postgres if that stage needs them; open Android in emulator; navigate its new flow. In stage 18, also run web dashboard.
- **Check good and bad paths:** try success, wrong input, cancel, loss of Internet, app restart and unauthorized actions.
- **Inspect `docs/BUILD_STATUS.md`:** mark Complete only when tests and manual check pass. Mark Partial/Blocked if not.
- **Ask Codex to fix stage defects:** use `COPY_TO_CODEX_REVIEW.txt`. **Do not move on** with a critical broken stage.
- **Save a checkpoint:** Git commit working code after each verified stage (or use a backup if unfamiliar with Git).
- **Only then paste next prompt:** `prompts/01_...md`, then `02_...md`, through `20_...md`.

## 4. What you should see after each stage

| Step | What was built | What to manually check |
|---|---|---|
| **00** | Project foundation | Android app opens; backend boots; database migrations and tests run. |
| **01** | Design system & navigation | All five root tabs open; buttons, colors and layouts are consistent. |
| **02** | Login backend & permissions | Test OTP works in *development*; invalid OTP fails; sessions persist. |
| **03** | Complete onboarding | New user finishes signup and lands on Home; relaunch skips completed onboarding. |
| **04** | Profiles & connections | Edit profile, follow someone, request/accept connection, block and report. |
| **05** | Real messaging | Accepted connections can message; other users cannot; messages persist after restart. |
| **06** | Posts & feed | Create and view post, upload image, like, comment, save, report. |
| **07** | Explore & search | Search and filter live people, posts, Pools, clubs, events and venues. |
| **08** | Individual Pools | Create 4-person table tennis Pool; three others request; host approves; capacity enforced. |
| **09** | Clubs & verification | Create club, approve members; 3 verified members cannot publish Event, 4 can only after club approval. |
| **10** | Official club Events | Verified authorized club publishes Event; members RSVP, waitlist and check in. |
| **11** | Café and venue booking | Venue owner lists availability; user books genuine open slot; no double booking. |
| **12** | Club × venue partnership | Club requests venue collaboration; venue accepts/counters; only eligible club publishes Event. |
| **13** | Plans & reminders | Upcoming accepted Pools, Events, and venue reservations appear in one Plans screen. |
| **14** | Passport & achievements | Verified attendance appears separately from self-recorded visits; private by default. |
| **15** | Stories & daily updates | Post temporary Story and activity updates; visibility and expiry work. |
| **16** | Payments & QR tickets | Use sandbox payment provider; verify webhook; never fake payment success. |
| **17** | Premium & ads | Free core remains usable; subscriptions gated by real entitlements; sponsored posts labeled. |
| **18** | Organizer/venue/admin dashboards | Web dashboards work with actual API; role restrictions tested. |
| **19** | Invite links & launch safety | Deep links work; reporting, spam protections and sharing are tested. |
| **20** | Final release audit | Run whole-app tests, performance, security, production config and release checklist. |

## 5. Typical flow of a stage in Codex

**You:** `Read AGENTS.md and specs/*.md. Implement ONLY prompts/08_ordinary-user_pools_....md completely. Keep prior stages working. Run tests and update docs/BUILD_STATUS.md. Do not begin stage 09.`

**Codex:** edits Kotlin/XML, FastAPI, migrations, tests; runs checks; writes detailed summary.

**You:** test Pool creation and approvals on two development accounts. If something fails, paste the error or screenshot into the same Codex thread and ask it to fix **stage 08 only**.

**You:** once complete, use Git commit, then start stage 09.

## 6. Common problems

- **Codex only explains or plans:** say 'Implement real code, run your available tests and show changed files; do not only describe the plan.'
- **Android doesn't run:** first verify Gradle sync, SDK location and emulator; give Codex the actual build error.
- **Backend can't reach database:** check Docker is running and the local `docker compose` service is up; don't point the app at the production database.
- **UI is generic:** show the relevant `design_reference/*.png` and ask Codex to match the DESIGN SYSTEM, never copy a screenshot as a background.
- **A service needs paid credentials:** leave it disabled with a clear blocker; never fabricate OTP, booking, payment, ticket or message success.
- **A stage seems too large:** tell Codex to divide it into backend+API+tests, then Android screen+integration+tests. Mark incomplete until both are verified.
- **A file appears to be missing:** check that you extracted the ZIP contents into the project root; the original 21-prompt ZIP had some Windows-unfriendly `:` filenames. This corrected kit removes those.

## 7. After Stage 20

Test the complete app on a physical Android device as well as emulator. Obtain real OTP, storage, payment, and messaging credentials where needed. Set up production PostgreSQL and backend on Render; use a staging environment first. Onboard your first real clubs and cafes only after safety, privacy, verification, booking and ticket checks pass. Then run a small Nagpur pilot before expanding.

**Important:** The files in this kit are **instructions and UI references**, not a prebuilt APK. Codex creates the app as you complete the stages.
