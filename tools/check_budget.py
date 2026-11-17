"""Verify budgetting.xlsx matches the budget design (see docs/superpowers/specs/2026-11-16-training-budget-design.md)."""
import re
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).parent))
from build_budget import OFFERS, PER_USD, PROVIDER_HEADER, ROWS, XLSX, evidence_key, indonesia_text, sorted_offers, usd  # noqa: E402

HEADER = ["Item Name", "Plan", "Period", "Quantity", "Price", "Tax (%)", "Total Amount"]
EXPECTED_TOTAL = 602.13  # 1.11 * (200 + 12 + 320 + 10.46)
EVIDENCE = Path(__file__).resolve().parent.parent / "docs/reviews/2026-11-17-vps-price-evidence.md"
REQUIRED_PROVIDERS = {"Vultr", "Hetzner", "Akamai Linode", "AWS Lightsail", "UpCloud", "DigitalOcean", "Contabo",
                      "OVHcloud", "Biznet Gio",
                      "IDCloudHost", "CloudKilat", "Dewaweb", "DomaiNesia", "Hostinger", "Niagahoster", "Rumahweb",
                      "Qwords", "Jagoan Hosting", "DewaBiz",
                      "AWS EC2", "Google Cloud", "Alibaba Cloud", "Tencent Cloud", "Huawei Cloud"}


def evidence_lines() -> dict[str, str]:
    """Offer key -> its table row, from the confirmed part of the evidence file only."""
    confirmed = EVIDENCE.read_text(encoding="utf-8").split("\n## Not confirmed\n")[0]
    rows = [ln.replace(r"\|", "\x00") for ln in confirmed.split("\n") if ln.startswith("| ") and "---" not in ln[:6]]
    return {ln.split("|")[1].strip().replace("\x00", "|"): ln.replace("\x00", "|") for ln in rows}


def spellings(amount: float) -> set[str]:
    """The ways a site may write this number: 341.49, 384, 6.850.000, 4,360,000."""
    whole = f"{amount:,.0f}"
    return {f"{amount:.2f}", f"{amount:.2f}".rstrip("0").rstrip("."), whole, whole.replace(",", "."), whole.replace(",", "")}


def check_offers(wb) -> None:
    pv = wb["VPS Providers"]
    assert [pv.cell(1, c).value for c in range(1, 16)] == PROVIDER_HEADER, "provider header"
    assert pv.freeze_panes == "A2" and pv.auto_filter.ref, "header not frozen/filtered"
    evidence = evidence_lines()
    ordered = sorted_offers()
    assert len(ordered) == len(OFFERS) == len({evidence_key(o) for o in OFFERS}), "duplicate offer"
    assert REQUIRED_PROVIDERS <= {o.provider for o in OFFERS}, REQUIRED_PROVIDERS - {o.provider for o in OFFERS}
    for r, o in enumerate(ordered, start=2):
        tag = f"row {r} {evidence_key(o)}"
        assert [pv.cell(r, 1).value, pv.cell(r, 2).value, pv.cell(r, 6).value] == [o.provider, o.plan, o.location], f"order {tag}"
        assert pv.cell(r, 7).value == indonesia_text(o), tag
        assert pv.cell(r, 7).value in ("Yes", "No", "Not confirmed"), tag
        assert pv.cell(r, 9).value == usd(o), f"usd {tag}"
        assert pv.cell(r, 15).hyperlink.target == o.link and o.link.startswith("https://"), f"link {tag}"
        assert "/" not in o.location and "surcharge" not in o.location.lower(), f"location {tag}"
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", o.checked), f"checked {tag}"
        assert o.currency in PER_USD, f"currency {tag}"
        if o.status == "Confirmed":
            assert o.amount and o.amount > 0, f"confirmed without price {tag}"
            assert evidence_key(o) in evidence, f"no evidence line {tag}"
            line = evidence[evidence_key(o)]
            used = line.rsplit("|", 2)[1].split()
            assert used == [o.currency, used[1]] and float(used[1]) == o.amount, f"amount differs from evidence {tag}: {used}"
            assert any(re.search(r"(?<![\d.,])" + re.escape(w) + r"(?!\d)", line.rsplit("|", 2)[0]) for w in spellings(o.amount)), \
                f"amount not in the evidence quote {tag}"
            assert re.search(r"shared|dedicated|CPU type not stated", f"{o.plan} {o.notes}", re.I), f"CPU type missing {tag}"
        else:
            assert re.fullmatch(r"Not confirmed \(.+\)", o.status) and o.amount is None, f"status {tag}"
        assert o.fits == "Yes" or re.fullmatch(r"(No|Not confirmed) \(.+\)", o.fits), f"fits {tag}"
        assert (o.vcpu is None or o.ram_gb is None) == o.fits.startswith("Not confirmed"), f"unknown size must read Not confirmed {tag}"
        assert (o.in_indonesia is None) == (o.location == "Not stated"), f"location and In Indonesia disagree {tag}"
        if o.fits == "Yes":
            assert (o.vcpu, o.ram_gb) == (16, 64), f"'Yes' is not 16/64 {tag}"
        if "term" in o.billing.lower():
            assert "renew" in o.notes.lower(), f"term price without renewal note {tag}"
        if "incl. tax" in o.price_text.lower():
            assert "before tax" in o.notes.lower(), f"tax-inclusive price without note {tag}"
    assert pv.cell(len(ordered) + 2, 1).value is None, "rows beyond the offers"
    footer = str(pv.cell(len(ordered) + 3, 1).value)
    assert "where the provider states it" in footer and all(str(v) in footer.replace(",", "") for v in (PER_USD["EUR"], PER_USD["IDR"], PER_USD["SGD"])), "footer"
    assert any(o.provider == "Biznet Gio" and "NEO Virtual Compute" in o.plan for o in OFFERS), "Biznet NEO Virtual Compute row missing"
    for p in ("AWS EC2", "Google Cloud", "Alibaba Cloud", "Tencent Cloud", "Huawei Cloud"):
        assert any(o.provider == p and o.in_indonesia for o in OFFERS), f"{p}: no Jakarta row"



def main() -> None:
    wb = openpyxl.load_workbook(XLSX)
    ws = wb.worksheets[0]
    assert [ws.cell(1, c).value for c in range(1, 8)] == HEADER, "header changed"

    last = 1 + len(ROWS)
    for i, (item, plan, period, qty, price, _note) in enumerate(ROWS, start=2):
        got = [ws.cell(i, c).value for c in range(1, 6)]
        assert got == [item, plan, period, qty, price], f"row {i}: {got}"
        f = ws.cell(i, 6)
        assert f.value == 0.11 and f.number_format == "0%", f"row {i} tax: {f.value} {f.number_format}"
        assert ws.cell(i, 7).value == f"=(1+F{i})*E{i}*D{i}", f"row {i} formula: {ws.cell(i, 7).value}"

    gt = last + 1
    assert ws.cell(gt, 1).value == "Grand Total", "grand total label"
    assert ws.cell(gt, 7).value == f"=SUM(G2:G{last})", f"grand total formula: {ws.cell(gt, 7).value}"

    for r in range(1, ws.max_row + 1):
        v = ws.cell(r, 7).value
        if isinstance(v, str) and v.startswith("=") and not (2 <= r <= gt):
            raise AssertionError(f"stray formula G{r}: {v}")

    note = str(ws.cell(gt + 2, 1).value or "")
    assert "Docker Desktop" in note and "optional" in note.lower(), f"note row: {note!r}"

    assumption = str(ws.cell(gt + 3, 1).value or "")
    assert "1 billing month" in assumption and "first year" in assumption, f"assumption row: {assumption!r}"

    total = round(sum(1.11 * price * qty for *_, qty, price, _n in ROWS), 2)
    assert total == EXPECTED_TOTAL, f"total {total} != {EXPECTED_TOTAL}"
    check_offers(wb)
    print(f"OK grand total {total}; {len(OFFERS)} offers")

if __name__ == "__main__":
    main()
