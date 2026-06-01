#!/usr/bin/env python3
"""Create a 20-item ponchi generation batch ledger.

The ledger is operational: existing final images are treated as legacy evidence,
not as proof that the new prompt/subject-stack/logo pipeline has been applied.
"""
from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
ENTRIES = REPO / "ledgers" / "entries.csv"
PROMPTS = REPO / "assets" / "ponchi" / "prompts"
FINAL = REPO / "assets" / "ponchi" / "final"
MATRIX = REPO / "docs" / "ponchi_logo_requirement_matrix_2026-06-01.md"
OUT = REPO / "ledgers" / "ponchi_generation_batches.csv"


@dataclass(frozen=True)
class LogoInfo:
    need: str = "unknown"
    status: str = "unclassified"
    asset: str = ""


KNOWN_BRAND_STATUS = {
    "Gemini": LogoInfo("required", "official_logo_source_review_required", ""),
    "Claude": LogoInfo("required", "official_logo_source_available_needs_import", ""),
    "ChatGPT": LogoInfo("required", "official_logo_source_review_required", ""),
    "Cursor": LogoInfo("required", "official_logo_source_available_needs_import", ""),
    "GitHub Copilot": LogoInfo(
        "required",
        "official_logo_applied",
        "assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Copilot_Lockup_Black_Clearspace.png",
    ),
    "Windsurf": LogoInfo("required", "blocked_brand_asset", ""),
    "Claude Code": LogoInfo("required", "official_logo_source_available_needs_import", ""),
    "Codex": LogoInfo("required", "official_logo_source_review_required", ""),
    "GitHub": LogoInfo(
        "required",
        "official_logo_applied",
        "assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png",
    ),
    "OpenAI": LogoInfo(
        "required",
        "official_logo_available",
        "assets/logos/openai/openai_wordmark_black_official_template_layer.png",
    ),
    "v0": LogoInfo("required", "official_logo_source_review_required", ""),
}


def natural_id_key(entry_id: str) -> tuple[str, int]:
    match = re.match(r"^([A-Z]+)-(\d+)$", entry_id)
    if not match:
        return (entry_id, 0)
    return (match.group(1), int(match.group(2)))


def load_logo_matrix(path: Path) -> dict[str, LogoInfo]:
    if not path.exists():
        return {}

    result: dict[str, LogoInfo] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0] == ":--":
            continue
        entry_id = cells[0].strip("`")
        if not re.match(r"^[A-Z]+-\d+$", entry_id):
            continue
        result[entry_id] = LogoInfo(
            need=cells[2].strip("`"),
            status=cells[3].strip("`"),
            asset="" if cells[4] == "none" else cells[4].strip("`"),
        )
    return result


def classify(row: dict[str, str], logo: LogoInfo, prompt_exists: bool) -> str:
    if logo.status == "blocked_brand_asset":
        return "blocked_brand_asset"
    if logo.status in {"official_logo_source_review_required", "official_logo_source_available_needs_import", "base_2to1_ready_logo_blocked"}:
        return "overlay_wait"
    if logo.status == "official_logo_applied":
        return "overlay_audit"
    if logo.status in {"official_logo_available", "official_overlay_ready"}:
        return "overlay_ready"
    if prompt_exists:
        return "prompt_review"
    return "brief_needed"


def next_action(stage: str) -> str:
    return {
        "brief_needed": "create subject_stack scene brief and prompt",
        "prompt_review": "lint prompt, generate 2:1 base, audit density",
        "overlay_wait": "do not final; import/confirm official logo asset first",
        "overlay_ready": "generate base if needed, then deterministic logo overlay",
        "overlay_audit": "review existing official overlay before final promotion",
        "blocked_brand_asset": "stop until official asset and usage conditions are confirmed",
    }.get(stage, "review manually")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args()

    if args.batch_size <= 0:
        raise SystemExit("--batch-size must be positive")
    if not ENTRIES.exists():
        raise SystemExit(f"missing entries csv: {ENTRIES}")

    logo_matrix = load_logo_matrix(MATRIX)
    final_ids = {path.stem for path in FINAL.glob("*.webp")}
    prompt_ids = {path.stem for path in PROMPTS.glob("*.md")}

    with ENTRIES.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row.get("status") != "archived"]

    rows.sort(key=lambda row: natural_id_key(row["new_id"]))

    output_rows: list[dict[str, str]] = []
    for index, row in enumerate(rows):
        entry_id = row["new_id"]
        batch_index = index // args.batch_size + 1
        item_index = index % args.batch_size + 1
        logo = logo_matrix.get(entry_id) or KNOWN_BRAND_STATUS.get(row.get("title", ""), LogoInfo())
        prompt_exists = entry_id in prompt_ids
        final_exists = entry_id in final_ids
        stage = classify(row, logo, prompt_exists)
        output_rows.append(
            {
                "batch_id": f"ponchi-batch-{batch_index:03d}",
                "batch_index": str(batch_index),
                "item_index": str(item_index),
                "entry_id": entry_id,
                "title": row.get("title", ""),
                "category": row.get("category", ""),
                "subtype": row.get("subtype", ""),
                "entry_status": row.get("status", ""),
                "md_path": row.get("path", ""),
                "legacy_final_exists": "yes" if final_exists else "no",
                "prompt_exists": "yes" if prompt_exists else "no",
                "logo_need": logo.need,
                "logo_status": logo.status,
                "official_asset": logo.asset,
                "pipeline_stage": stage,
                "confirmation_status": "not_reviewed",
                "next_action": next_action(stage),
            }
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0].keys()))
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"wrote {args.out}")
    print(f"entries={len(output_rows)} batch_size={args.batch_size} batches={(len(output_rows) + args.batch_size - 1) // args.batch_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
