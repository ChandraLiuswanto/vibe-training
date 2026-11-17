# Project log — AI Vibe Coding for Business Users (Day 3–5)

Running record of what we're building, what's been decided, and what's still open.
Newest entries go at the top of **Log**.

## Course at a glance

- **Audience:** business users with no programming background.
- **Concept:** use case first, technology later. Participants direct an AI coding agent to build, extend, automate and deploy one app.
- **Language:** Bahasa Indonesia (source curriculum).
- **Thread through all days:** one Financial App (BBCA as the running example), grown session by session.
- **End goal:** participants can build, extend and run a business app with an AI coding agent more independently.

| Day | Session | Topic | Output |
|-----|---------|-------|--------|
| 3 | 1 | Build Your First AI Financial App — coding agent & tools, model selection, Git basics, skills & workflows; workflow Interview → Plan (Approve/Edit/Reject) → Execute → Test/Debug → Iterate | Dashboard + basic chatbot |
| 3 | 2 | Watchlist & AI Knowledge — database basics, yfinance → DB, watchlist dashboard; Wiki from OJK PDFs, system prompt, before/after chatbot test | App with watchlist, DB, price history, Wiki-aware chatbot |
| 3 | 3 | AI-Powered Reports & Presentations — agentic workflows, prompt vs skill vs multi-step workflow; stock report → PowerPoint; iterate; save reusable workflow | Report + PPT + reusable workflow |
| 4 | 1 | API, FastAPI & MCP — consume vs expose, endpoints, Swagger `/docs`, MCP | App consuming external APIs + FastAPI backend |
| 4 | 2 | Web scraping for BI — BBCA news, headline/date/source/summary, feed chatbot | News & market intelligence feature |
| 4 | 3 | Login & access control — authn vs authz, mock LDAP, RBAC (Admin/User) | Login + RBAC on app and API |
| 5 | 1 | Admin panel & audit trail | User management + audit log |
| 5 | 2 | Docker & VPS deployment — Dockerfile, Compose, env vars, API key | App + API live on VPS |
| 5 | 3 | Monitor, maintain, improve — health checks, logs, redeploy | Maintainable live app |
| 5 | Final | AI-powered product showcase — HyperFrames demo video, live demo | Live app + stakeholder demo |

## Current scope

**Day 3 only** (Sessions 1–3). Days 4–5 come later but must build on the same app.

## Decisions

- 2026-11-11 — Scope is Day 3 first. *(user)*
- Every session is an **interactive session**: participants work hands-on, not lecture-only. *(user)*
- 2026-11-11 — Each session is **3 hours**, interactive, with Q&A and hands-on practice. *(user)*
- 2026-11-11 — Decks are **HTML** (single self-contained file, per `AGENTS.md`: `presentation-creator` for story, `frontend-slides` for build). *(user)*
- 2026-11-11 — Deck language is **English**. *(user)*
- 2026-11-11 — Coding agent harness is **opencode**. *(user)*
- 2026-11-11 — Participant setup (opencode + model access) is **already done** before Day 3. S1 "instalasi tools" becomes a quick check, not an install. *(user)*
- 2026-11-11 — Approach **B**: HTML decks + tested reference Financial App with per-block checkpoints + handouts. *(user)*
- 2026-11-11 — In-app chatbot uses the already-provided OpenAI-compatible API. *(user)*
- 2026-11-11 — GitHub is the remote; participants create accounts in S1. *(user)*
- 2026-11-11 — Mixed OS, Python preinstalled. *(user)*
- 2026-11-11 — Wiki sources: participants search via opencode; checkpoint ships a vetted copy. *(user + my call)*
- 2026-11-11 — Frontend is **React**, not Streamlit. *(user)*
- 2026-11-11 — S1 adds an **LLM basics** block: stateless model, context length, AGENTS.md, message roles (system/user/assistant/tool) and tool calling. *(user)* Merged with the "what is a coding agent" block; 35 min, taken from skills (−5), build (−5), test (−5), Q&A (−5) and the old first-message block. *(my call)*
- 2026-11-11 — Backend is **FastAPI from Day 3** (yfinance, SQLite, LLM key). Day 4 S1 shifts from "introduce FastAPI" to "understand and expose your back end". *(user)*
- 2026-11-11 — Node.js preinstalled. *(user)*
- 2026-11-11 — Build method taught in the decks is **Brainstorm → Spec → Plan → Execute → Test → Iterate** (replaces Interview → Plan). S1 teaches it in full; S2/S3 reuse it per feature; S3 saves it as a workflow. *(user)* New checkpoint `s1-spec`. S1 timings: Git 35, skills 5, build loop 50. *(call)*
- 2026-11-11 — ~~Participant skill kit~~ dropped: participants use **whatever skills they already have**. Prompts are tested with no extra skills. S1 still focuses on skills. *(user)*
- 2026-11-11 — Build is done with **subagents plus a reviewer**. *(user)*
- 2026-11-11 — S1 skills block is a 20-min focus block (6 slides). Models 10, Git 30, build loop 45. S1 = 55 slides. *(user approved)*
- 2026-11-11 — Build plan approved (phases: plan → reference app → story/copy → style → decks → handouts → final check), subagents + cross-family reviewer. *(user)*
- Deck rules from `AGENTS.md` apply to any slides (story gate, assertion titles, word budgets). *(project)*

## Existing assets

- `demos/git-basics.html` — finished English deck "Git basics for non-developers" (local vs remote, commit, push, pull, checks). Covers part of D3S1.
- No Financial App reference build, OJK Wiki source, or exercise material yet.

## Open questions

1. ~~Deliverable~~ → approach B: HTML decks + tested reference app with checkpoints + handouts.
2. ~~Interactive format~~ → 3h, Q&A + hands-on. Still open: how a hands-on block runs (follow-along vs demo-then-repeat).
3. ~~Coding agent~~ → opencode, pre-set-up. Still open: which models appear in their picker (for the fast-vs-smart segment).
4. ~~Deck language~~ → English (existing Git deck reusable as-is).
5. ~~Session length~~ → 3 hours each.
6. ~~Chatbot LLM~~ → already-provided OpenAI-compatible API.
7. ~~Git remote~~ → GitHub, accounts created in S1.
8. ~~OS/Python~~ → mixed OS, Python installed.
9. ~~Wiki source~~ → participants find it via opencode web search.
10. Model names in participants' opencode picker (for fast-vs-smart segment) — placeholder until known.
11. ~~Backend~~ → FastAPI from Day 3.
12. ~~Node.js~~ → installed.
13. Where the checkpoint repo is hosted (client GitHub org / public repo / zips).
14. Test access: an API key + model matching participants', so prompts can be tested here.

## Log

- **2026-11-11** — Received full Day 3–5 curriculum. Confirmed my read of Day 3 and the repo state. User set scope to Day 3 and made every session interactive. Created this log.
- **2026-11-11** — User: each session 3h interactive with Q&A and hands-on; decks are HTML.
- **2026-11-11** — User: decks in English; harness is opencode. Checked: opencode binary not on PATH here (only ~/.config/opencode exists), so hands-on steps can't be verified locally yet.
- **2026-11-11** — User: setup already done for participants. Noted opencode config here has HyperFrames skills installed (relevant to Day 5 final activity).
- **2026-11-11** — User picked approach B. Wrote draft design: `docs/superpowers/specs/2026-11-11-day3-design.md`. Checked: yfinance not installed here; Python 3.14 available.
- **2026-11-11** — User answered chatbot API, GitHub, OS, Wiki-source questions. Design doc updated; awaiting approval.
- **2026-11-11** — User asked for the slide list. Wrote headline-only outline: `docs/outlines/day3-outline.md` (S1 38, S2 31, S3 27 slides). Awaiting story-gate approval.
- **2026-11-11** — User: React instead of Streamlit; add LLM basics to S1. Outline S1 now 47 slides; S2 slide 20 becomes a recap of the system message. Design timings rebalanced (still 180 min).
- **2026-11-11** — User: FastAPI back end from Day 3; Node installed.
- **2026-11-11** — User asked for a proper spec. Rewrote `docs/superpowers/specs/2026-11-11-day3-design.md` as a full spec: objectives per session, deliverables D1–D5, block timings with checkpoints, app stack/layout/data model, per-checkpoint acceptance checks, recovery flow, build & verification method, risks, open items. Builder check done by self-read (no subagent tool).
- **2026-11-11** — User clarified: the deck should teach a proper brainstorm → spec → plan workflow. Outline updated (S1 51, S2 33, S3 29 slides); spec updated.
- **2026-11-11** — User: skill-focused S1 OK; asked for my build plan and skills; wants subagents with a reviewer.
- **2026-11-11** — User: skip the participant skill kit; participants use what they have. Build plan Phase 2 removed.
- **2026-11-11** — User approved the 20-min S1 skills block and the build plan. Outline S1 = 55 slides (S1 timings sum to 180). Wrote `docs/superpowers/plans/2026-11-11-day3-build.md` (Tasks 0–10). Blocked at Task 0 on test API key.
- **2026-11-11** — User: test with 9router **sol**. Task 0 done: opencode **1.19.5** (npm `opencode-ai`) installed; clean config at `/var/tmp/oc-home` (HOME override, no extra skills — participant baseline), provider `ninerouter` → `http://fedora:20128/v1`, model `ninerouter/sol` (`gpt-6.1-sol`). `opencode run` works. Node v25.9, Python 3.14; yfinance BBCA.JK 1y = 240 rows (last close 5325 on 2026-11-11). `financial-app/` gitignored in vibe-training.

- **2026-11-11** — Task 1 built (sonnet): 3/3 clean runs pass; `financial-app/` tags `s1-start` fb72a71, `s1-spec` 9826942; prompts in `prompts/s1.md`. Findings: spec prompt needs "Don't build anything yet" (v1 built the whole app); saving the plan needs a Plan→Build switch. Review by sol in progress (ctx_1aefc21f66bb).
- **2026-11-11** — Review 1 (sol) FAILED Task 1: `/init` auto-rejected (external dir) in CLI so AGENTS.md came from the rule prompt; an undisclosed plan retry; missing approve/edit/reject checkpoint; word-count nits. Sent back to the builder (ctx_d4b125eacd67).
- **2026-11-11** — User: start the S1 deck now; Task 2 (dashboard/chatbot prompts) later, so those slides carry UNTESTED prompts. Task 6 S1 copy dispatched (sonnet, ctx_3289b7bd8e62).
- **2026-11-11** — Deck style: **B — Swiss Modern** (white/black/red #ff3300, Archivo + Nunito + JetBrains Mono, visible grid). Preview: `.frontend-slides/slide-previews/style-b.html`. *(user)*
- **2026-11-11** — Review (sol) FAILED S1 copy: slide 34 over budget once diagram labels counted; slide 36 demo prompt untested + overclaims; slide 49 skips loop steps; slides 5/14 notes conflate apps with models; slide 28 template exception. Sent back (ctx_58d44f8214b8). Slides 18/45 wait for Task 1 fixes.
- **2026-11-11** — S1 copy re-review: findings 2–6 resolved; slide 34 recount corrected by coordinator to 30/40 (13 text + 17 labels). Copy passes, pending slides 18/45 from Task 1 fixes.
- **2026-11-11** — Task 1 fixes (builder): /init rejection caused by the agent reading a mistyped path outside the project (external-directory permission; CLI auto-rejects). 3 fresh runs pass (--auto on /init only); TUI shows Allow once/Allow always/Reject → tell participants Allow once. Edit prompt + approve/edit/reject added. financial-app re-tagged s1-start f91d452, s1-spec 0038445. Re-review sent to sol.
- **2026-11-11** — S1 copy: slides 18/45 updated to the fixed prompts (Allow once; approve/edit/reject before save). Task 8 S1 deck build dispatched (sonnet), Swiss Modern.
- **2026-11-11** — Task 1 re-review (sol) **PASS**. Coordinator fixed 3 wording nits in prompts/s1.md (first question, plan identical, >40 words) and noted the TUI dialog is builder-reported. Facilitator guide: 'no movement for 2 min → Esc, resend' (3/20 stalls).
- **2026-11-11** — S1 deck: user stopped the single sonnet builder (~45 min, no file yet) and asked to parallelize with **opus low**. Coordinator built the shared shell (.scratch/deck-s1/shell: theme.css, runtime.js, assemble.py with notes injected from slides.json), verify.mjs (titles, overflow, tiny text, prompt text, copy buttons, reveals, screenshots) and 4 exemplar slides (1, 7, 19, 41; all PASS). 4 opus-low workers write fragments 2–14, 15–28, 29–42, 43–55.
- **2026-11-11** — S1 deck assembled from 4 parallel opus-low parts: 55 slides, 106 KB, `verify.mjs 1 55` PASS at 1920 and 1280. Coordinator squared off rounded corners (24/26/39). Sol review dispatched.
- **2026-11-11** — S1 deck review 1 (sol) FAILED: static timers, labels <28px, slide 51 dots, no hashchange. Coordinator fixed all four; re-review **PASS**. `decks/day3-s1.html` done (55 slides). Open: 10 UNTESTED prompts (Task 2 later), placeholders [FAST MODEL]/[SMART MODEL] (22), [SKILL NAME] (36), [TIME] (31).
- **2026-11-12** — User feedback on S1 deck (viewed on phone): too many slides, too many runs, wants more visuals/animation, no break, max 3 participant runs. Approved **outline v2** (`docs/outlines/day3-s1-v2.md`): 28 headlines / ~31 slides; 3 coherent runs (Set up → Decide what to build → Build it); concept slides become click-to-build animated diagrams; presenter demos cut to optional notes. Timing: 10/30/15/25/15/35/40/10 = 180. v1 deck kept as `decks/day3-s1-v1.html`.
- **2026-11-12** — S1 copy v2 (31 slides) review (sol) FAILED on 5 diagram/count details; coordinator fixed them (7 App→Model step, 16/17 placeholder marks, not invented text, 24a s1-dashboard as Run 3 midpoint, 24b single handout label; counts recomputed). v2 shell built: click-to-build steps ([data-step]), self-drawing SVG arrows, travelling dot, step indicator; exemplars 4, 8, 21a PASS.
- **2026-11-12** — User: animations should loop. Added looping effects to the v2 theme (flow dashes, travelling packets, endless loop dot, pulse, float, caret, spin, seq highlight; active slide only; reduced-motion off). Applied to exemplars 4 and 8; the 3 part-builders were told.
- **2026-11-12** — S1 v2 deck assembled (31 slides, 124 KB) from 3 parallel opus-low parts; `verify.mjs` PASS all 31 at every build step, both sizes. Builder terminals closed. Sol review dispatched.
- **2026-11-12** — S1 v2 deck review (sol) FAILED on 7 points (timer on entry, ← after reveal, too many loops on 13/4/23, box-shadow pulse, missing 'Agent's context' on 16, yellow note on 9, 'Time' label). Coordinator fixed all; verify PASS all 31; re-review sent. Repo pushed public: github.com/ChandraLiuswanto/vibe-training (.pi/ excluded).
- **2026-11-12** — S1 v2 deck re-review (sol) **PASS**. Taildropped to Oppo. All worker terminals closed.
- **2026-11-12** — User edits to S1 v2: slide 5 context window redrawn (fixed frame, blocks arrive in order, oldest incl. rules fall out); slide 6 rows made overflow-proof; new slide 11b "Effort sets how long the model thinks" (variants, Ctrl+T, verified in opencode 1.19.5 binary keybind variant_cycle=ctrl+t); slide 16 (deck 18) skills diagram clarified (request → matching row → card on shelf → loads into context, one card); slide 19 (deck 21) left→right order, square return arrow Iterate→Plan; slide 20 (deck 22) 'Spec = PRD'; slide 27 (deck 31) timer replaced by drifting shapes. 32 slides, 180 min, verify PASS all 32.
- **2026-11-12** — User: switch the course example stock from BBCA to **NISP (Bank OCBC NISP, NISP.JK)** everywhere. yfinance NISP.JK 1y = 240 rows, last close 1,155 (2026-11-12). Replaced in spec, plan, outlines, copy v2, prompts/s1.md, v2 deck fragments, style previews; v1 deck and earlier log entries left as history. Deck v2 verify PASS all 32. Prompt re-test with NISP dispatched (sonnet); financial-app to be rebuilt from the NISP runs.
- **2026-11-12** — User: focus on decks. Approved **S2 v2** (`docs/outlines/day3-s2-v2.md`, 21 headlines / 24 slides) and **S3 v2** (`day3-s3-v2.md`, 20 / 22) in the S1 v2 style: 3 runs, no break, animated + looping, NISP. Copy for both dispatched in parallel (opus low). NISP prompt re-test (sonnet) continues in background.
- **2026-11-12** — NISP re-test (sonnet): 3/3 runs pass all checks. Brainstorm prompt changed to name 'NISP (Bank OCBC NISP, NISP.JK)' (bare 'NISP' made 2/3 agents spend a question asking which company); 46 words. One stall + resend on run 3 spec (known). financial-app rebuilt: s1-start 65bfb70, s1-spec d58bce6. Copy + deck slide 21a updated to the new prompt; verify PASS.
- **2026-11-12** — S3 copy v2 written (22 slides, 180 min). Verified in opencode 1.19.5: custom commands live in `.opencode/commands/<name>.md`; `$ARGUMENTS` gets the args (`opencode run --command echo-arg TLKM.JK` → ARG=TLKM.JK). Review dispatched.
- **2026-11-12** — S2 copy v2 written (24 slides, 180 min). Web search checked in opencode 1.19.5 (clean config, 9router sol): default has no websearch tool, but the agent used **webfetch** and returned a valid ojk.go.id page (HTTP 200). With env `OPENCODE_ENABLE_EXA=1` a **websearch** tool appears and worked without a key. → Facilitator setup: set OPENCODE_ENABLE_EXA=1, or rely on webfetch. S2 copy review dispatched.
- **2026-11-12** — S3 copy v2 review: 4 findings + 1 recount fixed by coordinator (reveal counted on checks, slide 6 quiz exception; command path + $ARGUMENTS in build prompt; blank sample grids; rehearsal note instead of unverified quit/reopen; spec prompt 50 words). S3 deck build: 3 opus-low parts dispatched.
- **2026-11-12** — S2 copy v2 review (sol) FAILED on 7 points; fixed by opus (webfetch-or-search prompt, mandatory Wiki brainstorm, reveal-inclusive counts, history on add + fixed API, URL citation + facts/risks rule, 'Illustrative' before/after). Coordinator trimmed the 10a spec prompt 53→47 words. S2 deck build: 3 opus-low parts dispatched.
- **2026-11-12** — S3 deck assembled: `decks/day3-s3.html`, 22 slides, 95 KB, verify PASS all 22. Sol review dispatched.
- **2026-11-12** — S2 deck assembled (`decks/day3-s2.html`, 24 slides, verify PASS all 24); sol review dispatched. S3 deck review FAILED (5 duplicate figure, 15 cards don't fold into chip, too much motion on 4/9/18, 11 line overflow); fixes dispatched (opus low).
- **2026-11-12** — S2 deck review (sol) FAILED: motion budget on 2/4/9/14/15/19, text glow on 5/7, builds not staged on 2/14/15, green ticks + packet overflow on 15. Q&A drifting shapes kept (user request). Fixes dispatched (opus low).
- **2026-11-12** — S3 deck re-review **PASS** (slide 15 real fold via .fold + .st1 hook; motion budget enforced deck-wide).
- **2026-11-12** — S2 deck re-review: all findings resolved except pulsing run tags (text); coordinator removed the pulse from run tags in all three decks (S2 8a/8b/10a/10b/16a/16b, S3 8a/8b/13a, S1 14a/14b). verify PASS: S1 32, S2 24, S3 22. **All three Day 3 decks done**; user asked to stop here.
- **2026-11-12** — S1 v2 deck reviewed by 5 read-only reviewers (accuracy, storyline, hands-on, visuals, redesign). Synthesis: `.review/day3-s1-v2-review-report.md` (P0s: wrong agent model on slides 4–10, unsafe run habits — Allow it, unredacted errors, public push — workflow shown too late). Spec `docs/superpowers/specs/2026-11-12-day3-s1-v3-deck-design.md` approved (repair + targeted reorder) and plan `docs/superpowers/plans/2026-11-12-day3-s1-v3-deck.md` written.
- **2026-11-12** — S1 v3 deck built on branch `s1-v3`: `decks/day3-s1-v3.html`, 33 slides, 180 min, 91 run minutes. Slides 6/7/8/10 redesigned, five workflow names (Interview → Plan → Execute → Test / Debug → Iterate), safe permission/secret/push steps, notes injected from `docs/copy/day3-s1-v3.md`. Check tools `tools/deck-check/` (lint + Edge renderer). Subagents gpt-6.1-sol, fallback chandra/sol after upstream DNS errors. Open: [FAST MODEL]/[SMART MODEL]; UNTESTED prompts on slides 17, 28, 29, 30 need a Windows + Mac rehearsal with real GitHub sign-in; handout, recovery card and checkpoint links don't exist yet.
- **2026-11-12** — Merged main (S2 deck, S3 deck, S1 NISP re-test, v2 slides 3/4) into s1-v3, keeping both sides. Ported into v3: brainstorm prompt naming 'NISP (Bank OCBC NISP, NISP.JK)' (slide 24), the Indonesia prediction example (slide 4), and the Tokyo stateless example (slide 5; v3 caption kept, words 42 with exception). Lint allows the verb 'live there'. Lint 0, render 244 PNGs 0 failing.
- **2026-11-12** — S2 deck (`decks/day3-s2.html`) reviewed by three independent gpt-6.1-sol reviewers (material, storyline, visual). Synthesis: `docs/reviews/2026-11-12-day3-s2-review.md` — 6 P0, 10 P1, 10 P2, 2 P3.
- **2026-11-12** — S2 v3 deck built on branch `s2-v3`: `decks/day3-s2-v3.html`, 27 slides, 180 min, 110 run minutes. Outline `docs/outlines/day3-s2-v3.md`, copy `docs/copy/day3-s2-v3.md`, `prompts/s2.md` (22 prompts, all UNTESTED). deck-check gained an s2 profile, a placeholder lint and a focus/Space render check. Day 3 design doc updated (step names, recovery sentence, `s2-watchlist` row). Slide 20 source: OJK "Tasks and Functions" page (spec fallback; idx.co.id returned 403); re-open and re-check the quoted OJK sentence before class. Delivery blockers: rehearse every UNTESTED prompt end to end on Windows and Mac, including webfetch/websearch and GitHub sign-in (P0-6); host checkpoints `s1-chatbot`, `s2-database`, `s2-watchlist`, `s2-wiki` with saved NISP/BBRI/TLKM prices; write the recovery card and the verified OJK/IDX URL list for the handout. Follow-ups: align the S3 deck to the new step names and drop the TLKM-history assumption; embed fonts for offline laptops (P3-2, all three decks; test with network off); S1 v3 deck has the same focus/Space bug (P2-9).
- **2026-11-12** — S2 v3 verified (3 gpt-6.1-sol reviews + Opus final review, fixes applied) and merged into `s1-v3`. Deck renamed `decks/day3-s2-v3.html` → `decks/day3-s2.html`; v2 kept only as test fixture `tools/deck-check/fixtures/day3-s2-v2.html`. Report: `.review/s2-v3-check.md`. Delivery blockers unchanged (rehearse prompts, checkpoints, fallback data, OJK/IDX URL list).
