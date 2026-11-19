# Day 4 · Session 2 — web-scraping deck rebuild (design + plan)

Status: approved by owner 2026-11-19 (approach, outline, sources). Copy deck still needs owner review (Task 1 gate).
Target: `decks/session-2-web-scraping-visual.html` (rewrite in place; merged in PR #9).
Branch: `day4-s2-scraping-rebuild` (create from `main`).

## 1. Why

Participants are business users building the Financial App. The current deck teaches one feature (watchlist news from a fake saved page) and says "stop when blocked", but never explains how scraping works. The owner wants it more insightful: how real scrapers reach data, how sites detect and block them, and the tools people use against blocks (headless vs headed browsers, proxy types, CAPTCHA). Concepts, not code.

After the session a participant can tell what "use residential proxies" or "solve the CAPTCHA" means, roughly what it costs, and that it needs approval. They have also read a real news feed in their own app.

## 2. Goals, non-goals, anti-goals

- **Goals:** one connected story built on the web-scraping skill's "cheapest door first" ladder; status codes as "how you know you hit a wall" (a 200 can still be wrong); the four things a site checks; headless vs headed; the four proxy types; CAPTCHA and challenge pages; a lab that reads a real feed.
- **Non-goals:** handouts; the stale Day 4 tools and docs left by PR #9; scraping a page behind a login; full article text.
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
