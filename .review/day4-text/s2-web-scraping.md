# s2 — decks/session-2-web-scraping-visual.html

## Slide 1: Your watchlist can show company news.

- Eyebrow: SESSION 2 · WEB SCRAPING
- Minutes: 2
- Reveal steps: 0

**Visible text (all steps)**

```text
Financial App Watchlist BBCA BBRI BMRI News panel Headline · date · source 60min talk 60min practice 
```

**Speaker notes**

Open the watchlist and pick a company. By the end of the practice hour, a panel under it lists recent news that mentions that company, with a link back to where each story came from. The first hour explains how that news gets collected and why some websites push back. The second hour you build it. (2 min)

## Slide 2: The news panel builds on the app you already have.

- Eyebrow: 
- Minutes: 2
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Ask the room to name what they already have: the stock dashboard, the database, the Wiki, the chatbot and the exchange-rate feature from Session 1. Nothing gets replaced. The news panel reads which company is selected and shows its own list. (2 min)

## Slide 3: A useful result shows a headline, a date and a source.

- Eyebrow: 
- Minutes: 2
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Ask: if you saw a headline with no date and no source, what would you check before acting on it? A story might mention the company only in passing. Every row we save keeps all three, so anyone can click through and read the original. (2 min)

## Slide 4: A web page is built for people; a scraper picks out the few details your app needs.

- Eyebrow: 
- Minutes: 3
- Reveal steps: 2

**Visible text (all steps)**

```text
 
```

**Speaker notes**

A news page mixes stories with menus, ads and links to other sections. A scraper is a small program that reads the page and keeps only the fields the app needs. It doesn't copy the whole article. Pages change their layout, so a scraper needs tests and a clear message when it stops finding things. Click once to show what the scraper keeps. (3 min)

## Slide 5: Scrapers try the cheapest way to the data first.

- Eyebrow: 
- Minutes: 4
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

This is the order experienced scrapers follow. Each step down costs more, runs slower and breaks more often when the site changes. Most jobs finish on steps 1 to 3. A browser is a different way of showing up at the site; it isn't automatically stronger. A paid service starts to make sense when fixing your own scraper takes more than a couple of days a month. Today we stay on step 1. (4 min)

## Slide 6: The data is often already in a feed or behind the page.

- Eyebrow: 
- Minutes: 3
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

An RSS feed is a list of the latest stories that the site publishes for other programs to read: title, link and exact time. Many sites built on WordPress also answer a simple data request. A sitemap lists every page so search engines can find them. Session 1's exchange-rate service worked the same way: labelled data for software, not a page for people. Each of these returned a normal answer on 19 November to one request from a training identity. That can change; the facilitator checks again before class. (3 min)

## Slide 7: The site's reply code tells you what happened.

- Eyebrow: 
- Minutes: 3
- Reveal steps: 1

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Every reply from a website starts with a three-digit code. 429 is a negotiation: you asked too often, so wait and ask less often. 403 is a judgement: something about your request looked wrong, and asking faster won't help. And 200 doesn't always mean success. A 200 can carry an empty list, a login page or a "Just a moment…" check page instead of the news. The lab's tests look at what came back as well as the code. Ask the question, take two answers, then click to reveal. (3 min)

## Slide 8: A site checks four things before it trusts a visitor.

- Eyebrow: 
- Minutes: 3
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Who: the browser name your request announces. How: the technical handshake your software makes, which differs between Chrome and a Python script. Where: an office line, a home line, a phone network or a cloud server. Behave: speed and pattern, such as 50 pages in a second. Sites block when these disagree. A request that says "I'm Chrome" but connects like a script from a cloud server gets stopped before the page loads. (3 min)

## Slide 9: A hidden browser is easy to spot; a visible one gets further.

- Eyebrow: 
- Minutes: 3
- Reveal steps: 1

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Some pages only show their news after the browser runs the page's code. For those, scrapers drive a real browser. Headless means the browser runs without a window, controlled by a program. It's fast, but it leaves small traces that check scripts look for. Headed means a normal visible window. In one 2026 test, a plain automated browser was blocked on five protected sites when headless, and got into four of them when headed. Real example from our news scraper (November 2026): Tempo's index page blocks a headless browser and only works with a visible one. 2026 snapshot, re-check. Click to show the headed side. (3 min)

## Slide 10: A proxy changes where your request seems to come from.

- Eyebrow: 
- Minutes: 4
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

A proxy is a middleman: your request goes through someone else's internet address. Sites rate addresses: cloud servers look like bots, home and phone addresses look like people. Prices in the 2026 guide run from cents per GB for datacenter to dollars per GB for residential and mobile; re-check before quoting. Residential addresses come from ordinary people's devices that share their connection, often through an app. A 2026 investigation found one such network carrying ad fraud and spam traffic, and an FBI seizure found part of another was a botnet. Real example: our news scraper sends all Antara regional sites through a proxy, because their shared server drops an address after a burst of requests. (4 min)

## Slide 11: A CAPTCHA asks the visitor to prove it is human.

- Eyebrow: 
- Minutes: 3
- Reveal steps: 1

**Visible text (all steps)**

```text
 
```

**Speaker notes**

reCAPTCHA is Google's version; Turnstile is Cloudflare's. The newer kinds often show nothing at all: the page scores your behaviour in the background. A check page usually arrives with code 200, which is why a scraper can "succeed" and save a page of nothing. Paid solving services exist and are cheap, and using them usually breaks the site's terms. Real example: Bisnis.com showed our news scraper a "Just a moment…" page in September and a Turnstile block in November. Click to show the course rule. (3 min)

## Slide 12: Knowing these tools is not permission: we check the rules and stop when blocked.

- Eyebrow: 
- Minutes: 4
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Three checks before any live request: the site's terms of use, its robots.txt file (the site's note to bots about where they may go), and approval inside the company. robots.txt isn't permission on its own. Some news sites name AI agents directly: on 19 November, Antara, Kontan and Republika named ClaudeBot. Proxies and solvers are how people get past a "no". Whether to do that is decided by the business and legal teams, before anyone writes code. Run the quiz: let two people argue A and B before revealing C. (4 min)

## Slide 13: One feed item shows what to keep.

- Eyebrow: 
- Minutes: 3
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

This is a real item captured from the feed on 19 November. Point to how the feed already labels each field, so nothing has to be dug out of a page layout. The date is exact. A search page would only say "2 jam lalu" (two hours ago). We keep headline, date, link and the time we fetched it, never the full article. If the room has no internet or the source isn't approved, the downloadable sample page and sample feed have three made-up stories with the same fields. (3 min)

## Slide 14: Saved results feed the panel, and Refresh is the only fetch.

- Eyebrow: 
- Minutes: 3
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Opening the dashboard never contacts the news site; it shows what's saved. Only the Refresh button sends a request, and only one. If the refresh fails, the panel keeps the last good results and shows how old they are. No background jobs, no automatic retries. (3 min)

## Slide 15: The agent proposes the work, and you approve each change.

- Eyebrow: 
- Minutes: 3
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Paste the practice prompt into a coding agent. Read the files, commands and checks it proposes before approving. The prompt asks the agent to wait; the tool's approval settings are what actually enforce it. (3 min)

## Slide 16: The dashboard shows mentions for one company at a time.

- Eyebrow: 
- Minutes: 3
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Select one company in the mock dashboard. A story that mentions a company is only a mention, not a claim about the company. Show where the source, the published time and the fetch time appear, and what the panel says when the last refresh didn't work. The rows are placeholders, not real headlines. (3 min)

## Slide 17: Text from a web page is data, even when it sounds like an instruction.

- Eyebrow: 
- Minutes: 3
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Point to the made-up teaser in the sample page and ask who wrote it. The app received it from outside, so it can't tell the app or the chatbot what to do. Show it as plain text or leave it out. The tests prove it changes nothing. (3 min)

## Slide 18: The sample page helps you prove the scraper works.

- Eyebrow: 
- Minutes: 4
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Start with the three expected sample rows. Then test no matches, a changed page layout and a blocked refresh, all offline. An empty result and a scraper that no longer recognises the page look alike; the tests tell them apart. If an update fails, the last good results stay visible. (4 min)

## Slide 19: In the lab, you build the scraper and news panel first.

- Eyebrow: 
- Minutes: 2
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Start with the plan. Read the facilitator-approved feed, or the sample if offline. Wire the results into the news panel, then use the last ten minutes for checks. The search-page comparison and the Wiki are extras if time allows. (2 min)

## Slide 20: You finish by showing what works and what you couldn't verify.

- Eyebrow: 
- Minutes: 1
- Reveal steps: 0

**Visible text (all steps)**

```text
 
```

**Speaker notes**

Everyone shows the scraper's rows and the news panel for one company. Each person says which checks ran, which were skipped, and whether they used the live feed or the sample. Session 3 adds sign-in, roles and an audit trail. (1 min)
