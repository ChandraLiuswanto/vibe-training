"""Verify budgetting.xlsx matches the budget design (see docs/superpowers/specs/2026-11-16-training-budget-design.md)."""
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).parent))
from build_budget import PROVIDER_HEADER, PROVIDERS, ROWS, XLSX  # noqa: E402

HEADER = ["Item Name", "Plan", "Period", "Quantity", "Price", "Tax (%)", "Total Amount"]
EXPECTED_TOTAL = 602.13  # 1.11 * (200 + 12 + 320 + 10.46)


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
    pv = wb["VPS Providers"]
    assert [pv.cell(1, c).value for c in range(1, 13)] == PROVIDER_HEADER, "provider header"
    for r, row in enumerate(PROVIDERS, start=2):
        assert pv.cell(r, 1).value == row[0], f"provider row {r}"
        assert pv.cell(r, 12).hyperlink and pv.cell(r, 12).hyperlink.target.startswith("https://"), f"link row {r}"
    fits = [p for p in PROVIDERS if p[9] == "Yes"]
    assert all(p[2] == 16 and p[3] == 64 for p in fits), "a 'Yes' row is not 16/64"
    print(f"OK grand total {total}; {len(PROVIDERS)} providers")


if __name__ == "__main__":
    main()
