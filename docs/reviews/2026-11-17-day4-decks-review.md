# Review report — Day 4 visual decks (Sessions 1–3)

Date: 2026-11-17. Decks reviewed:

- **S1** — `decks/session-1-external-data-visual.html` (18 slides): exchange-rate API and Google Drive for the agent
- **S2** — `decks/session-2-access-control-visual.html` (18 slides): login, roles, admin page, audit trail
- **S3** — `decks/session-3-vps-deployment-visual.html` (16 slides): moving the app to a server

## How the review was done

Three independent reviewers, one angle each, across all three decks. None saw another's work.

| Angle | Model | Raw review | Findings |
|---|---|---|---|
| Material accuracy and safety habits | claude-opus-5-5, high | `.review/day4-r-material.md` (M1–M18) | 18 |
| Storyline and ease for business users | gpt-6.1-sol, medium | `.review/day4-r-audience.md` (A1–A10) | 10 |
| Visual quality and slide craft | claude-sonnet-5-5, medium | `.review/day4-r-visuals.md` (V1–V26) | 26 |

The coordinator merged the 54 raw findings into 47, re-checked the one P0 against the slide, the prompt text and the OpenCode documentation, looked at the screenshots behind the merged findings, and measured text sizes in the browser (see Coordinator notes).

**Not checked:**

- No practice prompt was run. No app, server, Google sign-in or SSH connection was tried. Every statement about what a prompt does comes from reading it.
- Classroom timing was not measured.
- The pinned version of the Google Drive tool (2.13.0) could not be confirmed; the package site timed out.
- What OpenCode does by default comes from its documentation as of today, not from the version installed for the class.
- The visuals reviewer looked at shrunken images, and did not see the lower part of long prompt panels.

"Slide" below is the slide's position in its deck, which is the number shown on the slide.

Severity:

- **P0** — wrong, misleading or ambiguous knowledge, or an unsafe habit. Fix before teaching.
- **P1** — the idea is right but poorly taught, missing, or in the wrong place; or a slide a non-technical user cannot follow.
- **P2** — a visual or layout problem that hurts clarity.
- **P3** — polish.

"Raised by" = how many of the three reviewers raised it independently, with their raw IDs.

---

## Summary

The material is mostly accurate and unusually careful, and the three decks tell one story across the day. S2 is the strongest deck; S3 is the weakest for this audience. Three things need attention before teaching:

1. **One P0:** S1 slide 16 promises that the agent writes to Google Drive only after you approve. That is a request in the prompt, not something the tool enforces, and the agent is given access to the whole Drive.
2. **The slides are simple; the practice is not.** The slides explain ideas in plain pictures, but the practice prompts ask participants to approve technical steps the slides never explain. This is the main obstacle for non-technical users, most of all in S3.
3. **S2's "must finish" is not enough for S3.** A participant can finish S2 as the slide defines it and then be blocked from publishing in S3.

Counts after merging: **1 P0, 20 P1, 14 P2, 12 P3.** No slide is over its word budget.

---

## Verdict per deck

**S1 — good, with one unsafe promise.** The exchange-rate half is accurate: the live service returned exactly the four fields slide 6 shows, the division is the right way round, and "never an invented rate" is a strong habit to teach. The Google Drive half is the weak part. Its slide titles promise the agent will stop and ask; the setup steps use words a business user has not met; and the rule that only made-up data may be used is not on any slide.

**S2 — the strongest of the three.** An unexplained watchlist change leads naturally to "who are you", "what may you do" and "who did what". The named people (Alya, Budi, Citra), the permission table and the audit pictures teach well, and the core lesson — hiding a menu protects nothing; the server must check — is right and well defended. Problems are narrower: two overstatements a bank audience will notice (the audit trail, the company directory), and practice prompts that require protections no slide explains.

**S3 — technically the most careful, and the hardest to follow.** The backup method, file protections, the publication checks and replacing the published practice password are all correct. But several pictures are unclear or contradict their titles, it does not look like the same course as S1 and S2, and the gap between the simple slides and the long, technical prompts is widest here. For this audience it is a facilitator-led lab, not an exercise participants can follow alone in an hour.

---

## Ease for non-technical business users

Ratings assume participants arrive with the Financial App from earlier training and can already use OpenCode. None of the decks states that as a checklist.

| Deck | Rating | Why |
|---|---|---|
| S1 | **Manageable with a facilitator** | The before/after dashboard, the currency example and the four finish checks are concrete. The Drive half adds consent, a credential file, installation and configuration in two slides. The deck sensibly makes the exchange rate the minimum outcome. |
| S2 | **Manageable with a facilitator** | Most slides ask for one decision or one small comparison. The practice is harder: approving the login prompt needs security vocabulary the slides do not give, and proving "refused" needs a test no slide demonstrates. |
| S3 | **Hard** | A beginner must approve server access, which files are public and which private, a running service, and a long list of publication checks. Sixty minutes depends on heavy facilitator preparation, complete earlier work and rehearsed prompts. |

**Hardest slides**

| Deck | Slide | What makes it hard |
|---|---|---|
| S1 | 14 | Four setup hand-offs plus consent and broad access; unclear what is the facilitator's job and what is the participant's |
| S1 | 15 | Version check, configuration, installation and Google sign-in shown as two lists with no order |
| S1 | 6 | The request and reply are shown in code-like notation with no translation |
| S2 | 17 | Six timed stages hide four linked features; the minimum is named but its consequence for S3 is not |
| S2 | 10 | The participant understands allowed and refused, but not how to run the test or recognise the result |
| S2 | 7 | Directory check, session, repeated requests, "401" and sign-out arrive together |
| S3 | 3 | Account, service, private files, address, port and folders: six assignments with no filled-in example |
| S3 | 9 | Built files, public files, private code and data, a snapshot, and excluded secret files, all before approving a transfer |
| S3 | 11 | A service manager, logging out, and "lingering" — a new way of running things with unfamiliar names |

**Words used without a plain explanation** (first slide where each appears; full tables with what is missing are in `.review/day4-r-audience.md`). "Prompt" means the word appears only in a practice prompt opened from that slide.

| Deck | Slide | Words |
|---|---|---|
| S1 | 1 | Database, Wiki, system prompt (assumed from earlier training) |
| S1 | 6 | API key, GET, base, quote, endpoint |
| S1 | 8 | Back end, React, FastAPI, validate, cache |
| S1 | 10–11 (prompt) | Dependencies, timeout, TTL, HTTP, null, deterministic tests |
| S1 | 13–15 | CSV, OAuth, Cloud project, client file, scopes, configuration, token, npm, pinned package |
| S1 | 16–18 (prompt) | Markdown, revoke, OAuth grant |
| S2 | 6 | Back end, function, `check(name, password)` |
| S2 | 10 | GET, `/api/admin/users`, endpoint, 200 |
| S2 | 13 | Protected API call |
| S2 | 14 (prompt) | Cookie, cookie flags, HttpOnly, SameSite, Secure, HTTPS, expiry, CSRF, token, session ID |
| S2 | 17 (prompt) | Salted hash, header, localhost, seed, front-end guard, direct API request |
| S3 | 1 | VPS, deploy, Docker, backend, LLM |
| S3 | 2 | SSH, Linux, terminal, key agent |
| S3 | 3 | Service, port, paths, proxy, host-key fingerprint |
| S3 | 4 | Frontend, localhost, CORS, TLS |
| S3 | 6 | Rotate passwords, revoke sessions, CSRF, rate limiting, `.env` |
| S3 | 7 | Release, persistent state, 0700, 0600 |
| S3 | 8–9 (prompt) | Allowlist, lockfile, SFTP, quota, build, snapshot, checksum |
| S3 | 10–11 | Python venv, dependencies, pip, systemd, lingering, uvicorn |
| S3 | 12–14 | Certificate, schema migration, rollback |

Well explained and **not** counted: authentication and authorization (S2 slide 4), the company directory (S2 slide 5), the mock directory (S2 slide 6), the audit trail (S2 slide 12), and MCP's purpose (S1 slide 12).

The pattern across all three decks: low word counts do not make a slide easy when it introduces four or five new ideas at once, and most of the unexplained words sit in the prompts, not on the slides. The most useful single fix is a one-page participant sheet per session: prompt number, what you are approving, what a good result looks like, and when to call the facilitator. The technical detail can stay in the prompt for the agent.

---

## P0 — Fix before teaching

| # | Deck | Slide | Problem | Raised by | Fix |
|---|---|---|---|---|---|
| 1 | S1 | 16 | **The slide states a safety guarantee that does not exist.** Title: "The agent writes to Drive only after you approve a preview." Footer: "No overwrites. No deletes. No sharing changes." Both are instructions in the prompt, which the agent may or may not follow. The install prompt gives the tool access to the whole Drive (`GOOGLE_DRIVE_MCP_SCOPES=drive`, which the prompt itself calls "broad Drive access, not a folder sandbox"), and OpenCode's documented default lets the agent use any tool without asking. The deck's own help text says "Prompt instructions are not an access-control boundary", but the slide says the opposite. Bank staff will leave believing Drive writes are safe by design. | 1/3 (M1) | Reword the title as an instruction: "Ask the agent to show a preview before it writes to Drive." Add one visible line: "The prompt is a request. Only settings can force a stop." Then either add a step to the install prompt that sets the Drive tools to "ask first" in OpenCode's permission settings (the documentation shows each tool can be set this way; test it on the class version), or say plainly on the slide that the real safeguard is the practice account with made-up files. |

---

## P1 — Material and teaching weaknesses

### Material and safety

| # | Deck | Slide | Problem | Raised by | Fix |
|---|---|---|---|---|---|
| 2 | S1, S2, S3 | S1: 10, 13, 15 · S2: 14 · S3: 8 | **Same false promise as #1, for code and server work.** Titles state as fact that the agent plans first, reads only one folder, proposes each install step, or builds one approved stage. All rest on the agent obeying the prompt. In S3 the agent may run commands on a shared server. | 1/3 (M2) | Teach once, early in S1: "the prompt asks; settings enforce". Reword these titles as instructions ("Ask the agent to plan first…"). For S3, have the facilitator set commands to "ask first" for the lab and say so on slide 8. |
| 3 | S1 | 13, 16 | **The data rule for bank staff is on no slide.** Whatever the agent reads from Drive is sent to the outside AI provider, so only made-up data may be used. This is only in the slide 16 speaker notes and the help window. Slide 14 says only "Use a non-sensitive account." | 1/3 (M3) | Add one visible line on slide 13 or 16: "What the agent reads goes to the AI provider. Made-up files only — never customer or bank data." |
| 4 | S1, S3 | Prompt windows | **Untested prompts are labelled in S2 only.** S2 marks every prompt "Untested — rehearse before class." S1's prompt window has no label, although its help text says Google sign-in and the Drive read and write were "NOT tested end to end". S3 says only "Training VPS only". | 2/3 (M4, V26) | Use S2's label in all three decks. |
| 5 | S1 | 15 | **The install prompt calls an outside tool "the reviewed package".** The speaker notes say the version is fixed "for reproducibility, not security certification". Bank staff will read "reviewed" as "approved". Nothing tells anyone to check that bank IT allows an outside tool to reach a Google account from a work laptop. | 1/3 (M5) | Replace "reviewed" with "the version the facilitator chose (not a security review)". Add to slide 14 or 15: "Confirm with bank IT before class." |
| 6 | S2 | 12 | **"Added, never edited." overstates the audit trail.** Only the app has no edit button; anyone who can open the database file can change or delete lines. In a bank, "audit trail" implies a protected record with retention rules. | 1/3 (M6) | "The app only adds lines; it has no edit or delete." Bring the note's caveat on screen in a few words: "A real audit log also needs protection and retention set by IT." |
| 7 | S2 | 5, 6 | **The company-directory explanation is overstated.** Notes say LDAP is "the standard way most company directories are reached" and that a real directory would change "only that one function". Banks commonly use single sign-on, where the app never sees the password; that changes the sign-in page and more. This rests on the reviewer's own knowledge, not a project file. | 1/3 (M7) | Note for slide 6: "Later, bank IT decides how a real sign-in connects — often single sign-on, which changes more than this function." Soften "standard way most" to "one common way". |
| 8 | S3 | 4 | **The picture does not say which path is wrong, and leaves out half the title.** Two identical boxes at the bottom ("Browser → laptop localhost", "Browser → assigned HTTPS") carry no mark. The one red cross hangs under the browser. The title says "frontend and backend" but the picture shows only the back end. | 2/3 (M9, V12) | Mark the left box ✗ "Laptop address — fails for others" and the right box ✓, or draw both as arrows in the picture and drop the boxes. Add a "Website files" box served at the entry point. |
| 9 | S3 | 5 | **The picture contradicts the title.** The title says the back end calls the outside services. The price service is drawn as a browser window, with its arrow pointing *into* the back end, so it reads as a browser pushing data in. | 2/3 (M10, V13) | Draw the price service as an outside box like "LLM provider", with the arrow going from the back end out to it. |
| 10 | S3 | 5, 6 | **Nothing says which AI key may go on the shared server.** The prompts make participants supply one; no slide, card or help text says where it comes from. Staff may paste a personal or work key. | 1/3 (M11) | State on slide 6: "Use only the training key the facilitator gives you. Never a personal or bank key." |
| 11 | S3 | 2, 8 | **The prompts require a check the slides never teach.** Participants must confirm the server's identity code with the facilitator and must stop if it ever changes. No slide or note explains what that is or why it matters. | 1/3 (M12) | A few words on slide 2: "First connection: check the server's code matches your card. If it ever changes, stop and call the facilitator." |

### Teaching and ease of following

| # | Deck | Slide | Problem | Raised by | Fix |
|---|---|---|---|---|---|
| 12 | S2 → S3 | S2: 17 | **S2's minimum outcome is not enough for S3.** Slide 17 says "Must finish: Login and Roles." The login prompt allows two protections (against forged requests, and a limit on failed sign-ins) to be reported as not done. S3 refuses to publish without them and forbids building them during deployment. No S2 slide explains either one. | 2/3 (M8, A1) | End S2 with a visible "ready for deployment / needs catch-up" checklist. Add one line on slide 17: "Also needed before Session 3 can publish: prompt 2, steps 4–5." Plan a catch-up slot. Keep the protections. |
| 13 | S2 | 14 | **Participants are asked to approve security steps they cannot judge.** The planning and login prompts list cookie settings, forged-request protection, password storage and sign-in limits. Slides 4–13 explain sign-in and roles at a much simpler level. | 1/3 (A5) | Add a plain approval card: what each protection prevents, what evidence to ask for, when to call the facilitator. Leave the technical wording in the prompt for the agent. |
| 14 | S1, S2 | S1: 7 · S2: 9 | **Both quiz slides give away the answer.** S1 slide 7's title is "Divide the IDR amount by the rate to get USD.", the picture shows 160,000 ÷ 16,000 = $10.00, and the choices are Multiply / Divide / Relabel — with no question on the slide. S2 slide 9's title is "Hiding the Admin menu does not stop a User." above the question it answers. | 2/3 (V1, A10) | On the quiz slide use a neutral heading ("Quick check") and put the question in the body; reveal the answer on the next slide. Or ask a different question that needs the idea applied (a new amount; what would prove a request was refused). |
| 15 | S2 | 10 | **The central test is described, not shown.** The slide shows the request getting "200" or "403 Refused"; slide 18 makes the refusal a finish condition. Nowhere does a participant see how to run that test or what the evidence looks like. | 1/3 (A6) | Demonstrate one direct request through the agent, show the refused result, and give participants the exact sentence to ask the agent plus the expected answer. |
| 16 | S1 | 14 | **The Drive setup gives vocabulary but no decision.** "Review consent" is not enough to spot an unexpected permission request. The help text admits the participant flow was not tested end to end. | 1/3 (A7) | Walk through one rehearsed example with the account, the permission screen and the file location. Say which requested access is expected, and give a stop-and-ask rule for anything else. |
| 17 | S1 | 6 | **The first real request is shown in code-like notation with no translation.** `GET /v2/rate/usd/idr`, `base`, `quote`. | 1/3 (A8) | Add "Ask: what is one USD worth in IDR?" Label GET as "a read request", and base and quote as "from" and "to" currency. |
| 18 | S3 | 3 | **The starting assignments are too abstract to act on.** "Your service", "Assigned HTTPS + port", "Separate paths + port". The downloadable card is blank, and the first prompt stops if assignments are missing. | 1/3 (A2) | Show one clearly fictional filled-in card, marked "facilitator supplies / participant checks", and tell participants to collect their own card before prompt 1. |
| 19 | S3 | 11 | **Participants must approve and recognise a healthy running service without ever seeing one.** | 1/3 (A3) | Pair the diagram with a short worked approval and a cleaned-up example of a healthy status. Mark what the participant checks and what only the facilitator fixes. |
| 20 | S3 | 15 | **Seven prompts in sixty minutes, with no shorter route.** The timeline (10 plan, 15 transfer, 15 start, 15 verify, 5 show) hides several approvals, replacing passwords, data checks, live service checks and a restore test. The notes admit more time may be needed. | 1/3 (A4) | Rehearse on participant-like laptops. Publish the readiness checklist before practice. State a safe "blocked" outcome, allow overflow time, and take the restore test out of the five-minute show slot. |
| 21 | S3 | 13 | **The picture covers one quarter of what the title promises, and its labels mislead.** The title lists login, permissions, API calls and Wiki answers; the picture shows only the permission check. Both rows are labelled "Admin request", so it does not say Budi is refused because he is a User. | 2/3 (A9, V16) | Label Budi's row "User tries admin page". Add a small evidence sheet with one expected result each for login and roles, saved data, exchange rate, Wiki answer, and "still works after logout". |

---

## P2 — Visual problems that hurt clarity

| # | Deck | Slide | Problem | Raised by | Fix |
|---|---|---|---|---|---|
| 22 | S3 | all | **S3 does not look like the same course.** S1 and S2 use flat white cards, solid red arrows and screen mock-ups. S3 uses sketch-style line drawings, grey-green dashed arrows with red dots, no cards, and a different typeface. | 1/3 (V9) | Redraw S3's diagrams on the S1/S2 card system, or at least match the title style, footer and buttons (#23, #24). |
| 23 | S3 | 1 | No opening slide like S1 and S2 ("Session N of 3", the two timing chips). Slide 1 is already a diagram, with the timing as a faint caption. | 1/3 (V18) | Add the same opening layout. |
| 24 | S3 | all | Prompt buttons are outlined boxes at bottom left; S1 and S2 use filled black buttons. S3's footer has no "Financial App · Session 3" label. | 1/3 (V20) | Reuse the S1/S2 buttons and footer. |
| 25 | S3 | 8 | The arrow runs through the word "Approve" like a strike-through — on the one word the slide teaches. | 2/3 (V11, M13) | Move the label above the arrow. |
| 26 | S3 | 3 | The arrow tip crosses the label "Assigned HTTPS + port". | 1/3 (V10) | Stop the arrow above the label. |
| 27 | S3 | 6 | Loose small icons at lower left (magnifier, crossed circle, arrow, key) over "Rotate test passwords"; the meaning cannot be read. | 1/3 (V14) | One labelled pair: "Old practice password ✕ → New private password ✓". |
| 28 | S3 | 14 | The recovery picture has no reading order. "Diagnose" has no arrow; the "Live DB" and "Test restore" boxes with a crossed line are not explained. | 1/3 (V15) | Two rows in reading order: Fail → Logs → Diagnose, and Backup → Test restore (separate place, never over the live data). |
| 29 | S1 | 15 | Six install steps with no numbers or arrows. Agent steps are on the left and participant steps on the right, but the real order alternates. | 1/3 (V6) | Number the six steps in true order, or draw the zig-zag. |
| 30 | S1 | 12 | The two rows are named only by small sideways labels "APP" and "AGENT" (14 px) — and those labels are the whole point of the slide. | 1/3 (V3) | Horizontal row headings at heading size. |
| 31 | S1 | 4 | Two rows of three cards teach "coffee shop = API", but nothing says the top row is the comparison and the bottom row is our app. | 1/3 (V5) | Add row labels ("Coffee shop", "Our app"). |
| 32 | S1 | 3, 6 | The lines that stop the numbers being read as real prices ("Illustrative values · not a trading quote", "Reference rates—not real-time trading prices.") are pale grey and among the least prominent text on the slide. | 1/3 (V2) | Darken them and place them next to the number. |
| 33 | S1, S2 | S1: 10 · S2: 14 | The OpenCode mock-up has small text (labels measure 13 px) and its buttons sit loose beside it at different heights. | 1/3 (V4) | Enlarge the mock-up, cut it to the three lines that teach, align the buttons under it. |
| 34 | S2 | 6 | The mock-directory card carries the key idea of the slide in its smallest text ("Practice accounts only" measures 14 px). | 1/3 (V7) | Make this card the largest element. |
| 35 | S2 | 18 | Card 4 says "Audit trail shows steps 1 to 3", but no step is numbered anywhere, including slide 16's audit rows. | 1/3 (V8) | Number Budi's rows on slide 16 and reuse the numbers, or reword to "Budi's sign-in, watchlist change and refusal". |

---

## P3 — Polish

| # | Deck | Slide | Problem | Raised by | Fix |
|---|---|---|---|---|---|
| 36 | S1 | 14 | "One-time OAuth setup" is too absolute: while Google's setup is in test mode, the sign-in expires after about a week (confirmed in the Drive tool's documentation). | 1/3 (M14) | "…needs a facilitator setup first." Note: "Sign-in lasts about a week in test mode." |
| 37 | S1 | 8 | "Fetches the rate once" could mean once ever; the prompt keeps it for one hour. | 1/3 (M15) | "…fetches the rate, keeps it for an hour and reuses it." |
| 38 | S1 | 4 | Under "Service counter" the caption says "A defined request", but the request is the order, so the two rows do not line up. | 1/3 (M16) | "Takes defined orders". |
| 39 | S2 | 4 | "Proved once, at sign-in" against "Checked every time" clashes with slide 7, where the pass is checked on every request. | 1/3 (M17) | "Proved at sign-in; the pass is shown on every request." |
| 40 | all | — | Different spellings and names for the same thing: "back end / front end" (S1, S2) and "backend / frontend" (S3); "practice password" (S2) and "test passwords" (S3). | 1/3 (M18) | One spelling and one name across the day. |
| 41 | S3 | prompts | S3's prompts are far longer than S1's and S2's — five or six dense paragraphs — so the window shows about the first third. | 1/3 (V25) | Add a one-line plain summary above each prompt, or split into steps. |
| 42 | S3 | 9, 11, 12 | Two captions carrying teaching content (".env · sessions · MCP tokens" on slide 9, "Lingering prepared by facilitator" on slide 11) are grey and easy to miss, though not small (about 24 px on screen). The mock-up label "Local app" and the address on slide 12 are about 18 px. Lowered from P2: all are larger than the smallest text in S1 and S2. | 1/3 (V17) | Move the key warning ("secret files are not copied") into a visible label. |
| 43 | S3 | 8 | Large empty area under the mock-up; the two prompt buttons sit far away and read as captions. | 1/3 (V19) | Put the buttons beside the picture. |
| 44 | S3 | all | Title letters are set tighter than in S1 and S2; several titles wrap leaving one or two words on the second line (slides 2, 3, 4, 11). | 1/3 (V23) | Match the S1/S2 title style; shorten the longest titles. |
| 45 | S2 | 18 | Cards 1–3 show a picture; card 4, the audit trail, shows only a grey icon. | 1/3 (V21) | A three-row mini audit table in card 4. |
| 46 | S1 | 11 | Four tall cards hold an icon and two lines each; mostly empty. | 1/3 (V22) | Shorten the cards and number the four checks. |
| 47 | S1 | 2, 3 | Small grey labels in the app mock-ups: "Saved price history · Wiki chatbot" on slide 2 (15 px) and "NISP.JK · SAMPLE" on slide 3 (14 px). The reviewer also named the timing chips on slide 1; those measure 17 px in dark text and are left out. | 1/3 (V24) | Raise to body size or cut. |

---

## What works well

- **S1 slides 3–9: the exchange-rate story.** A business request becomes a specific reply and simple arithmetic. The direction of the division is explained by units, a missing rate shows IDR only ("never an invented rate"), and stored rates are labelled. Slide 6 was confirmed against the live service.
- **S1 slides 12 and 16: app and agent kept apart.** Two separate lanes prevent the expectation of a Drive button in the app; read → preview → approve → save is a memorable routine (once worded as a request, see #1).
- **S2 slides 9, 10, 15: the right lesson, proved the right way.** Hiding a menu is tidiness, not protection; the server checks; and it is tested with a direct request rather than by looking at the screen.
- **S2 slides 12, 13, 16: the audit trail.** Who, what and when, then the real log table; passwords and session passes are never recorded.
- **S2 slides 3, 8: named people and a permission table** answer the opening question without anyone reading code.
- **S3 slides 2, 7, 16: three boundaries made visible** — server login versus app login, data that survives updates, and the app still working after the participant logs out.
- **S3 slide 6 and its prompts: the published practice password is treated as compromised** before the app goes public, and "HTTPS alone is not sufficient" is said plainly.
- **Practice slides (S1 17, S2 17, S3 15)** are clear timelines, and S1 and S2 name a smaller minimum outcome.
- **Word budgets are respected everywhere:** S1 20–54, S2 23–57, S3 15–25 visible words; the two highest are exercise slides with a limit of 60.

---

## Suggested order of fixes

1. **#1, then #2 and #3** — the false "the agent will ask first" promise and the missing data rule. These are the habits bank staff should not take away. Decide first whether the class laptops will have "ask first" switched on; that decides the wording.
2. **#12** — make S2's finish line match what S3 needs. Otherwise part of the room is blocked in the last session.
3. **#8 and #9** — two S3 pictures that teach the wrong thing. Small redraws.
4. **#4, #5, #10, #11** — one-line additions: untested labels, "reviewed package", which AI key, the server identity check.
5. **The participant sheet** (#13, #15, #16, #18, #19, #21) — one page per session: prompt number, what you are approving, what good looks like, when to call the facilitator. This is the largest single gain for non-technical users.
6. **#14** — the two quizzes.
7. **#6, #7** — soften the audit-trail and company-directory wording.
8. **#20** — rehearse S3 and decide its fallback before the day.
9. **S3 visuals** (#22–#28), then the remaining P2 and P3.

---

## Coordinator notes

- **The P0 (#1) was re-checked and kept.** The slide title and footer were read on the screenshot (`.review/day4-shots/s1/s16.png`). The install prompt's wording about broad Drive access and the help text's "not an access-control boundary" sentence were found in the deck. OpenCode's permissions page, fetched 2026-11-17, says every agent starts with a base policy that allows actions, and shows that each outside tool can be given its own rule — so the suggested fix is possible. **Caveat:** the project log records that during the Day 3 rehearsal (OpenCode 1.19.5) the tool did show "Allow once / Allow always / Reject" for some actions. Behaviour depends on the version and settings on the class laptops. If those laptops ask before each Drive action, #1 drops to a wording fix; the title should still not state a guarantee.
- **Text-size findings were measured, not estimated.** The visuals reviewer worked from shrunken images. Sizes were measured in the browser at 1600×900 (`.review/day4-fontsize.mjs`). Results: S1 and S2 small labels are 13–15 px, slightly larger than the reviewer's estimates of 10–12 px but still small; S3's mock-up labels are about 18 px and its grey captions about 24 px on screen. V17 was therefore lowered from P2 to P3 (#42) and slide 3 was removed from it (no small caption found there). In V24 the slide 1 chips were dropped at 17 px and the slide 3 label was added (#47). The disclaimers in V2 are not the smallest text on their slides; that finding is kept for their pale colour and placement, not their size.
- **Merged findings** (7): M8+A1 (#12), M4+V26 (#4), M9+V12 (#8), M10+V13 (#9), V1+A10 (#14), A9+V16 (#21), V11+M13 (#25). Each keeps the highest severity given.
- **Reviewers disagreed on the quizzes (#14):** the visuals reviewer rated them P1, the audience reviewer P3. Kept at P1, because S1 slide 7 has no question at all on the slide. They also differ on the fix: the visuals reviewer would replace the title with a neutral heading and reveal the answer afterwards; the audience reviewer would keep the explanatory titles and ask a different question that applies the idea. #14 lists both.
- **Session 2's titles.** The 2026-11-17 Session 2 design called for short titles. The deck now shows full-sentence titles matching `docs/outlines/session-2-access-control-visual.md` (changed in commit `aa85733`). All three decks follow the full-sentence rule; no finding.
- **Not confirmed by a second source:** #7 (single sign-on) rests on the reviewer's knowledge. #2 rests on the same OpenCode documentation as #1.
- **No finding was dropped.** Every P0 and P1 from the raw reviews appears above.
- **Process note.** All three first-choice models failed with connection errors partway through; the reviews were completed on a later attempt with the same models. The audience reviewer's final confirmation message did not reach the coordinator, who checked its file directly (10 findings, three ratings, all cells filled, committed as `69541ec`).

---

## Corrections after the review

Added 2026-11-18, when the findings were fixed. The findings tables above are left as they were written.

- **#8 (S3 slide 4) described the slide wrongly.** The two boxes at the bottom ("Browser → laptop localhost", "Browser → assigned HTTPS") were clickable quiz options with feedback, not unmarked labels. No reviewer clicked them, and nothing on the slide said they were a question. The fix makes the quiz visible (a question, "A ·" and "B ·" options) and shows the crossed-out laptop path only after an answer is clicked.
- **The fixes are specified in** `docs/superpowers/specs/2026-11-18-day4-decks-fixes-design.md`, which lists the change made for each finding #1–#47.
- **Two findings cannot be fixed by editing** and are now facilitator checklist items in the decks' help windows: #20 (whether sixty minutes is enough for Session 3 is unknown until a timed rehearsal) and #5 (bank IT has not confirmed the Drive tool may be used on work laptops).
- **Nothing was tested live.** Every practice prompt, and the new step that sets OpenCode to ask before Drive and server actions, is untested and labelled so.
