# VPS Providers Pricing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the `VPS Providers` sheet of `budgetting.xlsx` so every row is one provider, plan and location with the price the provider's website shows for it, and add the providers commonly used in Indonesia.

**Architecture:** `tools/build_budget.py` holds the data as a list of `Offer` records and writes the sheet with openpyxl; USD figures and row order are computed, never typed. `tools/check_budget.py` asserts the sheet against the data and the spec's rules. Each confirmed price has a line in an evidence file, so a reviewer can re-open the page and compare.

**Tech Stack:** Python 3.12, openpyxl 3.1.5, `curl` for reading pricing pages and public pricing APIs.

**Spec:** `docs/superpowers/specs/2026-11-17-vps-providers-pricing-design.md`

## Global Constraints
- Target size is 16 vCPU / 64 GB. A provider with nothing that size gets its closest plan, with Fits = `No (reason)`.
- A location cell names exactly one place. It never contains `/` or `(surcharge)`.
- The price in a row is the website price for that plan in that location, including any location surcharge. One-off fees go in Notes with the amount.
- A price is `Confirmed` only when read from the provider's own site or API during this work. Otherwise the row stays, with `Not confirmed (reason)` and no USD figure. Never fill a price from a third-party site, from memory, or by converting another region's price.
- Prices exclude tax. Where a site shows tax-inclusive prices only, `amount` is the price before tax and Notes says so.
- Locations per provider: every Indonesian location it offers, plus Singapore. One extra cheapest-region row only when it is at least 10% cheaper than that provider's Singapore row.
- Use the month-to-month price. Where only term pricing exists, Billing states the term and Notes states the renewal price.
- Hourly-only prices (AWS EC2, Google Cloud and similar): monthly = hourly × 730, Linux, on-demand, no commitment; Notes says so and says disk is extra.
- Currency: keep the original figure; USD = amount ÷ `PER_USD[currency]`, rates from `https://api.frankfurter.app/latest?from=USD&to=EUR,IDR,SGD` on the check date.
- The main sheet's pick stays Vultr Singapore. Its price and `EXPECTED_TOTAL = 602.13` change only if Vultr's website price for `vc2-16c-64gb` in Singapore changed.
- `Checked` is the date the price was actually read, as `YYYY-MM-DD`.

## Review Focus
- **`budgetting.xlsx` open in Excel:** the save raises `PermissionError`. Expected: the build stops with "Close budgetting.xlsx in Excel, then rerun", not a traceback. Pinned in Task 1 Step 5.
- **Pricing page rendered by JavaScript or behind a login:** `curl` returns no price. Expected: a `Not confirmed (reason)` row, not a guess. Pinned by `check_offers` (confirmed ⇔ has amount ⇔ has evidence line) in Task 1.
- **Promo or first-term price shown larger than the renewal price** (Hostinger, Niagahoster, Contabo): expected the regular price in the row and the term in Billing. Pinned by the `term` → `renew` assertion in Task 1.
- **Tax-inclusive rupiah prices:** expected the before-tax amount, with a note. Pinned by the `incl. tax` → `before tax` assertion in Task 1.
- **A row with no USD price in the sort:** expected last in its group, and no crash comparing `None`. Pinned by the order assertion in Task 1.

---

### Task 1: New sheet structure, checks, and the existing providers re-checked

**Files:**
- Modify: `tools/build_budget.py` (replace `EUR_USD`, `PROVIDER_HEADER`, `PROVIDERS`, `build_providers`; module docstring)
- Modify: `tools/check_budget.py` (replace the `VPS Providers` block at the end of `main`)
- Create: `docs/reviews/2026-11-17-vps-price-evidence.md`
- Modify: `budgetting.xlsx`

**Interfaces:**
- Produces, in `tools/build_budget.py`:

```python
@dataclass(frozen=True)
class Offer:
    provider: str
    plan: str            # as the website names it
    vcpu: int
    ram_gb: int
    disk: str
    location: str        # one place, e.g. "Jakarta", "Singapore"
    in_indonesia: bool
    price_text: str      # as shown on the site, e.g. "Rp4,990,000/mo incl. tax"
    currency: str        # key of PER_USD
    amount: float | None # monthly, before tax, in `currency`; None when not confirmed
    billing: str
    fits: str            # "Yes" or "No (reason)"
    status: str          # "Confirmed" or "Not confirmed (reason)"
    checked: str         # YYYY-MM-DD
    notes: str
    link: str            # https page the price came from

PER_USD: dict[str, float]   # {"USD": 1.0, "EUR": ..., "IDR": ..., "SGD": ...}
RATES_DATE: str             # date frankfurter.app reports
OFFERS: list[Offer]
PROVIDER_HEADER: list[str]  # the 15 names below, in order
def usd(o: Offer) -> float | None      # round(amount / PER_USD[currency], 2), None when amount is None
def sorted_offers() -> list[Offer]     # key: (fits != "Yes", amount is None, usd or 0, provider, location)
def evidence_key(o: Offer) -> str      # f"{provider} | {plan} | {location}"
```

- `PROVIDER_HEADER = ["Provider", "Product / plan", "vCPU", "RAM (GB)", "Disk", "Location", "In Indonesia?", "Price (website)", "Price USD / month", "Billing", "Fits 16/64?", "Price status", "Checked", "Notes", "Link"]`. `In Indonesia?` is written as `Yes` / `No`.
- `PROVIDERS` and `EUR_USD` are removed. Nothing else imports them.

- [ ] **Step 1: Make the branch and move the docs onto it**

The current branch holds unrelated work, so use a worktree. From `vibe-training/`:

```bash
git worktree add ../vibe-training-vps -b budget/vps-providers main
mv docs/superpowers/specs/2026-11-17-vps-providers-pricing-design.md ../vibe-training-vps/docs/superpowers/specs/
mv docs/superpowers/plans/2026-11-17-vps-providers-pricing.md ../vibe-training-vps/docs/superpowers/plans/
cd ../vibe-training-vps
git add docs/superpowers && git commit -m "docs: VPS providers pricing spec and plan"
python tools/check_budget.py
```
Expected: `OK grand total 602.13; 11 providers`. All later commands run in `../vibe-training-vps`.

- [ ] **Step 2: Replace the provider checks in `tools/check_budget.py`**

Add `import re`. Import `OFFERS, PER_USD, PROVIDER_HEADER, ROWS, XLSX, evidence_key, sorted_offers, usd`. Add `EVIDENCE = Path(__file__).resolve().parent.parent / "docs/reviews/2026-11-17-vps-price-evidence.md"` and `REQUIRED_PROVIDERS = {"Vultr", "Hetzner", "Akamai Linode", "AWS Lightsail", "UpCloud", "DigitalOcean", "Contabo", "OVHcloud", "Biznet Gio"}`. Replace everything from `pv = wb["VPS Providers"]` to the `print` with a call to:

```python
def check_offers(wb) -> None:
    pv = wb["VPS Providers"]
    assert [pv.cell(1, c).value for c in range(1, 16)] == PROVIDER_HEADER, "provider header"
    assert pv.freeze_panes == "A2" and pv.auto_filter.ref, "header not frozen/filtered"
    evidence = EVIDENCE.read_text(encoding="utf-8")
    ordered = sorted_offers()
    assert len(ordered) == len(OFFERS) == len({evidence_key(o) for o in OFFERS}), "duplicate offer"
    assert REQUIRED_PROVIDERS <= {o.provider for o in OFFERS}, REQUIRED_PROVIDERS - {o.provider for o in OFFERS}
    for r, o in enumerate(ordered, start=2):
        tag = f"row {r} {evidence_key(o)}"
        assert [pv.cell(r, 1).value, pv.cell(r, 2).value, pv.cell(r, 6).value] == [o.provider, o.plan, o.location], f"order {tag}"
        assert pv.cell(r, 7).value == ("Yes" if o.in_indonesia else "No"), tag
        assert pv.cell(r, 9).value == usd(o), f"usd {tag}"
        assert pv.cell(r, 15).hyperlink.target == o.link and o.link.startswith("https://"), f"link {tag}"
        assert "/" not in o.location and "surcharge" not in o.location.lower(), f"location {tag}"
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", o.checked), f"checked {tag}"
        assert o.currency in PER_USD, f"currency {tag}"
        if o.status == "Confirmed":
            assert o.amount and o.amount > 0, f"confirmed without price {tag}"
            assert evidence_key(o) in evidence, f"no evidence line {tag}"
        else:
            assert re.fullmatch(r"Not confirmed \(.+\)", o.status) and o.amount is None, f"status {tag}"
        assert o.fits == "Yes" or re.fullmatch(r"No \(.+\)", o.fits), f"fits {tag}"
        if o.fits == "Yes":
            assert (o.vcpu, o.ram_gb) == (16, 64), f"'Yes' is not 16/64 {tag}"
        if "term" in o.billing.lower():
            assert "renew" in o.notes.lower(), f"term price without renewal note {tag}"
        if "incl. tax" in o.price_text.lower():
            assert "before tax" in o.notes.lower(), f"tax-inclusive price without note {tag}"
    assert pv.cell(len(ordered) + 2, 1).value is None, "rows beyond the offers"
```

`main` ends with `print(f"OK grand total {total}; {len(OFFERS)} offers")`.

- [ ] **Step 3: Run the check and confirm it fails**

Run: `python tools/check_budget.py`
Expected: `ImportError: cannot import name 'OFFERS'`.

- [ ] **Step 4: Read today's prices for the existing providers and write `OFFERS`**

Fetch the rates first and set `PER_USD` and `RATES_DATE`. Then, for each provider below, read the price of every row the location rule in Global Constraints asks for, and write one `Offer` per row. Public APIs give region prices without JavaScript: `https://api.vultr.com/v2/plans` and `https://api.linode.com/v4/linode/types` (`region_prices`). Where `curl` gets no price, the row is `Not confirmed (reason)`.

| Provider | Plan to price | Known trap from the old sheet |
|---|---|---|
| Vultr | Cloud Compute Regular `vc2-16c-64gb`; Optimized Cloud General Purpose 16/64 | Main sheet depends on the first one |
| Hetzner | CCX43; CPX62 (16/32, Fits = No) | Old rows showed the EU price under "Singapore" |
| Akamai Linode | Shared CPU Linode 64GB `g6-standard-16` | Jakarta costs more than Singapore: separate rows |
| AWS Lightsail | Linux bundle 16 vCPU / 64 GB | Old row said "Singapore / Jakarta": separate rows |
| UpCloud | 16 cores / 64 GB | Plan tier was never confirmed |
| DigitalOcean | General Purpose 16/64 | |
| Contabo | Cloud VPS with 16 vCPU / 64 GB | Price must include the Singapore surcharge; setup fee in Notes |
| OVHcloud | Largest VPS (Fits = No) | Priced in SGD |
| Biznet Gio | NEO Lite largest (Fits = No) | Priced in IDR; check tax-inclusive |

For every `Confirmed` row add a line to `docs/reviews/2026-11-17-vps-price-evidence.md`, a table with the columns `Offer | URL | How read | Quote`, where `Offer` is `evidence_key(o)` and `Quote` is the text or JSON fragment that holds the price.

- [ ] **Step 5: Rewrite `build_providers(wb)` and handle the locked file**

It writes `PROVIDER_HEADER` in bold, one row per `sorted_offers()` entry (USD cell from `usd(o)`, format `$#,##0.00`; Link cell as a hyperlink), sets `ws.freeze_panes = "A2"` and `ws.auto_filter.ref` over the table, and puts this note two rows below the last offer, in column A: `Prices excl. tax, each checked on the date in its row. Rates per 1 USD on {RATES_DATE} (ECB via frankfurter.app): EUR {..}, IDR {..}, SGD {..}. Hourly-billed servers cost far less than the monthly cap if deleted after Day 5.` The row right after the last offer stays empty.

In `build()`, wrap `wb.save(XLSX)`: on `PermissionError`, `raise SystemExit("Close budgetting.xlsx in Excel, then rerun")`. Update the module docstring's spec path and "Prices checked" line.

- [ ] **Step 6: Build and check**

Run: `python tools/build_budget.py && python tools/check_budget.py`
Expected: `OK grand total 602.13; N offers`. If Vultr's `vc2-16c-64gb` Singapore price is no longer $320, update that entry in `ROWS`, `EXPECTED_TOTAL` and its comment, then rerun.

Then, with `budgetting.xlsx` open in Excel, run `python tools/build_budget.py`. Expected: the one-line "Close budgetting.xlsx…" message and exit code 1.

- [ ] **Step 7: Commit**

```bash
git add tools/build_budget.py tools/check_budget.py budgetting.xlsx docs/reviews/2026-11-17-vps-price-evidence.md
git commit -m "Budget: VPS Providers sheet, one row per provider and location, prices re-checked"
```

---

### Task 2: Indonesian providers

**Files:**
- Modify: `tools/build_budget.py` (`OFFERS`)
- Modify: `tools/check_budget.py` (`REQUIRED_PROVIDERS`)
- Modify: `docs/reviews/2026-11-17-vps-price-evidence.md`, `budgetting.xlsx`

**Interfaces:**
- Consumes: `Offer`, `OFFERS`, `evidence_key` from Task 1.

- [ ] **Step 1: Extend the check**

Add to `REQUIRED_PROVIDERS`: `"IDCloudHost", "CloudKilat", "Dewaweb", "DomaiNesia", "Hostinger", "Niagahoster", "Rumahweb", "Qwords", "Jagoan Hosting"`. Add to `check_offers`: `assert any(o.provider == "Biznet Gio" and "NEO Virtual Compute" in o.plan for o in OFFERS), "Biznet NEO Virtual Compute row missing"`.

- [ ] **Step 2: Run the check and confirm it fails**

Run: `python tools/check_budget.py`
Expected: `AssertionError` listing the nine missing providers.

- [ ] **Step 3: Read the prices and add the offers**

For each of the nine providers and for Biznet Gio NEO Virtual Compute: the 16 vCPU / 64 GB cloud VPS plan, or the closest plan with Fits = `No (reason)`. `in_indonesia=True` only when the provider's page names an Indonesian data centre for that plan. Most show rupiah prices; check each page for "termasuk PPN" / "belum termasuk PPN" and apply the tax rule. Hostinger and Niagahoster show term prices: apply the term rule. If Niagahoster's site now redirects to Hostinger, keep one `Niagahoster` row with `Not confirmed (site redirects to Hostinger)` and no price. Add the evidence lines.

- [ ] **Step 4: Build and check**

Run: `python tools/build_budget.py && python tools/check_budget.py`
Expected: `OK grand total …; N offers`, with N larger than after Task 1.

- [ ] **Step 5: Commit**

```bash
git add tools/build_budget.py tools/check_budget.py budgetting.xlsx docs/reviews/2026-11-17-vps-price-evidence.md
git commit -m "Budget: add Indonesian VPS providers"
```

---

### Task 3: Global clouds with a Jakarta region, and the docs

**Files:**
- Modify: `tools/build_budget.py` (`OFFERS`), `tools/check_budget.py` (`REQUIRED_PROVIDERS`)
- Modify: `docs/reviews/2026-11-17-vps-price-evidence.md`, `budgetting.xlsx`
- Modify: `docs/superpowers/specs/2026-11-16-training-budget-design.md`, `docs/project-log.md`

**Interfaces:**
- Consumes: `Offer`, `OFFERS`, `evidence_key` from Task 1.

- [ ] **Step 1: Extend the check**

Add to `REQUIRED_PROVIDERS`: `"AWS EC2", "Google Cloud", "Alibaba Cloud", "Tencent Cloud", "Huawei Cloud"`. Add to `check_offers`: `for p in ("AWS EC2", "Google Cloud", "Alibaba Cloud", "Tencent Cloud", "Huawei Cloud"): assert any(o.provider == p and o.in_indonesia for o in OFFERS), f"{p}: no Jakarta row"`.

- [ ] **Step 2: Run the check and confirm it fails**

Run: `python tools/check_budget.py`
Expected: `AssertionError` listing the five missing providers.

- [ ] **Step 3: Read the prices and add the offers**

Per cloud: the cheapest current-generation general-purpose instance with 16 vCPU / 64 GB that the Jakarta region offers, plus the same instance in Singapore. Apply the hourly rule (× 730, Linux, on-demand, disk extra in Notes). A cloud whose price list needs a login or a calculator that `curl` can't read gets `Not confirmed (reason)` rows for Jakarta and Singapore. Add the evidence lines.

- [ ] **Step 4: Build and check**

Run: `python tools/build_budget.py && python tools/check_budget.py`
Expected: `OK grand total …; N offers`.

- [ ] **Step 5: Update the docs**

In `docs/superpowers/specs/2026-11-16-training-budget-design.md`, add under the last section: `## Change 2026-11-17` with one bullet saying the `VPS Providers` sheet was rebuilt per `2026-11-17-vps-providers-pricing-design.md` (one row per provider and location, prices re-checked, Indonesian providers added), and whether the Vultr price changed. Append one dated line to the Log in `docs/project-log.md` with the offer count, the number of unconfirmed rows, and the evidence file path.

- [ ] **Step 6: Commit**

```bash
git add tools/build_budget.py tools/check_budget.py budgetting.xlsx docs
git commit -m "Budget: add Jakarta-region clouds; log the VPS Providers rebuild"
```

- [ ] **Step 7: Report**

Give the user: the number of rows, the unconfirmed rows with their reasons, any row whose price differs from the 2026-11-16 sheet (old → new), and whether the main budget total changed. Remind them the rebuilt `budgetting.xlsx` is on branch `budget/vps-providers` until merged, and that the copy open in Excel is the old one.
