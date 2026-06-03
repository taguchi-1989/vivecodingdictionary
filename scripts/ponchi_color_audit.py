#!/usr/bin/env python3
"""Audit ponchi candidates for generated-body color policy drift."""
from __future__ import annotations

import argparse
import colorsys
import csv
import math
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("This script requires Pillow. Use the bundled Codex Python runtime.") from exc

try:
    import numpy as np
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("This script requires NumPy. Use the bundled Codex Python runtime.") from exc


REPO = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST_ROOT = REPO / "assets" / "ponchi" / "final_candidates"
DEFAULT_OUT_CSV = REPO / "ledgers" / "ponchi_color_audit.csv"
DEFAULT_OUT_MD = REPO / "docs" / "ponchi_color_audit_summary.md"
DEFAULT_CONTACT = REPO / "docs" / "ponchi_batch_audits" / "ponchi-color-audit-contact-sheet.png"

ALLOWED_HEX = {
    "#FFFFFF": (255, 255, 255),
    "#F7F9FC": (247, 249, 252),
    "#1A1A1A": (26, 26, 26),
    "#6B7280": (107, 114, 128),
    "#EAF1FB": (234, 241, 251),
    "#D6E6FA": (214, 230, 250),
    "#8DB7E8": (141, 183, 232),
    "#3F7FD1": (63, 127, 209),
    "#123E82": (18, 62, 130),
}


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO).as_posix()
    except ValueError:
        return str(path)


def entry_id_from_path(path: Path) -> str:
    name = path.name
    for suffix in (
        "_candidate.png",
        "_candidate.webp",
        "_base_1254x627.png",
        "_overlay_1254x627.png",
        ".png",
        ".webp",
    ):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return path.stem.split("_", 1)[0]


def parse_rect(value: str) -> tuple[int, int, int, int]:
    parts = [int(part.strip()) for part in value.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("rect must be x,y,w,h")
    x, y, w, h = parts
    if w < 0 or h < 0:
        raise argparse.ArgumentTypeError("rect width and height must be non-negative")
    return (x, y, x + w, y + h)


def in_rects(x: int, y: int, rects: list[tuple[int, int, int, int]]) -> bool:
    return any(left <= x < right and top <= y < bottom for left, top, right, bottom in rects)


def color_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return math.sqrt(sum((a[index] - b[index]) ** 2 for index in range(3)))


def color_name(hue_degrees: float, saturation: float, value: float) -> str:
    if value < 0.18:
        return "dark"
    if saturation < 0.12:
        return "neutral"
    hue = hue_degrees % 360
    if hue < 18 or hue >= 345:
        return "red"
    if hue < 45:
        return "orange"
    if hue < 70:
        return "yellow"
    if hue < 165:
        return "green"
    if hue < 195:
        return "cyan_teal"
    if hue < 235:
        return "blue"
    if hue < 285:
        return "purple"
    if hue < 345:
        return "magenta"
    return "other"


def is_allowed_rgb(
    rgb: tuple[int, int, int],
    palette_tolerance: float,
    neutral_sat_limit: float,
    blue_hue_min: float,
    blue_hue_max: float,
) -> bool:
    if min(color_distance(rgb, allowed) for allowed in ALLOWED_HEX.values()) <= palette_tolerance:
        return True

    r, g, b = [channel / 255 for channel in rgb]
    hue, saturation, value = colorsys.rgb_to_hsv(r, g, b)
    hue_degrees = hue * 360

    if saturation <= neutral_sat_limit:
        return True

    # Permit antialiased or shaded pixels that still read as the approved blue
    # family. Teal/cyan drift and purple-blue drift remain off-policy.
    if blue_hue_min <= hue_degrees <= blue_hue_max and saturation <= 0.72:
        return True

    return False


def choose_audit_file_from_manifest(candidate_dir: Path, row: dict[str, str]) -> tuple[Path, str]:
    source_raw = row.get("source_file", "")
    source = (REPO / source_raw.replace("\\", "/")).resolve() if source_raw else candidate_dir / row["candidate_png"]
    source_type = row.get("source_type", "")
    entry_id = row.get("entry_id") or entry_id_from_path(source)
    if source_type.endswith("overlay") or "_overlay_1254x627" in source.name:
        base = source.with_name(f"{entry_id}_base_1254x627.png")
        if base.exists():
            return base, "source_base_for_overlay"
    if source.exists():
        return source, "source_image"
    return candidate_dir / row["candidate_png"], "candidate_image"


def manifest_rows(root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for manifest in sorted(root.glob("ponchi-batch-*/manifest.csv")):
        batch_id = manifest.parent.name
        with manifest.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                audit_file, audit_source_type = choose_audit_file_from_manifest(manifest.parent, row)
                candidate = manifest.parent / row["candidate_png"]
                rows.append(
                    {
                        "batch_id": batch_id,
                        "entry_id": row["entry_id"],
                        "title": row.get("title", ""),
                        "candidate_file": rel(candidate),
                        "audited_file": rel(audit_file),
                        "audit_source_type": audit_source_type,
                        "candidate_status": row.get("candidate_status", ""),
                        "source_type": row.get("source_type", ""),
                    }
                )
    return rows


def direct_image_rows(images: list[Path]) -> list[dict[str, str]]:
    return [
        {
            "batch_id": image.parent.name,
            "entry_id": entry_id_from_path(image),
            "title": "",
            "candidate_file": rel(image),
            "audited_file": rel(image),
            "audit_source_type": "direct_image",
            "candidate_status": "",
            "source_type": "",
        }
        for image in images
    ]


def audit_row(
    row: dict[str, str],
    args: argparse.Namespace,
    ignore_rects: list[tuple[int, int, int, int]],
) -> dict[str, str]:
    path = REPO / row["audited_file"]
    if not path.exists():
        return {
            **row,
            "size": "missing",
            "inspected_pixels": "0",
            "disallowed_pixels": "0",
            "disallowed_ratio": "1.000000",
            "disallowed_bbox": "",
            "dominant_disallowed": "missing",
            "status": "missing",
            "notes": "audited file not found",
        }

    image = Image.open(path).convert("RGBA")
    data = np.asarray(image, dtype=np.uint8)
    rgb = data[:, :, :3].astype(np.float32)
    alpha = data[:, :, 3]

    valid_mask = alpha >= args.alpha_min
    for left, top, right, bottom in ignore_rects:
        valid_mask[max(0, top) : min(image.height, bottom), max(0, left) : min(image.width, right)] = False

    inspected = int(valid_mask.sum())
    if inspected == 0:
        disallowed_mask = np.zeros((image.height, image.width), dtype=bool)
        ratio = 0.0
    else:
        allowed_stack = np.asarray(list(ALLOWED_HEX.values()), dtype=np.float32)
        diff = rgb[:, :, None, :] - allowed_stack[None, None, :, :]
        min_distance = np.sqrt(np.sum(diff * diff, axis=3)).min(axis=2)
        near_allowed = min_distance <= args.palette_tolerance

        r = rgb[:, :, 0] / 255.0
        g = rgb[:, :, 1] / 255.0
        b = rgb[:, :, 2] / 255.0
        maxc = np.maximum(np.maximum(r, g), b)
        minc = np.minimum(np.minimum(r, g), b)
        delta = maxc - minc
        saturation = np.zeros_like(maxc)
        nonzero = maxc > 0
        saturation[nonzero] = delta[nonzero] / maxc[nonzero]

        hue = np.zeros_like(maxc)
        delta_nonzero = delta > 0
        red_max = (maxc == r) & delta_nonzero
        green_max = (maxc == g) & delta_nonzero
        blue_max = (maxc == b) & delta_nonzero
        hue[red_max] = ((g[red_max] - b[red_max]) / delta[red_max]) % 6
        hue[green_max] = ((b[green_max] - r[green_max]) / delta[green_max]) + 2
        hue[blue_max] = ((r[blue_max] - g[blue_max]) / delta[blue_max]) + 4
        hue_degrees = hue * 60

        neutral = saturation <= args.neutral_sat_limit
        approved_blue = (
            (hue_degrees >= args.blue_hue_min)
            & (hue_degrees <= args.blue_hue_max)
            & (saturation <= 0.72)
        )
        allowed = near_allowed | neutral | approved_blue
        disallowed_mask = valid_mask & ~allowed
        disallowed = int(disallowed_mask.sum())
        ratio = disallowed / max(1, inspected)
    if ratio <= args.pass_ratio:
        status = "pass"
    elif ratio <= args.review_ratio:
        status = "review"
    else:
        status = "fail"

    bbox = ""
    ys_array, xs_array = np.where(disallowed_mask)
    if len(xs_array):
        bbox = f"{int(xs_array.min())},{int(ys_array.min())},{int(xs_array.max() - xs_array.min() + 1)},{int(ys_array.max() - ys_array.min() + 1)}"

    buckets: dict[str, int] = {}
    if len(xs_array):
        disallowed_rgb = rgb[disallowed_mask] / 255.0
        for r_value, g_value, b_value in disallowed_rgb[:: max(1, len(disallowed_rgb) // 20000)]:
            hue_value, saturation_value, value_value = colorsys.rgb_to_hsv(float(r_value), float(g_value), float(b_value))
            name = color_name(hue_value * 360, saturation_value, value_value)
            buckets[name] = buckets.get(name, 0) + 1
    dominant = ";".join(f"{name}:{count}" for name, count in sorted(buckets.items(), key=lambda item: item[1], reverse=True)[:5])

    notes = ""
    if row["audit_source_type"] == "source_base_for_overlay":
        notes = "official overlay excluded by auditing matching base image"

    return {
        **row,
        "size": f"{image.width}x{image.height}",
        "inspected_pixels": str(inspected),
        "disallowed_pixels": str(disallowed),
        "disallowed_ratio": f"{ratio:.6f}",
        "disallowed_bbox": bbox,
        "dominant_disallowed": dominant,
        "status": status,
        "notes": notes,
    }


def write_csv(rows: list[dict[str, str]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys())
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, str]], out: Path, csv_path: Path, contact_sheet: Path | None) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = {}
    batch_counts: dict[tuple[str, str], int] = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
        key = (row["batch_id"], row["status"])
        batch_counts[key] = batch_counts.get(key, 0) + 1
    worst = sorted(rows, key=lambda row: float(row["disallowed_ratio"]), reverse=True)[:20]
    lines = [
        "# Ponchi Color Audit Summary",
        "",
        "This audit checks generated-body color drift against the ponchi palette.",
        "For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.",
        "",
        "## Counts",
        "",
        "| status | count |",
        "| --- | ---: |",
    ]
    for status in ("pass", "review", "fail", "missing"):
        lines.append(f"| `{status}` | {counts.get(status, 0)} |")
    lines.extend(
        [
            "",
            "## Artifacts",
            "",
            f"- CSV: `{rel(csv_path)}`",
        ]
    )
    if contact_sheet:
        lines.append(f"- Contact sheet: `{rel(contact_sheet)}`")
    lines.extend(
        [
            "",
            "## By Batch",
            "",
            "| batch | pass | review | fail | missing |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for batch_id in sorted({row["batch_id"] for row in rows}):
        lines.append(
            "| "
            f"`{batch_id}` | "
            f"{batch_counts.get((batch_id, 'pass'), 0)} | "
            f"{batch_counts.get((batch_id, 'review'), 0)} | "
            f"{batch_counts.get((batch_id, 'fail'), 0)} | "
            f"{batch_counts.get((batch_id, 'missing'), 0)} |"
        )
    lines.extend(
        [
            "",
            "## Highest Off-Palette Ratios",
            "",
            "| entry | title | batch | ratio | status | dominant off-palette | audited file |",
            "| --- | --- | --- | ---: | --- | --- | --- |",
        ]
    )
    for row in worst:
        lines.append(
            "| "
            f"`{row['entry_id']}` | {row['title']} | `{row['batch_id']}` | "
            f"{row['disallowed_ratio']} | `{row['status']}` | "
            f"`{row['dominant_disallowed']}` | `{row['audited_file']}` |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- `pass` means the mechanical color gate did not find material off-palette body pixels.",
            "- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.",
            "- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.",
            "- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_contact_sheet(rows: list[dict[str, str]], out: Path, limit: int) -> None:
    selected = sorted(rows, key=lambda row: float(row["disallowed_ratio"]), reverse=True)[:limit]
    thumb_w, thumb_h = 418, 209
    label_h = 68
    cols = 3
    row_count = max(1, (len(selected) + cols - 1) // cols)
    sheet = Image.new("RGB", (cols * thumb_w, row_count * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    outlines = {
        "pass": (90, 150, 90),
        "review": (200, 150, 40),
        "fail": (190, 70, 70),
        "missing": (80, 80, 80),
    }
    for index, row in enumerate(selected):
        source = REPO / row["audited_file"]
        col = index % cols
        grid_row = index // cols
        x0 = col * thumb_w
        y0 = grid_row * (thumb_h + label_h)
        draw.rectangle([x0, y0, x0 + thumb_w - 1, y0 + thumb_h + label_h - 1], outline=outlines.get(row["status"], (80, 80, 80)), width=3)
        draw.text((x0 + 8, y0 + 8), f"{row['entry_id']} {row['title']}", fill=(20, 20, 20))
        draw.text((x0 + 8, y0 + 28), f"{row['status']} off={row['disallowed_ratio']} {row['dominant_disallowed']}", fill=(80, 80, 80))
        draw.text((x0 + 8, y0 + 47), row["audit_source_type"], fill=(80, 80, 80))
        if source.exists():
            image = Image.open(source).convert("RGB")
            image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            sheet.paste(image, (x0 + (thumb_w - image.width) // 2, y0 + label_h + (thumb_h - image.height) // 2))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="*", type=Path)
    parser.add_argument("--manifest-root", type=Path, default=None)
    parser.add_argument("--out-csv", type=Path, default=DEFAULT_OUT_CSV)
    parser.add_argument("--out-md", type=Path, default=DEFAULT_OUT_MD)
    parser.add_argument("--contact-sheet", type=Path, default=DEFAULT_CONTACT)
    parser.add_argument("--contact-limit", type=int, default=30)
    parser.add_argument("--ignore-rect", action="append", type=parse_rect, default=[])
    parser.add_argument("--palette-tolerance", type=float, default=34.0)
    parser.add_argument("--neutral-sat-limit", type=float, default=0.09)
    parser.add_argument("--blue-hue-min", type=float, default=195.0)
    parser.add_argument("--blue-hue-max", type=float, default=224.0)
    parser.add_argument("--alpha-min", type=int, default=16)
    parser.add_argument("--pass-ratio", type=float, default=0.010)
    parser.add_argument("--review-ratio", type=float, default=0.020)
    args = parser.parse_args()

    if args.manifest_root:
        rows = manifest_rows(args.manifest_root)
    elif args.images:
        rows = direct_image_rows(args.images)
    else:
        rows = manifest_rows(DEFAULT_MANIFEST_ROOT)

    if not rows:
        raise SystemExit("no images or manifest rows found")

    audited = [audit_row(row, args, args.ignore_rect) for row in rows]
    write_csv(audited, args.out_csv)
    if args.contact_sheet:
        write_contact_sheet(audited, args.contact_sheet, args.contact_limit)
    write_md(audited, args.out_md, args.out_csv, args.contact_sheet)

    counts: dict[str, int] = {}
    for row in audited:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    print("color audit counts: " + ", ".join(f"{key}={counts[key]}" for key in sorted(counts)))
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    if args.contact_sheet:
        print(f"wrote {args.contact_sheet}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
