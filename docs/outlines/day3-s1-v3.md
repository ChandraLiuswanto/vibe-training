# Day 3 · Session 1 — outline v3 (repair + targeted reorder)

Source: spec `docs/superpowers/specs/2026-11-12-day3-s1-v3-deck-design.md` §5 (approved by the owner 2026-11-12). Headlines are copied verbatim from §5.
Input deck: `decks/day3-s1-v2.html` (32 slides). Output deck: `decks/day3-s1-v3.html` (33 slides, `data-n` 1…33).
Finding IDs (M*, H*, S*, R*, A*) refer to `.review/day3-s1-v2-review-report.md`. "v2 N" is the v2 deck position "N / 32".

## Slide sequence and timing

| # | Headline (assertion title) | From | Change | Min |
|---|---|---|---|---|
| **Opening** | | | | **10** |
| 1 | Build your first AI Financial App | v2 1 | none | 2 |
| 2 | Today you direct opencode to build a NISP dashboard and chatbot, without writing code | v2 2 | title names opencode; notes say "latest available price" | 5 |
| 3 | Your job today: interview, approve the plan, then test what the agent builds | v2 21 | **moved**; 5 workflow steps (§6.5); brackets "Run 2" / "Run 3" | 3 |
| **How a coding agent works** | | | | **27** |
| 4 | An LLM writes its answer one small piece of text at a time | v2 3 | label the bars "Illustration"; fix notes (M13) | 3 |
| 5 | The model doesn't remember earlier requests; opencode sends the context it needs | v2 4 | title, caption and notes rescoped (M4); Turn-1 arrow fixed (A1) | 3 |
| 6 | On every turn, opencode sends the model a stack: rules, skills, the chat so far, your message | v2 5 | **redesign** §6.1 | 4 |
| 7 | The context window has a limit, so old chat gets summarised; save decisions in files | v2 6 | **replaces** the roles slide; §6.2 | 3 |
| 8 | The model asks for a tool; opencode checks permission and runs it | v2 7 | **redesign** §6.3 | 4 |
| 9 | A coding agent repeats model decisions and tool actions, then you check the result | v2 8 | title, exit boxes and punch line (M6) | 3 |
| 10 | AGENTS.md is the project's standing brief, so keep it current | v2 9 | **redesign** §6.4 | 4 |
| 11 | Check: a new conversation ignored your preference. What do you do? | v2 10 | new choices (§6.4) | 3 |
| **Models and Git** | | | | **12** |
| 12 | Use a quick model for small edits and a stronger one for planning and debugging | v2 11 | title softened; placeholders stay *(user)*; car/truck loops run once (A5) | 3 |
| 13 | On supported models, higher effort lets the model reason more before answering | v2 12 | title, caption, one-click dial, reduced-motion fix (M11, A3, A4) | 2 |
| 14 | Everyone works on a local copy and shares through GitHub | v2 13 | punch line "Saving alone doesn't upload your work" | 3 |
| 15 | A commit is a save point on your laptop; push copies it to GitHub, pull brings changes back | v2 14 | three states saved → committed → pushed; `.env` shown as left out (M12) | 4 |
| **Run 1** | | | | **26** |
| 16 | Run 1a: sign up to GitHub and draft AGENTS.md with /init | v2 15 | title (R1); permission line (H1); setup line (R2) | 12 |
| 17 | Run 1b: add your rule, check it, then push to a private repository | v2 16 | title (R1); check step (R3); "private" in Prompt 2 (H2) | 14 |
| **Skills** | | | | **11** |
| 18 | Choose how to instruct the agent by the job: this task, project rules, expertise or a sequence | v2 17 | equal cards instead of stairs (S9) | 3 |
| 19 | The agent sees each skill's name and description, and loads the full skill when it decides one fits | v2 18 | wording (M10); card stays inside the box, real text (A2) | 4 |
| 20 | A brainstorming skill makes "ask questions first" a repeatable habit | v2 19 | "Illustration" label; panels show short real text (M9) | 4 |
| **Run 2 — Interview and plan** | | | | **35** |
| 21 | An agent builds what it guesses you want, so interview first | v2 20 | "make it ask first" → "interview first" | 3 |
| 22 | The interview produces a spec (what and why); the plan says how, and you approve, edit or reject it | v2 22 | keep "Spec = PRD" *(user, from v2 edit)* | 4 |
| 23 | Check: approve, edit or reject these three plans | v2 25 | **moved before Run 2b** (S3); subtler plans (S6) | 4 |
| 24 | Run 2a: interview for the dashboard and save the spec | v2 23 | title (R1); "Up to five questions" (R7); tech line boxed as course-supplied (S5) | 12 |
| 25 | Run 2b: get the plan, approve, edit or reject it, then save it | v2 24 | title (R1); "stay in this conversation" (R4); Plan-mode wording (M14) | 12 |
| **Run 3 — Execute, test, iterate** | | | | **49** |
| 26 | Your financial app has a screen, a back end, a data source and an AI service | v2 26 | `.env` fix (M7); vocabulary | 4 |
| 27 | When something breaks, remove secrets, paste the error, and ask the agent to explain it | v2 29 | **moved before Run 3** (S4); redaction step (H4) | 4 |
| 28 | Run 3a: build the dashboard and check its numbers | v2 27 | title (R1); permission line (H1); acceptance list (S13, M16) | 15 |
| 29 | Run 3b: protect the key, then interview and plan the chatbot | v2 28 | **split** (S7); secrets first (H3); spec prompt fixes (M7, M8) | 12 |
| 30 | Run 3c: build and test the chatbot, then push without secrets | v2 28 | **split** (S7); tests and pass criteria (M8, S13); push checks the file list (H3) | 14 |
| **Close** | | | | **10** |
| 31 | You built a financial app by directing an AI and checking its work | v2 30 | recap fixed (M4, M12); 5 steps; finish check (S12) | 4 |
| 32 | Questions | v2 31 | none | 5 |
| 33 | Next session: your app stores price history and the chatbot reads reference pages | v2 32 | title and notes (M15) | 1 |

Total: 180 min. Hands-on run slides: 12 + 14 + 12 + 12 + 15 + 12 + 14 = **91 min** (v2: 77). 33 slides (v2: 32).

180 min · run 91

## Changes from v2

- **2:** title names opencode; notes say "latest available price", not "live" (M16).
- **3:** moved from v2 21; the brief's five workflow steps Interview → Plan (Approve / Edit / Reject) → Execute → Test / Debug → Iterate; brackets "Run 2" / "Run 3" (S1, S2).
- **4:** title "one small piece of text at a time"; bars labelled "Illustration"; notes drop "That is all it does" (M13).
- **5:** title, caption and notes rescoped from "stateless … whole conversation" to "doesn't remember; opencode sends the context" (M4); Turn-1 arrow shown on arrival (A1).
- **6:** redesign: the five-row stack opencode sends on every turn, rules rows never drop (M1, M5, spec §6.1). Replaces the v2 conveyor slide.
- **7:** replaces the v2 roles slide: context limit, older chat summarised, rules stay; save decisions in files (M1, M5, spec §6.2). Role glossary moves to the handout.
- **8:** redesign: three lanes opencode · Model · Tool, six numbered rows used once, permission gate, "opencode" instead of "App" (M2, H1, spec §6.3).
- **9:** title and punch line; exit boxes "Agent reports back" → "You test"; no "Task done" (M6).
- **10:** redesign: AGENTS.md as the project's standing brief (onboarding note), in/out lists, upkeep cycle, "ask the agent, then review" as a recommendation with a reason (M3, spec §6.4).
- **11:** quiz rewritten around a new conversation, not "overnight"; plausible distractors (M4, S6, spec §6.4).
- **12:** title softened to quick / stronger; `[FAST MODEL]` / `[SMART MODEL]` placeholders stay (user); car and truck run once (S11, A5).
- **13:** title and caption scoped to supported models and Ctrl+T options; one click moves the dial and it stays; reduced-motion fix (M11, A3, A4).
- **14:** punch line "Saving alone doesn't upload your work." (M12).
- **15:** three states saved → committed → pushed; `.env` shown as left out of the commit (M12).
- **16:** split title Run 1a (R1); permission line replaces "Allow once" (H1); setup line for the financial-app folder (R2).
- **17:** split title Run 1b (R1); AGENTS.md check step before the push (R3); "private" in Prompt 2 (H2).
- **18:** four equal cards by job instead of a staircase (S9).
- **19:** title says the agent decides when a skill fits (M10); request text, real descriptions, card inside the box, shelf "Not loaded" (A2).
- **20:** title "repeatable habit"; "Illustration" label; panels show short real text (M9).
- **21:** "make it ask first" → "interview first" (S1).
- **22:** title uses approve, edit or reject; keeps "Spec = PRD" (user).
- **23:** quiz moved before Run 2b (S3); subtler plans and plausible distractors (S6).
- **24:** title Run 2a (R1); "Up to five questions" (R7); tech line marked as course-supplied (S5).
- **25:** title Run 2b (R1); "Stay in this conversation" (R4); Plan-mode wording (M14).
- **26:** title "your financial app"; AI service outside the laptop; `.env` card "Not the AI" (M7).
- **27:** debugging moved before Run 3 (S4); redaction step (H4).
- **28:** title Run 3a (R1); permission line (H1); acceptance checklist (S13, M16); Iterate prompt.
- **29:** split from v2 28 (S7): secrets first (H3); chatbot spec prompt fixes (M7, M8).
- **30:** split from v2 28 (S7): tests with pass criteria (M8, S13); push lists files first (H3).
- **31:** recap fixed (M4, M12); five steps; finish check (S12).
- **33:** title and notes: stores price history, reads reference pages, model not retrained (M15).
