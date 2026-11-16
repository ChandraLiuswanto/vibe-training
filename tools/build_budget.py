"""Rebuild Sheet1 of budgetting.xlsx from ROWS.

Spec: docs/superpowers/specs/2026-11-16-training-budget-design.md
Prices checked 2026-11-16: digitalocean.com/pricing/droplets, api.vultr.com/v2/plans, cfdomainpricing.com (Cloudflare Registrar at cost).
"""
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


EUR_USD = 1.1052  # frankfurter.app (ECB), 2026-11-13
PROVIDER_HEADER = ["Provider", "Product / plan", "vCPU", "RAM (GB)", "Disk", "Location (closest to ID)",
                   "Price (original)", "Price USD / month", "Billing", "Fits 16/64?", "Safety / notes", "Link"]
# Day 5 deploy VPS candidates, 16 vCPU / 64 GB. Checked 2026-11-16 on each provider's site/API.
PROVIDERS = [
    ("Vultr", "Cloud Compute Regular vc2-16c-64gb", 16, 64, "1280 GB SSD", "Singapore",
     "$320/mo", 320, "Hourly, monthly cap", "Yes",
     "RECOMMENDED. Established, firewall + snapshots + DDoS protection included", "https://www.vultr.com/pricing/"),
    ("Vultr", "Optimized Cloud General Purpose (dedicated vCPU)", 16, 64, "320 GB NVMe", "Singapore",
     "$480/mo", 480, "Hourly, monthly cap", "Yes", "Dedicated vCPU: steadier under 30 parallel builds",
     "https://www.vultr.com/pricing/"),
    ("Hetzner", "CCX43 (dedicated vCPU)", 16, 64, "360 GB NVMe", "Singapore",
     "EUR 234.99/mo (EU price)", round(234.99 * EUR_USD, 2), "Hourly, monthly cap", "Yes",
     "Cheapest reputable; Singapore price is higher than EU (confirm at checkout); new accounts may need ID check",
     "https://www.hetzner.com/cloud/general-purpose"),
    ("Akamai Linode", "Shared CPU Linode 64GB (g6-standard-16)", 16, 64, "1280 GB SSD", "Jakarta (id-cgk)",
     "$460.80/mo (Jakarta)", 460.80, "Hourly, monthly cap", "Yes",
     "Only one with a Jakarta DC (lowest latency); $384 in other regions", "https://www.linode.com/pricing/"),
    ("AWS Lightsail", "Linux bundle 64 GB / 16 vCPU", 16, 64, "1280 GB SSD", "Singapore / Jakarta",
     "$384/mo", 384, "Hourly, monthly cap", "Yes", "AWS-grade security; simple fixed bundle",
     "https://aws.amazon.com/lightsail/pricing/"),
    ("UpCloud", "Cloud Server 64 GB / 16 cores", 16, 64, "300 GB MaxIOPS", "Singapore",
     "EUR 384/mo", round(384 * EUR_USD, 2), "Hourly, monthly cap", "Yes", "99.999% SLA; verify exact plan tier at checkout",
     "https://upcloud.com/pricing/"),
    ("DigitalOcean", "General Purpose Droplet (dedicated vCPU)", 16, 64, "200 GB SSD", "Singapore",
     "$504/mo", 504, "Hourly, monthly cap", "Yes", "Same provider as 9router VPS; Basic plans stop at 8/16",
     "https://www.digitalocean.com/pricing/droplets"),
    ("Contabo", "Cloud VPS 16", 16, 64, "500 GB SSD / 250 GB NVMe", "Singapore (surcharge)",
     "EUR 37/mo (EUR 29.60 on 24-mo term)", round(37 * EUR_USD, 2), "Monthly contract, setup fee, region surcharge",
     "Yes", "Very cheap but oversold/noisy-neighbour reputation; risky for live class", "https://contabo.com/en/vps/"),
    ("Hetzner", "CPX62 (shared vCPU)", 16, 32, "640 GB NVMe", "Singapore",
     "EUR 110.99/mo (EU price)", round(110.99 * EUR_USD, 2), "Hourly, monthly cap", "No (32 GB RAM)",
     "Listed for reference only", "https://www.hetzner.com/cloud/regular-performance"),
    ("OVHcloud", "VPS-4 (largest VPS)", 8, 24, "200 GB NVMe", "Singapore",
     "S$30/mo", None, "Monthly", "No (max 8/24)", "Listed for reference only", "https://www.ovhcloud.com/en-sg/vps/"),
    ("Biznet Gio", "NEO Lite LL 16.16 (largest)", 16, 16, "60 GB SSD", "Jakarta",
     "Rp499,000/mo", round(499000 / 18245, 2), "Monthly", "No (16 GB RAM)",
     "Indonesian provider, listed for reference only", "https://www.biznetgio.com/product/neo-lite"),
]


def build_providers(wb) -> None:
    if "VPS Providers" in wb.sheetnames:
        del wb["VPS Providers"]
    ws = wb.create_sheet("VPS Providers")
    for c, h in enumerate(PROVIDER_HEADER, start=1):
        ws.cell(1, c, h).font = Font(bold=True)
    for r, row in enumerate(PROVIDERS, start=2):
        for c, v in enumerate(row, start=1):
            ws.cell(r, c, v)
        ws.cell(r, 8).number_format = "$#,##0.00"
        link = ws.cell(r, 12)
        link.hyperlink = row[-1]
        link.style = "Hyperlink"
    note = len(PROVIDERS) + 3
    ws.cell(note, 1, "Prices excl. tax, checked 2026-11-16. EUR->USD 1.1052, USD->IDR 18,245 (ECB via frankfurter.app, 2026-11-13). "
                     "Hourly-billed servers cost far less than the monthly cap if deleted after Day 5.")
    for col, width in zip("ABCDEFGHIJKL", [15, 44, 6, 9, 24, 22, 34, 16, 34, 15, 80, 48]):
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
    build()
