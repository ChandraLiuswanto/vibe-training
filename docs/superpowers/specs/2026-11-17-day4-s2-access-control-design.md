# Day 4 · Session 2 deck — Login, roles, admin page and audit trail — design

Status: draft for approval · 2026-11-17
Output: `decks/session-2-access-control-visual.html` (new file) and `tools/session-2-visual-check.mjs` (new file).
Branch: `autopilot/day4-s2-access-control` (already created from `main`).
Reference deck (read-only, not in this repo's branch): `C:\Users\HP\pr-reviews\vibe-training-pr4\decks\session-1-external-data-visual.html` (PR #4, 206 lines). Called "S1" below.
Tags: *(user)* = decided by the owner · *(call)* = coordinator's call, correctable.

---

## 1. Intent

Session 1 connected the Financial App to outside data. Session 2 makes the app safe for several people: each person signs in, the app knows their role, an admin manages roles on one page, and the app keeps a record of who did what. The audience is bank business users with no coding background who build with OpenCode. The deck is presented for 60 minutes, then participants practise for 60 minutes *(user)*.

The deck must look and behave like S1 *(user)*: same shell, same visual language, short titles, mostly diagrams and app mock-ups, speaker notes behind the Notes button, and a built-in pack of practice prompts.

## 2. Goals, non-goals, anti-goals

**Goals**
- One self-contained HTML deck with 18 slides covering both topics in two acts: Act 1 login and roles, Act 2 admin page and audit trail *(user: one deck, approach A)*.
- A pack of 7 practice prompts that build four small pieces in order: login with a mock directory, two roles enforced in the back end, an admin page, an audit trail.
- Every claim on a slide is true for a mock set-up; the deck never suggests the mock directory is real security.

**Non-goals**
- No Financial App code is written or run. No app exists on this machine, so every prompt is untested and is labelled so (§7).
- No change to S1, to PR #4, to the Day 3 decks, or to `tools/deck-check`.
- No real LDAP server, no new software for participants to install.
- No outline or copy files under `docs/outlines/`; the headline list in §5 is the outline *(call)*.

**Anti-goals** (failure even if the deck renders)
- Wording that says hiding a button protects a feature. Protection is the back-end check.
- Wording that says the mock directory, or this training build, is production-grade security.
- A prompt that tells the agent to log passwords, tokens or session IDs.
- Meeting the word budget by shrinking type.

## 3. Constraints

- **Language:** English *(call, matches S1 and repo decks)*.
- **Self-contained:** one HTML file, no network requests, no external fonts, images or scripts.
- **Shell reuse:** the two CSS blocks of S1 (line 7 and line 10 of the reference file) are copied byte-for-byte. New component styles go in a third block that starts with the comment `/* Session 2 additions */`. The S1 script is copied and changed only where §6 says.
- **Stage:** fixed 1600×900, scaled to the window, as in S1.
- **Titles:** short, in S1's style. This deliberately departs from the `AGENTS.md` full-sentence-title rule because the owner asked to match S1 *(user)*.
- **Word budgets** (visible text, title and footer excluded, speaker notes excluded): at most 40 words per slide; the practice slide (17) at most 60. Over budget: move text to the notes, never shrink type.
- **Logos:** only the logos already embedded in S1 may be reused (React, FastAPI, OpenCode). No new brand logos. New pictures are inline SVG icons in S1's `.vi` style (32×32 view box, stroke only).
- **Colours and fonts:** only S1's CSS variables and Arial/Helvetica.
- **`AGENTS.md` story gate:** approval of this spec, which contains the headline-only sequence (§5), is the story gate *(call)*.
- `tools/deck-check` is built for the Day 3 deck format (`data-n`, `#notes-data`) and is not run on this deck; the new check script (§8) replaces it here *(call)*.

## 4. Content decisions

### 4.1 The model taught

- **Authentication** = who are you. **Authorization** = what may you do.
- **LDAP** is presented as the company directory: one place that knows staff accounts, which many apps ask instead of keeping their own passwords.
- **Mock LDAP** *(call)*: a small fake directory inside the back end, behind one function described as "check with the directory". It holds three practice accounts. One slide shows that a real directory would replace only that one function.
- **The directory answers only "who are you".** Roles live in the app's own database, so the admin page can change them *(call)*. This links the two acts.
- **Two roles** *(user)*:

| Action | User | Admin |
|---|---|---|
| View dashboard, prices, Wiki, chatbot | yes | yes |
| Add or remove watchlist items | yes | yes |
| See the list of users | no | yes |
| Promote or demote a user | no | yes |
| See usage (user count, activity list) | no | yes |

- The watchlist stays as it is in the app (one shared list); the deck does not add per-user watchlists *(call)*.
- **Practice accounts** *(call)*: `alya` (starts as Admin), `budi` (User), `citra` (User, the one who gets promoted in the demo). One shared practice password, `Training-2026`, shown on the slide with the label "Practice accounts only".
- **Safety rule taught:** an admin cannot demote the last remaining Admin.
- **Audit trail** records: sign-in success and failure and sign-out (one event type on slide 13), watchlist add and remove, role changes, refused requests (403), and calls to the protected API endpoints. Each record has time, user, action, target and result. It never holds passwords or session tokens. Records are added, never edited or deleted through the app.
- **Usage** on the admin page is read from the same audit records: number of users, sign-ins today, and the latest activity *(user: "how many users, activities")*.

### 4.2 Cast

Alya (Admin) and Budi (User) appear in the mock-ups from slide 3 to slide 18. Citra appears only where a role is changed.

## 5. Slide sequence (the story gate)

Eyebrow of slide 1: `Financial App · Session 2 of 3`. Footer text on every slide: `Financial App · Session 2 · Access control`.

| # | `data-title` | Visible title | Main visual |
|---|---|---|---|
| 1 | Give Every User the Right Access | One app.<br>Many people. | Hero: app tile with a lock, two people |
| 2 | Continue the app you already built | Same app. Now with a front door. | S1's app tiles (dashboard, database, chatbot, FX) plus four new tiles: Login, Roles, Admin page, Audit trail |
| 3 | The business need | "Who changed the watchlist?" | Dashboard mock-up with no user name anywhere; question bubble |
| 4 | Authentication versus authorization | Who are you? What may you do? | Two-column split: ID badge versus key ring |
| 5 | LDAP: the company directory | One directory. Many apps. | Three app tiles pointing to one directory tile |
| 6 | Mock LDAP for practice | A practice directory. Same question. | App → "check with the directory" → mock directory, with a dashed real-directory tile that swaps in; three practice accounts |
| 7 | Sign in once, carry a pass | Sign in once. Carry a pass. | Rail: login form → directory check → session pass → every later request shows the pass |
| 8 | Two roles | Two roles. One table. | The table from §4.1 as a tick/cross grid |
| 9 | Quick check: hidden button | Is hiding the button enough? | Quiz, three options (§5.1) |
| 10 | Where the check belongs | Check at the back end. Every time. | Browser → back-end gate → data; Budi's request to the users endpoint stopped with 403 |
| 11 | The admin page | One page to manage people. | Admin page mock-up: user count, user rows with role and a Promote/Demote button, "last admin" lock on Alya's row |
| 12 | Audit trail | Who. What. When. | Three tiles (who, what, when) feeding one log line |
| 13 | What to record | Record the action. Never the password. | Left: five recorded event types with icons. Right: struck-through password and token |
| 14 | Demo: brief, plan, approve, build | Brief → plan → approve → build. | OpenCode terminal mock-up as in S1 slide 10, with a button that opens prompt 1 |
| 15 | Evidence: two accounts | Two accounts. Two results. | Side by side: Alya sees the Admin menu and users list; Budi sees no Admin menu and gets 403 from the endpoint |
| 16 | Evidence: the audit trail | Change as Budi. Read as Alya. | Audit table mock-up, 5 rows: Budi sign-in, Budi watchlist add, Budi refused request, Alya promotes Citra, failed sign-in |
| 17 | Your 60-minute practice | Build all four pieces. | S1's timeline rows (§5.2) plus buttons "All practice prompts" and "Setup help" |
| 18 | Finish check and next session | Show the result—not just "done". | Four finish cards (§5.3) and the line `Next → Session 3` |

Slide 18 names no Session 3 topic, because the owner has not fixed it *(call)*.

### 5.1 Quiz (slide 9)

Question on the slide: "Budi's screen has no Admin menu. Can he still reach the users list?" Options: A "No. The menu is hidden." · B "Yes, unless the back end checks his role." · C "Only if he knows Alya's password." Correct: B. Answer text after a click: "B. The back end must refuse the request." Uses S1's `.quiz` and `.answer` markup; the answer strings hard-coded in S1's click handler are replaced, and the same "B. …" sentence is shown whichever option is clicked.

### 5.2 Practice timeline (slide 17)

| Time | Label | Detail |
|---|---|---|
| 00–05 | Prepare | Run the app + agree the plan |
| 05–20 | Login | Mock directory + sign-in page |
| 20–33 | Roles | Admin and User, checked in the back end |
| 33–45 | Admin page | Users, promote, demote |
| 45–55 | Audit trail | Record and show activity |
| 55–60 | Verify | Two accounts, two results |

Small text beside the buttons: "Behind? Finish Login and Roles first."

### 5.3 Finish cards (slide 18)

1. Sign-in works for `alya` and `budi`; a wrong password is refused.
2. Budi gets 403 from the users endpoint.
3. Alya promoted Citra on the admin page.
4. The audit trail shows steps 1 to 3.

### 5.4 Speaker notes

Every slide has one `<aside class="speaker-note">` of 35 to 90 words, facilitator voice, as in S1. Required content:
- Slide 2 or 3: this login is separate from the Google Drive sign-in used in Session 1 (S1's last note promised this).
- Slide 6: the mock directory is for practice; a real directory needs the bank's IT team and is out of scope.
- Slide 7: the pass is a session kept by the back end; do not teach token formats.
- Slide 13: audit records can themselves hold personal data; keep them minimal.
- Slide 14: all prompts are `[UNTESTED]`; the facilitator must rehearse them on a real app before class.
- Slide 17: Login and Roles are the minimum outcome; Admin page and Audit trail may be finished later.

## 6. Shell changes from S1

Only these parts of the S1 markup and script change; everything else is copied as is.
- `<title>`: `Session 2 — Give Every User the Right Access · Visual Edition`. `<main aria-label>`: `Session 2 presentation`.
- Footer string in the script: `Financial App · Session 2 · Access control`.
- The `csv` constant and any CSV download control are removed; nothing in Session 2 downloads a data file.
- `prompts` array: replaced by §7.
- `promptList()` intro text: "Build the four pieces in order during the practice hour. Open a prompt, read it, then copy it into OpenCode."
- `help()` dialog: title `Setup help and limitations`; content is three short sections: "What was checked" (the deck renders and its controls work; no prompt has been run on a real app), "Limits of this build" (mock directory, practice passwords, training only, not a security review), "If you are stuck" (finish Login and Roles first; paste the error into OpenCode and ask for a plain-language cause before a fix). No external links.
- Print handout heading: `Session 2 · Practice handout`, with intro "Four pieces, in order: login, roles, admin page, audit trail."
- Any other Session 1-specific string or control is changed or removed to fit Session 2: the `#download-csv` button and its handler (removed), the download file name (`session-2-practice-prompts.txt`), the "Setup help + sources" button label (`Setup help`), and the `promptDialog()` text, which gains the `Untested — rehearse before class` label.
- Slide numbers that S1's script or markup refers to directly (for example a button that jumps to a slide) are updated to the Session 2 numbering.

## 7. Practice prompts

Seven prompts, same object shape as S1 (`id`, `title`, `text`), same tone: plain English, numbered requirements, "wait for my approval", "do not commit or push". Each is 120 to 330 words. Buttons that open a prompt: slide 14 opens prompt 1; slide 17 opens the full list.

Rules for all seven:
- Work inside the existing Financial App and reuse its conventions (React front end, FastAPI back end, existing database).
- Explain any new package before installing it and ask first. Prefer what is already installed and the Python standard library.
- Never store or log a plain password, token or session ID.
- State that this is a training build with a mock directory.

| # | `id` | `title` | Must ask for |
|---|---|---|---|
| 1 | `access-plan` | 1 · Plan login, roles, admin page and audit trail | At most 3 questions, one at a time; update `docs/spec.md`; a numbered plan in four stages (login, roles, admin page, audit trail); planned files, risks and tests in plain language; wait for approval; no code yet |
| 2 | `login-build` | 2 · Build the login with a mock directory | One back-end function that checks a user name and password against a mock directory holding `alya`, `budi`, `citra` with the practice password stored as a salted hash; a sign-in page; sign-out; a server-side session with a random ID in an HttpOnly cookie; every existing API endpoint except sign-in refuses requests without a valid session (401); the same message for unknown user and wrong password; a comment marking where a real directory would be called; tests |
| 3 | `roles-build` | 3 · Add Admin and User roles | A role per user in the app database, default User, `alya` seeded as Admin; the directory is not asked about roles; one shared back-end check used by admin-only endpoints, returning 403 for a User; the front end hides the Admin menu for a User but the back end stays the real check; the current user's name and role shown in the header; tests for 401, 403 and 200 |
| 4 | `admin-build` | 4 · Build the admin page | Admin-only endpoints to list users and change a role; an Admin page with the number of users, each user's name and role, and Promote/Demote buttons; refuse to demote the last Admin; a user appears in the list after their first sign-in, and the three practice accounts are listed from the start; tests |
| 5 | `audit-build` | 5 · Add the audit trail | One audit table with time, user, action, target, result; record sign-in success and failure, sign-out, watchlist add and remove, role changes, refused requests (403) and calls to protected API endpoints; never record passwords, cookies or request bodies; no edit or delete endpoint; an Admin-only endpoint and a section on the Admin page showing the latest 50 records, sign-ins today and the user count; tests |
| 6 | `access-test` | 6 · Test with two accounts | A scripted check list the agent runs and reports: wrong password refused; `budi` can change the watchlist; `budi` gets 403 from the users and audit endpoints; `alya` can promote `citra` and cannot demote herself while she is the last Admin; each step appears in the audit trail with the right user; then the list of checks the participant must do by hand in the browser; explain the cause in plain language before any fix |
| 7 | `finish` | 7 · Final verification and safe cleanup | Evidence for each finish card in §5.3; changed file names; a scan for real-looking passwords or secrets in changed files; completed, incomplete and blocked items; do not count a demo or mock result the participant did not run; no commit, push or deletion without approval |

The handout (print view) and the prompt dialog label every prompt `Untested — rehearse before class`.

## 8. Verification

`tools/session-2-visual-check.mjs` is a Node script that loads the deck in Edge through `tools/deck-check/node_modules/playwright-core` (already installed; Edge is at `C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe`). Run from the repo root: `node tools/session-2-visual-check.mjs`. It exits non-zero and prints each failure when any check fails:

1. Exactly 18 `.slide` sections; each has a non-empty `data-title` equal to §5, one `h1` or `h2`, and one `.speaker-note` of 35 to 90 words.
2. Visible word count per slide (title, footer and note excluded) is at most 40, or 60 on slide 17.
3. At 1920×1080 and 1280×720, no element of the active slide extends outside the slide and the slide does not overflow vertically.
4. No console errors, no page errors, no request other than `file:`, `data:` or `blob:`.
5. `prompts` has 7 entries with the ids of §7 in order; each text is 120 to 330 words; every `[data-prompt]` value in the markup is one of those ids.
6. Slide 14's prompt button opens the dialog with prompt 1's title; the Prompts control lists 7 prompts; on slide 9, clicking option B shows an answer starting with "B.".
7. The first two CSS blocks are byte-identical to S1's when the reference file exists at the path above; if it does not exist the script prints a warning and skips this check.
8. The words `Frankfurter`, `Google Drive`, `Session 1` and `csv` do not appear in visible slide text or in the script (`.speaker-note` text is excluded from this check for all four words).
9. Screenshots of all 18 slides at 1920×1080 are written to `.review/session-2-shots/` (git-ignored by the existing `.review/*-shots/` rule).

A person (the coordinator) looks at every screenshot before the work is called complete; the script cannot judge whether a diagram reads well.

## 9. Deliverables

- `decks/session-2-access-control-visual.html`
- `tools/session-2-visual-check.mjs`
- One dated entry in `docs/project-log.md` recording the owner's decisions marked *(user)* above.
- Final report: per slide, the title and visible word count; the list of placeholders (mock accounts, mock audit rows, untested prompts).

## 10. Open items for the owner (not blocking the deck)

- The prompts need one rehearsal on a real Financial App before class.
- Session 3's topic is not named on slide 18.
- The owner's Indonesian brief lists LDAP and audit as two separate sessions' worth of material; with 60 minutes of practice, Admin page and Audit trail are stretch outcomes for slower participants.
