#!/usr/bin/env python3
"""Generate a current-state audit markdown for one ponchi batch."""
from __future__ import annotations

import argparse
import csv
import subprocess
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
LEDGER = REPO / "ledgers" / "ponchi_generation_batches.csv"
PROMPTS = REPO / "assets" / "ponchi" / "pipeline_prompts"
EXPERIMENTS = REPO / "assets" / "ponchi" / "experiments" / "batches"
OUT_DIR = REPO / "docs" / "ponchi_batch_audits"
BASE_AUDIT_PREFIX = REPO / "ledgers"


def load_batch(ledger: Path, batch_id: str) -> list[dict[str, str]]:
    with ledger.open("r", encoding="utf-8-sig", newline="") as handle:
        return [row for row in csv.DictReader(handle) if row["batch_id"] == batch_id]


def run_lint(prompt_dir: Path) -> tuple[str, str]:
    if not prompt_dir.exists():
        return "missing", "prompt directory does not exist"
    files = sorted(prompt_dir.glob("*.md"))
    if not files:
        return "missing", "no prompt files"
    result = subprocess.run(
        ["python", "scripts/ponchi_prompt_lint.py", *[str(path) for path in files]],
        cwd=REPO,
        text=True,
        capture_output=True,
    )
    status = "pass" if result.returncode == 0 else "fail"
    output = (result.stdout + result.stderr).strip()
    return status, output


def load_base_audit(batch_id: str) -> dict[str, dict[str, str]]:
    path = BASE_AUDIT_PREFIX / f"{batch_id.replace('-', '_')}_base_audit.csv"
    if not path.exists():
        return {}
    result: dict[str, dict[str, str]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            stem = Path(row["file"]).name.split("_base_", 1)[0]
            result[stem] = row
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_id")
    parser.add_argument("--ledger", type=Path, default=LEDGER)
    parser.add_argument("--out-dir", type=Path, default=OUT_DIR)
    args = parser.parse_args()

    rows = load_batch(args.ledger, args.batch_id)
    if not rows:
        raise SystemExit(f"batch not found: {args.batch_id}")

    prompt_dir = PROMPTS / args.batch_id
    experiment_dir = EXPERIMENTS / args.batch_id
    prompt_files = sorted(prompt_dir.glob("*.md")) if prompt_dir.exists() else []
    base_images = sorted(experiment_dir.glob("*_base_1254x627.png")) if experiment_dir.exists() else []
    overlay_images = sorted(experiment_dir.glob("*_overlay_1254x627.png")) if experiment_dir.exists() else []
    contact_sheets = sorted(experiment_dir.glob("*contact*.png")) if experiment_dir.exists() else []
    lint_status, lint_output = run_lint(prompt_dir)
    stage_counts = Counter(row["pipeline_stage"] for row in rows)
    base_audit_rows = load_base_audit(args.batch_id)
    base_status_counts = Counter(row.get("status", "missing") for row in base_audit_rows.values())

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out = args.out_dir / f"{args.batch_id}.md"

    lines: list[str] = []
    lines.append(f"# {args.batch_id} audit")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- items: {len(rows)}")
    lines.append(f"- prompt files: {len(prompt_files)}")
    lines.append(f"- prompt lint: `{lint_status}`")
    lines.append(f"- base images: {len(base_images)}")
    lines.append(f"- overlay images: {len(overlay_images)}")
    lines.append(f"- contact sheets: {len(contact_sheets)}")
    if base_audit_rows:
        lines.append(
            "- base audit: "
            + ", ".join(f"`{status}` {count}" for status, count in sorted(base_status_counts.items()))
        )
    lines.append("")
    lines.append("## Stage Counts")
    lines.append("")
    lines.append("| stage | count |")
    lines.append("| --- | ---: |")
    for stage, count in sorted(stage_counts.items()):
        lines.append(f"| `{stage}` | {count} |")
    lines.append("")
    lines.append("## Prompt Lint Output")
    lines.append("")
    lines.append("```text")
    lines.append(lint_output)
    lines.append("```")
    lines.append("")
    legacy_audit = args.out_dir / f"{args.batch_id}-legacy-final-image-audit.md"
    legacy_contact = args.out_dir / f"{args.batch_id}-legacy-final-contact-sheet.png"
    if legacy_audit.exists() or legacy_contact.exists():
        lines.append("## Legacy Final Image Audit")
        lines.append("")
        lines.append("Existing `assets/ponchi/final/` images are legacy evidence only. Use this audit to decide whether to regenerate; do not treat these files as approved final candidates.")
        lines.append("")
        if legacy_audit.exists():
            lines.append(f"- image audit: `{legacy_audit.name}`")
        if legacy_contact.exists():
            lines.append(f"- contact sheet: `{legacy_contact.name}`")
        lines.append("")
    base_audit_path = args.out_dir / f"{args.batch_id}-base-image-audit.md"
    base_contact = args.out_dir / f"{args.batch_id}-base-contact-sheet.png"
    if base_audit_path.exists() or base_contact.exists():
        lines.append("## Generated Base Image Audit")
        lines.append("")
        lines.append("Generated base images must pass size, density, and logo-clearspace checks before official logo overlays or final-candidate staging.")
        lines.append("")
        if base_audit_path.exists():
            lines.append(f"- image audit: `{base_audit_path.name}`")
        if base_contact.exists():
            lines.append(f"- contact sheet: `{base_contact.name}`")
        lines.append("")
    lines.append("## Items")
    lines.append("")
    lines.append("| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |")
    lines.append("| ---: | --- | --- | --- | --- | --- | --- | --- | --- |")
    for row in rows:
        entry_id = row["entry_id"]
        prompt = "yes" if (prompt_dir / f"{entry_id}.md").exists() else "no"
        base = "yes" if any(path.name.startswith(f"{entry_id}_") for path in base_images) else "no"
        base_status = base_audit_rows.get(entry_id, {}).get("status", "")
        overlay = "yes" if any(path.name.startswith(f"{entry_id}_") for path in overlay_images) else "no"
        lines.append(
            f"| {row['item_index']} | `{entry_id}` | {row['title']} | `{row['pipeline_stage']}` | {prompt} | {base} | `{base_status}` | {overlay} | `{row['confirmation_status']}` |"
        )
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
