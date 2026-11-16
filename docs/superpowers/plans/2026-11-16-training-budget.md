# Training Budget Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fill `budgetting.xlsx` with every item the Day 3–5 training needs, priced, taxed and totalled.

**Architecture:** One Python script (`tools/build_budget.py`) rewrites Sheet1 from a row list, using openpyxl. A check script recomputes the totals and compares them with the expected numbers. Excel shows formulas, not hard-coded totals.

**Tech Stack:** Python 3.12, openpyxl.

**Spec:** `docs/superpowers/specs/2026-11-16-training-budget-design.md`

## Global Constraints
- Keep the columns A–G: `Item Name, Plan, Period, Quantity, Price, Tax (%), Total Amount`.
- Tax is `0.11` on every row. Prices are in USD.
- Total formula per row: `=(1+F{r})*E{r}*D{r}`.
- Free items are $0 rows. Optional items (Docker Desktop seat) go in a note, not the total.
- Remove the empty formula rows (G3:G16) from the old template.

## Review Focus
- If the old template's leftover formulas in G3:G16 stay below the new rows, they show 0s and break the total range. Test: no formula cells beyond the last item row except the Grand Total.
- Quantity was ignored by the old formula. Test: each G formula contains `*D`.
- The Grand Total must cover exactly the item rows. Test: its SUM range is `G2:G{last}`.
- Excel opens the file without errors. Test: openpyxl loads it, and the LibreOffice recalculation (if available) gives the expected total.
- The tax column should display as a %. Test: F cells have the number format `0%`.

---

### Task 1: Build and verify the budget sheet

**Files:**
- Create: `tools/build_budget.py`
- Create: `tools/check_budget.py`
- Modify: `budgetting.xlsx`

**Interfaces:**
- Produces: `ROWS: list[tuple[str, str, str, int, float, str]]` (item, plan, period, qty, price, note) in `build_budget.py`. `check_budget.py` imports `ROWS` from it.

- [ ] **Step 1: Write `tools/check_budget.py`**
Load `budgetting.xlsx` and assert:
  - The header row is unchanged.
  - Item rows match `ROWS` (A–E). Each F is `0.11` with format `0%`. Each G is `=(1+F{r})*E{r}*D{r}`.
  - Row `last+1` has A=`Grand Total` and G=`=SUM(G2:G{last})`.
  - No other cell in G holds a formula.
  - The expected grand total, computed in Python as `sum(1.11*price*qty)`, equals `1.11*(200+12+48+11) = 300.81`. Print it.
  - A note row (column A, two rows below Grand Total) mentions `Docker Desktop` and `optional`.

- [ ] **Step 2: Run it and confirm it fails**
Run: `python tools/check_budget.py` → fails (ROWS missing, or the sheet still holds the old template).

- [ ] **Step 3: Write `tools/build_budget.py`**
The `ROWS` values are copied from the spec table:

| item | plan | period | qty | price |
|---|---|---|---|---|
| Codex | Pro 200 | Monthly | 1 | 200 |
| VPS - 9router | DigitalOcean Basic 1 vCPU / 2 GB / 50 GB SSD, Singapore (SGP1) | Monthly | 1 | 12 |
| VPS - Day 5 deploy (shared, subdomain per team) | DigitalOcean Basic 4 vCPU / 8 GB / 160 GB SSD, Singapore (SGP1) | Monthly | 1 | 48 |
| Domain | .com for teamN.<domain> subdomains | Yearly | 1 | 11 |
| GitHub | Free | - | 1 | 0 |
| opencode | Open source | - | 1 | 0 |
| Container tool (laptops) | Podman Desktop (free) | - | 1 | 0 |
| TLS certificates | Let's Encrypt | - | 1 | 0 |
| Market data | yfinance | - | 1 | 0 |
| Demo video | HyperFrames (open source) | - | 1 | 0 |

Put each note in column H, headed `Notes` (from the spec's Note column). On `__main__`: clear rows 2+, write the rows, add the formulas, the Grand Total and the note row (`Optional, not in total: Docker Desktop Business ~$24/user/mo, only if OCBC IT requires Docker Desktop.`), set the `$#,##0.00` format on E/G and `0%` on F, then save.
*(Adding column H for notes is a builder call: the spec keeps A–G, and a Notes column carries the reasons without changing them.)*

- [ ] **Step 4: Run the build, then the check**
Run: `python tools/build_budget.py && python tools/check_budget.py` → `OK grand total 300.81`.

- [ ] **Step 5: Spot-check the domain price**
Look up a .com first-year price at the registrar (Cloudflare or Namecheap). If it isn't ~$11, update `ROWS` and the expected total, then rerun Step 4.

- [ ] **Step 6: Commit**
```bash
git add tools/build_budget.py tools/check_budget.py budgetting.xlsx docs/superpowers/specs/2026-11-16-training-budget-design.md docs/superpowers/plans/2026-11-16-training-budget.md
git commit -m "Budget: fill training budget sheet (Codex, 9router VPS, shared deploy VPS, domain, free stack)"
```
