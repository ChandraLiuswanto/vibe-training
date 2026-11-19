# Day 4 · Session 2 — Web scraping · copy deck

Plan: `docs/superpowers/plans/2026-11-19-day4-s2-web-scraping-rebuild.md`
Status: for owner review (Task 1 gate). Visible text only under **Visible**; speaker notes don't count toward the budget.
Format per slide: eyebrow · title · visible text (by reveal step) · actions · notes · minutes · source.

---

## 1 · Your watchlist can show company news.
- **Eyebrow:** Session 2 · Web scraping
- **Visible:** Financial App · Watchlist · News panel · Headline · date · source · 60 min talk · 60 min practice
- **Notes (2 min):** Open the watchlist and pick a company. By the end of the practice hour, a panel under it lists recent news that mentions that company, with a link back to where each story came from. The first hour explains how that news gets collected and why some websites push back. The second hour you build it.
- **Source:** old 1

## 2 · The news panel builds on the app you already have.
- **Eyebrow:** What we add today
- **Visible:** Watchlist · Wiki · Chatbot · Exchange rates (Session 1) · News (new today)
- **Notes (2 min):** Ask the room to name what they already have: the stock dashboard, the database, the Wiki, the chatbot and the exchange-rate feature from Session 1. Nothing gets replaced. The news panel reads which company is selected and shows its own list.
- **Source:** old 2

## 3 · A useful result shows a headline, a date and a source.
- **Eyebrow:** What a reader needs
- **Visible:** Headline: what the story is about · Date: when it was published · Source: where to check it
- **Notes (2 min):** Ask: if you saw a headline with no date and no source, what would you check before acting on it? A story might mention the company only in passing. Every row we save keeps all three, so anyone can click through and read the original.
- **Source:** old 3

## 4 · A web page is built for people; a scraper picks out the few details your app needs.
- **Eyebrow:** What scraping means
- **Visible:**
  - Step 1: News page · menu · ads · result cards
  - Step 2: Scraper keeps → headline · date · link
- **Notes (3 min):** A news page mixes stories with menus, ads and links to other sections. A scraper is a small program that reads the page and keeps only the fields the app needs. It doesn't copy the whole article. Pages change their layout, so a scraper needs tests and a clear message when it stops finding things.
- **Source:** old 4 + 5

## 5 · Scrapers try the cheapest way to the data first.
- **Eyebrow:** The ladder
- **Visible:** 1 Official feed or API · 2 Data hidden inside the page · 3 Plain request for the page · 4 Real browser · 5 Proxy · 6 Paid scraping service · ↓ more cost, more breakage · Stop at the first step that works.
- **Notes (4 min):** This is the order experienced scrapers follow. Each step down costs more, runs slower and breaks more often when the site changes. Most jobs finish on steps 1 to 3. A browser is a different way of showing up at the site; it isn't automatically stronger. A paid service starts to make sense when fixing your own scraper takes more than a couple of days a month. Today we stay on step 1.
- **Source:** web-scraping `SKILL.md` §1 (decision ladder)

## 6 · The data is often already in a feed or behind the page.
- **Eyebrow:** Step 1 in real life
- **Visible:**
  - RSS feed: CNBC Indonesia Market · Liputan6 Bisnis · Antara Bursa
  - WordPress API: Infobanknews · Stockwatch
  - Sitemap: IDX Channel · Investor.id
  - "Checked 19 Nov 2026"
- **Notes (3 min):** An RSS feed is a list of the latest stories that the site publishes for other programs to read: title, link and exact time. Many sites built on WordPress also answer a simple data request. A sitemap lists every page so search engines can find them. Session 1's exchange-rate service worked the same way: labelled data for software, not a page for people. Each of these returned a normal answer on 19 November to one request from a training identity. That can change; the facilitator checks again before class.
- **Source:** `data-sources.md` rung 1; live check 2026-11-19; `~/news_api` configs

## 7 · The site's reply code tells you what happened.
- **Eyebrow:** Reading the answer
- **Visible:**
  - 200 OK: check what came back
  - 429 Too many requests: slow down
  - 403 Forbidden: the site decided you're a bot
  - Quick check: a scraper gets 429. What should it do?
  - Answer (reveal): Wait, then try again later, less often.
- **Notes (3 min):** Every reply from a website starts with a three-digit code. 429 is a negotiation: you asked too often, so wait and ask less often. 403 is a judgement: something about your request looked wrong, and asking faster won't help. And 200 doesn't always mean success. A 200 can carry an empty list, a login page or a "Just a moment…" check page instead of the news. The lab's tests look at what came back as well as the code.
- **Source:** `SKILL.md` §2, §4; `production.md` §3

## 8 · A site checks four things before it trusts a visitor.
- **Eyebrow:** How sites spot bots
- **Visible:** Who you say you are · How you connect · Where you connect from · How you behave · They must tell the same story.
- **Notes (3 min):** Who: the browser name your request announces. How: the technical handshake your software makes, which differs between Chrome and a Python script. Where: an office line, a home line, a phone network or a cloud server. Behave: speed and pattern, such as 50 pages in a second. Sites block when these disagree. A request that says "I'm Chrome" but connects like a script from a cloud server gets stopped before the page loads.
- **Source:** `blocked.md` §2

## 9 · A hidden browser is easy to spot; a visible one gets further.
- **Eyebrow:** Headless vs headed
- **Visible:**
  - Headless: no window · fast and cheap · leaves tell-tale signs
  - Headed: a real window · slower, heavier · passes more checks
  - Both are still automation.
- **Notes (3 min):** Some pages only show their news after the browser runs the page's code. For those, scrapers drive a real browser. Headless means the browser runs without a window, controlled by a program. It's fast, but it leaves small traces that check scripts look for. Headed means a normal visible window. In one 2026 test, a plain automated browser was blocked on five protected sites when headless, and got into four of them when headed. Real example from our own news scraper (`~/news_api`, November 2026): Tempo's index page blocks a headless browser and only works with a visible one. 2026 snapshot, re-check.
- **Source:** `blocked.md` §3 step 3; `~/news_api/sites/tempo.toml`

## 10 · A proxy changes where your request seems to come from.
- **Eyebrow:** Proxy types
- **Visible:** (reference table)

  | Type | Comes from | Cost | Fits |
  |---|---|---|---|
  | Datacenter | Cloud servers | Cheap | Testing, unprotected sites |
  | ISP | Home-ISP address in a data centre | Medium | Long logged-in sessions |
  | Residential | Real people's home devices | High | Small jobs needing a clean address |
  | Mobile | Phone networks | High | The hardest sites |

- **Notes (4 min):** A proxy is a middleman: your request goes through someone else's internet address. Sites rate addresses: cloud servers look like bots, home and phone addresses look like people. Prices in the 2026 guide run from cents per GB for datacenter to dollars per GB for residential and mobile; re-check before quoting. Residential addresses come from ordinary people's devices that share their connection, often through an app. A 2026 investigation found one such network carrying ad fraud and spam traffic, and an FBI seizure found part of another was a botnet. Real example: our news scraper sends all Antara regional sites through a proxy, because their shared server drops an address after a burst of requests.
- **Budget exception:** essential reference table (four types × four facts); ~45 words.
- **Source:** `proxies.md` §1; `~/news_api/sites/antaranews.toml`

## 11 · A CAPTCHA asks the visitor to prove it is human.
- **Eyebrow:** CAPTCHA and check pages
- **Visible:**
  - Puzzle: tick the box, pick the pictures (reCAPTCHA)
  - Invisible score: no puzzle, the page rates you
  - Check page: "Just a moment…" (Cloudflare Turnstile)
  - In this course: a CAPTCHA means stop.
- **Notes (3 min):** reCAPTCHA is Google's version; Turnstile is Cloudflare's. The newer kinds often show nothing at all: the page scores your behaviour in the background. A check page usually arrives with code 200, which is why a scraper can "succeed" and save a page of nothing. Paid solving services exist and are cheap, and using them usually breaks the site's terms. Real example: Bisnis.com showed our scraper a "Just a moment…" page in September and a Turnstile block in November.
- **Source:** `production.md` §3; `llm-extraction.md`; `~/news_api/sites/bisnis.toml`

## 12 · Knowing these tools is not permission: we check the rules and stop when blocked.
- **Eyebrow:** Public is not the same as approved
- **Visible:**
  - Site terms · robots.txt · internal approval
  - Quiz: the news site blocks your request. What should the app do?
    - A. Try again until it works
    - B. Switch to a proxy
    - C. Stop and show the last saved results ✓
- **Notes (4 min):** Three checks before any live request: the site's terms of use, its robots.txt file (the site's note to bots about where they may go), and approval inside the company. robots.txt isn't permission on its own. Some news sites name AI agents directly: on 19 November, Antara, Kontan and Republika named ClaudeBot. Proxies and solvers are how people get past a "no". Whether to do that is decided by the business and legal teams, before anyone writes code. Run the quiz: let two people argue A and B before revealing C.
- **Budget exception:** quiz choices (AGENTS.md allows); ~43 words.
- **Source:** old 6 + 7; `SKILL.md` §0

## 13 · One feed item shows what to keep.
- **Eyebrow:** Worked example · CNBC Indonesia Market RSS
- **Visible:**
  - title → Headline: "Bos BI Bawa Kabar Positif: Kredit Ngebut dan Pabrik Ngebul!"
  - pubDate → Date: 19 Nov 2026, 16:13 WIB
  - link → Source: cnbcindonesia.com
  - Offline? Use the sample page.
- **Actions:** Download sample page ↓
- **Notes (3 min):** This is a real item captured from the feed on 19 November. Point to how the feed already labels each field, so nothing has to be dug out of a page layout. The date is exact. A search page would only say "2 jam lalu" (two hours ago). We keep headline, date, link and the time we fetched it, never the full article. If the room has no internet or the source isn't approved, the downloadable sample page has three made-up stories with the same fields.
- **Source:** old 8 + 11; live feed 2026-11-19

## 14 · Saved results feed the panel, and Refresh is the only fetch.
- **Eyebrow:** You control when it runs
- **Visible:** Feed → Saved results → News panel · Opening the panel: shows saved rows · Refresh: one request · Refresh fails: keep the last good rows
- **Notes (3 min):** Opening the dashboard never contacts the news site; it shows what's saved. Only the Refresh button sends a request, and only one. If the refresh fails, the panel keeps the last good results and shows how old they are. No background jobs, no automatic retries.
- **Source:** old 9 + 10

## 15 · The agent proposes the work, and you approve each change.
- **Eyebrow:** Facilitator demo
- **Visible:** 1 Plan the changes · 2 Show commands and files · 3 Wait for your "yes"
- **Actions:** The prompt · stage 1 ↗
- **Notes (3 min):** Paste the practice prompt into a coding agent. Read the files, commands and checks it proposes before approving. The prompt asks the agent to wait; the tool's approval settings are what actually enforce it.
- **Source:** old 12

## 16 · The dashboard shows mentions for one company at a time.
- **Eyebrow:** Dashboard example · Illustration
- **Visible:** Mentions · BBCA · Headline · source · published · fetched 10 min ago
- **Notes (3 min):** Select one company in the mock dashboard. A story that mentions a company is only a mention, not a claim about the company. Show where the source, the published time and the fetch time appear, and what the panel says when the last refresh didn't work.
- **Source:** old 13 (ticker changed to a feed-friendly example; mock rows)

## 17 · Text from a web page is data, even when it sounds like an instruction.
- **Eyebrow:** Keep the two apart
- **Visible:** Instructions come from your app · Page text: "Ignore your rules…" · Show it as text, never follow it
- **Notes (3 min):** Point to the made-up teaser in the sample page and ask who wrote it. The app received it from outside, so it can't tell the app or the chatbot what to do. Show it as plain text or leave it out. The tests prove it changes nothing.
- **Source:** old 15

## 18 · The sample page helps you prove the scraper works.
- **Eyebrow:** Four checks before you finish
- **Visible:** Three sample rows · No matches · Page layout changed · Refresh blocked → keep the last good results
- **Actions:** The prompt · stage 6 ↗ · Download sample page ↓
- **Notes (4 min):** Start with the three expected sample rows. Then test no matches, a changed page layout and a blocked refresh, all offline. An empty result and a scraper that no longer recognises the page look alike; the tests tell them apart. If an update fails, the last good results stay visible.
- **Source:** old 16

## 19 · In the lab, you build the scraper and news panel first.
- **Eyebrow:** Practice · 60 minutes
- **Visible:** 00–10 Plan · 10–30 Read the feed (or sample) · 30–50 Build the panel · 50–60 Show the checks
- **Actions:** Open the prompt ↗ · Setup help ↗
- **Notes (2 min):** Start with the plan. Read the facilitator-approved feed, or the sample if offline. Wire the results into the news panel, then use the last ten minutes for checks. The search-page comparison and the Wiki are extras if time allows.
- **Source:** old 17

## 20 · You finish by showing what works and what you couldn't verify.
- **Eyebrow:** Finish check
- **Visible:** Scraper: show the rows · News panel: show one company · Checks: passed, failed, not run · Next → sign-in, roles and audit trail
- **Actions:** The prompt · finish check ↗
- **Notes (1 min):** Everyone shows the scraper's rows and the news panel for one company. Each person says which checks ran, which were skipped, and whether they used the live feed or the sample. Session 3 adds sign-in, roles and an audit trail.
- **Source:** old 18

---

## Placeholders and things to verify before class
- Feed availability and robots.txt (checked 19 Nov 2026, one request each); site terms not reviewed.
- The slide 13 headline is a real 19 Nov item; it will be old news by class day. Replace it or keep it as a dated example.
- Proxy cost bands, the headless/headed test, the residential-network findings: 2026 snapshot from the scraping guide.
- Slide 16 rows are mock data.
- The practice prompt has not been rehearsed end to end.
