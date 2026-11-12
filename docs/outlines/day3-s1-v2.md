# Day 3 · Session 1 — outline v2 (draft for approval)

Changes from v1 (55 slides), requested by the user on 2026-11-11:
- About 28 slides instead of 55. Related slides are merged.
- **3 participant runs** (hands-on), down from 14. They form one continuous project: set it up → decide what to build → build it.
- The break slide is gone.
- More visuals: concept slides become animated diagrams that build step by step on each click.
- Presenter demos are cut to one quick look at the finished app. The skill comparison becomes a visual slide.

Legend: [visual] = animated diagram · [run] = participant hands-on · [check] = quiz

## Opening
1. Build your first AI Financial App [title]
2. Today you build a NISP dashboard and chatbot without writing code [visual: app mock-up assembles]

## How an AI coding agent works
3. An LLM predicts the next words from the text you send it [visual: words appear one by one]
4. The model is stateless, so the app resends the whole conversation every turn [visual: message rows grow]
5. The context window is the most the model can read at once; when it fills, old details drop off [visual: a bar fills and old blocks fall out]
6. Every request is one list of messages: system, user, assistant, tool [visual: the stack builds]
7. With tool calling, the model asks for a tool and the app runs it [visual: numbered arrows animate]
8. A coding agent is an LLM calling tools in a loop until the task is done [visual: the loop spins]
9. AGENTS.md is a note the agent reads at the start of every session [visual]
10. The agent forgot your preference overnight. Why, and how do you fix it? [check]

## Choosing models and saving work
11. Use fast models for small edits and smart models for planning and debugging [visual: two lanes]
12. Everyone works on a local copy and shares through GitHub [visual: laptop ⇄ GitHub]
13. A commit is a save point; push sends it to GitHub, pull brings changes back [visual: commits travel]

## Run 1 — Set up your project
14. Run 1: create your GitHub account, add AGENTS.md with one rule, and push [run, 2 slides: 14a sign-up + /init; 14b rule + push]

## Skills
15. You can instruct the agent four ways: prompt, AGENTS.md, skill, workflow [visual: rising steps]
16. A skill is packaged expertise the agent loads only when a task needs it [visual: list → one skill loads]
17. The same request gives a more structured result when a skill is loaded [visual: side-by-side; optional live demo in notes]

## Run 2 — Decide what to build
18. An agent builds what it guesses you want, so make it ask first [visual]
19. Every build follows six steps: brainstorm, spec, plan, execute, test, iterate [visual: steps light up]
20. A spec says what and why; a plan says how, and you approve, edit or reject it [visual]
21. Run 2: brainstorm the dashboard, write the spec, then plan it [run, 2 slides: 21a brainstorm + spec; 21b Plan mode, approve/edit/reject, save]
22. Approve, edit or reject: what would you do with each of these three plans? [check]

## Run 3 — Build it
23. Your app has two parts: a React screen and a FastAPI back end that fetches data and talks to the AI [visual: request flows through]
24. Run 3: build the dashboard, then add the chatbot through the same loop [run, 2 slides: 24a dashboard; 24b chatbot + test + push]
25. When something breaks, paste the error and ask the agent to explain it [visual]

## Close
26. You built an app by directing an AI, not by writing code [recap; checkpoint s1-chatbot]
27. Questions [Q&A]
28. Next session: your app remembers prices and learns the rules

Total: 28 headlines, 31 slides counting the run parts.

## Proposed timing (180 min, no break)
| Block | Min |
|---|---|
| Opening | 10 |
| How an AI coding agent works | 30 |
| Models and Git | 15 |
| Run 1 | 25 |
| Skills | 15 |
| Run 2 | 35 |
| Run 3 | 40 |
| Close + Q&A | 10 |
