"""Verify budgetting.xlsx matches the budget design (see docs/superpowers/specs/2026-11-16-training-budget-design.md)."""
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).parent))
from build_budget import ROWS, XLSX  # noqa: E402

HEADER = ["Item Name", "Plan", "Period", "Quantity", "Price", "Tax (%)", "Total Amount"]
EXPECTED_TOTAL = 300.21  # 1.11 * (200 + 12 + 48 + 10.46)


def main() -> None:
    ws = openpyxl.load_workbook(XLSX).active
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
    print(f"OK grand total {total}")


if __name__ == "__main__":
    main()
