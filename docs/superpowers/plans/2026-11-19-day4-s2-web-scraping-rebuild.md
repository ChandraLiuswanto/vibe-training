# Day 4 · Session 2 — web-scraping deck rebuild (design + plan)

Status: round 1 shipped to `main` 2026-11-19 (`f9e2a23`, 20 slides). **Round 2 approved 2026-11-19, see §10**; it supersedes §5 and §8 where they differ.
Target: `decks/session-2-web-scraping-visual.html` (rewrite in place).
Branch: work on `main` and push to `origin/main` (owner: no PR).

## 1. Why

Participants are business users building the Financial App. The current deck teaches one feature (watchlist news from a fake saved page) and says "stop when blocked", but never explains how scraping works. The owner wants it more insightful: how real scrapers reach data, how sites detect and block them, and the tools people use against blocks (headless vs headed browsers, proxy types, CAPTCHA). Concepts, not code.

After the session a participant can tell what "use residential proxies" or "solve the CAPTCHA" means, roughly what it costs, and that it needs approval. They have also read a real news feed in their own app.

## 2. Goals, non-goals, anti-goals

- **Goals:** one connected story built on the web-scraping skill's "cheapest door first" ladder; status codes as "how you know you hit a wall" (a 200 can still be wrong); the four things a site checks; headless vs headed; the four proxy types; CAPTCHA and challenge pages; a lab that reads a real feed.
- **Non-goals:** the session-3 and VPS handouts; the stale Day 4 tools and docs left by PR #9; scraping a page behind a login; full article text.
- **Anti-goals:** the deck reads as a how-to for getting past blocks; prices, vendors or pass rates shown as current facts on slides; the "check the rules, stop when blocked" rule weakened.

## 3. Decisions (owner)

| Decision | Choice |
|---|---|
| Structure | B: rebuild the concept half around the ladder; build half trimmed |
| Talk length | stays 60 min (practice 60 min) |
| Output | single HTML file, not .pptx |
| Look | Swiss Modern shared with S1/S3: Archivo 800 + Nunito, off-white `#fafaf7`, ink `#101010`, red `#f30`; every slide gets a new layout and diagram |
| Depth | teach proxies, headless and CAPTCHA as concepts, not technical |
| Lab data | a real news source, RSS first; the saved sample stays as fallback |

## 4. Sources

### Fact source
The `web-scraping` skill (`~/trust-me-bro/skills/web-scraping/`: `SKILL.md`, `data-sources.md`, `blocked.md`, `proxies.md`, `production.md`), distilled from Asad Ikram's 2026 scraping guide. Dated items (prices, vendors, pass rates) go only in speaker notes, marked "2026 snapshot, re-check".

### Easy news sources for the lab
Checked live 2026-11-19 with `FinancialAppTraining/1.0 (classroom training exercise)`, one request each: 200, no challenge page. Each also runs "ok" without a browser or proxy in `~/news_api`.

| Source | Door | URL |
|---|---|---|
| **CNBC Indonesia Market (default)** | RSS, 100 items | https://www.cnbcindonesia.com/market/rss |
| Liputan6 Bisnis | RSS, 50 items | https://feed.liputan6.com/rss/bisnis |
| Antara Ekonomi Bursa | RSS, 20 items | https://www.antaranews.com/rss/ekonomi-bursa.xml |
| Pasardana | RSS | https://pasardana.id/rss |
| Media Indonesia | RSS | https://mediaindonesia.com/feed/all |
| Infobanknews | WordPress JSON | https://infobanknews.com/wp-json/wp/v2/posts?per_page=10 |
| Stockwatch | WordPress JSON | https://stockwatch.id/wp-json/wp/v2/posts?per_page=10 |
| IDX Channel Market | sitemap | https://www.idxchannel.com/market-news/sitemap.xml |
| Investor.id | sitemap | https://investor.id/sitemap_post.xml |
| EmitenNews | sitemap | https://www.emitennews.com/sitemap-current-1.xml |

- robots.txt of Antara, Kontan and Republika names ClaudeBot (Kontan and Republika also GPTBot). Pick a source whose robots.txt doesn't name the participants' agent.
- No site's terms of use were reviewed. The facilitator approves the source before class.
- Antara's category feeds cap at 20 items and some refresh only every few days (`~/news_api/sites/antaranews.toml`).

### Hard cases from `~/news_api` (speaker-note examples for slides 9–11)
- **Tempo:** Cloudflare 403s a headless browser on the index; only a headed browser works (config note, 2026-11-10).
- **Bisnis.com:** "Just a moment…" challenge 2026-09-27; Turnstile 403 2026-11-10; a client imitating Chrome's connection got through.
- **Antara regionals:** 20 sites share one server that drops the IP after a burst; now behind a proxy at low concurrency.
- **Pikiran Rakyat network:** 63 sites; Cloudflare challenges a plain script.
- **Fleet:** 520 configs; 111 need a browser or browser-like client, 67 a Cloudflare solver, 35 a proxy, 7 a headed browser.

## 5. Outline (approved)

| # | Title | Min | From |
|---|---|---|---|
| 1 | Your watchlist can show company news. | 2 | old 1 |
| 2 | The news panel builds on the app you already have. | 2 | old 2 |
| 3 | A useful result shows a headline, a date and a source. | 2 | old 3 |
| 4 | A web page is built for people; a scraper picks out the few details your app needs. | 3 | old 4+5 |
| 5 | Scrapers try the cheapest way to the data first. | 4 | new: ladder (feed/API → data inside page → plain request → browser → proxy → paid service) |
| 6 | The data is often already in a feed or behind the page. | 3 | new: RSS, sitemap, WordPress JSON; real examples from §4 |
| 7 | The site's reply code tells you what happened. | 3 | new: 429 slow down · 403 judged a bot · 200 can be a challenge or empty; quick check |
| 8 | A site checks four things before it trusts a visitor. | 3 | new: who you claim to be · how you connect · where from · how you behave |
| 9 | A hidden browser is easy to spot; a visible one gets further. | 3 | new: headless vs headed; Tempo example |
| 10 | A proxy changes where your request seems to come from. | 4 | new: datacenter · ISP · residential · mobile; Antara regionals example |
| 11 | A CAPTCHA asks the visitor to prove it is human. | 3 | new: puzzle, invisible score, challenge page; Bisnis.com example; solving services exist; in this course it means stop |
| 12 | Knowing these tools is not permission: we check the rules and stop when blocked. | 4 | old 6+7, keeps the quiz |
| 13 | One feed item shows what to keep. | 3 | old 8+11, now a real RSS item plus the sample fallback |
| 14 | Saved results feed the panel, and Refresh is the only fetch. | 3 | old 9+10 |
| 15 | The agent proposes the work, and you approve each change. | 3 | old 12 |
| 16 | The dashboard shows mentions for one company at a time. | 3 | old 13 |
| 17 | Text from a web page is data, even when it sounds like an instruction. | 3 | old 15 |
| 18 | The sample page helps you prove the scraper works. | 4 | old 16 |
| 19 | In the lab, you build the scraper and news panel first. | 2 | old 17 |
| 20 | You finish by showing what works and what you couldn't verify. | 1 | old 18 |

Total ≈ 58 min. Old 14 (optional Wiki/chatbot) leaves the deck; it stays as optional stage 5 in the prompt.

## 6. Constraints

- AGENTS.md: assertion titles; visible words ≤40 per slide (≤40 per reveal step, ≤60 on lab/instruction slides 18–20); per-slide report. The proxy table on slide 10 may exceed as an essential reference table (give the reason).
- Keep the file's shell: `<style>`, controls, notes panel, prompt modal, copy, downloads, print block, runtime script. Only slide content, order, new CSS, the prompt and the sample change.
- Body type ≥24px on the 1920×1080 stage; never shrink to fit. Mock screens labelled "Illustration". Reduced motion respected.

## 7. How the current file is built

- One `<style>` block (~145 KB); 18 `<section class="slide" data-title data-minutes>`; controls `#controls #notes #modal #toast`; `.print-prompts`; JSON `<script id="deck-data">` with `slides[] {title, eyebrow, notes, minutes, visual, actions}`, `prompts[]`, `pack`, `sample`; runtime script (nav, notes from `slides[i]`, prompt modal, copy, downloads, quiz `.quiz[data-answer][data-feedback]` → `.answer`).
- Section count and `slides[]` must stay in step.
- `tools/day4-deck-check.mjs` still points at old file names; it can't be used unchanged.

## 8. Tasks

### Task 1 — Copy deck · `docs/copy/day4-s2-web-scraping.md`
Per slide: title, eyebrow, visible copy, reveal steps, speaker notes with timing, source (skill file, `~/news_api` config, or old slide).
- Plain words; explain once each: headless, proxy, IP address, CAPTCHA, status code, RSS.
- Quick checks after each chunk: slide 7 (which code means "slow down"?), slide 12 (existing quiz).
- Polish with `clarity` (rewrite, slides medium), then the `writing-like-a-human` cut list. No "not X but Y", no kicker lines, no invented facts.
- **Gate: owner reviews the copy before Task 2.**

### Task 2 — Build script · `tools/build-s2-scraping.py`
Stdlib Python. Keeps the shell (§6), replaces sections and `slides[]` from a slide list in the script, writes the deck. Idempotent.
- Check first: feeding the current 18 slides back in gives a byte-identical file.

### Task 3 — Visual system
`/* s2 rebuild */` CSS block at the end of `<style>`, existing tokens and fonts only. Components: `ladder` (6 rungs, cost arrow), `codes` (3 status cards), `checks` (4 quadrants), `versus` (headless | headed browser frames), `proxy-table` (where / cost / fits / breaks), `captcha` (puzzle, score meter, "Just a moment…" page), `rule` (3 checks + stop path), `feed-item` (real RSS item mapped to fields). Reveal steps `[data-step]` on next/prev; extend the runtime only if needed, keeping keyboard, touch and wheel behaviour.

### Task 4 — Slides 1–12
New visuals and copy through the build script. Reuse old 1–3 SVGs where the copy is unchanged.

### Task 5 — Slides 13–20
Port old 8+11 → 13, 9+10 → 14, 12 → 15, 13 → 16, 15 → 17, 16 → 18, 17 → 19, 18 → 20 with their buttons and actions. Drop old 14.

### Task 6 — Practice prompt and sample
- Stage 2 reads one facilitator-approved feed from §4 (RSS or WordPress JSON), filters items by the selected company name or ticker, stores headline, link, source, exact publish date and fetch time. Fall back to `sample-news-page.html` when offline or not approved.
- Stage 4 (optional): compare the same company on the site's search page and note what the feed saved (fuzzy "2 jam lalu" times, layout parsing).
- Keep: honest request identity, one request per Refresh with timeout and size limit, stop on 403/429/CAPTCHA/challenge-as-200, no bypasses, no full article text, page text treated as data.
- Sample page: keep the three fictional cards (incl. the injection teaser); add one RSS-shaped sample file so offline tests cover the feed path.
- Update `pack`, the print block and the help dialog to match.

### Task 7 — Verify · `tools/s2-scraping-check.mjs`
playwright-core from `tools/deck-check/node_modules`, local Chrome:
1. 20 sections = 20 `slides[]`; titles match and end with "."
2. Visible words per slide and per reveal step vs budget (same `collect()` rules as `day4-deck-check.mjs`).
3. No overflow at 1920×1080 and 1280×720, including inside `overflow:hidden` boxes and under the control bar.
4. Every reveal step forward and back; quizzes set `.answer`.
5. Prompt modal, copy, both downloads, print view.
6. No external requests.
7. Sum of `data-minutes` 55–60.
Screenshot every click state at 1920 and phone width into `.scratch/s2-rebuild/` and look at each one.
Prompt check: dry-run stage 2 against the default feed once (one request) and against the RSS sample offline.

### Task 8 — Review, report, commit
- Independent review against this doc and AGENTS.md.
- Text dump to `.review/day4-text/s2-web-scraping.md`.
- Report: per slide title, word count, budget exceptions with reasons; placeholders (proxy cost bands, CAPTCHA kinds, mock-ups, source terms not reviewed, prompt not rehearsed end to end).
- Commit on `day4-s2-scraping-rebuild`; owner decides on PR.

## 9. Open
- No extra "Diagnose the scraper" exercise (owner skipped it 2026-11-19); the two quick checks on slides 7 and 12 stay.
- Session 3 handout and the stale Day 4 tools still use the old numbering (out of scope here).

## 10. Round 2 (owner approved 2026-11-19)

Owner review of round 1: "still missing a lot of parts". Owner chose **fix all** of the gaps below, approved the 25-slide outline, and asked for better visuals: **moving diagrams** and **real screenshots**. Handout: **overwrite** `handouts/session-2-participant-sheet.html` (leave session-3 / VPS sheets alone).

### 10.1 Gaps fixed

| # | Gap in round 1 | Fix |
|---|---|---|
| 1 | Ladder wrong vs the skill: "Proxy" at rung 5, AI extraction missing | Skill's ladder: feed/API → data inside page → plain request → browser → AI reads messy pages → paid service. Proxies move to the "when blocked" chunk as a fix, not a rung |
| 2 | `~/news_api` real cases only in notes | Visible dated callouts on slides 11–13 and a fleet slide (14) |
| 3 | Rungs 2, 3, 6 never explained | Slide 6 covers 1–3 with real captures; slide 7 covers 5–6 |
| 4 | No silent-failure visual | New slide 10: a 200 that is a challenge page, empty list, login wall or stale copy |
| 5 | Static boxes; old deck had moving SVG flows | Moving request diagrams (see 10.3) and real screenshots (10.4) |
| 6 | Seven talking slides, one check, no recap | Agenda (2), recap with a 3-scenario check before the lab (16) |
| 7 | Prompt stages 4–5 had no slide; no stage-2 button | Slide 23 (extras); stage-2 button on slide 17 |
| 8 | Handout still access control | New session-2 participant sheet for the scraping lab |

### 10.2 Outline (supersedes §5)

| # | Title | Min | Visual |
|---|---|---|---|
| 1 | Your watchlist can show company news. | 2 | app mock |
| 2 | Today: how scraping works, then you build the news panel. | 1 | agenda: 3 chunks + lab |
| 3 | A useful result shows a headline, a date and a source. | 2 | three fields |
| 4 | A web page is built for people; a scraper picks out the few details your app needs. | 2 | moving: page → scraper → 3 fields |
| 5 | Scrapers try the cheapest way to the data first. | 3 | ladder, 6 rungs, builds one per click; cost arrow |
| 6 | The data is often already in a feed or behind the page. | 3 | real captures: CNBC RSS, Infobanknews WordPress JSON, JSON-LD in CNBC page source |
| 7 | AI writes the scraper; plain code reads the pages. | 3 | moving: page → AI (once) → rules → code reads every page; repair-agent fact; paid-service rule |
| 8 | A site checks four things before it trusts a visitor. | 2 | moving: request passes four gates |
| 9 | The site's reply code tells you what happened. | 2 | moving: request → site → 200 / 429 / 403 |
| 10 | A 200 reply can still be a failure. | 3 | four mock replies (challenge, empty, login, stale), labelled Illustration |
| 11 | A hidden browser is easy to spot; a visible one gets further. | 2 | headless vs headed side by side; Tempo dated callout |
| 12 | A proxy changes where your request seems to come from. | 3 | moving: you → proxy → site; table; Antara regionals callout |
| 13 | A CAPTCHA asks the visitor to prove it is human. | 2 | real reCAPTCHA demo capture + "Just a moment…" Illustration; Bisnis.com dated callout |
| 14 | Our own scraper shows how often sites push back. | 2 | fleet bar: 454 live sites, 122 need a browser, proxy or solver |
| 15 | Knowing these tools is not permission: we check the rules and stop when blocked. | 3 | three checks + quiz |
| 16 | Before you build: cheapest door first, read what came back, stop when blocked. | 3 | recap + 3 scenarios, answers revealed per click |
| 17 | One feed item shows what to keep. | 3 | real RSS item mapped to fields; stage 2 button |
| 18 | Saved results feed the panel, and Refresh is the only fetch. | 2 | moving: feed → saved → panel; refresh fail path |
| 19 | The agent proposes the work, and you approve each change. | 2 | 3 steps |
| 20 | The dashboard shows mentions for one company at a time. | 2 | dashboard mock |
| 21 | Text from a web page is data, even when it sounds like an instruction. | 2 | two columns |
| 22 | The sample page helps you prove the scraper works. | 3 | four checks |
| 23 | Extras: compare the search page, then add news to the Wiki. | 2 | stage 4 and 5 cards with buttons |
| 24 | In the lab, you build the scraper and news panel first. | 1 | timeline |
| 25 | You finish by showing what works and what you couldn't verify. | 1 | finish check |

Total 57 min.

### 10.3 Moving diagrams
- Inline SVG, one request "packet" travelling along a path (CSS `offset-path`, the mechanism the old deck used). Starts when the slide becomes active; plays a few times, then rests in its final state so the slide is readable when still.
- Meaning only: the packet is a request; red stop marks a block. No decorative motion.
- `prefers-reduced-motion` and print: no motion, final state shown.
- Swiss Modern tokens only.

### 10.4 Real screenshots
- Captured 2026-11-19, one page load each with `FinancialAppTraining/1.0 (classroom training exercise)`, cropped and embedded as base64 (no external requests). Each carries a "Captured 19 Nov 2026 · source" label.
- Usable: CNBC Market RSS, Infobanknews WordPress JSON, JSON-LD in the CNBC Market page source, Google's public reCAPTCHA demo.
- Not reproducible today: Bisnis.com showed no challenge and Tempo's index returned the same page headless and headed (one load each, no retries). Those stay as dated callouts from `~/news_api` configs ("Sept/Nov 2026, our scraper saw…"), never as current facts; the "Just a moment…" page is a labelled Illustration.
- Keep the deck size reasonable: JPEG/PNG crops, target < 1.2 MB total.

### 10.5 Tasks (round 2)
1. Copy deck update: rewrite `docs/copy/day4-s2-web-scraping.md` for the 25-slide outline (same rules as Task 1; clarity + writing-like-a-human). Fix round-1 notes that state the Tempo case as current.
2. Captures: crop the four screenshots, plus a JSON-LD source view; save under `.scratch/`, embed via the build script.
3. Build: extend `tools/build_s2_scraping.py` (slides, moving-diagram helper, image embedding, new CSS). Keep the round-trip shell and runtime patches.
4. Check: update `tools/s2-scraping-check.mjs` for 25 slides, the copy deck titles, image labels, reduced-motion final state, deck size, and slide 16's per-click answers.
5. Look at every click state at 1920 and 1280; fix what the check can't see.
6. Handout: rewrite `handouts/session-2-participant-sheet.html` (two A4 pages, same frame as the other sheets): page 1 the six prompt stages with "what you approve / good result / call the facilitator if"; page 2 the approved feeds, the stop rules (403, 429, CAPTCHA, challenge-as-200), and the four tests.
7. Refresh `.review/day4-text/s2-web-scraping.md`; update the README row for decks and handouts that PR #9 left stale for Session 2 only.
8. Commit on `main`, push to `origin/main`, Taildrop the deck and handout to `oppo-reno15-5g`.

### 10.6 Placeholders to report
Screenshots age (dated labels); fleet numbers are a 2026-11-19 snapshot of `~/news_api` configs; Tempo/Bisnis.com cases are past observations not reproduced today; proxy cost bands and the headless test are the 2026 guide's snapshot; prompt not rehearsed end to end.
