"""Rebuild budgetting.xlsx: Sheet1 from ROWS, sheet "VPS Providers" from OFFERS.

Specs: docs/superpowers/specs/2026-11-16-training-budget-design.md (Sheet1),
       docs/superpowers/specs/2026-11-17-vps-providers-pricing-design.md (sheet "VPS Providers").
Sheet1 prices checked 2026-11-16: digitalocean.com/pricing/droplets, api.vultr.com/v2/plans, cfdomainpricing.com (Cloudflare Registrar at cost).
VPS Providers: each row carries its own check date; sources in docs/reviews/2026-11-17-vps-price-evidence.md.
"""
from dataclasses import dataclass
from pathlib import Path

import openpyxl
from openpyxl.styles import Font

XLSX = Path(__file__).resolve().parent.parent / "budgetting.xlsx"
TAX = 0.11

# (item, plan, period, quantity, price USD, note)
ROWS = [
    ("Codex", "Pro 200", "Monthly", 1, 200,
     "Shared via 9router for opencode (agentic coding) + in-app chatbot"),
    ("VPS - 9router", "DigitalOcean Basic 1 vCPU / 2 GB / 50 GB SSD, Singapore (SGP1)", "Monthly", 1, 12,
     "Separate from deploy box so a broken deploy can't stop the agents; hourly billing, monthly cap"),
    ("VPS - Day 5 deploy (shared, subdomain per team)",
     "Vultr Cloud Compute 16 vCPU / 64 GB / 1.28 TB SSD, Singapore (vc2-16c-64gb)", "Monthly", 1, 320,
     "Recommended pick; see sheet 'VPS Providers' for alternatives. Hourly billing, monthly cap"),
    ("Domain", ".com via Cloudflare Registrar (at-cost) for teamN.<domain>", "Yearly", 1, 10.46,
     "Free fallback: teamN.<ip>.sslip.io"),
    ("GitHub", "Free", "-", 1, 0, "Participant repos + checkpoint repo"),
    ("opencode", "Open source", "-", 1, 0, "Coding agent"),
    ("Container tool (laptops)", "Podman Desktop (free)", "-", 1, 0,
     "Docker Desktop is not free for companies >250 staff / >$10M revenue"),
    ("TLS certificates", "Let's Encrypt", "-", 1, 0, "HTTPS for team subdomains"),
    ("Market data", "yfinance", "-", 1, 0, "Yahoo Finance data, no key"),
    ("Demo video", "HyperFrames (open source)", "-", 1, 0, "Final showcase"),
]

NOTE = ("Optional, not in total: Docker Desktop Business ~$24/user/mo, "
        "only if OCBC IT requires Docker Desktop instead of Podman.")
ASSUMPTION = ("Assumes trainer prep + Day 3-5 delivery fit within 1 billing month; "
              "domain = first year. If prep spans 2 months, set Quantity = 2 on the Monthly rows.")


# 1 USD in each currency. ECB via https://api.frankfurter.app/latest?from=USD&to=EUR,IDR,SGD
PER_USD = {"USD": 1.0, "EUR": 0.90794, "IDR": 18259, "SGD": 1.2888}
RATES_DATE = "2026-11-16"

PROVIDER_HEADER = ["Provider", "Product / plan", "vCPU", "RAM (GB)", "Disk", "Location", "In Indonesia?",
                   "Price (website)", "Price USD / month", "Billing", "Fits 16/64?", "Price status", "Checked",
                   "Notes", "Link"]


@dataclass(frozen=True)
class Offer:
    """One plan in one location, with the price the provider's own site shows for exactly that."""
    provider: str
    plan: str             # as the website names it
    vcpu: int
    ram_gb: int
    disk: str
    location: str         # one place
    in_indonesia: bool
    price_text: str       # as shown on the site
    currency: str         # key of PER_USD
    amount: float | None  # monthly, before tax, in `currency`; None when not confirmed
    billing: str
    fits: str             # "Yes" or "No (reason)"
    status: str           # "Confirmed" or "Not confirmed (reason)"
    checked: str          # YYYY-MM-DD the price was read
    notes: str
    link: str             # page the price came from


HOURLY_CAP = "Hourly, capped at the monthly price"
# Day 5 deploy VPS candidates, target 16 vCPU / 64 GB. Evidence per row: docs/reviews/2026-11-17-vps-price-evidence.md
OFFERS = [
    Offer("Vultr", "Cloud Compute Regular vc2-16c-64gb", 16, 64, "1280 GB SSD", "Singapore", False,
          "$320/mo ($0.438/hr)", "USD", 320, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Current pick in the main sheet. Shared vCPU. Same price in every Vultr region; Vultr has no Indonesian region.",
          "https://www.vultr.com/pricing/"),
    Offer("Vultr", "Optimized Cloud General Purpose voc-g-16c-64gb-320s-amd", 16, 64, "320 GB", "Singapore", False,
          "$480/mo ($0.658/hr)", "USD", 480, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Dedicated vCPU: steadier under 30 parallel builds. Same price in every Vultr region.",
          "https://www.vultr.com/pricing/"),
    Offer("Hetzner", "CCX43 (dedicated vCPU)", 16, 64, "360 GB NVMe", "Singapore", False,
          "EUR 341.49/mo excl. VAT", "EUR", 341.49, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Singapore costs 45% more than Helsinki. Price includes IPv4. "
          "New accounts may need an ID check.",
          "https://www.hetzner.com/cloud/general-purpose"),
    Offer("Hetzner", "CCX43 (dedicated vCPU)", 16, 64, "360 GB NVMe", "Helsinki", False,
          "EUR 234.99/mo excl. VAT", "EUR", 234.99, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Reference only: Hetzner's cheapest region, far from Indonesia (high latency). "
          "This is the price the old sheet showed under 'Singapore'.",
          "https://www.hetzner.com/cloud/general-purpose"),
    Offer("Hetzner", "CPX62 (shared vCPU)", 16, 32, "640 GB NVMe", "Singapore", False,
          "EUR 172.49/mo excl. VAT", "EUR", 172.49, HOURLY_CAP, "No (32 GB RAM)", "Confirmed", "2026-11-17",
          "Listed for reference only. Helsinki price is EUR 110.99.",
          "https://www.hetzner.com/cloud/regular-performance"),
    Offer("Akamai Linode", "Shared CPU Linode 64GB (g6-standard-16)", 16, 64, "1280 GB SSD", "Jakarta", True,
          "$460.80/mo ($0.691/hr)", "USD", 460.80, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Jakarta region (id-cgk) costs 20% more than Linode's standard regions.",
          "https://www.linode.com/pricing/"),
    Offer("Akamai Linode", "Shared CPU Linode 64GB (g6-standard-16)", 16, 64, "1280 GB SSD", "Singapore", False,
          "$384/mo ($0.576/hr)", "USD", 384, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Standard price; Singapore has no regional surcharge.",
          "https://www.linode.com/pricing/"),
    Offer("AWS Lightsail", "Linux bundle 64 GB / 16 vCPU, public IPv4", 16, 64, "1280 GB SSD", "Jakarta", True,
          "$384 USD/mo", "USD", 384, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Same bundle price in every Region, but Jakarta includes half the data transfer (4 TB instead of 8 TB).",
          "https://aws.amazon.com/lightsail/pricing/"),
    Offer("AWS Lightsail", "Linux bundle 64 GB / 16 vCPU, public IPv4", 16, 64, "1280 GB SSD", "Singapore", False,
          "$384 USD/mo", "USD", 384, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "Same bundle price in every Region; 8 TB data transfer included.",
          "https://aws.amazon.com/lightsail/pricing/"),
    Offer("UpCloud", "Premium 64 GB / 16 cores", 16, 64, "300 GB MaxIOPS", "Singapore", False,
          "EUR 384/mo (Global price)", "EUR", 384, "Hourly, capped at 28 days per month", "Yes", "Confirmed", "2026-11-17",
          "'Global price' applies to every UpCloud data centre, Singapore (SG-SIN1) included. 99.999% SLA. "
          "A Cloud Native 64 GB / 16 cores plan is EUR 270/mo with storage billed separately.",
          "https://upcloud.com/pricing/"),
    Offer("DigitalOcean", "General Purpose Droplet g-16vcpu-64gb (dedicated vCPU)", 16, 64, "200 GB SSD", "Singapore", False,
          "$504.00/mo ($0.75/hr)", "USD", 504, HOURLY_CAP, "Yes", "Confirmed", "2026-11-17",
          "The pricing page shows one price, with no per-region difference. Same provider as the 9router VPS.",
          "https://www.digitalocean.com/pricing/droplets"),
    Offer("Contabo", "Cloud VPS 16", 16, 64, "500 GB SSD or 250 GB NVMe", "Singapore", False,
          "EUR 37.00/mo + EUR 20.75/mo Asia (Singapore) location fee", "EUR", 57.75,
          "Monthly, prepaid; 1-month contract", "Yes", "Confirmed", "2026-11-17",
          "Price includes the Singapore location fee, which the old sheet left out. No setup fee. The order page does not state VAT. "
          "Singapore was marked out of stock on the order page when checked. 12-month price EUR 31.45, 24-month EUR 29.60, "
          "plus the same location fee. Very cheap, shared hosts: the old sheet flagged it as risky for a live class.",
          "https://contabo.com/en/vps/cloud-vps-core-16"),
    Offer("Contabo", "Cloud VPS 16", 16, 64, "500 GB SSD or 250 GB NVMe", "European Union", False,
          "EUR 37.00/mo", "EUR", 37.00, "Monthly, prepaid; 1-month contract", "Yes", "Confirmed", "2026-11-17",
          "Reference only: Contabo's cheapest region (no location fee), far from Indonesia. No setup fee. The order page does not state VAT.",
          "https://contabo.com/en/vps/cloud-vps-core-16"),
    Offer("OVHcloud", "VPS-4 (largest VPS)", 8, 24, "200 GB NVMe", "Singapore", False,
          "From S$30 ex. GST/month", "SGD", None, "Monthly", "No (max 8 vCPU / 24 GB)",
          "Not confirmed (the Singapore site shows a 'from' price without naming the data centre or the commitment)",
          "2026-11-17", "Listed for reference only.",
          "https://www.ovhcloud.com/en-sg/vps/"),
    Offer("Biznet Gio", "NEO Lite LL 16.16 (largest NEO Lite)", 16, 16, "60 GB SSD", "Indonesia", True,
          "Rp998.000/bulan (promo Rp499.000)", "IDR", 998000, "Monthly", "No (16 GB RAM)", "Confirmed", "2026-11-17",
          "Regular price used; Rp499.000 is a new-customer promo. The page says 'Data Center di Indonesia' without naming "
          "the city, and does not say whether PPN is included. Listed for reference only.",
          "https://www.biznetgio.com/product/neo-lite"),
]


def usd(o: Offer) -> float | None:
    return None if o.amount is None else round(o.amount / PER_USD[o.currency], 2)


def sorted_offers() -> list[Offer]:
    """Plans that fit first, cheapest first; unconfirmed prices last in their group."""
    return sorted(OFFERS, key=lambda o: (o.fits != "Yes", o.amount is None, usd(o) or 0, o.provider, o.location))


def evidence_key(o: Offer) -> str:
    return f"{o.provider} | {o.plan} | {o.location}"


def build_providers(wb) -> None:
    if "VPS Providers" in wb.sheetnames:
        del wb["VPS Providers"]
    ws = wb.create_sheet("VPS Providers")
    for c, h in enumerate(PROVIDER_HEADER, start=1):
        ws.cell(1, c, h).font = Font(bold=True)
    offers = sorted_offers()
    for r, o in enumerate(offers, start=2):
        row = [o.provider, o.plan, o.vcpu, o.ram_gb, o.disk, o.location, "Yes" if o.in_indonesia else "No",
               o.price_text, usd(o), o.billing, o.fits, o.status, o.checked, o.notes, o.link]
        for c, v in enumerate(row, start=1):
            ws.cell(r, c, v)
        ws.cell(r, 9).number_format = "$#,##0.00"
        link = ws.cell(r, 15)
        link.hyperlink = o.link
        link.style = "Hyperlink"
    last = len(offers) + 1
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:O{last}"
    ws.cell(last + 2, 1, f"Prices excl. tax, each checked on the date in its row. Rates per 1 USD on {RATES_DATE} "
                         f"(ECB via frankfurter.app): EUR {PER_USD['EUR']}, IDR {PER_USD['IDR']:,}, SGD {PER_USD['SGD']}. "
                         "Hourly-billed servers cost far less than the monthly cap if deleted after Day 5.")
    for col, width in zip("ABCDEFGHIJKLMNO", [15, 46, 6, 9, 24, 16, 13, 40, 16, 32, 22, 30, 11, 90, 46]):
        ws.column_dimensions[col].width = width


def build() -> None:
    wb = openpyxl.load_workbook(XLSX)
    ws = wb.active
    ws.delete_rows(2, ws.max_row)
    ws.cell(1, 8, "Notes")

    for r, (item, plan, period, qty, price, note) in enumerate(ROWS, start=2):
        for c, v in enumerate([item, plan, period, qty, price, TAX, f"=(1+F{r})*E{r}*D{r}", note], start=1):
            ws.cell(r, c, v)
        ws.cell(r, 5).number_format = "$#,##0.00"
        ws.cell(r, 6).number_format = "0%"
        ws.cell(r, 7).number_format = "$#,##0.00"

    last = 1 + len(ROWS)
    gt = last + 1
    ws.cell(gt, 1, "Grand Total").font = Font(bold=True)
    g = ws.cell(gt, 7, f"=SUM(G2:G{last})")
    g.font = Font(bold=True)
    g.number_format = "$#,##0.00"
    ws.cell(gt + 2, 1, NOTE)
    ws.cell(gt + 3, 1, ASSUMPTION)

    for col, width in zip("ABCDEFGH", [44, 62, 10, 10, 10, 9, 14, 90]):
        ws.column_dimensions[col].width = width
    build_providers(wb)
    wb.save(XLSX)


if __name__ == "__main__":
    try:
        build()
    except PermissionError:  # Excel holds the file: opening or saving it fails
        raise SystemExit("Close budgetting.xlsx in Excel, then rerun") from None
