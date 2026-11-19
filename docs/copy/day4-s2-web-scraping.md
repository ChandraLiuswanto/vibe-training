# Day 4 · Session 2 — Web scraping · copy deck (round 2)

Plan: `docs/superpowers/plans/2026-11-19-day4-s2-web-scraping-rebuild.md` §10 (25-slide outline, approved 2026-11-19).
Status: reviewed by fedora/sol (READY WITH FIXES); fixes applied 2026-11-19. Visible text is what the room reads; speaker notes don't count toward the word budget.
Per slide: eyebrow · title · visual · visible text (by click step) · actions · notes (minutes) · source.

Budgets (AGENTS.md): ≤40 visible words per slide and per reveal step; ≤60 on the lab and instruction slides (22–25). Exceptions are listed on the slide.

---

## 1 · Your watchlist can show company news.
- **Eyebrow:** Session 2 · Web scraping
- **Visual:** app mock: watchlist with BBCA selected, news panel beside it.
- **Visible:** Financial App · Watchlist · News panel · Headline · date · source · 60 min talk · 60 min practice
- **Notes (2 min):** Open the watchlist and pick a company. By the end of the practice hour, a panel next to it lists recent news that mentions that company, with a link back to each story. The first hour explains how that news gets collected and why some websites push back. The second hour you build it.
- **Source:** old 1

## 2 · You learn how scraping works, then you build the news panel.
- **Eyebrow:** Agenda
- **Visual:** four blocks in a row, the last one dark.
- **Visible:** 1 How scrapers reach data · 2 When sites push back · 3 The rules we follow · Lab: build the news panel
- **Notes (1 min):** Three short chunks, then the lab. Chunk 1 is the order scrapers try things in. Chunk 2 is what happens when a website doesn't want to be scraped, and the tools people use against it. Chunk 3 is what we do in this course. Each chunk ends with a quick question.
- **Source:** new (plan §10.1 gap 6)

## 3 · A useful result shows a headline, a date and a source.
- **Eyebrow:** What a reader needs
- **Visual:** three columns.
- **Visible:** Headline: what the story is about · Date: when it was published · Source: where to check it
- **Notes (2 min):** Ask: if you saw a headline with no date and no source, what would you check before acting on it? A story might mention the company only in passing. Every row we save keeps all three, so anyone can click through and read the original.
- **Source:** old 3

## 4 · A web page is built for people; a scraper picks out the few details your app needs.
- **Eyebrow:** What scraping means
- **Visual:** moving: a news page (menu, ads, cards) → scraper → three fields; a dot travels along the arrow.
- **Visible:**
  - News page: menu · ads · result cards
  - Click 1: Scraper keeps → headline · date · link
- **Notes (2 min):** A news page mixes stories with menus, ads and links to other sections. A scraper is a small program that reads the page and keeps only the fields the app needs. It doesn't copy the whole article. Pages change their layout, so a scraper needs tests and a clear message when it stops finding things.
- **Source:** old 4 + 5

## 5 · Scrapers try the cheapest way to the data first.
- **Eyebrow:** 1 · How scrapers reach data
- **Visual:** ladder of six rungs, one added per click; a cost arrow down the side.
- **Visible:** 1 Feed or API · 2 Data inside the page · 3 Plain page request · 4 Real browser · 5 AI reads messy pages · 6 Paid service · ↓ more cost, more breakage · Stop at the first step that works.
- **Steps:** rungs 1–3, then 4–6, then the rule.
- **Notes (3 min):** This is the order experienced scrapers follow. Each step down costs more, runs slower and breaks more often when the site changes. Most jobs finish on steps 1 to 3. A browser is a different way of showing up at a site; it isn't automatically stronger. Notice what isn't on the ladder: proxies and CAPTCHA tools. Those are what people reach for when a site blocks them, and that's the next chunk. Today's lab stays on step 1.
- **Source:** web-scraping `SKILL.md` §1

## 6 · The data is often already in a feed or behind the page.
- **Eyebrow:** Steps 1–3 in real life
- **Visual:** three real captures side by side, each labelled "Captured 19 Nov 2026".
  - CNBC Indonesia Market RSS (raw feed: title, link, pubDate)
  - Infobanknews WordPress API (raw JSON: date, link, title)
  - CNBC Market page source: a `ld+json` block (headline, date)
- **Visible:** Feed · Data API · Tucked inside the page · Captured 19 Nov 2026
- **Notes (3 min):** Step 1: an RSS feed is a list of the latest stories a site publishes for other programs: title, link and exact time. Many WordPress sites also answer a simple data request with the same fields. Step 2: even when there's no feed, the page often carries its data in a hidden block for search engines, called JSON-LD. A scraper reads that block instead of the layout. Step 3 is a plain request for the page and reading the layout itself: it works, but it can break when the layout changes. (API: a way for apps to request data.) Session 1's exchange-rate service was step 1 too. Each capture came from one request on 19 November with a training identity.
- **Source:** `data-sources.md` rungs 1–2; captures 2026-11-19

## 7 · AI writes the scraper; plain code reads the pages.
- **Eyebrow:** Steps 5 and 6
- **Visual:** moving: a sample page goes to AI once → AI produces rules → plain code applies the rules to many pages (many dots).
- **Visible:**
  - AI reads one page once → writes the rules · Code reads every page
  - Click 1: Our scraper, 20 Oct – 19 Nov 2026: 35 automated repairs by an AI agent. · Paid service: rule of thumb, upkeep over 2 days a month.
- **Notes (3 min):** Step 5. When pages are too messy for fixed rules, an AI model can read them. Sending every page to a model is slow and costly, so the smarter split is: the model reads one example and writes the extraction rules, and ordinary code applies them to thousands of pages. That's one approach, and our news scraper uses a version of it: when a site changes and the nightly check fails, an AI agent rewrites that one site's settings and has to show the site's check passing before the fix is kept. Its history has 35 commits labelled as these automated repairs between 20 October and 19 November 2026. Step 6. A common rule of thumb: a paid scraping service makes sense when keeping your own scraper working costs more than about two days a month. Compare price per thousand usable records, not per request, and don't trust the vendor's success-rate claims.
- **Source:** `llm-extraction.md` §1; `SKILL.md` §1 rung 6; `~/news_api` git log 2026-10-20 → 2026-11-19, `newsscrape/repair.py`

## 8 · A site checks four things before it trusts a visitor.
- **Eyebrow:** 2 · When sites push back
- **Visual:** moving: a request passes four gates in a row; a red stop at the last gate.
- **Visible:** Who you say you are · How you connect · Where you connect from · How you behave · Sites block when these don't match. · In this course: we learn these to recognise a block, not to get past it.
- **Notes (2 min):** Say the course rule first: before any live request we check the site's terms, its robots.txt and internal approval, and if a site blocks us we stop. This chunk explains what's happening when that happens, and what tools you'll hear vendors and AI agents suggest. Sites may consider several signals, usually these four. Who: the browser name your request announces. How: the technical handshake your software makes, which differs between Chrome and a Python script. Where: an office line, a home line, a phone network or a cloud server. Behave: speed and pattern, such as 50 pages in a second. Sites block when these disagree. A refusal does not tell you which signal mattered.
- **Source:** `blocked.md` §2

## 9 · The site's reply code tells you what happened.
- **Eyebrow:** Reading the answer
- **Visual:** moving: request → site → reply card; three cards.
- **Visible:** 200 OK: check what came back · 429 Too many requests: asking too often · 403 Forbidden: the site refused; the code doesn't say why · In our lab: 429 or 403 means stop and keep saved results.
- **Notes (2 min):** Every reply from a website starts with a three-digit code. 429 means you asked too often. In general, scrapers wait and ask less often; in our lab the app doesn't retry on its own: it stops, keeps the saved results, and you try again later by pressing Refresh. 403 means the site refused. The code doesn't say why: it could be the rules, the address or something about the request. Asking again won't change it.
- **Source:** `SKILL.md` §2

## 10 · A 200 reply can still be a failure.
- **Eyebrow:** Silent failures
- **Visual:** four small mock replies, each tagged "200 OK", labelled Illustration.
- **Visible:** Check page: "Just a moment…" · Expected fields missing · Login page instead of news · Yesterday's copy · All four can say 200 OK.
- **Notes (3 min):** These are the expensive failures, because nothing crashes. The scraper "succeeds" and saves a check page, a page without the expected fields, a login page or a stale copy. The fix is to look at what came back: is it the feed we expected, with the fields we expect, and how many rows compared with last time? A sudden drop from 20 rows to 2 is worth a look. Careful: a real feed with no story about your company today is a valid result, "no matches". It's different from a reply that isn't the feed at all. The lab tests both.
- **Source:** `production.md` §3; `SKILL.md` §4

## 11 · A headless browser runs without a visible window.
- **Eyebrow:** Headless vs headed
- **Visual:** side by side: an empty dashed frame "no window" vs a real browser frame; click reveals the headed side.
- **Visible:**
  - Headless: no window · fast and cheap · leaves tell-tale signs
  - Click 1: Headed: a visible window · useful for watching what the page does
  - Both are still automation.
  - Callout: Our scraper's settings, 10 Nov 2026: Tempo's index needed a headed browser.
- **Notes (2 min):** Some pages only show their news after the browser runs the page's code. For those, scrapers drive a real browser. Headless means the browser runs without a window, controlled by a program. It's fast, but it leaves small traces that check scripts look for. Headed means a normal visible window.  The Tempo note comes from our scraper's settings on 10 November. On 19 November one load of the same page wasn't blocked either way. Blocks come and go, which is part of the cost.
- **Source:** `blocked.md` §3 step 3; `~/news_api/sites/tempo.toml`; check 2026-11-19

## 12 · A proxy changes where your request seems to come from.
- **Eyebrow:** Proxy types
- **Visual:** moving path: you → proxy → site (the site sees the proxy's address); table below.
- **Visible:**

  | Type | Comes from | Cost | Fits |
  |---|---|---|---|
  | Datacenter | Cloud servers | Cheap | Testing |
  | ISP | Home-ISP address in a data centre | Medium | Long sessions |
  | Residential | Real people's home devices | High | Small, one-off jobs |
  | Mobile | Phone networks | High | Sites that distrust other addresses |

  Callout: Our scraper, 20 Oct 2026: Antara's regional sites blocked it after a burst; it now uses a proxy.
- **Budget exception:** essential reference table; ~50 words.
- **Notes (3 min):** A proxy is a middleman: your request goes out through someone else's internet address. Sites rate addresses: cloud servers look like bots, home and phone addresses look like people. It isn't a step on the ladder. People reach for one when the address is the reason for a block, and that's exactly the moment our course rule says stop. Prices in the 2026 guide run from cents per GB for datacenter to dollars per GB for residential and mobile; re-check before quoting. Residential addresses come from ordinary people's devices that share their connection, often through an app. A 2026 investigation found one such network carrying ad fraud and spam, and an FBI seizure found part of another was a botnet. The Antara case: 20 regional sites share one server, and our scraper's settings record a block within 15 minutes of a burst on 20 October; the configuration later changed. That's a record of one incident, not the site's stated policy. If time is short, skip the anecdotes and keep the table.
- **Source:** `proxies.md` §1; `~/news_api/sites/antaranews.toml`

## 13 · A CAPTCHA asks the visitor to prove it is human.
- **Eyebrow:** CAPTCHA and check pages
- **Visual:** real capture of Google's public reCAPTCHA demo ("I'm not a robot"), "Captured 19 Nov 2026"; mock "Just a moment…" page labelled Illustration; a score meter.
- **Visible:**
  - Puzzle: tick the box, pick the pictures (reCAPTCHA)
  - Invisible score: no puzzle, the page rates you
  - Check page: "Just a moment…" while the site checks the browser
  - Callout: Our scraper's settings: Bisnis.com check page 27 Sep, Turnstile block 10 Nov.
  - Click 1: In this course: a CAPTCHA means stop.
- **Notes (2 min):** reCAPTCHA is Google's; Turnstile is Cloudflare's, and it often shows nothing at all: the page scores your behaviour in the background. A check page can arrive with code 200, which is the silent failure from three slides ago. Paid solving services exist; using them usually breaks the site's terms, and in this course the answer is no. On 19 November one load of Bisnis.com showed no check page; the callout records what our scraper saw on 27 September and 10 November.
- **Source:** `production.md` §3; `llm-extraction.md`; `~/news_api/sites/bisnis.toml`; reCAPTCHA demo capture

## 14 · Our own scraper shows how often sites push back.
- **Eyebrow:** From our news scraper
- **Visual:** one bar of 454 sites; 122 highlighted; small breakdown.
- **Visible:** 19 Nov 2026: 454 enabled site settings · 122 use one or more: 94 a browser or browser-like client · 61 a Cloudflare solver · 30 a proxy · 7 a visible browser · Counts overlap.
- **Notes (2 min):** These are the settings of the news scraper we run, read on 19 November. 332 sites have none of these settings: they use feeds, sitemaps, data APIs or plain page requests. 122, about one in four, use something heavier, and a site can use more than one, so the numbers overlap. The settings show what the scraper is configured to do, not that each site needs it today. Every extra tool is another thing that breaks and another cost.
- **Source:** `~/news_api/sites/*.toml`, enabled configs, 2026-11-19

## 15 · Knowing these tools is not permission: we check the rules and stop when blocked.
- **Eyebrow:** 3 · The rules we follow
- **Visual:** three check chips; quiz below.
- **Visible:**
  - Site terms · robots.txt · Internal approval
  - Quiz: the news site blocks your request. What should the app do?
    - A. Try again until it works
    - B. Switch to a proxy
    - C. Stop and show the last saved results ✓
- **Budget exception:** quiz choices; ~43 words.
- **Notes (3 min):** Three checks before any live request: the site's terms of use, its robots.txt file (the site's note to bots about where they may go), and approval inside the company. robots.txt isn't permission on its own. Some news sites name AI agents directly: on 19 November, Antara, Kontan and Republika named ClaudeBot. Do not change tools to work around a refusal. Robots.txt observations are from 19 November; terms have not been reviewed. Run the quiz: let two people argue A and B before revealing C.
- **Source:** old 6 + 7; `SKILL.md` §0

## 16 · A good scraper uses the cheapest door, checks what came back and stops when blocked.
- **Eyebrow:** Recap · your turn
- **Visual:** three scenario cards; each answer appears on its own click.
- **Visible:**
  - The site has an RSS feed. → Click 1: Use it. Step 1.
  - You get 429. → Click 2: In our lab: stop, keep saved results, try later.
  - 200, but the page says "Just a moment…". → Click 3: It's a block. Stop.
- **Notes (3 min):** Read each scenario aloud and take an answer from the room before clicking. These are the three habits the lab needs: look for the cheapest door, read what actually came back, and stop when the site says no.
- **Source:** new (plan §10.1 gap 6)

## 17 · One feed item shows what to keep.
- **Eyebrow:** Worked example · CNBC Indonesia Market RSS
- **Visual:** real feed tags mapped to fields.
- **Visible:**
  - title → Headline: "Bos BI Bawa Kabar Positif: Kredit Ngebut dan Pabrik Ngebul!"
  - pubDate → Date: 19 Nov 2026, 16:13 WIB
  - link → Link, source shown as cnbcindonesia.com
  - Offline? Sample feed.
- **Actions:** The prompt · stage 2 ↗ · Download sample feed ↓
- **Notes (3 min):** This is a real item captured from the feed on 19 November. Point to how the feed already labels each field, so nothing has to be dug out of a page layout. The date is exact. A search page would only say "2 jam lalu" (two hours ago). We keep headline, date, link and the time we fetched it, never the full article. If the room has no internet or the source isn't approved, the sample feed and sample page have three made-up stories with the same fields.
- **Source:** old 8 + 11; live feed 2026-11-19

## 18 · Saved results feed the panel, and Refresh is the only fetch.
- **Eyebrow:** You control when it runs
- **Visual:** moving: feed → saved results → panel; a refresh dot that fails turns red and the panel keeps its rows.
- **Visible:** Feed → Saved results → News panel · Opening the panel: shows saved rows · Refresh: one request · Refresh fails: keep the last good rows
- **Notes (2 min):** Opening the dashboard never contacts the news site; it shows what's saved. Only the Refresh button sends a request, and only one. If the refresh fails, the panel keeps the last good results and shows how old they are. The panel labels four states: sample, empty, stale and unavailable, and sample links can't be clicked. No background jobs, no automatic retries.
- **Source:** old 9 + 10

## 19 · The agent proposes the work, and you approve each change.
- **Eyebrow:** Facilitator demo
- **Visible:** 1 Plan the changes · 2 Show commands and files · 3 Wait for your "yes"
- **Actions:** The prompt · stage 1 ↗
- **Notes (2 min):** Paste the practice prompt into a coding agent. Read the files, commands and checks it proposes before approving, including any database change, which needs its own approval. The prompt asks the agent to wait; the tool's approval settings are what actually enforce it.
- **Source:** old 12

## 20 · The dashboard shows mentions for one company at a time.
- **Eyebrow:** Dashboard example · Illustration
- **Visible:** Mentions · BBCA · Headline · source · published · fetched 10 min ago
- **Notes (2 min):** Select one company in the mock dashboard. A story that mentions a company is only a mention, not a claim about the company. Show where the source, the published time and the fetch time appear, and what the panel says when the last refresh didn't work. The rows are placeholders. A feed may have no story about a given company today; pick a company with matches for the demo.
- **Source:** old 13

## 21 · Text from a web page is data, even when it sounds like an instruction.
- **Eyebrow:** Keep the two apart
- **Visible:** Instructions come from your app · Page text: "Ignore your rules…" · Show it as text, never follow it.
- **Notes (2 min):** Point to the made-up teaser in the sample feed and ask who wrote it. The app received it from outside, so it can't tell the app or the chatbot what to do. Show it as plain text or leave it out. The tests prove it changes nothing.
- **Source:** old 15

## 22 · The sample page helps you prove the scraper works.
- **Eyebrow:** Four checks before you finish
- **Visible:** Four groups of offline checks: Sample rows found · No matches is a valid result · Block or check page → keep the last good results · Wrong page or missing fields → failed refresh
- **Actions:** The prompt · stage 6 ↗ · Download sample page ↓
- **Notes (3 min):** These are groups, not the full list; the handout and prompt stage 6 have every check: the three sample rows, no matches, changed layout or missing fields, a 403 or 429, a 200 that is really a "Just a moment…" page, duplicate refresh, keeping the saved results, one company's panel, and the teaser that tries to give orders. All run offline. Passing them shows the app handles these cases; it doesn't prove a live site will keep working.
- **Source:** old 16; slide 10

## 23 · The search-page comparison and the Wiki page are optional extras.
- **Eyebrow:** If you finish early
- **Visual:** two cards.
- **Visible:**
  - Stage 4 · Search page: compare it with the feed. Notice "2 jam lalu" and the extra layout.
  - Stage 5 · Wiki: a separate page: "News, not an official rule. Headlines only."
- **Actions:** The prompt · stages 4–5 ↗
- **Notes (2 min):** Both are optional. Stage 4 shows why the feed was the cheaper door: the search page has fuzzy times, ads and repeated links. It uses a saved copy, or one approved live request. Stage 5 has its own approval step. Stage 5 gives the chatbot a labelled news page it can cite, kept apart from the official Wiki pages. Sample rows never go into the real Wiki.
- **Source:** prompt stages 4–5 (plan §10.1 gap 7)

## 24 · In the lab, you build the scraper and news panel first.
- **Eyebrow:** Practice · 60 minutes
- **Visible:** 00–10 Plan · 10–30 Read the feed (or sample) · 30–50 Build the panel · 50–60 Show the checks
- **Actions:** Open the prompt ↗ · Setup help ↗
- **Notes (1 min):** Start with the plan. Read the facilitator-approved feed, or the sample if offline. Wire the results into the news panel, then use the last ten minutes for checks. Extras only if time allows.
- **Source:** old 17

## 25 · You finish by showing what works and what you couldn't verify.
- **Eyebrow:** Finish check
- **Visible:** Scraper: show the rows · News panel: show one company · Checks: passed, failed, blocked, not run · Live feed: used, skipped or blocked · Next → sign-in, roles and audit trail
- **Actions:** The prompt · finish check ↗
- **Notes (1 min):** Everyone shows the scraper's rows and the news panel for one company. Each person says which checks ran, which were skipped, and whether they used the live feed or the sample. Session 3 adds sign-in, roles and an audit trail.
- **Source:** old 18

---

## Placeholders and things to verify before class
- Feeds, robots.txt and screenshots: one request each on 19 Nov 2026; site terms not reviewed.
- Slide 17's headline is a real 19 Nov item; it will be old news by class day.
- Fleet numbers (slides 7, 14) are a 19 Nov snapshot of `~/news_api` settings and git history (35 repair commits counted from 20 Oct 00:00 to 19 Nov 2026).
- Tempo and Bisnis.com cases are past observations from `~/news_api` configs, not reproduced on 19 Nov.
- Proxy cost bands, the headless/headed test, and the residential-network findings: 2026 scraping-guide snapshot.
- Slides 10, 13 (check page) and 20 contain mock content, labelled Illustration.
- Practice prompt not rehearsed end to end. The CNBC Market feed had few matches for some tickers on 19 Nov (BBCA 1, BMRI 0).
