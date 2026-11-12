# Day 3 · Session 2 — outline v2 (draft for approval)

These are the Session 1 v2 rules applied to Session 2:
- about 28 slides
- **3 participant runs** that build on each other
- no break
- concept slides are animated diagrams that build on each click, with gentle looping motion

Example stock: **NISP (NISP.JK)**. The watchlist adds BBRI and TLKM.

Legend: [visual] = animated diagram · [run] = participant hands-on · [check] = quiz

## Opening
1. Upgrade your Financial App: watchlist and AI knowledge [title]
2. Today your app remembers prices and your chatbot learns the rules [visual: app gains a database and a book]
3. Start from your own app or switch to checkpoint s1-chatbot [talk, short; recovery sentence]

## Why an app needs memory
4. Your app forgets everything when it restarts [visual: the page reloads and the numbers vanish]
5. A database keeps what the app must remember, in tables of rows and columns [visual: a table fills row by row]
6. In this price table, which is a row and which is a column? [check]
7. A watchlist needs two tables: the stocks you follow and their daily prices [visual: two tables linked by ticker]

## Run 1 — Save prices to a database
8. Run 1: brainstorm the watchlist, update the spec, then save NISP's price history to a database [run, 2 slides: 8a brainstorm + spec + plan; 8b build + "show me what's inside the database"]

## Run 2 — Build the watchlist
9. yfinance is free but unofficial, so the app keeps a cached copy [visual: live feed with a cache shield]
10. Run 2: build a watchlist page, add BBRI and TLKM, remove one, and push [run, 2 slides: 10a build; 10b add/remove + push]
11. You removed a stock but it's still on the dashboard. What do you tell the agent? [check]

## Why the chatbot needs knowledge
12. A chatbot knows what it was trained on, not your rules [visual: a model with a gap where OJK rules should be]
13. The system message sets the chatbot's role and rules; you write it [visual: links back to S1 message roles]
14. A Wiki is a set of pages the chatbot reads before it answers [visual: question → finds a page → answers with source]
15. Only official sources go in: ojk.go.id and idx.co.id, each page with its link [visual: two sources pass the gate, others bounce]

## Run 3 — Teach the chatbot
16. Run 3: ask three OJK questions, build the Wiki from official sources, then ask again [run, 2 slides: 16a baseline questions + Wiki spec/plan + web search; 16b Wiki pages + system prompt + re-ask + push]
17. The chatbot quotes a rule but gives no source. Is that good enough? [check]
18. Before and after: the same question, now with a source [visual: side-by-side answers]

## Close
19. Data lives in the database, knowledge in the Wiki, behaviour in the system prompt [recap visual: three boxes]
20. Questions [Q&A, moving shapes]
21. Next session: turn your data into a report and a deck

Total: 21 headlines, 24 slides counting the run parts.

## Proposed timing (180 min, no break)
| Block | Min |
|---|---|
| Opening + recovery | 10 |
| Why an app needs memory | 20 |
| Run 1 — database | 35 |
| Run 2 — watchlist | 35 |
| Why the chatbot needs knowledge | 20 |
| Run 3 — Wiki + system prompt | 45 |
| Close + Q&A | 15 |
