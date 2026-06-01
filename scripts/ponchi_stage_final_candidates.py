#!/usr/bin/env python3
"""Stage reviewed ponchi outputs as final candidates without touching final/."""
from __future__ import annotations

import argparse
import csv
import shutil
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("This script requires Pillow. Use the bundled Codex Python runtime.") from exc


REPO = Path(__file__).resolve().parents[1]
LEDGER = REPO / "ledgers" / "ponchi_generation_batches.csv"
BATCH_ROOT = REPO / "assets" / "ponchi" / "experiments" / "batches"
OUT_ROOT = REPO / "assets" / "ponchi" / "final_candidates"
AUDIT_ROOT = REPO / "docs" / "ponchi_batch_audits"


def load_rows(batch_id: str, ledger: Path) -> list[dict[str, str]]:
    with ledger.open("r", encoding="utf-8-sig", newline="") as handle:
        return [row for row in csv.DictReader(handle) if row["batch_id"] == batch_id]


def candidate_source(row: dict[str, str], batch_dir: Path, include_overlay_audit: bool) -> tuple[Path, str] | None:
    entry_id = row["entry_id"]
    confirmation = row["confirmation_status"]
    stage = row["pipeline_stage"]
    if confirmation in {"rerun_prompt", "rerun_density", "rerun_clearspace", "overlay_wait", "reject"}:
        return None

    if confirmation == "accept_overlay":
        source = batch_dir / f"{entry_id}_overlay_1254x627.png"
        return (source, "accepted_overlay") if source.exists() else None
    if confirmation == "accept_base":
        source = batch_dir / f"{entry_id}_base_1254x627.png"
        return (source, "accepted_base") if source.exists() else None
    if include_overlay_audit and stage == "overlay_audit":
        source = batch_dir / f"{entry_id}_overlay_1254x627.png"
        return (source, "review_pending_overlay") if source.exists() else None
    return None


def make_contact_sheet(rows: list[dict[str, str]], out_dir: Path) -> Path:
    thumb_w, thumb_h = 418, 209
    label_h = 54
    cols = 2
    row_count = max(1, (len(rows) + cols - 1) // cols)
    sheet = Image.new("RGB", (cols * thumb_w, row_count * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for index, row in enumerate(rows):
        col = index % cols
        grid_row = index // cols
        x0 = col * thumb_w
        y0 = grid_row * (thumb_h + label_h)
        image = Image.open(out_dir / row["candidate_png"]).convert("RGB")
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        draw.rectangle([x0, y0, x0 + thumb_w - 1, y0 + thumb_h + label_h - 1], outline=(140, 170, 210))
        draw.text((x0 + 8, y0 + 8), f"{row['entry_id']} {row['title']}", fill=(20, 20, 20))
        draw.text((x0 + 8, y0 + 28), row["candidate_status"], fill=(80, 80, 80))
        sheet.paste(image, (x0 + (thumb_w - image.width) // 2, y0 + label_h + (thumb_h - image.height) // 2))
    out = out_dir / "final_candidates_contact_sheet.png"
    sheet.save(out)
    return out


def write_audit(batch_id: str, rows: list[dict[str, str]], out_dir: Path, contact_sheet: Path) -> Path:
    AUDIT_ROOT.mkdir(parents=True, exist_ok=True)
    out = AUDIT_ROOT / f"{batch_id}-final-candidates.md"
    lines = [
        f"# {batch_id} final candidates",
        "",
        "These files are staged review candidates. They do not overwrite `assets/ponchi/final/`.",
        "",
        "## Contact Sheet",
        "",
        f"`{contact_sheet.relative_to(REPO).as_posix()}`",
        "",
        "## Candidates",
        "",
        "| entry | title | source | candidate png | candidate webp | status |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            "| "
            f"`{row['entry_id']}` | {row['title']} | `{row['source_type']}` | "
            f"`{row['candidate_png']}` | `{row['candidate_webp']}` | "
            f"`{row['candidate_status']}` |"
        )
    lines.extend(
        [
            "",
            "## Gate",
            "",
            "- Promote to `assets/ponchi/final/` only after visual confirmation.",
            "- Keep source official-logo provenance in `docs/brand_usage_audit.md`.",
            "- Keep rejected candidates in this folder for audit history unless the batch is intentionally reset.",
        ]
    )
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_id")
    parser.add_argument("--ledger", type=Path, default=LEDGER)
    parser.add_argument("--batch-root", type=Path, default=BATCH_ROOT)
    parser.add_argument("--out-root", type=Path, default=OUT_ROOT)
    parser.add_argument(
        "--include-overlay-audit",
        action="store_true",
        help="Stage overlay_audit items as review-pending candidates before user acceptance.",
    )
    args = parser.parse_args()

    rows = load_rows(args.batch_id, args.ledger)
    if not rows:
        raise SystemExit(f"batch not found: {args.batch_id}")
    batch_dir = args.batch_root / args.batch_id
    if not batch_dir.exists():
        raise SystemExit(f"batch image dir not found: {batch_dir}")

    out_dir = args.out_root / args.batch_id
    out_dir.mkdir(parents=True, exist_ok=True)
    for stale in out_dir.glob("*_candidate.png"):
        stale.unlink()
    for stale in out_dir.glob("*_candidate.webp"):
        stale.unlink()
    for stale in (out_dir / "manifest.csv", out_dir / "final_candidates_contact_sheet.png"):
        if stale.exists():
            stale.unlink()
    staged: list[dict[str, str]] = []
    for row in rows:
        source_info = candidate_source(row, batch_dir, args.include_overlay_audit)
        if not source_info:
            continue
        source, source_type = source_info
        if not source.exists():
            continue

        png_name = f"{row['entry_id']}_candidate.png"
        webp_name = f"{row['entry_id']}_candidate.webp"
        png_path = out_dir / png_name
        webp_path = out_dir / webp_name
        shutil.copy2(source, png_path)
        Image.open(source).convert("RGB").save(webp_path, "WEBP", quality=92, method=6)
        staged.append(
            {
                "entry_id": row["entry_id"],
                "title": row["title"],
                "source_file": str(source.relative_to(REPO)),
                "source_type": source_type,
                "candidate_png": png_name,
                "candidate_webp": webp_name,
                "candidate_status": "review_pending" if source_type.startswith("review_pending") else "accepted",
            }
        )

    if not staged:
        raise SystemExit("no candidates staged")

    manifest = out_dir / "manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(staged[0].keys()))
        writer.writeheader()
        writer.writerows(staged)
    contact_sheet = make_contact_sheet(staged, out_dir)
    audit = write_audit(args.batch_id, staged, out_dir, contact_sheet)
    print(f"staged {len(staged)} candidate(s)")
    print(f"wrote {manifest}")
    print(f"wrote {contact_sheet}")
    print(f"wrote {audit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
