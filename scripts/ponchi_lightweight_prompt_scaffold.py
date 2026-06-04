#!/usr/bin/env python3
"""Scaffold prompt files for lightweight ponchi regeneration batches."""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from ponchi_prompt_scaffold import make_prompt  # noqa: E402


BATCHES = REPO / "ledgers" / "ponchi_lightweight_regen_batches.csv"
VISIBLE_PLAN = REPO / "ledgers" / "ponchi_lightweight_visible_regen_plan.csv"
ENTRIES = REPO / "ledgers" / "entries.csv"
OUT_ROOT = REPO / "assets" / "ponchi" / "pipeline_prompts"


REGEN_NOTES = {
    "composition_regen": [
        "The existing image is treated as a weak mechanical 2:1 conversion.",
        "Do not preserve the old centered-box composition.",
        "Use the full horizontal canvas to show a meaningful flow, contrast, or layered structure.",
    ],
    "richer_scene_regen": [
        "The existing image is too dependent on a logo and sparse box-arrow graphics.",
        "Make the service use case visible through people, work context, and 2-4 substantial visual blocks.",
        "Do not create another logo-plus-document-node diagram.",
    ],
    "lightweight_quality_regen": [
        "The existing image is too lightweight in the visible gallery.",
        "Increase meaningful visual density with clearer blocks, stronger relationships, and more legible 200px silhouette.",
        "Do not merely add tiny cards or decorative dots; improve the conceptual scene.",
    ],
}


def read_csv(path: Path, key: str) -> dict[str, dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return {row[key]: row for row in csv.DictReader(handle)}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def pipeline_stage(row: dict[str, str]) -> str:
    logo_need = row.get("logo_need", "")
    logo_status = row.get("logo_status", "")
    if logo_status == "blocked_brand_asset":
        return "blocked_brand_asset"
    if logo_status in {"official_logo_applied", "official_logo_available", "official_overlay_ready"}:
        return "overlay_audit"
    if logo_need == "required":
        return "overlay_wait"
    return "brief_needed"


def prompt_row(batch_row: dict[str, str], entry: dict[str, str], visible: dict[str, str]) -> dict[str, str]:
    return {
        "entry_id": batch_row["entry_id"],
        "title": entry.get("title", batch_row.get("title", "")),
        "category": entry.get("category", ""),
        "subtype": entry.get("subtype", ""),
        "md_path": entry.get("path", ""),
        "pipeline_stage": pipeline_stage(visible),
        "logo_need": visible.get("logo_need", ""),
        "logo_status": visible.get("logo_status", ""),
        "official_asset": visible.get("official_asset", ""),
    }


def append_regen_notes(prompt: str, batch_row: dict[str, str], visible: dict[str, str]) -> str:
    notes = REGEN_NOTES.get(batch_row["regen_type"], [])
    lines = [
        "",
        "## Lightweight Regeneration Notes",
        "",
        f"- visible_rank: {batch_row['visible_rank']}",
        f"- file_size_kb: {batch_row['file_size_kb']}",
        f"- current_score: {batch_row['score']}",
        f"- regen_type: `{batch_row['regen_type']}`",
        f"- current_action: `{batch_row['current_action']}`",
        f"- user_visible_decision: `regen_user_ng_visible`",
        f"- target: {batch_row['target_brief']}",
    ]
    for note in notes:
        lines.append(f"- {note}")
    if visible.get("decision") == "keep_user_ok":
        lines.append("- This entry was user-approved and should not be regenerated in this batch.")
    return prompt.rstrip() + "\n" + "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_id", nargs="?", default=None)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    batch_rows = read_rows(BATCHES)
    entries = read_csv(ENTRIES, "new_id")
    visible_rows = read_csv(VISIBLE_PLAN, "entry_id")
    if args.all:
        selected = batch_rows
    elif args.batch_id:
        selected = [row for row in batch_rows if row["batch_id"] == args.batch_id]
    else:
        raise SystemExit("pass a batch_id or --all")
    if not selected:
        raise SystemExit("no matching rows")

    wrote = 0
    skipped = 0
    for batch_row in selected:
        entry_id = batch_row["entry_id"]
        entry = entries.get(entry_id)
        visible = visible_rows.get(entry_id)
        if not entry or not visible:
            print(f"skip missing metadata: {entry_id}")
            continue
        out_dir = OUT_ROOT / batch_row["batch_id"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / f"{entry_id}.md"
        if out.exists() and not args.overwrite:
            skipped += 1
            continue
        prompt = make_prompt(prompt_row(batch_row, entry, visible))
        prompt = append_regen_notes(prompt, batch_row, visible)
        out.write_text(prompt, encoding="utf-8")
        wrote += 1

    print(f"wrote={wrote} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
