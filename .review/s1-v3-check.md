# S1 v3 deck — verification report

Deck: `decks/day3-s1-v3.html` (branch `s1-v3`). Date: 2026-11-12.

## Automated checks
- Lint (`check_deck.py` with outline, copy, prompts): **0 errors** — titles match the outline, notes on every slide, no banned phrases, only the five workflow names, tested prompts verbatim, timing 180 min (run 91).
- Render (`render.mjs`, Edge, 1920×1080 and 1280×720): all 33 slides, every step — **0 failures** for bounds, ≥28 px type, word budget, a visible change on each step, ← restoring the previous step. Same with `--reduced-motion`. Slides 17 and 26–31 re-rendered after the final fixes: 0 failures.
- Notes re-injected from the copy doc; the deck matches.

## Per slide (title, type, minutes, words)
| # | Title | Type | Min | Words · budget · exception |
|---|---|---|---|---|
| 1 | Build your first AI Financial App | title | 2 | 11 · budget: 40 · exception: none |
| 2 | Today you direct opencode to build a NISP dashboard and chatbot, without writing code | visual | 5 | 16 · budget: 40 · exception: none |
| 3 | Your job today: interview, approve the plan, then test what the agent builds | visual | 3 | 18 · budget: 40 · exception: none |
| 4 | An LLM writes its answer one small piece of text at a time | visual | 3 | 25 · budget: 40 · exception: none |
| 5 | The model doesn't remember earlier requests; opencode sends the context it needs | visual | 3 | 34 · budget: 40 · exception: none |
| 6 | On every turn, opencode sends the model a stack: rules, skills, the chat so far, your message | visual | 4 | 39 · budget: 40 · exception: none |
| 7 | The context window has a limit, so old chat gets summarised; save decisions in files | visual | 3 | 35 · budget: 40 · exception: none |
| 8 | The model asks for a tool; opencode checks permission and runs it | visual | 4 | 39 · budget: 40 · exception: none |
| 9 | A coding agent repeats model decisions and tool actions, then you check the result | visual | 3 | 24 · budget: 40 · exception: none |
| 10 | AGENTS.md is the project's standing brief, so keep it current | visual | 4 | 36 · budget: 40 · exception: none |
| 11 | Check: a new conversation ignored your preference. What do you do? | check | 3 | 52 · budget: 60 · exception: none |
| 12 | Use a quick model for small edits and a stronger one for planning and debugging | visual | 3 | 28 · budget: 40 · exception: none |
| 13 | On supported models, higher effort lets the model reason more before answering | visual | 2 | 30 · budget: 40 · exception: none |
| 14 | Everyone works on a local copy and shares through GitHub | visual | 3 | 21 · budget: 40 · exception: none |
| 15 | A commit is a save point on your laptop; push copies it to GitHub, pull brings changes back | visual | 4 | 39 · budget: 40 · exception: none |
| 16 | Run 1a: sign up to GitHub and draft AGENTS.md with /init | run | 12 | 24 · budget: 60 · exception: none |
| 17 | Run 1b: add your rule, check it, then push to a private repository | run | 14 | 33 · budget: 60 · exception: none |
| 18 | Choose how to instruct the agent by the job: this task, project rules, expertise or a sequence | visual | 3 | 20 · budget: 40 · exception: none |
| 19 | The agent sees each skill's name and description, and loads the full skill when it decides one fits | visual | 4 | 38 · budget: 40 · exception: none |
| 20 | A brainstorming skill makes "ask questions first" a repeatable habit | visual | 4 | 32 · budget: 40 · exception: none |
| 21 | An agent builds what it guesses you want, so interview first | visual | 3 | 23 · budget: 40 · exception: none |
| 22 | The interview produces a spec (what and why); the plan says how, and you approve, edit or reject it | visual | 4 | 31 · budget: 40 · exception: none |
| 23 | Check: approve, edit or reject these three plans | check | 4 | 55 · budget: 60 · exception: none |
| 24 | Run 2a: interview for the dashboard and save the spec | run | 12 | 36 · budget: 60 · exception: none |
| 25 | Run 2b: get the plan, approve, edit or reject it, then save it | run | 12 | 44 · budget: 60 · exception: none |
| 26 | Your financial app has a screen, a back end, a data source and an AI service | visual | 4 | 29 · budget: 40 · exception: none |
| 27 | When something breaks, remove secrets, paste the error, and ask the agent to explain it | visual | 4 | 27 · budget: 40 · exception: none |
| 28 | Run 3a: build the dashboard and check its numbers | run | 15 | 38 · budget: 60 · exception: none |
| 29 | Run 3b: protect the key, then interview and plan the chatbot | run | 12 | 33 · budget: 60 · exception: none |
| 30 | Run 3c: build and test the chatbot, then push without secrets | run | 14 | 45 · budget: 60 · exception: none |
| 31 | You built a financial app by directing an AI and checking its work | recap | 4 | 32 · budget: 40 · exception: none |
| 32 | Questions | Q&A | 5 | 1 · budget: 40 · exception: none |
| 33 | Next session: your app stores price history and the chatbot reads reference pages | talk | 1 | 14 · budget: 40 · exception: none |

## Independent review
One final reviewer (gpt-6.1-sol, high), all 5 lenses in one pass (owner chose fast finish instead of 5 reviewers).
- First verdict: **3 P0**, all fixed:
  1. Slide 30 push prompt listed, committed and pushed in one go, so the participant could not stop it → split into "list files, don't commit" then "commit and push", with a read-and-stop line in between.
  2. Slide 26 placed yfinance outside the laptop → external box is now "Yahoo Finance: NISP data"; the back end shows "FastAPI · yfinance · 8000".
  3. Slide 30 "memory" test (which stock?) passes without memory → "Say 'My name is Rina', then ask 'What is my name?'".
- P1 fixed: slide 17 Prompt 2 now labelled UNTESTED.
- All 20 v2 P0 findings (M1–M16, H1–H4) marked fixed, H3 after fix 1 above.
- Not re-reviewed after the fixes (fast finish); checked by lint and render only.

## Open (not fixed, for the owner)
- P1: slide 29 — copying `.env.example` to `.env` is hard for non-coders (hidden files, `.env.txt`); needs a short Windows/Mac setup card.
- P1: slide 29 — "Interview" is highlighted but the visible steps paste a supplied spec; the interview is only in the notes.
- P2: slide 7 — the stack bars have no labels; slide 31 — arrival shows an empty panel before the recap.
- From spec §9: `[FAST MODEL]` / `[SMART MODEL]` placeholders; UNTESTED prompts on slides 17, 28, 29, 30 (now including the two new push prompts) need a Windows + Mac rehearsal with real GitHub sign-in; handout, recovery card and checkpoint links don't exist yet.
