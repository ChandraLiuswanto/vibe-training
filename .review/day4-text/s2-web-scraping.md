# Session 2 — Web scraping

## 1. Your watchlist can show company news.

Financial App WatchlistBBCABBRIBMRI News panelHeadline · date · source 60mintalk60minpractice

**Notes:** Open the watchlist and pick a company. By the end of the practice hour, a panel next to it lists recent news that mentions that company, with a link back to each story. The first hour explains how that news gets collected and why some websites push back. The second hour you build it.

## 2. You learn how scraping works, then you build the news panel.

Reach dataFeeds, pages and browsersRead the replyWhat came back?Build the panelApprove, build and check

**Notes:** Three short chunks, then the lab. Chunk 1 is the order scrapers try things in. Chunk 2 is what happens when a website doesn't want to be scraped, and the tools people use against it. Chunk 3 is what we do in this course. Each chunk ends with a quick question.

## 3. A useful result shows a headline, a date and a source.

01HeadlineWhat the story is about 02DateWhen it was published 03SourceWhere to check it

**Notes:** Ask: if you saw a headline with no date and no source, what would you check before acting on it? A story might mention the company only in passing. Every row we save keeps all three, so anyone can click through and read the original.

## 4. A web page is built for people; a scraper picks out the few details your app needs.

News page→Scraper→Headline · date · link

**Notes:** A news page mixes stories with menus, ads and links to other sections. A scraper is a small program that reads the page and keeps only the fields the app needs. It doesn't copy the whole article. Pages change their layout, so a scraper needs tests and a clear message when it stops finding things.

## 5. Scrapers try the cheapest way to the data first.

1Feed or API2Data inside the page3Plain page request4Browser5AI extraction6Paid service

**Notes:** This is the order experienced scrapers follow. Each step down costs more, runs slower and breaks more often when the site changes. Most jobs finish on steps 1 to 3. A browser is a different way of showing up at a site; it isn't automatically stronger. Notice what isn't on the ladder: proxies and CAPTCHA tools. Those are what people reach for when a site blocks them, and that's the next chunk. Today's lab stays on step 1.

## 6. The data is often already in a feed or behind the page.

CNBC Market RSS · 19 Nov 2026Infobanknews API · 19 Nov 2026Page dataStructured fields can sit inside the page HTML.Plain request: read the page without opening a browser.

**Notes:** Step 1: an RSS feed is a list of the latest stories a site publishes for other programs: title, link and exact time. Many WordPress sites also answer a simple data request with the same fields. Step 2: even when there's no feed, the page often carries its data in a hidden block for search engines, called JSON-LD. A scraper reads that block instead of the layout. Step 3 is a plain request for the page and reading the layout itself: it works, but it can break when the layout changes. (API: a way for apps to request data.) Session 1's exchange-rate service was step 1 too. Each capture came from one request on 19 November with a training identity.

## 7. AI writes the scraper; plain code reads the pages.

Sample page→AI proposes fields or rules→Code checks results35 repair commits · 20 Oct–19 Nov 2026Compare paid services by cost per usable result.

**Notes:** Step 5. When pages are too messy for fixed rules, an AI model can read them. Sending every page to a model is slow and costly, so the smarter split is: the model reads one example and writes the extraction rules, and ordinary code applies them to thousands of pages. That's one approach, and our news scraper uses a version of it: when a site changes and the nightly check fails, an AI agent rewrites that one site's settings and has to show the site's check passing before the fix is kept. Its history has 35 commits labelled as these automated repairs between 20 October and 19 November 2026. Step 6. A common rule of thumb: a paid scraping service makes sense when keeping your own scraper working costs more than about two days a month. Compare price per thousand usable records, not per request, and don't trust the vendor's success-rate claims.

## 8. A site checks four things before it trusts a visitor.

Identity→Connection→Network→Request patternBefore fetching: check terms, robots guidance and internal approval. If blocked, stop.

**Notes:** Say the course rule first: before any live request we check the site's terms, its robots.txt and internal approval, and if a site blocks us we stop. This chunk explains what's happening when that happens, and what tools you'll hear vendors and AI agents suggest. Sites may consider several signals, usually these four. Who: the browser name your request announces. How: the technical handshake your software makes, which differs between Chrome and a Python script. Where: an office line, a home line, a phone network or a cloud server. Behave: speed and pattern, such as 50 pages in a second. Sites block when these disagree. A refusal does not tell you which signal mattered.

## 9. The site's reply code tells you what happened.

200 OKCheck what came back429Too many requests403Request refusedIn this lab: stop on 429 or 403. Keep saved results.

**Notes:** Every reply from a website starts with a three-digit code. 429 means you asked too often. In general, scrapers wait and ask less often; in our lab the app doesn't retry on its own: it stops, keeps the saved results, and you try again later by pressing Refresh. 403 means the site refused. The code doesn't say why: it could be the rules, the address or something about the request. Asking again won't change it.

## 10. A 200 reply can still be a failure.

200 OK→Inspect content→Reject the wrong replyChallenge or loginWrong pageMissing fieldsUnexpected formatOld copyCheck freshnessIllustrations · A valid feed with no matches is okay.

**Notes:** These are the expensive failures, because nothing crashes. The scraper "succeeds" and saves a check page, a page without the expected fields, a login page or a stale copy. The fix is to look at what came back: is it the feed we expected, with the fields we expect, and how many rows compared with last time? A sudden drop from 20 rows to 2 is worth a look. Careful: a real feed with no story about your company today is a valid result, "no matches". It's different from a reply that isn't the feed at all. The lab tests both.

## 11. A headless browser runs without a visible window.

HeadlessBrowser without a windowHeadedBrowser with a windowTempo: our configuration recorded a difference on 10 Nov 2026. A later check did not reproduce it.

**Notes:** Some pages only show their news after the browser runs the page's code. For those, scrapers drive a real browser. Headless means the browser runs without a window, controlled by a program. It's fast, but it leaves small traces that check scripts look for. Headed means a normal visible window.  The Tempo note comes from our scraper's settings on 10 November. On 19 November one load of the same page wasn't blocked either way. Blocks come and go, which is part of the cost.

## 12. A proxy changes where your request seems to come from.

Your app→Proxy→WebsiteTypeAddress comes fromDatacenterCloud serverISPISP-registered address hosted in a data centreResidentialHome connectionMobileCarrier networkOur fleet logged an Antara block on 20 Oct 2026.

**Notes:** A proxy is a middleman: your request goes out through someone else's internet address. Sites rate addresses: cloud servers look like bots, home and phone addresses look like people. It isn't a step on the ladder. People reach for one when the address is the reason for a block, and that's exactly the moment our course rule says stop. Prices in the 2026 guide run from cents per GB for datacenter to dollars per GB for residential and mobile; re-check before quoting. Residential addresses come from ordinary people's devices that share their connection, often through an app. A 2026 investigation found one such network carrying ad fraud and spam, and an FBI seizure found part of another was a botnet. The Antara case: 20 regional sites share one server, and our scraper's settings record a block within 15 minutes of a burst on 20 October; the configuration later changed. That's a record of one incident, not the site's stated policy. If time is short, skip the anecdotes and keep the table.

## 13. A CAPTCHA asks the visitor to prove it is human.

Google reCAPTCHA demo · 19 Nov 2026Risk scoreMay run without a puzzle.Just a moment…Browser check · IllustrationBisnis.com: checks recorded Sep–Nov 2026. In this lab, stop.

**Notes:** reCAPTCHA is Google's; Turnstile is Cloudflare's, and it often shows nothing at all: the page scores your behaviour in the background. A check page can arrive with code 200, which is the silent failure from three slides ago. Paid solving services exist; using them usually breaks the site's terms, and in this course the answer is no. On 19 November one load of Bisnis.com showed no check page; the callout records what our scraper saw on 27 September and 10 November.

## 14. Our own scraper shows how often sites push back.

454Enabled configurations122With extra browser or network settings332Without those settings19 Nov 2026 · Configuration snapshot

**Notes:** These are the settings of the news scraper we run, read on 19 November. 332 sites have none of these settings: they use feeds, sitemaps, data APIs or plain page requests. 122, about one in four, use something heavier, and a site can use more than one, so the numbers overlap. The settings show what the scraper is configured to do, not that each site needs it today. Every extra tool is another thing that breaks and another cost.

## 15. Knowing these tools is not permission: we check the rules and stop when blocked.

Site termsrobots.txtInternal approval Quiz: the news site blocks your request. What should the app do? A. Try again until it works B. Switch to a proxy C. Stop and show the last saved results

**Notes:** Three checks before any live request: the site's terms of use, its robots.txt file (the site's note to bots about where they may go), and approval inside the company. robots.txt isn't permission on its own. Some news sites name AI agents directly: on 19 November, Antara, Kontan and Republika named ClaudeBot. Do not change tools to work around a refusal. Robots.txt observations are from 19 November; terms have not been reviewed. Run the quiz: let two people argue A and B before revealing C.

## 16. A good scraper uses the cheapest door, checks what came back and stops when blocked.

RSS existsCheck permission. Use the feed.429Stop. Keep saved results.200: check pageStop. Report the challenge.

**Notes:** Read each scenario aloud and take an answer from the room before clicking. These are the three habits the lab needs: look for the cheapest door, read what actually came back, and stop when the site says no.

## 17. One feed item shows what to keep.

<title>→HeadlineBos BI Bawa Kabar Positif: Kredit Ngebut dan Pabrik Ngebul! <pubDate>→Date19 Nov 2026, 16:13 WIB <link>→Sourcecnbcindonesia.com Offline? Use the sample page.

**Notes:** This is a real item captured from the feed on 19 November. Point to how the feed already labels each field, so nothing has to be dug out of a page layout. The date is exact. A search page would only say "2 jam lalu" (two hours ago). We keep headline, date, link and the time we fetched it, never the full article. If the room has no internet or the source isn't approved, the sample feed and sample page have three made-up stories with the same fields.

## 18. Saved results feed the panel, and Refresh is the only fetch.

Feed→Saved results→News panelRefresh failed? Keep the last good results.

**Notes:** Opening the dashboard never contacts the news site; it shows what's saved. Only the Refresh button sends a request, and only one. If the refresh fails, the panel keeps the last good results and shows how old they are. The panel labels four states: sample, empty, stale and unavailable, and sample links can't be clicked. No background jobs, no automatic retries.

## 19. The agent proposes the work, and you approve each change.

1Plan the changes 2Show commands and files 3Wait for your “yes”

**Notes:** Paste the practice prompt into a coding agent. Read the files, commands and checks it proposes before approving, including any database change, which needs its own approval. The prompt asks the agent to wait; the tool's approval settings are what actually enforce it.

## 20. The dashboard shows mentions for one company at a time.

Financial AppMentions · BBCAfetched 10 min ago Headlinesourcepublished

**Notes:** Select one company in the mock dashboard. A story that mentions a company is only a mention, not a claim about the company. Show where the source, the published time and the fetch time appear, and what the panel says when the last refresh didn't work. The rows are placeholders. A feed may have no story about a given company today; pick a company with matches for the demo.

## 21. Text from a web page is data, even when it sounds like an instruction.

Instructionscome from your app Page text“Ignore your rules…” Show it as text, never follow it.

**Notes:** Point to the made-up teaser in the sample feed and ask who wrote it. The app received it from outside, so it can't tell the app or the chatbot what to do. Show it as plain text or leave it out. The tests prove it changes nothing.

## 22. The sample page helps you prove the scraper works.

Valid feedSample rows or no matchesBad replyWrong page or missing fieldsBlocked refreshKeep last good results

**Notes:** These are groups, not the full list; the handout and prompt stage 6 have every check: the three sample rows, no matches, changed layout or missing fields, a 403 or 429, a 200 that is really a "Just a moment…" page, duplicate refresh, keeping the saved results, one company's panel, and the teaser that tries to give orders. All run offline. Passing them shows the app handles these cases; it doesn't prove a live site will keep working.

## 23. The search-page comparison and the Wiki page are optional extras.

Stage 4Compare an approved search page with its feed.Stage 5Keep Wiki news separate from official rules.

**Notes:** Both are optional. Stage 4 shows why the feed was the cheaper door: the search page has fuzzy times, ads and repeated links. It uses a saved copy, or one approved live request. Stage 5 has its own approval step. Stage 5 gives the chatbot a labelled news page it can cite, kept apart from the official Wiki pages. Sample rows never go into the real Wiki.

## 24. In the lab, you build the scraper and news panel first.

00–10Plan 10–30Read the feed (or sample) 30–50Build the panel 50–60Show the checks

**Notes:** Start with the plan. Read the facilitator-approved feed, or the sample if offline. Wire the results into the news panel, then use the last ten minutes for checks. Extras only if time allows.

## 25. You finish by showing what works and what you couldn't verify.

Scrapershow the rows News panelshow one company Checkspassed, failed, blocked, not run Next → sign-in, roles and audit trail

**Notes:** Everyone shows the scraper's rows and the news panel for one company. Each person says which checks ran, which were skipped, and whether they used the live feed or the sample. Session 3 adds sign-in, roles and an audit trail.

## Browser word-count report

```text
Slide | words (final state) | steps | title
 1 |  21 | 0 | Your watchlist can show company news.
 2 |  20 | 0 | You learn how scraping works, then you build the news panel.
 3 |  23 | 0 | A useful result shows a headline, a date and a source.
 4 |   9 | 0 | A web page is built for people; a scraper picks out the few details your app needs.
 5 |  26 | 5 | Scrapers try the cheapest way to the data first.
 6 |  35 | 0 | The data is often already in a feed or behind the page.
 7 |  29 | 1 | AI writes the scraper; plain code reads the pages.
 8 |  22 | 0 | A site checks four things before it trusts a visitor.
 9 |  27 | 0 | The site's reply code tells you what happened.
10 |  32 | 0 | A 200 reply can still be a failure.
11 |  30 | 0 | A headless browser runs without a visible window.
12 |  37 (exception: essential reference table (proxy types)) | 0 | A proxy changes where your request seems to come from.
13 |  32 | 1 | A CAPTCHA asks the visitor to prove it is human.
14 |  23 | 0 | Our own scraper shows how often sites push back.
15 |  41 (exception: quiz choices) | 0 | Knowing these tools is not permission: we check the rules and stop when blocked.
16 |  22 | 3 | A good scraper uses the cheapest door, checks what came back and stops when blocked.
17 |  38 | 0 | One feed item shows what to keep.
18 |  17 | 1 | Saved results feed the panel, and Refresh is the only fetch.
19 |  20 | 0 | The agent proposes the work, and you approve each change.
20 |  14 | 0 | The dashboard shows mentions for one company at a time.
21 |  21 | 0 | Text from a web page is data, even when it sounds like an instruction.
22 |  27 | 0 | The sample page helps you prove the scraper works.
23 |  25 | 0 | The search-page comparison and the Wiki page are optional extras.
24 |  24 | 0 | In the lab, you build the scraper and news panel first.
25 |  27 | 0 | You finish by showing what works and what you couldn't verify.

Talk minutes: 56

PASS
```
