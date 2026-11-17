Size: small change (no spec reviewer)

# VPS Providers sheet: prices that match the website, more Indonesian options

Date: 2026-11-17 · Target: sheet `VPS Providers` in `budgetting.xlsx`, built by `tools/build_budget.py`, checked by `tools/check_budget.py`.

Tags: *(user)* = decided by the user · *(call)* = my call, correctable.

## Intent
The user will use this sheet to recommend one deploy VPS to the team *(user)*. Today it misleads: several rows show a price that is not the price for the location in the same row. Every price must be the one the provider's website shows for that exact plan and location *(user)*. The list must also cover the providers commonly used in Indonesia *(user)*.

## What is wrong today
- Hetzner CCX43 and CPX62: location "Singapore", price is the EU price.
- Contabo: location "Singapore (surcharge)", price leaves out the surcharge and the setup fee.
- AWS Lightsail: "Singapore / Jakarta" with one unconfirmed price.
- UpCloud: plan tier never confirmed.
- Biznet Gio is the only Indonesian provider.
- All prices date from 2026-11-16 and have no per-row check date.

## Goals
- One row per provider, plan and location. A location cell names exactly one place.
- The price in a row is the website price for that plan in that location, including any location surcharge. One-off fees (setup) are stated in the notes with the amount.
- Each row carries the date its price was checked and a link to the page it came from.
- The team can sort and filter: by price, by location, by "in Indonesia".

## Non-goals
- Changing the pick in the main budget sheet. It stays Vultr Singapore until the team decides *(call)*. Exception: if the re-check shows Vultr's own price changed, the main row and the expected total follow the website.
- A shortlist or recommendation sheet. The user chose the plain full list.
- Benchmarks or latency tests.

## Anti-goals
- A guessed, converted-from-another-region or remembered price shown as if confirmed.
- A row whose price and location come from different pages.

## Approaches
- **A. One row per provider and location, sorted by price: picked** *(user)*. Each price belongs to one location, so it can't mismatch.
- B. One row per provider, a price column per location. Shorter, but breaks when plans differ by location, and can't be sorted by price.
- C. A plus a shortlist sheet of top picks. Not chosen.

## Design
Columns, in order:

| Column | Content |
|---|---|
| Provider | |
| Product / plan | The plan name as the website shows it |
| vCPU, RAM (GB), Disk | |
| Location | One city or region |
| In Indonesia? | Yes / No |
| Price (website) | Original currency and figure, as shown |
| Price USD / month | Number. Empty when not confirmed |
| Billing | Hourly with monthly cap, monthly, contract term |
| Fits 16/64? | Yes, or "No (reason)" |
| Price status | "Confirmed" or "Not confirmed (reason)" |
| Checked | Date the price was read from the website |
| Notes | Surcharges, setup fees, caveats |
| Link | The page the price came from |

- **Size** stays 16 vCPU / 64 GB *(call)*. A provider with nothing that size gets its closest plan, marked "No".
- **Locations per provider** *(call)*: every Indonesian location it offers, plus Singapore. Other regions are left out, except one cheapest-region row when it is clearly cheaper, as a reference.
- **Order** *(call)*: rows that fit first, cheapest first; then rows that don't fit; unconfirmed rows last in their group. The header row gets a filter and is frozen.
- **Currency** *(call)*: keep the original figure, convert to USD with the ECB rate of the check date (frankfurter.app). The rates and their date go in the note under the table. Rows priced in rupiah or euro compute USD from the original in the script, never typed by hand.
- **Tax**: prices exclude tax, as today. Where a website shows tax-inclusive prices only (common for Indonesian providers), the note says so and the USD figure is the price before tax.
- **Not confirmed** *(call)*: when the price can't be read from the provider's own site (login wall, quote only, calculator that won't load), the row stays in the list with an empty USD cell and the reason. It is never filled from a third-party site.

Providers to cover:
- Kept and re-checked: Vultr (both plans), Hetzner, Akamai Linode, AWS Lightsail, UpCloud, DigitalOcean, Contabo, OVHcloud, Biznet Gio.
- Added, Indonesian providers: IDCloudHost, Biznet Gio's larger line (NEO Virtual Compute), CloudKilat, Dewaweb, DomaiNesia, Hostinger / Niagahoster, Rumahweb, Qwords, Jagoan Hosting.
- Added, global clouds with a Jakarta region: AWS EC2, Google Cloud, Alibaba Cloud, Tencent Cloud, Huawei Cloud.

## Checks (`tools/check_budget.py`)
- No location cell holds "/" or "(surcharge)".
- Every row has a link, a check date and a price status.
- A confirmed row has a USD price; an unconfirmed row has none and gives a reason.
- Every "Yes" row is exactly 16 vCPU / 64 GB.
- Non-USD rows: the USD figure equals the original figure times the stated rate.
- Rows are in the stated order.
- The main sheet checks stay as they are, and its total is unchanged unless Vultr's price changed.

## Constraints
- `budgetting.xlsx` is open in Excel now (`~$budgetting.xlsx` exists). It must be closed before the build runs, or the save fails.
- The current branch `autopilot/day4-s2-access-control` holds unrelated work in progress. This change goes on its own branch from `main` *(call)*.

## Left to the builder
- How each price is read (pricing page, public API, calculator).
- Column widths and number formats.
- Updating the "Change" section of `2026-11-16-training-budget-design.md` with a pointer to this doc.

## Review Decisions (2026-11-17, after the final review)
- **Fits 16/64?** may also read "Not confirmed (reason)", for a provider whose plan list could not be read. "No" is kept for plans known to be too small or too big.
- **Location** reads "Not stated", and **In Indonesia?** reads "Not confirmed", when the provider's page does not name where the server is.
- Each confirmed row says whether the vCPUs are shared or dedicated, or "CPU type not stated" when the page is silent. It goes in Notes; the column list is unchanged.
- The note under the table says prices exclude tax where the provider states it, because several Indonesian pages do not say.
- The evidence file has an `Amount used` column, and the check compares it with the row.
