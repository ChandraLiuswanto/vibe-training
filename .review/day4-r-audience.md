# Day 4 decks — storyline and audience review

Checked: All 52 slides in order, their speaker notes, all 21 complete practice prompts, and all 73 supplied PNGs (s1 and s2: s01–s18 and p01–p07; s3: s01–s16 and p01–p07). Read the three deck files for slide/prompt content and setup/help wording, the three `docs/outlines/session-*-visual.md` outlines, `AGENTS.md`, and the Day 4 Session 2 design spec. PNGs show the complete slides, but only the top of long prompt panels; full prompt text was checked in `.review/day4-text/` and embedded deck content. This is a teaching review, not an app or security certification: no prompt, installation, account sign-in, API call or deployment was run, and no classroom timing was measured. Other reviewers' files were not read.

## Verdict per deck
- s1: The currency-conversion story starts with a business need, explains the connection, works through the arithmetic, then asks for evidence. Drive adds a second, distinct workflow, clearly separated from the app, but its permission and installation steps need guided support rather than just a copyable prompt.
- s2: The strongest story of the three: an unexplained watchlist change leads naturally to identity, permissions and a record of actions. The named people and screen examples are accessible; the practical work becomes harder when participants must approve login protections and prove a direct request was refused.
- s3: The order is sensible—understand the destination, plan, transfer, start, publish, verify—but the explanatory slides are much simpler than the work hidden behind their buttons. For this audience, this is a facilitator-led technical lab, not an independently followable one-hour exercise.

## Ease for business users

Ratings assume participants bring the Financial App from previous training and can already open it and use OpenCode. The decks recall the app, but do not establish a complete starting-readiness checklist. Knowing a feature exists is not the same as knowing server commands or how to evaluate their output.

The term tables list technical vocabulary left without a usable plain explanation at first encounter in that deck, counting speaker notes as available facilitator support. They include inherited terms not explicitly established as prerequisites, marked **recall**, and new terms confined to prompts, marked **prompt**. Related labels share a row but each term is named; this is not a demand to teach every implementation detail. For prompt-only terms, the slide number is where the relevant prompt opens, or the practice slide for a prompt available only from the pack. The better fix is often to separate agent instructions from the short explanation the participant needs.

### s1 — Manageable with a facilitator

The before/after dashboard, currency example and four finish checks give a business user something concrete to understand and verify. The Drive half adds consent, a credential file, installation and configuration, so the hour is plausible only as a rehearsed, supported target; the deck rightly makes FX the minimum outcome and admits Drive may remain blocked.

Three hardest slides:
1. **14:** four setup handoffs plus consent and broad access; the participant must distinguish facilitator work from their own private file handling.
2. **15:** configuration, version checking, installation approval and Google sign-in are grouped as two people's responsibilities, not a worked sequence of screens and decisions.
3. **6:** the request path and response labels need translation before a newcomer can read the example confidently.

| Unexplained term(s) | First slide | What is missing for this audience |
| --- | --- | --- |
| Database; Wiki; system prompt (**recall**, including notes) | 1 | A prerequisite or brief reminder of what each holds in this app. |
| API key; GET; base; quote; endpoint (notes) | 6 | “Read request”, “from currency”, “to currency”, service address, and why a key would otherwise be needed. |
| Back end; React; FastAPI (**recall**); validate; cache | 8 | The server part, screen part and stored-for-reuse copy are not named in everyday language; the title explains reuse but not the label “cache”. |
| Mocked response (notes) | 9 | A deliberately supplied test reply, not live data. |
| Dependencies; timeout; TTL; HTTP; null; in-process cache (**prompt**, p01–p02) | 10 | Which are agent implementation details, and which results the participant must judge. |
| Deterministic tests; non-finite (**prompt**, p03) | 11 | Repeatable supplied-input checks; a rate that is not a usable number. |
| Interface standard (notes) | 12 | MCP's purpose is explained well, but this additional description remains abstract. |
| CSV | 13 | A table saved as a text file; the visible example helps but does not name the format. |
| OAuth; Cloud project; client file; scopes (notes) | 14 | What permission is being granted, what the file is for, and what the learner must inspect before agreeing. |
| Configuration; token; local stdio; npm; loopback callback; pinned package (some in notes) | 15 | Settings, a secret access pass, and which installation details require facilitator help. |
| Node.js; XDG_CONFIG_HOME; auth command; environment; repository (**prompt**, p04) | 15 | The prompt assumes these can be recognized when the agent proposes changes. |
| Markdown (**prompt**, p06) | 16 | The summary is a plain-text document with simple formatting. |
| Revoke; OAuth grant; credential JSON (**prompt**, p07) | 18 | Disconnecting locally versus withdrawing Google's permission, with a recognizable place to do each. |

### s2 — Manageable with a facilitator

The business problem, two questions, permission table and action record build one coherent mental model, with most slides asking for one decision or one small comparison. Practice still needs a facilitator: approving the login prompt requires security vocabulary absent from the explanation, and the minimum outcome does not guarantee readiness for the next session.

Three hardest slides:
1. **17:** six timed stages hide the complexity of building and testing four linked features; the minimum is named but the next-session consequences are not.
2. **10:** the learner understands allowed/refused, but is not shown how to perform and recognize the direct-request test.
3. **7:** directory check, server session, repeated requests, 401 and sign-out all arrive together; the pass analogy and notes help, but this needs a slow walkthrough.

| Unexplained term(s) | First slide | What is missing for this audience |
| --- | --- | --- |
| Database; Wiki; FX (**recall**) | 2 | A stated prerequisite or brief reminder; FX is inherited from s1. |
| Back end; function; `check(name, password)` | 6 | Where the check runs and how to read the code-like label. “Mock” itself is explained as a fake practice directory. |
| GET; `/api/admin/users`; endpoint (notes); 200 | 10 | A read request to the users-list address and a successful reply; 403 is already labelled “Refused”. |
| Protected API call | 13 | An app request that requires a valid sign-in, not a separate external service. |
| React; FastAPI (**recall**, p01); cookie; cookie flags; HttpOnly; SameSite; Secure; HTTPS; expiry; CSRF; token; session ID; Python standard library (**prompt**, p01) | 14 | Plain reasons for the checks the participant is asked to approve; the session-pass concept alone does not explain them. |
| Salted hash; scrypt; PBKDF2; header; state-changing request; localhost (**prompt**, p02) | 17 | Password-storage and request-protection details should be identified as agent work, with participant-facing checks alongside. |
| Seed; unsigned request (**prompt**, p03) | 17 | Set up initial practice roles; a request without a signed-in session. |
| Front-end guard; direct API request (**prompt**, p04) | 17 | A screen-only check versus a request sent to the server without using that menu. |
| Recursive logging (**prompt**, p05) | 17 | Recording a log-reading action can trigger further log records; not a business-user concept taught here. |
| Synthetic fixture (**prompt**, p07) | 18 | Intentional made-up practice data, not a real credential leak. |

Authentication and authorization are **not** unexplained-term findings: slide 4 and its notes translate both. LDAP is tied to the company directory on slide 5, the mock directory is explained on slide 6, session/401 in the notes on slide 7, and audit trail on slide 12. Not expanding an acronym is not by itself a teaching failure.

### s3 — Hard

The pictures establish the desired result and several useful boundaries, but a novice must still approve server access, public/private file placement, a running service and a long set of publication checks. Sixty minutes is a target dependent on extensive facilitator preparation, complete earlier work and rehearsed prompts—not an established completion time for independent business users.

Three hardest slides:
1. **3:** account, service, private files, address, port and paths are six related assignments, without a filled-in deployment card to connect them.
2. **9:** local build, public files, private code/data, a consistent snapshot and excluded secret/session files must all be distinguished before approving transfer.
3. **11:** the service manager, logout, persistent operation and facilitator-prepared “lingering” add a new operating model with unfamiliar names.

| Unexplained term(s) | First slide | What is missing for this audience |
| --- | --- | --- |
| VPS; deployment/deploy; Docker; backend; LLM; OAuth; DB (**recall**, notes); LDAP (**recall**, notes) | 1 | A rented remote computer, making the app available there, and what prior knowledge is assumed. “No Docker” introduces an unnecessary new product name without explanation. |
| SSH; Linux; terminal; key agent | 2 | A private remote-control connection, where to open it, and which identity it uses. The two-login distinction itself is good. |
| Ubuntu; Debian; service; HTTPS; port; paths; loopback; proxy; sudo; host-key fingerprint (some in notes) | 3 | A plain map of the assigned server space, address, numbered connection and folders, and the changes reserved for the facilitator. |
| Frontend; FastAPI (**recall**); localhost; same-origin; CORS; API prefix; base path; TLS; Vite; streaming/timeouts (some in notes) | 4 | What the browser contacts, what forwards the request and why the laptop's address no longer works. |
| SQLite (**recall**); runtime configuration; model endpoint; token (notes) | 5 | Names for the database and model service already used, with a reminder of their role after the move. |
| Rotate passwords; hash; revoke sessions; Secure/HttpOnly/SameSite cookies; CSRF; rate limiting; VITE variables; EnvironmentFile; dotenv (some in notes) | 6 | What participants must change or prove before publishing; these are not explained by “No key” versus “LLM key”. |
| Release; persistent state; absolute runtime paths; 0700; 0600 (some in notes) | 7 | A code version versus data retained across versions; access numbers are implementation instructions without a participant translation. |
| Allowlist; lockfile; import target; artifact; 127.0.0.1 (**prompt**, p01); SFTP; quota; user manager; SPA; DNS; TCP (**prompt**, p02) | 8 | A guided example of checking the server identity and recognizing a ready/not-ready report; most terms belong in an agent appendix. |
| Build; snapshot; `.env`; WAL; quiesce; checksum (some in notes); symlink; integrity_check (**prompt**, p03) | 9 | Prepared website files, a complete point-in-time data copy and a worked inventory the participant can approve. |
| Python venv; dependencies (first in p01 at slide 8); packages; wheels; apt; pip (some in notes) | 8 (prompt), 10 (slide) | The notes explain the purpose of a venv, but never translate its name or the installation labels. |
| systemd --user; lingering; uvicorn; unit; WorkingDirectory; ExecStart; restart policy (some in notes) | 11 | The server's app supervisor, its settings and an example of healthy status. |
| Certificate; SPA deep link; proxy activation (notes); cookie Path (**prompt**, p05) | 12 | A browser-ready checklist and where each result can be seen without showing secrets. |
| Deterministic fixture; schema migration; rollback (notes or linked prompts) | 13 (fixture), 14 (migration/rollback) | Repeatable supplied test inputs, data-structure changes and returning to an earlier code version without replacing current data. |

### The day's story and practice handoffs

The three decks are recognizably one day: s1 adds outside data, s2 adds named people and permissions, and s3 moves that same app off the laptop. The repeated app features, Alya/Budi/Citra accounts and explicit separation of Drive access from app login prevent unnecessary restarts. The weak link is readiness: s1 allows Drive to be incomplete, which s3 handles explicitly, while s2 allows a smaller login/roles outcome that may still lack protections required to publish in s3.

The title generally states the learning point clearly, including the actual assertion titles now shown in s2; its historical short-title decision is not a finding. Most explanatory slides contain one central idea with two to four supporting parts. The burden rises at s1/14–15, s2/7 and s3/3, 9 and 11: low word counts do not make a cluster of new concepts easy. The practice slides are sensible summaries of an hour, but cannot substitute for a short learner action sheet showing prompt number, approval decision, expected evidence and when to ask for help.

## Findings

All rows below are teaching judgments grounded in the cited deck content, not claims that an app was tested. Findings are ordered by likely impact on completing the training day.

| ID | Sev | Deck | Slide | Problem | Evidence | How checked | Suggested fix |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | P1 | s2 | 17 | The minimum outcome is not visibly reconciled with the next session's publication requirements. A learner can follow the allowed shorter path and then be blocked in s3. | `.review/day4-shots/s2/s17.png`: “Must finish: Login and Roles”; p02 permits CSRF and the sign-in limit to be not done; p07 mentions s3 reliance. S3 p04 says a missing control must stop publication and must not be built during deployment. | Deck text, full s2 p02/p07 and s3 p04; screenshots s2/s17.png and s3/s11.png. | End s2 with a visible “ready for deployment / needs catch-up” checklist; reserve a catch-up slot or explicitly use a restricted preview path for incomplete builds. Keep every publication protection. |
| A2 | P1 | s3 | 3 | The starting assignments are too abstract to act on without help; the downloadable card is blank and no filled example connects its fields to the diagram. | `.review/day4-shots/s3/s03.png`: “Your service”, “Assigned HTTPS + port”, “Separate paths + port”. Embedded card has blank host, user, fingerprint, folders, port and service fields; p01 stops if assignments are missing. | Deck text and project file `decks/session-3-vps-deployment-visual.html` (card, help and p01–p02); screenshot. | Show one clearly fictional filled card annotated “facilitator supplies / participant checks”, and a visible instruction to collect the completed personal card before prompt 1. |
| A3 | P1 | s3 | 11 | The learner is expected to approve and recognize a healthy running service without seeing what that approval or healthy result looks like. | `.review/day4-shots/s3/s11.png` shows “systemd --user” and “Lingering prepared by facilitator”; notes and p04 add service settings, permissions, syntax/status/log checks. | Deck text, notes, full p04 and screenshot; teaching judgment, not a service test. | Pair the diagram with a short worked approval and sanitized healthy-status example; label what the learner checks and what only the facilitator fixes. Translate the service-manager names. |
| A4 | P1 | s3 | 15 | The seven-prompt workload has no beginner-sized route through an hour if checks or installs take longer; the visible timeline hides those dependencies. | `.review/day4-shots/s3/s15.png`: 10 minutes plan, 15 transfer, 15 start, 15 verify, 5 show. P01–p07 include multiple approvals, credential replacement, data checks, live model/API checks and a separate restore; notes admit extra time may be needed. | Deck text and all seven full prompts; screenshot; timing risk inferred from task scope, not measured. | Rehearse on participant-like devices, publish the prerequisite checklist before practice and allocate explicit support/overflow time. State a safe blocked outcome, and separate the full recovery rehearsal from the five-minute show slot without claiming it passed. |
| A5 | P1 | s2 | 14 | The planning/login prompts introduce a bundle of security requirements that the learner has not been taught to evaluate; “approve one stage” alone does not explain the approval decision. | `.review/day4-shots/s2/p01.png`: cookie flags, HttpOnly, SameSite, Secure, CSRF; p02 adds salted hashes, sign-in limits and request headers. Slides 4–13 explain identity/roles/session at a simpler level. | Deck text, s2 slide notes, complete p01–p02 and screenshots s2/s14.png, p01.png. | Add a plain-language approval card: what each protection prevents, what evidence to request, and when to call the facilitator. Keep the technical instructions for the agent; do not remove protections to simplify the exercise. |
| A6 | P1 | s2 | 10 | The core refusal check says what must happen but not how a beginner performs it or recognizes its evidence independently. | `.review/day4-shots/s2/s10.png`: `GET /api/admin/users` gives 200/403; slide 15 notes ask for the same request directly, and slide 18 makes 403 a finish condition. P06 delegates the scripted check but gives no worked participant view. | Deck text and complete p06, screenshots s2/s10.png, s15.png and s18.png. | Demonstrate one direct request through the agent, show sanitized 403 evidence and contrast it with merely hiding the menu. Give the participant an exact request-to-agent instruction plus expected result; no need to teach a new command tool. |
| A7 | P1 | s1 | 14 | The Drive handoff introduces permission and credential-file vocabulary but lacks a worked learner decision; “Review consent” is not enough to identify an unexpected permission request. | `.review/day4-shots/s1/s14.png`: OAuth, Cloud project, client file, broad access and consent; slide 15 groups install/configuration/sign-in checks. P04 supplies commands and settings; setup help admits the exact participant flow was not tested end to end. | Deck text, notes, full p04, embedded help, screenshots s1/s14.png and s15.png. | Walk through a rehearsed, redacted account/permission/file-location example. Explain OAuth as permission granted to the tool, name acceptable requested access, and give a stop-and-ask rule for any mismatch. |
| A8 | P1 | s1 | 6 | The first concrete request introduces code-like notation without translating how to read it. | `.review/day4-shots/s1/s06.png`: `GET /v2/rate/usd/idr`, `base`, `quote`; notes say inspect the endpoint but do not translate these labels. Slide 7 explains the arithmetic, not the request notation. | Deck text, notes and screenshots s1/s06.png–s07.png. | Add “ask for the value of one USD in IDR”; label GET as a read request and base/quote as from/to currencies. |
| A9 | P1 | s3 | 13 | The slide's visual supports only the permissions portion of a much broader finish check, so the learner cannot use it to remember what proves the complete app survived the move. | `.review/day4-shots/s3/s13.png`: title promises login, permissions, API calls and Wiki answers; picture shows only Budi's refused request and Alya's audit access. Full p06 has eight groups covering data, FX, live model, restart and another device. | Deck text, notes, full p06 and screenshot. | Add a small participant evidence sheet with separate login/roles, saved data, FX, Wiki/model and after-logout checks, linked to the detailed agent checklist. Show one expected result for each; distinguish not-run from pass. |
| A10 | P3 | s1 | 7 | The quick check reveals the answer before the room votes; it checks recognition more than understanding. | `.review/day4-shots/s1/s07.png` visibly says “Divide” and shows the division above “Multiply / Divide / Relabel”. S2 slide 9 similarly states that hiding the menu does not stop a User before asking its quiz. | Deck text and screenshots s1/s07.png and s2/s09.png; no reveal steps hide these answers. | Keep the explanatory titles, but ask a different transfer question, such as calculating a new amount or identifying the evidence that proves a request was refused. |

## What works well

- **s1, slides 3–7:** the business request becomes a specific rate response and simple arithmetic; the before/after screen gives the technical connection a visible purpose.
- **s1, slides 12 and 16:** separate app/agent lanes prevent the mistaken expectation of a Drive button in the app; read → preview → approve → save gives a memorable user responsibility.
- **s2, slides 3, 8 and 12:** the named people, permission table and action-record example answer the opening watchlist question without asking participants to read source code.
- **s2, slides 15–18:** two accounts and concrete finish cards demand evidence, not the agent saying “done”; the practice slide also names a smaller minimum outcome.
- **s3, slides 2, 7 and 16:** separate server/app logins, data retained across updates and access after SSH closes make three important deployment boundaries visible.
