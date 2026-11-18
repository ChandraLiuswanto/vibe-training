# Day 4 visual decks — fix the review findings — design

Status: draft for approval · 2026-11-18
Branch: `autopilot/day4-decks-fixes` (created from `main`).
Source of the work: `docs/reviews/2026-11-17-day4-decks-review.md`, findings #1–#47. "#N" below is a finding number in that report.
Tags: *(user)* = decided by the owner · *(call)* = coordinator's call, correctable.

---

## 1. Intent

The review found 47 problems in the three Day 4 decks. The owner asked for all of them to be fixed *(user)*. The aim is that bank business users with no coding background are taught nothing unsafe or untrue, can follow the pictures, and can get through the practice hour with a facilitator.

Decks, with the short names used below:

- **S1** = `decks/session-1-external-data-visual.html` (18 slides)
- **S2** = `decks/session-2-access-control-visual.html` (18 slides)
- **S3** = `decks/session-3-vps-deployment-visual.html` (16 slides)

## 2. Goals, non-goals, anti-goals

**Goals**
- Every finding #1–#47 is fixed in the decks or the new participant sheets, except the two that editing cannot fix (§8), which become facilitator checklist items.
- One participant sheet per session (§7).
- One check script that all three decks and the three sheets pass (§9).
- Outlines, README and the review report agree with the changed decks.

**Non-goals**
- No slide is added or removed: S1 and S2 stay at 18 slides, S3 at 16.
- No Financial App code is written or run. OpenCode is not installed on this machine, so no prompt and no setting is tested. Every prompt stays labelled untested.
- No change to the Day 3 decks (`decks/day3-*`), `prompts/`, `demos/` or `tools/deck-check/`.
- S3 is not rebuilt on the S1/S2 shell and keeps its typefaces (§6) *(user: approach A)*.
- No new technical content beyond what a finding asks for.

**Anti-goals** (failure even if the check passes)
- A slide title or visible line that states as fact that the agent will stop, ask or stay inside a folder.
- Meeting a word budget by shrinking type, or a text-size floor by deleting a warning.
- Removing a security protection from a prompt to make the exercise easier.
- A participant sheet that repeats the prompt's technical wording instead of translating it.
- Wording that presents the practice set-up, the mock directory or the practice audit trail as bank-grade.

## 3. Approaches

**The ask-first question** *(user chose B)*:
- A — reword only: titles become instructions; the slide names the practice account with made-up files as the safeguard.
- **B — reword and add an ask-first setting (chosen):** the same rewording, plus a step in the prompts and the facilitator set-up that makes OpenCode ask before Drive and server actions. It is a real safeguard, but it cannot be tested here.

**Session 3's look** *(user chose A)*:
- **A — restyle in place (chosen):** keep S3's file and drawing code; redraw the flagged diagrams and match S1/S2's opening slide, footer, buttons, arrows and cards.
- B — rebuild all 16 slides on the S1/S2 shell: closest match, about three times the work, and the highest risk of breaking a deck whose technical content the review rated the most careful.
- C — redraw only the flagged pictures: leaves #22–#24 open.

**How the work is split** *(call)*: one worker per deck, in parallel, because each deck is one file; one worker for the check script and outlines, first; one worker for the participant sheets. Wording that must match across decks is fixed in §4 so that parallel workers cannot drift.

## 4. Constraints

### 4.1 Rules that already apply
- `AGENTS.md` deck rules: single self-contained HTML file per deck, no network requests; full-sentence titles; visible words (title and footer excluded) at most 40 per slide and 60 on exercise slides; over budget means move text to the speaker notes, never shrink type.
- Exercise slides, limit 60: S1 slide 17, S2 slide 17, S3 slide 15. All other slides: 40.
- Several slides gain a line and are already near the limit (S1 slides 10, 13, 14, 16; S2 slides 14, 17, 18). The builder makes room by moving existing lower-value text into that slide's speaker notes.
- Language: English.
- Colours: only the variables each deck already defines. S1 and S2: `--paper`, `--ink`, `--accent` (`#f30`), `--muted`, `--line`, `--wash`, `--green`.

### 4.2 How each deck is built (verified 2026-11-18)
- **S1 and S2 share a shell.** Lines 7 and 10 of each file are CSS blocks that are byte-identical between the two decks. They must stay byte-identical and unchanged. S2 puts its own styles in a block starting `/* Session 2 additions */`. S1 has no such block: S1's new styles go in a new block starting `/* Session 1 additions */` *(call)*.
- **S1 and S2:** each slide is a `<section class="slide visual-slide" data-title="…">` with one heading and one `<aside class="speaker-note">`. Prompts are a JavaScript array `const prompts=[{id,title,text}, …]`, seven per deck. `promptDialog(id)` builds the prompt window.
- **S3 stores every slide twice.** Each slide exists as a `<section class="slide" data-title="…" data-minutes="…">` and again inside `<script id="deck-data" type="application/json">` as `slides[i]` with the keys `title`, `eyebrow`, `visual`, `notes`, `minutes`, `kind`, `actions`, `words`. The running deck reads `title` and `notes` from the JSON, and `prompts`, `pack` and `card` only from the JSON. No generator for this file is in the repository. **Every S3 edit must change both copies**, and `words` must equal the new visible word count.
- S3's stage is 1920×1080, scaled to the window; S1 and S2 use 1600×900. Unchanged.
- S3's speaker notes each begin with their minutes ("4 min.") and total 60. Keep the total at 60.

### 4.3 Wording shared by all three decks
These exact strings are used wherever the tables in §5 name them.

| Name | Exact text |
|---|---|
| ASK | `The prompt asks. Settings enforce.` |
| DATA | `What the agent reads goes to the AI provider. Made-up files only, never customer or bank data.` |
| UNTESTED | `Untested — rehearse before class.` (S2 already uses this text) |

- **Spelling:** "back end" and "front end" (two words) in every title, visible slide text, diagram label, `aria-label` and speaker note. S3 currently uses "backend" 63 times and "frontend" 15 times. Text inside practice prompts, file paths and code identifiers is left as it is *(call)*.
- **One name:** "practice password", never "test password", in titles, visible text, diagram labels and notes.

### 4.4 The ask-first setting *(user: approach B)*
- No slide and no prompt hard-codes OpenCode configuration keys *(call)*. Reason: OpenCode's permissions page (read 2026-11-17) documents `permissions` rules of the form `{ "action", "resource", "effect" }` with `"effect": "ask"`, and warns that the earlier version uses different field and action names. The version on the class laptops is not known.
- The prompt step is worded as an outcome: the agent reads the installed version's own permissions documentation, proposes a change that makes OpenCode ask before every use of the named tools, shows the change before saving, and then proves it by attempting one harmless action and reporting that OpenCode asked.
- The facilitator checklists (§8) get the matching item, so the setting can be prepared before class instead.
- Because it is untested, every place that mentions the setting keeps the UNTESTED label in reach, and the slide wording is true whether or not the setting works: titles are instructions, never guarantees.

## 5. What changes, finding by finding

### 5.1 Titles
All other titles stay as they are. The outlines in `docs/outlines/session-*-visual.md` are updated to match. Approval of this spec is the `AGENTS.md` story gate for these titles *(call)*.

| Deck | Slide | Current title | New title | Finding |
|---|---|---|---|---|
| S1 | 7 | Divide the IDR amount by the rate to get USD. | The rate turns an IDR amount into USD. | #14 |
| S1 | 8 | The back end fetches the rate once and reuses it. | The back end fetches the rate, keeps it for an hour and reuses it. | #37 |
| S1 | 10 | The agent plans first and builds only what you approve. | Ask the agent to plan first and build only what you approve. | #2 |
| S1 | 13 | The agent reads one folder, calculates, and saves a new file. | Ask the agent to read one folder, calculate, and save a new file. | #2 |
| S1 | 14 | Google Drive access needs a one-time OAuth setup. | Google Drive access needs a facilitator setup first. | #36 |
| S1 | 15 | The agent proposes each install step and you approve it. | Ask the agent to propose each install step, then approve it yourself. | #2 |
| S1 | 16 | The agent writes to Drive only after you approve a preview. | Ask the agent to show a preview before it writes to Drive. | #1 |
| S2 | 9 | Hiding the Admin menu does not stop a User. | Budi's screen shows no Admin menu. | #14 |
| S2 | 14 | The agent builds one approved stage at a time. | Ask the agent to build one stage at a time, and approve each one. | #2 |
| S3 | 4 | HTTPS connects the browser to your frontend and backend. | HTTPS connects the browser to your front end and back end. | #40 |
| S3 | 5 | The backend still calls the external APIs and LLM. | The back end still calls the external APIs and LLM. | #40 |
| S3 | 10 | A Python environment runs the backend without Docker. | A Python environment runs the back end without Docker. | #40 |
| S3 | 11 | A managed service keeps the backend running after logout. | A managed service keeps the back end running after logout. | #40 |

Imperative titles ("Ask the agent…") are accepted as full sentences; S3 already uses them (slide 8: "Inspect the app and approve a deployment plan first.").

### 5.2 S1

| Finding | Slide | Change |
|---|---|---|
| #1 | 16 | New title (§5.1). Replace the footer "No overwrites. No deletes. No sharing changes." with ASK. The four steps Read → Preview → Approve → Save stay. Notes: say that the three "no" rules are requests in the prompt, and that the ask-first setting or the practice account is what limits damage. |
| #1, #2 | prompt `drive-setup` (opens from slide 15) | Add the ask-first step of §4.4 for the Drive tools, before the first read. |
| #2 | 10 | New title. Add ASK as a visible line: this is where the idea is taught once. Notes explain it in two sentences. |
| #2 | 13, 15 | New titles. |
| #3 | 13 | Add DATA as a visible line. |
| #4 | prompt window | `promptDialog` shows UNTESTED in every prompt window, as S2 does. |
| #5 | prompt `drive-setup`; slide 14 | In the prompt, replace "the reviewed package" with "the version the facilitator chose (not a security review)". On slide 14 add the visible line "Confirm with bank IT before class." |
| #16 | 14 | Notes and participant sheet carry the worked consent example (§7). On the slide, replace "Review consent" with wording that names the decision: what access is expected, and "anything else: stop and ask". |
| #17 | 6 | Add a plain translation next to the request: "Ask: what is one USD worth in IDR?"; label `GET` as "a read request", `base` as "from currency", `quote` as "to currency". |
| #14 | 7 | New title. Add a visible question in the body: "160,000 IDR at 16,000 IDR per USD: multiply, divide or relabel?" Hide the "÷" sign and the result tile until an answer is clicked; the correct answer reveals both. The existing answer text stays. |
| #29 | 15 | Number the six steps 1–6 in their true order, alternating agent and participant. |
| #30 | 12 | Replace the sideways "APP" and "AGENT" labels with horizontal row headings at heading size. |
| #31 | 4 | Add row labels "Coffee shop" and "Our app". |
| #38 | 4 | Under "Service counter", change "A defined request" to "Takes defined orders". |
| #32 | 3, 6 | The two disclaimers use `--ink` or `--muted` at body size and sit next to the number they qualify. |
| #33 | 10 | Enlarge the OpenCode mock-up, keep the three lines that teach, align the prompt buttons in one row under it. |
| #36 | 14 | New title. Notes: "Sign-in lasts about a week while Google's setup is in test mode." |
| #46 | 11 | Shorten the four cards and number the checks 1–4. |
| #47 | 2, 3 | Mock-up labels meet the text-size floor (§9, check 9). |

### 5.3 S2

| Finding | Slide | Change |
|---|---|---|
| #2 | 14 | New title. Add ASK as a visible line. |
| #6 | 12 | Replace "Added, never edited." with "The app only adds lines; it has no edit or delete." Add the visible line "A real audit log also needs protection and retention set by IT." |
| #7 | 5, 6 notes | Slide 5 notes: "one common way" instead of "the standard way most". Slide 6 notes: replace "Later, only that one function would change." with "Later, bank IT decides how a real sign-in connects, often single sign-on, which changes more than this function." |
| #12 | 17 | Add the visible line "Session 3 also needs prompt 2, steps 4–5." |
| #12 | 18 | The finish slide carries a "Ready for Session 3" item; the full checklist is on the participant sheet (§7). |
| #13 | 14 notes; sheet | The plain approval card is on the participant sheet. Slide 14 notes point the facilitator to it. The prompts keep every protection. |
| #14 | 9 | New title. The question stays in the body. The answer text after a click becomes "B. Hiding the menu does not stop a User. The back end must refuse the request." |
| #15 | 15 notes; sheet | Notes: the facilitator demonstrates one direct request through the agent. The sheet gives the exact sentence to ask the agent and the expected "403 Refused". |
| #33 | 14 | As S1 slide 10: larger mock-up, buttons aligned under it. |
| #34 | 6 | The mock-directory card becomes the largest element; its labels meet the text-size floor. |
| #35 | 16, 18 | Number Budi's three audit rows 1–3 on slide 16. Slide 18 card 4 keeps "steps 1 to 3", which now refers to them. |
| #45 | 18 | Card 4 shows a three-row mini audit table instead of the grey icon. |
| #39 | 4 | Replace "Proved once / At sign-in." with "Proved at sign-in; the pass is shown on every request." |

### 5.4 S3
Every row below changes both copies of the slide (§4.2).

| Finding | Slide | Change |
|---|---|---|
| #2 | 8 | Add ASK as a visible line. Notes: the facilitator has set OpenCode to ask before server commands for this lab (§4.4, §8). |
| #2 | prompt `plan` | Add the ask-first step of §4.4 for shell commands, before any command that reaches the server. |
| #4 | prompt window | Every prompt window shows UNTESTED in addition to the existing "Training VPS only…" line. |
| #8 | 4 | New title (spelling). **Correction to the report:** the two bottom boxes are clickable quiz options with feedback (`data-answer`, `data-feedback`), not unmarked labels. Make that visible: add the question "Which address works for a colleague?", prefix the options "A ·" and "B ·" as S1 and S2 do, and keep the feedback on click. In the picture: add a "Website files" box served at the entry point, label the hop to FastAPI "inside the server", and draw the laptop-address path as a crossed-out arrow. |
| #9 | 5 | New title (spelling). Draw "Prices / FX" as an outside service box of the same kind as "LLM provider", with no browser frame. The arrow runs from the back end out to it. Number the two outgoing calls. |
| #10 | 6 | Add the visible line "Use only the training key the facilitator gives you. Never a personal or bank key." |
| #11 | 2 | Add the visible line "First connection: check the server's code matches your card. If it ever changes, stop and call the facilitator." Notes: one sentence on why. |
| #18 | 3 | Show a small filled-in example card with four fields (address, account, port, folders), marked "Example", using `example.invalid`. The full example card is on the participant sheet. Visible instruction: "Collect your own card before prompt 1." |
| #19 | 11 | Replace the labels "systemd --user" and "Lingering prepared by facilitator" with plain words ("Service manager", "Keeps running after you log out — set up by the facilitator"). The healthy-status example is on the participant sheet. |
| #20 | 15 | See §8. On the slide: name a safe blocked outcome ("Blocked? Stop, note where, call the facilitator") and mark the restore test (prompt `recover`) as "after class or facilitator demo". The five time blocks stay. |
| #21 | 13 | Label Budi's row "User tries admin page" and Alya's "Admin request", with each person's role shown. Add five small evidence labels: login and roles, saved data, exchange rate, Wiki answer, still works after logout. |
| #22 | all | Restyle (§6). |
| #23 | 1 | Opening slide in the S1/S2 layout (§6). |
| #24 | all | Buttons and footer (§6). |
| #25 | 8 | "Approve" sits above the arrow, clear of the line. |
| #26 | 3 | The arrow stops above the label "Assigned HTTPS + port". |
| #27 | 6 | Replace the loose icons with one labelled pair: "Old practice password ✕ → New private password ✓". |
| #28 | 14 | Two rows in reading order: "Fail → Logs → Diagnose" and "Backup → Test restore (separate place, never over the live data)". |
| #40 | all | Spelling and "practice password" (§4.3). |
| #41 | prompts | A one-line plain summary above each of the seven prompts in the prompt window, saying what the prompt makes the agent do. The prompt text itself stays. |
| #42 | 9 | The warning ".env · sessions · MCP tokens" becomes a visible label in `--ink`: "Secret files are not copied". |
| #43 | 8 | The prompt buttons sit beside the picture. |
| #44 | all | Titles (§6). |

## 6. Session 3 restyle *(user: approach A)*

- **Opening slide (slide 1):** the S1/S2 hero layout: a kicker "Financial App · Session 3 of 3", the title as the large statement, two chips "60 min · presentation" and "60 min · practice", and the existing laptop-to-VPS picture at reduced size on the right.
- **Footer:** every slide's footer carries "Financial App · Session 3 · VPS deployment" on the left, as S1 and S2 carry theirs. The slide counter stays on the right.
- **Buttons:** a slide's main prompt button is filled black with white text (S3 already defines `.btn.dark`); secondary buttons stay outlined. Buttons sit with the content they belong to, not alone at the bottom left.
- **Arrows:** solid lines in `#f30` with an arrowhead. No dashes, no travelling dots. S3's flow-dash and packet animations are removed; S1 and S2 have no animation.
- **Cards:** each diagram part sits on a white rounded card with a thin border, as in S1 and S2. Icons are stroke-only.
- **Titles:** letter-spacing no tighter than `-0.02em`, and no title leaves a single word on its last line (`text-wrap: balance` or a narrower `max-width`). Titles are not reworded for this.
- **Kept:** S3's embedded typefaces (Archivo, Nunito, JetBrains Mono), its 1920×1080 stage, its deck-data structure, its prompt pack and deployment-card download.
- Slides not named in §5.4 get the restyle only; their content does not change.

## 7. Participant sheets

Three new files, each one self-contained HTML file, printable on A4, at most two pages, Arial, no network requests:

- `handouts/session-1-participant-sheet.html`
- `handouts/session-2-participant-sheet.html`
- `handouts/session-3-participant-sheet.html`

Each sheet has one row per practice prompt (seven per session), in the order the prompts appear in the deck, with four columns: **Prompt** (number and title as shown in the deck) · **What you are approving** (plain words, no term from the "unexplained words" tables of the review unless translated in the same cell) · **A good result looks like** · **Call the facilitator if**. Each sheet states at the top that the prompts are untested, and carries DATA.

Session-specific blocks:

| Sheet | Block | Finding |
|---|---|---|
| S1 | The Google consent screen: which account, which access is expected (full Drive access for the practice account), where the client file lives in plain words, and "anything else: stop and ask". | #16 |
| S2 | Plain approval card: for each protection in prompts 1–2 (session cookie settings, forged-request protection, sign-in limit, password storage), one line on what it prevents and what evidence to ask for. | #13 |
| S2 | The refused-request test: the exact sentence to ask the agent, and the expected result "403 Refused". | #15 |
| S2 | "Ready for Session 3" checklist: login, roles, forged-request protection, sign-in limit, audit trail; each "done / needs catch-up". | #12 |
| S3 | A filled-in fictional deployment card with every field of the deck's card (`ssh_host`, `ssh_user`, `ssh_host_key_fingerprint`, `https_url`, `url_base_path`, `loopback_port`, `private_release_root`, `private_data_dir`, `private_config_path`, `public_static_dir`, `user_service_name`), marked "Example — not your values", each field tagged "facilitator supplies" or "you check". Hosts use `example.invalid`. | #18 |
| S3 | An example of a healthy service status in plain words, marked "Illustrative", and what to check versus what only the facilitator fixes. | #19 |
| S3 | Evidence sheet: login and roles, saved data, exchange rate, Wiki answer, still works after logout; one expected result each, with "pass / not run". | #21 |
| S3 | The safe blocked outcome and when to stop. | #20 |

The decks do not link to the sheets (a link would break when a deck is copied alone); the practice slide's notes tell the facilitator to hand them out *(call)*.

## 8. Findings that editing cannot fix

| Finding | What is done instead |
|---|---|
| #20 — S3 has seven prompts in sixty minutes | The slide and sheet changes in §5.4 and §7, plus a facilitator checklist item: "Rehearse the full practice on a participant-like laptop and time it." Whether sixty minutes is enough stays unknown until that rehearsal. |
| #5 — the Drive tool is not approved by anyone | The wording change in §5.2, plus a facilitator checklist item: "Confirm with bank IT that the Drive tool may be used on work laptops." |

Facilitator checklist items go in each deck's existing help window (S1 "Setup help", S2 help, S3 "Facilitator setup"). Each deck's checklist also gets: "Rehearse every prompt; all are untested" and "Set OpenCode to ask before Drive actions (S1) / server commands (S3), or run the ask-first prompt step and confirm it asks."

## 9. Checking

New file `tools/day4-deck-check.mjs`, run as `node tools/day4-deck-check.mjs` (all three decks and the sheets) or with `--only=s1|s2|s3|sheets`. It uses `playwright-core` from `tools/deck-check/node_modules` and Microsoft Edge at `C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe`, as the existing scripts do. It prints one `FAIL <check> <deck> slide <n>: <reason>` line per problem, then `PASS` or `FAILED: <n>`, and exits 1 on any failure.

`tools/session-2-visual-check.mjs` is deleted *(call)*: it already fails 20 checks on today's S2 (titles changed after it was written; its reference file is outside the repository), and the new script replaces it.

| # | Check |
|---|---|
| 1 | Slide count is 18 / 18 / 16. Each slide has exactly one heading and one speaker note. `data-title` equals the heading text and equals line N of that deck's outline in `docs/outlines/`. |
| 2 | Visible words, title and footer excluded: at most 40, and at most 60 on S1 17, S2 17, S3 15. |
| 3 | At 1600×900 and 1280×720, no visible element of the active slide lies outside the stage. |
| 4 | No console error, no page error, no request that is not `file:`, `data:` or `blob:`. |
| 5 | Each deck has seven prompts. Every prompt window contains UNTESTED. S3: every prompt window has a non-empty summary line. |
| 6 | Shared wording: ASK is visible on S1 slides 10 and 16, S2 slide 14, S3 slide 8. DATA is visible on S1 slide 13. |
| 7 | Banned in titles and visible text: "only after you approve", "one-time", "never edited", "test password". Banned in S1's prompts: "reviewed package". Banned in S3's titles, visible text, labels and notes: "backend", "frontend". |
| 8 | S3 only: for every slide, the JSON `title` and `notes` equal the section's `data-title` and speaker note, the JSON `visual` equals the section's visual markup, and `words` equals the count from check 2. Notes minutes total 60. |
| 9 | Text-size floor: every visible text element inside a slide's content is at least 16 px tall on screen at 1600×900. Excluded: the footer line, the slide counter and the control bar. |
| 10 | Quizzes (S1 slide 7, S2 slide 9, S3 slide 4): before any click the answer text is empty; on S1 slide 7 the "÷" and the result tile are not visible. After clicking the correct option the answer text is non-empty and, on S1 slide 7, both are visible. |
| 11 | S1 and S2: lines 7 and 10 of the two files are identical to each other. |
| 12 | S3: no `@keyframes` and no `animation` in the file. Every footer contains "Financial App · Session 3". |
| 13 | Sheets: the three files exist; each prints to at most two A4 pages; no network requests; each contains seven prompt rows, the word "untested", and DATA. |

After the decks pass, `node .review/day4-render.mjs` re-renders every slide so the final review can look at the result.

Not checkable by script, checked by the final reviewer from the screenshots: diagram reading order, arrows clear of labels (#25, #26), and whether S3 now looks like S1 and S2.

## 10. Other files

- `docs/outlines/session-1-external-data-visual.md`, `session-2-access-control-visual.md`, `session-3-vps-deployment-visual.md`: titles per §5.1, and a dated line saying the owner approved them with this spec.
- `README.md`: a row for `handouts/`, and the check command.
- `docs/reviews/2026-11-17-day4-decks-review.md`: a new section "Corrections after the review" with the #8 correction (§5.4), and a line pointing to this spec. The findings tables are not rewritten.
- `docs/project-log.md`: one dated entry at the end.

## 11. Left to the builder

- Layout, sizes and exact drawing of every redrawn diagram, within §6.
- Which existing words move to the notes to make room for a new line.
- The plain-language wording on the sheets, the S3 prompt summaries and the fictional card values.
- CSS class names and how the quiz reveal on S1 slide 7 is implemented.
- Wording of speaker-note additions, within what the tables ask for.
