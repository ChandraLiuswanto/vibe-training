# Day 3 deck outlines (headline-only, draft for approval)

Build method taught and used in every session: Brainstorm → Spec → Plan (Approve/Edit/Reject) → Execute → Test → Iterate.
Spine for every session: prerequisite → worked example → practice → check (teaching deck, per AGENTS.md).
Tags: [talk] explain · [demo] presenter shows · [hands-on] participants type in opencode · [check] quiz/discussion · [Q&A].
Hands-on slides show the exact prompt; prompts are written only after testing.

## Session 1 — Build your first AI Financial App (55 slides)

Opening
1. Build your first AI Financial App [title]
2. Today you build a NISP dashboard and chatbot without writing code [talk]
3. This is the app you will have by the end of this session [demo]
4. You will be at the keyboard for most of these three hours [talk, agenda]

LLM basics
5. An LLM predicts the next words from the text you send it [talk]
6. The model is stateless: it remembers nothing between requests [talk]
7. The app resends the whole conversation every turn, which looks like memory [talk, diagram]
8. Start a new opencode session and ask what you told it before [hands-on]
9. The context window is the most text the model can read at once [talk]
10. When the context fills up, old details get dropped or summarised [talk]
11. Watch the context counter in opencode grow as you chat [hands-on]
12. Every request is a list of messages: system, user, assistant, tool [talk]
13. System sets the rules, user asks, assistant answers, tool reports results [talk]
14. With tool calling, the model asks for a tool and the app runs it [talk, diagram]
15. A coding agent is an LLM calling tools in a loop until the task is done [talk]
16. You bring the goal and the judgement; the agent does the typing [talk]
17. AGENTS.md is a note the agent reads at the start of every session [talk]
18. Run /init to create AGENTS.md, then add one rule of your own [hands-on]
19. The agent forgot your preference overnight. Why, and how do you fix it? [check]

Model selection
20. Fast models answer in seconds; smart models reason before they act [talk]
21. Use fast models for small edits and smart models for planning and debugging [talk]
22. Give the same task to a fast and a smart model and compare [hands-on]
23. Which model would you pick for each of these three tasks? [check]

Git (from demos/git-basics.html)
24. Without version control, nobody knows which file is the real one [talk]
25. Everyone works on a local copy and shares through one remote [talk]
26. A commit is a save point with a note, and it stays on your computer [talk]
27. Push sends your commits to GitHub; pull brings your teammates' commits back [talk]
28. Create your GitHub account [hands-on]
29. Ask opencode to commit your project and push it to GitHub [hands-on]
30. Which copy survives if your laptop breaks? [check]
31. Break, 10 minutes

Skills (focus block)
32. You can instruct the agent four ways: prompt, AGENTS.md, skill, workflow [talk]
33. A skill is packaged expertise the agent loads when a task needs it [talk]
34. The agent sees only each skill's name and description until a task needs it [talk, diagram]
35. Ask opencode which skills you have, then open one and read it [hands-on]
36. The same request gives a different result with a skill than without [demo]
37. Would a skill help here, or is a plain prompt enough? [check]

Brainstorm → Spec → Plan → Execute
38. An agent builds what it guesses you want, so make it ask first [talk]
39. Every build follows six steps: brainstorm, spec, plan, execute, test, iterate [talk]
40. In a brainstorm the agent asks one question at a time and you answer in business terms [talk]
41. Ask opencode to brainstorm the NISP dashboard with you, one question at a time [hands-on]
42. A spec says what to build and why; a plan says how, step by step [talk]
43. A good spec lists goals, what's out of scope, and how you'll know it works [talk]
44. Ask the agent to write the spec to docs/spec.md, then read and correct it [hands-on]
45. Switch opencode to Plan mode and ask for a step-by-step plan from the spec [hands-on]
46. Approve, edit or reject: what would you do with each of these three plans? [check]
47. Your app has two parts: a React screen and a FastAPI back end that fetches data and talks to the AI [talk, diagram]
48. Approve the plan, let the agent build the dashboard, then open it in your browser [hands-on]
49. Add the chatbot: update the spec, get a new plan, approve, build [hands-on]

Test, debug, iterate
50. When something breaks, paste the error and ask the agent to explain it [talk]
51. Ask your chatbot three questions and fix one thing that's wrong [hands-on]
52. Commit and push your working app [hands-on]

Close
53. You built an app by directing an AI, not by writing code [recap; checkpoint s1-chatbot]
54. Questions [Q&A]
55. Next session: your app remembers prices and learns the rules [talk]

## Session 2 — Watchlist & AI knowledge (33 slides)

Opening
1. Upgrade your Financial App: watchlist and AI knowledge [title]
2. Today your app remembers prices and your chatbot learns the rules [talk]
3. Your app shows NISP and answers basic questions [recap]
4. Start from your own app or switch to checkpoint s1-chatbot [hands-on]

Part 1: Database & watchlist
5. Your app forgets everything when it restarts [talk]
6. A database is where an app keeps what it must remember [talk]
7. A table has columns for what you store and a row for each record [talk]
8. In this price table, which is a row and which is a column? [check]
9. A watchlist needs two tables: the stocks you follow and their daily prices [talk]
10. Brainstorm the watchlist with the agent, then update the spec and approve the plan [hands-on]
11. Ask opencode to save NISP's price history from yfinance into a database [hands-on]
12. Ask the agent to show you what is inside the database [hands-on]
13. Build a watchlist page that reads from the database [hands-on]
14. Add BBRI and TLKM, remove one, and watch the dashboard change [hands-on]
15. yfinance is free but unofficial, so the app keeps a cached copy [talk]
16. You removed a stock but it's still on the dashboard. What do you tell the agent? [check]
17. Commit and push: checkpoint s2-watchlist [hands-on]
18. Break, 10 minutes

Part 2: Wiki & system prompt
19. A chatbot knows what it was trained on, not your business [talk]
20. Ask your chatbot three OJK questions and save the answers [hands-on]
21. Remember the system message? Here you write one for your chatbot [recap from S1]
22. A Wiki is a set of pages the chatbot reads before it answers [talk]
23. Only official sources go into the Wiki: ojk.go.id and idx.co.id [talk]
24. Add the Wiki to your spec, then approve the plan [hands-on]
25. Ask opencode to search the web for official OJK investor-education material [hands-on]
26. Turn the sources into Wiki pages, each with its source link [hands-on]
27. Connect the Wiki to the chatbot and write its system prompt [hands-on]
28. Ask the same three questions again and compare the answers [hands-on]
29. The chatbot quotes a rule but gives no source. Is that good enough? [check]
30. Commit and push: checkpoint s2-wiki [hands-on]

Close
31. Data lives in the database, knowledge in the Wiki, behaviour in the system prompt [recap]
32. Questions [Q&A]
33. Next session: turn your data into a report and a deck [talk]

## Session 3 — AI-powered reports & presentations (29 slides)

Opening
1. AI-powered reports and presentations [title]
2. Today the AI turns your app's data into a report and a slide deck [talk]
3. Your app has a watchlist, price history and a chatbot that knows the rules [recap]
4. Start from your own app or switch to checkpoint s2-wiki [hands-on]

Agentic workflows
5. A prompt does one thing; a workflow runs many steps in order [talk]
6. Prompt, skill and workflow are three levels of reuse [talk]
7. One sentence starts a five-step workflow [demo]
8. Is each of these a prompt, a skill or a workflow? [check]

Practice 1: Report
9. A good analysis report has data, charts and an insight you can defend [talk]
10. Write a short spec for the report: audience, sections, and what counts as a defensible insight [hands-on]
11. Ask opencode to write a NISP analysis report from your database [hands-on]
12. Check every number in the report against your dashboard [hands-on]
13. AI can write confident insights the data doesn't support [talk]
14. Which claim in this report does the data not prove? [check]
15. Break, 10 minutes

Practice 2: PowerPoint
16. A report is for reading; a deck is for telling [talk]
17. Ask opencode to turn the report into a PowerPoint [hands-on]
18. Open the deck and write down three things to fix [hands-on]

Iterate
19. Give feedback the way you'd brief a colleague: what, why and an example [talk]
20. Improve the structure, visuals and story in two rounds [hands-on]
21. Feedback changed the deck from a data dump into a story [demo, before/after]

Reusable workflow
22. If you'll do it again next month, save it as a workflow [talk]
23. Brainstorm → spec → plan is itself a workflow you can save [talk]
24. Save the report-to-PowerPoint steps as an opencode command [hands-on]
25. Run your workflow on TLKM and get a new report and deck [hands-on]
26. What should you still check by hand every time? [check]

Close
27. In one day you built, upgraded and automated a business app [recap]
28. Questions [Q&A]
29. Day 4: connect your app to other services and the web [talk]
