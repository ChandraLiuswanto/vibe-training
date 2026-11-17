Size: small change (no spec reviewer)

# Training budget — design

Date: 2026-11-16 · Target file: `budgetting.xlsx` (Sheet1)

Tags: *(user)* = decided by the user · *(call)* = my call, correctable · *(verify)* = check the price while filling the sheet.

## Intent
One sheet that budgets the whole Day 3–5 "AI Vibe Coding for Business Users" training. It covers trainer prep/delivery and everything the class needs, and lists only what we truly need *(user)*.

## Goals / non-goals
- **Goal:** every paid item, with plan, period, quantity, price and 11% tax, using the sheet's existing format.
- **Goal:** free items appear as $0 rows, so the full stack is visible.
- **Non-goal:** the risk of sharing one Codex account across the class. It's accepted *(user)*.
- **Non-goal:** per-participant or per-team costs. There is one shared deploy VPS *(user)*.

## Approaches (Day 5 deploy)
- A — one VPS per participant: isolated but ~$130–360, with 30 servers to set up.
- **B — one shared VPS with a subdomain per team: picked** *(user)*. Cheapest that still lets everyone deploy.
- C — trainer-only demo VPS: cheapest, but turns Day 5 into a lecture.

## Sheet rows

| Item | Plan | Period | Qty | Price (USD) | Note |
|---|---|---|---|---|---|
| Codex | Pro 200 | Monthly | 1 | 200 | Existing row; models for opencode + chatbot via 9router *(user)* |
| VPS — 9router | DigitalOcean Basic, 1 vCPU / 2 GB / 50 GB, Singapore | Monthly | 1 | 12 | Kept separate from the deploy box so a broken deploy can't stop the agents *(call)* |
| VPS — Day 5 deploy | Vultr Cloud Compute, 16 vCPU / 64 GB, Singapore | Monthly | 1 | 320 | One shared box, subdomain per team; size 16/64 *(user, 2026-11-16 change)*; provider comparison in sheet `VPS Providers` |
| Domain | .com, for `teamN.<domain>` | Yearly | 1 | ~11 *(verify)* | Free fallback: sslip.io *(call)* |
| GitHub | Free | — | 1 | 0 | Participant + checkpoint repos |
| opencode | Open source | — | 1 | 0 | Coding agent |
| Container tool on laptops | Podman Desktop (free) | — | 1 | 0 | Docker Desktop isn't free for OCBC-size companies; optional paid seat ~$24/user/mo only if IT requires it *(call)* |
| TLS certificates | Let's Encrypt | — | 1 | 0 | |
| Market data | yfinance | — | 1 | 0 | |
| Demo video | HyperFrames (open source) | — | 1 | 0 | |

- VPS prices were checked on digitalocean.com on 2026-11-16. DigitalOcean bills hourly with a monthly cap, so the monthly figure is the upper bound for one month *(call)*.
- **Formula fix** *(call)*: column G becomes `=(1+F)*E*D`. Today it ignores Quantity.
- Add a **Grand Total** row under the items *(call)*.
- Optional rows like the Docker Desktop seat go in a note, not the total *(call)*.

## Left to the builder
- Confirm the domain price at the registrar.
- Cell formatting (currency, % for tax). Keep the existing column layout.

## Change 2026-11-16
- The user raised the deploy VPS to 16 vCPU / 64 GB and asked for a sheet listing every candidate provider, with prices and product links. Sheet `VPS Providers` was added. Vultr ($320) is the pick in the main sheet *(call)*, and the user can swap it from the comparison.

## Change 2026-11-17
- Sheet `VPS Providers` was rebuilt per `2026-11-17-vps-providers-pricing-design.md`: one row per provider, plan and location, every price re-read from the provider's own site, Indonesian providers and Jakarta-region clouds added. Vultr's price did not change ($320), so the main sheet and its total ($602.13) are unchanged.
