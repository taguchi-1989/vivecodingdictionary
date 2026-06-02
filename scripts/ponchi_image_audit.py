#!/usr/bin/env python3
"""Audit ponchi image density and logo clearspace cleanliness."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("This script requires Pillow. Use the bundled Codex Python runtime.") from exc


def ink_mask(image: Image.Image) -> list[tuple[int, int]]:
    rgb = image.convert("RGB")
    pixels = rgb.load()
    ink: list[tuple[int, int]] = []
    for y in range(rgb.height):
        for x in range(rgb.width):
            r, g, b = pixels[x, y]
            if min(255 - r, 255 - g, 255 - b) > 18 or (255 - r) + (255 - g) + (255 - b) > 55:
                ink.append((x, y))
    return ink


def bbox_coverage(image: Image.Image, ink: list[tuple[int, int]]) -> float:
    if not ink:
        return 0.0
    xs = [point[0] for point in ink]
    ys = [point[1] for point in ink]
    return ((max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)) / (image.width * image.height)


def clearspace_ink_ratio(image: Image.Image, x_start_ratio: float, y_end_ratio: float) -> float:
    rgb = image.convert("RGB")
    pixels = rgb.load()
    x_start = int(rgb.width * x_start_ratio)
    y_end = int(rgb.height * y_end_ratio)
    total = max(1, (rgb.width - x_start) * y_end)
    ink = 0
    for y in range(y_end):
        for x in range(x_start, rgb.width):
            r, g, b = pixels[x, y]
            if min(255 - r, 255 - g, 255 - b) > 18 or (255 - r) + (255 - g) + (255 - b) > 55:
                ink += 1
    return ink / total


def entry_id_from_path(path: Path) -> str:
    name = path.name
    for suffix in (
        "_base_1254x627.png",
        "_overlay_1254x627.png",
        "_base_selected_1254x627.png",
        ".webp",
        ".png",
    ):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return path.stem.split("_", 1)[0]


def load_clearspace_requirements(args: argparse.Namespace) -> dict[str, bool]:
    if not args.ledger or not args.batch_id:
        return {}
    requirements: dict[str, bool] = {}
    with args.ledger.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("batch_id") != args.batch_id:
                continue
            entry_id = row.get("entry_id", "")
            logo_need = row.get("logo_need", "")
            logo_status = row.get("logo_status", "")
            requirements[entry_id] = not (
                logo_need in {"not_needed", "avoid", "none"}
                or logo_status in {"logo_avoid", "not_required"}
            )
    return requirements


def audit_image(path: Path, args: argparse.Namespace, clearspace_requirements: dict[str, bool]) -> dict[str, str]:
    image = Image.open(path)
    ink = ink_mask(image)
    density = bbox_coverage(image, ink)
    clearspace = clearspace_ink_ratio(image, args.clearspace_x_start, args.clearspace_y_end)
    entry_id = entry_id_from_path(path)
    clearspace_required = clearspace_requirements.get(entry_id, True)
    size_ok = image.size == (args.width, args.height)
    density_ok = density >= args.min_bbox_coverage
    clearspace_ok = (clearspace <= args.max_clearspace_ink) if clearspace_required else True
    status = "pass" if size_ok and density_ok and clearspace_ok else "review"
    return {
        "file": str(path),
        "entry_id": entry_id,
        "size": f"{image.width}x{image.height}",
        "size_ok": str(size_ok).lower(),
        "bbox_coverage": f"{density:.3f}",
        "density_ok": str(density_ok).lower(),
        "clearspace_required": str(clearspace_required).lower(),
        "clearspace_ink_ratio": f"{clearspace:.4f}",
        "clearspace_ok": str(clearspace_ok).lower(),
        "status": status,
    }


def write_markdown(rows: list[dict[str, str]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("# Ponchi Image Audit\n\n")
        handle.write("| file | size | bbox | clearspace required | clearspace ink | status |\n")
        handle.write("| :-- | :-- | --: | :-- | --: | :-- |\n")
        for row in rows:
            handle.write(
                "| "
                f"`{Path(row['file']).name}` | `{row['size']}` | "
                f"{row['bbox_coverage']} | `{row['clearspace_required']}` | "
                f"{row['clearspace_ink_ratio']} | "
                f"`{row['status']}` |\n"
            )


def write_contact_sheet(rows: list[dict[str, str]], out: Path) -> None:
    thumb_w, thumb_h = 418, 209
    label_h = 50
    cols = 3
    row_count = (len(rows) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, row_count * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for index, row in enumerate(rows):
        source = Path(row["file"])
        col = index % cols
        sheet_row = index // cols
        x0 = col * thumb_w
        y0 = sheet_row * (thumb_h + label_h)
        image = Image.open(source).convert("RGB")
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        outline = (110, 170, 110) if row["status"] == "pass" else (210, 140, 80)
        draw.rectangle([x0, y0, x0 + thumb_w - 1, y0 + thumb_h + label_h - 1], outline=outline)
        draw.text((x0 + 8, y0 + 8), f"{source.stem}", fill=(20, 20, 20))
        draw.text(
            (x0 + 8, y0 + 27),
            f"bbox {row['bbox_coverage']}  clear {row['clearspace_ink_ratio']}  {row['status']}",
            fill=(80, 80, 80),
        )
        sheet.paste(image, (x0 + (thumb_w - image.width) // 2, y0 + label_h + (thumb_h - image.height) // 2))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--out-csv", type=Path, default=None)
    parser.add_argument("--out-md", type=Path, default=None)
    parser.add_argument("--contact-sheet", type=Path, default=None)
    parser.add_argument("--width", type=int, default=1254)
    parser.add_argument("--height", type=int, default=627)
    parser.add_argument("--min-bbox-coverage", type=float, default=0.50)
    parser.add_argument("--clearspace-x-start", type=float, default=0.60)
    parser.add_argument("--clearspace-y-end", type=float, default=0.25)
    parser.add_argument("--max-clearspace-ink", type=float, default=0.015)
    parser.add_argument("--ledger", type=Path, default=None)
    parser.add_argument("--batch-id", default=None)
    args = parser.parse_args()

    clearspace_requirements = load_clearspace_requirements(args)
    rows = [audit_image(path, args, clearspace_requirements) for path in args.images]
    if args.out_csv:
        args.out_csv.parent.mkdir(parents=True, exist_ok=True)
        with args.out_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    if args.out_md:
        write_markdown(rows, args.out_md)
    if args.contact_sheet:
        write_contact_sheet(rows, args.contact_sheet)
    for row in rows:
        print(
            f"{Path(row['file']).name}: {row['status']} "
            f"size={row['size']} bbox={row['bbox_coverage']} "
            f"clearspace={row['clearspace_ink_ratio']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
