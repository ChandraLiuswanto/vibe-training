# Session 2 — Web scraping

## 1. Your watchlist can show company news.

Financial App WatchlistBBCABBRIBMRI News panelHeadline · date · source 60mintalk60minpractice

**Notes:** Open the watchlist and pick a company. By the end of the practice hour, a panel next to it lists recent news that mentions that company, with a link back to each story. The first hour explains how that news gets collected and why some websites push back. The second hour you build it.

## 2. You learn how scraping works, then you build the news panel.

Reach dataFeeds, pages and browsersRead the replyWhat came back?Build the panelApprove, build and check

**Notes:** Three short chunks, then the lab. Chunk 1 is the order scrapers try things in. Chunk 2 is what happens when a website doesn't want to be scraped, and the tools people use against it. Chunk 3 is what we do in this course. Each chunk ends with a quick question.

## 3. The news panel links to the article without copying its body.

Publisher’s articleHeadline · Date · Article bodyThe full story stays on the publisher’s site.Watchlist cardHeadline · Date · SourceRead the full article ↗

**Notes:** Point to the body on the left: that is the full story. The watchlist helps someone decide whether to open it. We save the headline, date, source and link; the publisher keeps the article body.

## 4. A scraper turns a news page into a row your app can use.

What a person seesMenu · AdvertisementBank opens a new branch · 19 NovFull article body…What the app keepsBank opens a new branch19 Nov · Example News · Article link

**Notes:** Say: “A person sees a whole page. Our app needs one record per story.” Point to the menu, ad and article body on the left. Then point to the headline, date and link on the right. Those fields become one row. The example article is fictional.

## 5. Scrapers try the cheapest way to the data first.

1Feed or API2Data inside the page3Plain page request4Browser5AI extraction6Paid service

**Notes:** This is the order experienced scrapers follow. Each step down costs more, runs slower and breaks more often when the site changes. Most jobs finish on steps 1 to 3. A browser is a different way of showing up at a site; it isn't automatically stronger. Notice what isn't on the ladder: proxies and CAPTCHA tools. Those are what people reach for when a site blocks them, and that's the next chunk. Today's lab stays on step 1.

## 6. The data is often already in a feed or behind the page.

CNBC Market RSS · 19 Nov 2026Infobanknews API · 19 Nov 2026Page dataStructured fields can sit inside the page HTML.Plain request: read the page without opening a browser.

**Notes:** Step 1: an RSS feed is a list of the latest stories a site publishes for other programs: title, link and exact time. Many WordPress sites also answer a simple data request with the same fields. Step 2: even when there's no feed, the page often carries its data in a hidden block for search engines, called JSON-LD. A scraper reads that block instead of the layout. Step 3 is a plain request for the page and reading the layout itself: it works, but it can break when the layout changes. (API: a way for apps to request data.) Session 1's exchange-rate service was step 1 too. Each capture came from one request on 19 November with a training identity.

## 7. AI can suggest what to extract, and code checks the result.

Sample page“Bank opens a new branch”AI suggestsUse the title in each news card.Code verifiesRead the title. Flag it if missing.

**Notes:** Point to the fictional headline on slide 4. Ask: “Where is the headline in this news card?” AI can suggest a rule for finding it. Code uses the rule on the next card and flags a missing value. The lab uses the feed’s named fields, so it does not need AI to read each item. If you buy a service, compare the cost per usable result.

## 8. Sites can consider four kinds of signals when a request arrives.

1 · IdentityWhat software the request says it uses.2 · ConnectionHow the software starts the connection.3 · NetworkWhere the request comes from.4 · BehaviorHow often it sends requests.

**Notes:** Walk through the cards one at a time. Identity is what software the request says it uses. Connection is how that software starts talking to the server. Network is where a request comes from, such as a company or cloud network. Behavior is how often requests arrive. A refusal does not tell you which signal mattered.

## 9. An HTTP status code tells you how the server answered.

An HTTP status code is a three-digit number in the server’s reply.200 · OKThe request succeeded. Check the content.403 · ForbiddenThe server refuses the request.429 · Too Many RequestsThe server is limiting requests.

**Notes:** An HTTP status code is a three-digit number sent with a server reply. 200 means the request succeeded, not that the body contains what you wanted. 403 means the server refused it. 429 means the server is limiting requests. The next slide compares two replies with the same code.

## 10. Two replies can both say 200 OK and contain different things.

200 OK<rss> … <item>Expected feed · Read the items.200 OKJust a moment…Check page · Stop. Keep saved results.Illustration · Same status code, different content.

**Notes:** Read the response body as well as the code. On the left, the app got the feed it expected, so it can read the items. A valid feed can have no matching stories. On the right, it got a browser check instead of a feed. Stop and keep the saved results. Both replies are illustrations.

## 11. Headed browsers show a window, and headless browsers run without one.

HeadedVisible windowBrowser → Web pageUseful when you want to watch the page load.HeadlessNo visible windowBrowser → Web pageUseful for automated checks without a display.

**Notes:** Both are browsers and can run page JavaScript. A headed browser is useful when you want to watch the page load. A headless browser can run automated checks without a display. Neither changes whether the site has granted permission.

## 12. A proxy changes where your request seems to come from.

Your appProxyWebsite Sees the proxy’s address DatacenterCloud serverISPISP-registered addressResidentialHome connectionMobileCarrier network

**Notes:** A proxy is a middleman: your request goes out through someone else's internet address. Sites rate addresses: cloud servers look like bots, home and phone addresses look like people. It isn't a step on the ladder. People reach for one when the address is the reason for a block, and that's exactly the moment our course rule says stop. Prices in the 2026 guide run from cents per GB for datacenter to dollars per GB for residential and mobile; re-check before quoting. Residential addresses come from ordinary people's devices that share their connection, often through an app. A 2026 investigation found one such network carrying ad fraud and spam, and an FBI seizure found part of another was a botnet. The Antara case: 20 regional sites share one server, and our scraper's settings record a block within 15 minutes of a burst on 20 October; the configuration later changed. That's a record of one incident, not the site's stated policy. If time is short, skip the anecdotes and keep the table.

## 13. A CAPTCHA asks the visitor to prove it is human.

Google reCAPTCHA demo · 19 Nov 2026Risk scoreMay run without a puzzle.Just a moment…Browser check · IllustrationBisnis.com: checks recorded Sep–Nov 2026. In this lab, stop.

**Notes:** reCAPTCHA is Google's; Turnstile is Cloudflare's, and it often shows nothing at all: the page scores your behaviour in the background. A check page can arrive with code 200, which is the silent failure from three slides ago. Paid solving services exist; using them usually breaks the site's terms, and in this course the answer is no. On 19 November one load of Bisnis.com showed no check page; the callout records what our scraper saw on 27 September and 10 November.

## 14. We check permission before fetching and stop if blocked.

TermsCheck the site’s terms.Robots guidanceCheck the exact route.Internal approvalAsk before using a live source.If blocked, stop and keep the last good results.

**Notes:** Review the terms and robots guidance for the exact route. Get internal approval before any live request. If blocked, stop, keep the last good results and report what happened. Do not change tools to get around it.

## 15. A good scraper uses the cheapest door, checks what came back and stops when blocked.

RSS existsCheck permission. Use the feed.429Stop. Keep saved results.200: check pageStop. Report the challenge.

**Notes:** Read each scenario aloud and take an answer from the room before clicking. These are the three habits the lab needs: look for the cheapest door, read what actually came back, and stop when the site says no.

## 16. One feed item shows what to keep.

<title>→HeadlineBos BI Bawa Kabar Positif: Kredit Ngebut dan Pabrik Ngebul! <pubDate>→Date19 Nov 2026, 16:13 WIB <link>→Sourcecnbcindonesia.com Offline? Use the sample page. · Stage 2 ↗Download sample feed ↓

**Notes:** This is a real item captured from the feed on 19 November. Point to how the feed already labels each field, so nothing has to be dug out of a page layout. The date is exact. A search page would only say "2 jam lalu" (two hours ago). We keep headline, date, link and the time we fetched it, never the full article. If the room has no internet or the source isn't approved, the sample feed and sample page have three made-up stories with the same fields.

## 17. The agent proposes the work, and you approve each change.

1Plan the changes 2Show commands and files 3Wait for your “yes” · The prompt · stage 1 ↗

**Notes:** Paste the practice prompt into a coding agent. Read the files, commands and checks it proposes before approving, including any database change, which needs its own approval. The prompt asks the agent to wait; the tool's approval settings are what actually enforce it.

## 18. The dashboard shows mentions for one company at a time.

Financial AppMentions · BBCAfetched 10 min ago Headlinesourcepublished

**Notes:** Select one company in the mock dashboard. A story that mentions a company is only a mention, not a claim about the company. Show where the source, the published time and the fetch time appear, and what the panel says when the last refresh didn't work. The rows are placeholders. A feed may have no story about a given company today; pick a company with matches for the demo.

## 19. Text from a web page is data, even when it sounds like an instruction.

Instructionscome from your app Page text“Ignore your rules…” Show it as text, never follow it.

**Notes:** Point to the made-up teaser in the sample feed and ask who wrote it. The app received it from outside, so it can't tell the app or the chatbot what to do. Show it as plain text or leave it out. The tests prove it changes nothing.

## 20. The sample page helps you prove the scraper works.

Valid feedSample rows or no matchesBad replyWrong page or missing fieldsBlocked refreshKeep last good results · Stage 6 ↗

**Notes:** These are groups, not the full list; the handout and prompt stage 6 have every check: the three sample rows, no matches, changed layout or missing fields, a 403 or 429, a 200 that is really a "Just a moment…" page, duplicate refresh, keeping the saved results, one company's panel, and the teaser that tries to give orders. All run offline. Passing them shows the app handles these cases; it doesn't prove a live site will keep working.

## 21. The search-page comparison and the Wiki page are optional extras.

Stage 4Compare an approved search page with its feed.Stage 5Keep Wiki news separate from official rules. · Stages 4–5 ↗

**Notes:** Both are optional. Stage 4 shows why the feed was the cheaper door: the search page has fuzzy times, ads and repeated links. It uses a saved copy, or one approved live request. Stage 5 has its own approval step. Stage 5 gives the chatbot a labelled news page it can cite, kept apart from the official Wiki pages. Sample rows never go into the real Wiki.

## 22. In the lab, you build the scraper and news panel first.

00–10Plan 10–30Read the feed (or sample) 30–50Build the panel 50–60Show the checks · Open the prompt ↗Setup help ↗

**Notes:** Start with the plan. Read the facilitator-approved feed, or the sample if offline. Wire the results into the news panel, then use the last ten minutes for checks. Extras only if time allows.

## 23. You finish by showing what works and what you couldn't verify.

Scrapershow the rows News panelshow one company Checkspassed, failed, blocked, not run Next → sign-in, roles and audit trail · The prompt · finish check ↗

**Notes:** Everyone shows the scraper's rows and the news panel for one company. Each person says which checks ran, which were skipped, and whether they used the live feed or the sample. Session 3 adds sign-in, roles and an audit trail.

## Browser word-count report

```text
Slide | words (final state) | steps | title
 1 |  21 | 0 | Your watchlist can show company news.
 2 |  20 | 0 | You learn how scraping works, then you build the news panel.
 3 |  27 | 0 | The news panel links to the article without copying its body.
 4 |  34 | 0 | A scraper turns a news page into a row your app can use.
 5 |  26 | 0 | Scrapers try the cheapest way to the data first.
 6 |  35 | 0 | The data is often already in a feed or behind the page.
 7 |  29 | 0 | AI can suggest what to extract, and code checks the result.
 8 |  36 | 0 | Sites can consider four kinds of signals when a request arrives.
 9 |  39 | 0 | An HTTP status code tells you how the server answered.
10 |  28 | 0 | Two replies can both say 200 OK and contain different things.
11 |  32 | 0 | Headed browsers show a window, and headless browsers run without one.
12 |  22 | 0 | A proxy changes where your request seems to come from.
13 |  32 | 1 | A CAPTCHA asks the visitor to prove it is human.
14 |  33 | 0 | We check permission before fetching and stop if blocked.
15 |  22 | 3 | A good scraper uses the cheapest door, checks what came back and stops when blocked.
16 |  38 | 0 | One feed item shows what to keep.
17 |  20 | 0 | The agent proposes the work, and you approve each change.
18 |  14 | 0 | The dashboard shows mentions for one company at a time.
19 |  21 | 0 | Text from a web page is data, even when it sounds like an instruction.
20 |  27 | 0 | The sample page helps you prove the scraper works.
21 |  25 | 0 | The search-page comparison and the Wiki page are optional extras.
22 |  24 | 0 | In the lab, you build the scraper and news panel first.
23 |  27 | 0 | You finish by showing what works and what you couldn't verify.

Talk minutes: 55

PASS
```
