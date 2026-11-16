"""Rebuild Sheet1 of budgetting.xlsx from ROWS.

Spec: docs/superpowers/specs/2026-11-16-training-budget-design.md
Prices checked 2026-11-16: digitalocean.com/pricing/droplets, cfdomainpricing.com (Cloudflare Registrar at cost).
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
     "DigitalOcean Basic 4 vCPU / 8 GB / 160 GB SSD, Singapore (SGP1)", "Monthly", 1, 48,
     "One box, reverse proxy routes teamN.<domain> to each team's containers; hourly billing, monthly cap"),
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

    for col, width in zip("ABCDEFGH", [44, 62, 10, 10, 10, 9, 14, 90]):
        ws.column_dimensions[col].width = width
    wb.save(XLSX)


if __name__ == "__main__":
    build()
