#!/usr/bin/env python3
"""Collect the latest generated image outputs into a ponchi batch folder.

Run this immediately after generating one batch in prompt order. It maps the
latest N generated PNGs to the N prompt files in the batch directory.
"""
from __future__ import annotations

import argparse
import csv
import os
import shutil
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("This script requires Pillow. Use the bundled Codex Python runtime.") from exc


REPO = Path(__file__).resolve().parents[1]
DEFAULT_GENERATED_ROOT = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "generated_images"
PROMPTS = REPO / "assets" / "ponchi" / "pipeline_prompts"
OUT_ROOT = REPO / "assets" / "ponchi" / "experiments" / "batches"


def natural_key(path: Path) -> tuple[str, int]:
    stem = path.stem
    if "-" not in stem:
        return (stem, 0)
    prefix, _, number = stem.partition("-")
    try:
        return (prefix, int(number))
    except ValueError:
        return (prefix, 0)


def prompt_entries(batch_id: str) -> list[str]:
    prompt_dir = PROMPTS / batch_id
    if not prompt_dir.exists():
        raise SystemExit(f"missing prompt dir: {prompt_dir}")
    return [path.stem for path in sorted(prompt_dir.glob("*.md"), key=natural_key)]


def selected_entries(batch_id: str, entries_arg: str | None) -> list[str]:
    entries = prompt_entries(batch_id)
    if not entries_arg:
        return entries
    requested = [entry.strip() for entry in entries_arg.split(",") if entry.strip()]
    missing = [entry for entry in requested if entry not in entries]
    if missing:
        raise SystemExit(f"entries not found in {batch_id}: {', '.join(missing)}")
    return requested


def latest_pngs(root: Path, count: int) -> list[Path]:
    if not root.exists():
        raise SystemExit(f"missing generated image root: {root}")
    files = sorted(root.glob("**/*.png"), key=lambda path: path.stat().st_mtime)
    if len(files) < count:
        raise SystemExit(f"need {count} generated pngs, found {len(files)} in {root}")
    return files[-count:]


def bbox_coverage(path: Path) -> float:
    image = Image.open(path).convert("RGB")
    pixels = image.load()
    xs: list[int] = []
    ys: list[int] = []
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            if min(255 - r, 255 - g, 255 - b) > 18 or (255 - r) + (255 - g) + (255 - b) > 55:
                xs.append(x)
                ys.append(y)
    if not xs:
        return 0.0
    area = (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)
    return area / (image.width * image.height)


def make_contact_sheet(rows: list[dict[str, str]], out_dir: Path) -> Path:
    thumb_w, thumb_h = 376, 188
    label_h = 54
    cols = 2
    row_count = (len(rows) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, row_count * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for index, row in enumerate(rows):
        col = index % cols
        grid_row = index // cols
        x0 = col * thumb_w
        y0 = grid_row * (thumb_h + label_h)
        image = Image.open(out_dir / row["standard_file"]).convert("RGB")
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        draw.rectangle([x0, y0, x0 + thumb_w - 1, y0 + thumb_h + label_h - 1], outline=(210, 210, 210))
        draw.text((x0 + 8, y0 + 8), f"{row['entry_id']} coverage {row['bbox_coverage']}", fill=(20, 20, 20))
        draw.text((x0 + 8, y0 + 28), row["standard_file"][:46], fill=(80, 80, 80))
        sheet.paste(image, (x0 + (thumb_w - image.width) // 2, y0 + label_h + (thumb_h - image.height) // 2))
    out = out_dir / "contact_sheet.png"
    sheet.save(out)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_id")
    parser.add_argument("--generated-root", type=Path, default=DEFAULT_GENERATED_ROOT)
    parser.add_argument("--out-root", type=Path, default=OUT_ROOT)
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--count", type=int, default=None)
    parser.add_argument(
        "--entries",
        default=None,
        help="Comma-separated entry IDs to map to the latest generated PNGs.",
    )
    args = parser.parse_args()

    entries = selected_entries(args.batch_id, args.entries)
    if args.count is not None:
        if args.entries:
            raise SystemExit("--count cannot be combined with --entries")
        entries = entries[: args.count]
    files = latest_pngs(args.generated_root, len(entries))

    out_dir = args.out_dir if args.out_dir else args.out_root / args.batch_id
    out_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str]] = []
    for entry_id, source in zip(entries, files):
        raw_name = f"{entry_id}_base_raw.png"
        standard_name = f"{entry_id}_base_1254x627.png"
        raw_path = out_dir / raw_name
        standard_path = out_dir / standard_name
        shutil.copy2(source, raw_path)
        image = Image.open(source).convert("RGB")
        image.resize((1254, 627), Image.Resampling.LANCZOS).save(standard_path, optimize=True)
        coverage = bbox_coverage(standard_path)
        rows.append(
            {
                "entry_id": entry_id,
                "source_file": str(source),
                "raw_file": raw_name,
                "raw_size": f"{image.width}x{image.height}",
                "standard_file": standard_name,
                "standard_size": "1254x627",
                "bbox_coverage": f"{coverage:.3f}",
            }
        )

    manifest = out_dir / "manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    sheet = make_contact_sheet(rows, out_dir)
    print(f"wrote {manifest}")
    print(f"wrote {sheet}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
