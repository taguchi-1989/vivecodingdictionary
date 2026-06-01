#!/usr/bin/env python3
"""Render one ponchi generation batch as a Markdown review checklist."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
LEDGER = REPO / "ledgers" / "ponchi_generation_batches.csv"
OUT_DIR = REPO / "ledgers" / "ponchi_batches"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_id", help="Example: ponchi-batch-001")
    parser.add_argument("--ledger", type=Path, default=LEDGER)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args()

    if not args.ledger.exists():
        raise SystemExit(f"missing batch ledger: {args.ledger}")

    with args.ledger.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["batch_id"] == args.batch_id]

    if not rows:
        raise SystemExit(f"batch not found: {args.batch_id}")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out = args.out_dir / f"{args.batch_id}.md"

    lines: list[str] = []
    lines.append(f"# {args.batch_id} review")
    lines.append("")
    lines.append("## Gate")
    lines.append("")
    lines.append("- Do not promote any item to final until this batch is reviewed.")
    lines.append("- Generate or update scene briefs first, then lint prompts, then generate base images.")
    lines.append("- Stop brand entries at `overlay_wait` until official assets are imported and recorded.")
    lines.append("")
    lines.append("## Items")
    lines.append("")
    lines.append("| # | entry | title | stage | logo status | next action | confirmation |")
    lines.append("| ---: | --- | --- | --- | --- | --- | --- |")
    for row in rows:
        lines.append(
            "| {item_index} | `{entry_id}` | {title} | `{pipeline_stage}` | `{logo_status}` | {next_action} | `{confirmation_status}` |".format(
                **row
            )
        )
    lines.append("")
    lines.append("## Batch Commands")
    lines.append("")
    lines.append("```powershell")
    lines.append("python scripts\\ponchi_batch_plan.py --batch-size 20")
    lines.append(f"python scripts\\ponchi_batch_report.py {args.batch_id}")
    lines.append("python scripts\\ponchi_prompt_lint.py <prompt-files>")
    lines.append("```")
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
