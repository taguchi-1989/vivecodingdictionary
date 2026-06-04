#!/usr/bin/env python3
"""Score final ponchi images for outlier review and regeneration planning."""
from __future__ import annotations

import argparse
import colorsys
import csv
import math
import re
from dataclasses import dataclass
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
FINAL_DIR = REPO / "assets" / "ponchi" / "final"
ENTRIES = REPO / "ledgers" / "entries.csv"
GENERATION_BATCHES = REPO / "ledgers" / "ponchi_generation_batches.csv"
DEFAULT_OUT_CSV = REPO / "ledgers" / "ponchi_quality_scores.csv"
DEFAULT_OUT_MD = REPO / "docs" / "ponchi_quality_score_summary.md"
DEFAULT_LOW_CONTACT = REPO / "docs" / "ponchi_batch_audits" / "ponchi-quality-low-contact-sheet.png"
DEFAULT_MID_CONTACT = REPO / "docs" / "ponchi_batch_audits" / "ponchi-quality-mid-review-contact-sheet.png"
DEFAULT_KNOWN_CONTACT = REPO / "docs" / "ponchi_batch_audits" / "ponchi-quality-known-padding-contact-sheet.png"
DEFAULT_SPARSE_CONTACT = REPO / "docs" / "ponchi_batch_audits" / "ponchi-quality-sparse-diagram-contact-sheet.png"

KNOWN_PADDING_IDS = {
    "B-2",
    "B-3",
    "B-4",
    "E-25",
    "E-26",
    "E-27",
    "E-30",
    "E-50",
    "H-1",
    "H-5",
    "H-6",
    "H-7",
    "H-8",
    "I-2",
    "I-3",
    "I-4",
    "I-5",
    "J-100",
    "J-81",
    "J-90",
    "J-91",
    "J-92",
    "J-93",
}

ALLOWED_RGB = np.asarray(
    [
        (255, 255, 255),
        (247, 249, 252),
        (26, 26, 26),
        (107, 114, 128),
        (234, 241, 251),
        (214, 230, 250),
        (141, 183, 232),
        (63, 127, 209),
        (18, 62, 130),
    ],
    dtype=np.float32,
)


@dataclass(frozen=True)
class Metrics:
    r: float
    g: float
    b: float
    luma: float
    saturation: float
    contrast: float
    edge_density: float
    ink_ratio: float
    aspect: float
    bbox_coverage: float
    bbox_width_ratio: float
    bbox_height_ratio: float
    margin_balance: float
    off_palette_ratio: float
    file_size_kb: float


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO).as_posix()
    except ValueError:
        return str(path)


def natural_id_key(entry_id: str) -> tuple[str, int]:
    match = re.match(r"^([A-Z]+)-(\d+)$", entry_id)
    if not match:
        return (entry_id, 0)
    return (match.group(1), int(match.group(2)))


def load_entries(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return {row["new_id"]: row for row in csv.DictReader(handle)}


def load_generation_batches(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return {row["entry_id"]: row for row in csv.DictReader(handle)}


def quality(diff: float, tolerance: float) -> int:
    return max(0, round(100 * (1 - diff / tolerance)))


def distance(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.sqrt(sum((a[index] - b[index]) ** 2 for index in range(3)))


def analyze_image(path: Path, sample_size: int) -> Metrics:
    image = Image.open(path).convert("RGBA")
    natural_width, natural_height = image.size

    canvas = Image.new("RGBA", (sample_size, sample_size), (255, 255, 255, 255))
    scale = min(sample_size / natural_width, sample_size / natural_height)
    resized_size = (max(1, round(natural_width * scale)), max(1, round(natural_height * scale)))
    resized = image.resize(resized_size, Image.Resampling.LANCZOS)
    paste = ((sample_size - resized_size[0]) // 2, (sample_size - resized_size[1]) // 2)
    canvas.alpha_composite(resized, paste)

    data = np.asarray(canvas, dtype=np.float32)
    alpha = data[:, :, 3:4] / 255.0
    rgb = data[:, :, :3] * alpha + 255.0 * (1.0 - alpha)
    lumas = 0.2126 * rgb[:, :, 0] + 0.7152 * rgb[:, :, 1] + 0.0722 * rgb[:, :, 2]

    maxc = rgb.max(axis=2)
    minc = rgb.min(axis=2)
    saturation = np.zeros_like(maxc)
    nonzero = maxc > 0
    saturation[nonzero] = (maxc[nonzero] - minc[nonzero]) / maxc[nonzero]

    luma = float(lumas.mean())
    contrast = float(np.abs(lumas - luma).mean())
    edge_left = np.abs(lumas[:, 1:] - lumas[:, :-1])
    edge_up = np.abs(lumas[1:, :] - lumas[:-1, :])
    edge_sum = edge_left[1:, :] + edge_up[:, 1:]
    edge_density = float((edge_sum > 42).sum() / (sample_size * sample_size))
    ink_mask = lumas < 246
    ink_ratio = float(ink_mask.sum() / (sample_size * sample_size))

    if ink_mask.any():
        ys, xs = np.where(ink_mask)
        bbox_width = int(xs.max() - xs.min() + 1)
        bbox_height = int(ys.max() - ys.min() + 1)
        bbox_coverage = (bbox_width * bbox_height) / (sample_size * sample_size)
        bbox_width_ratio = bbox_width / sample_size
        bbox_height_ratio = bbox_height / sample_size
        left_margin = xs.min() / sample_size
        right_margin = (sample_size - 1 - xs.max()) / sample_size
        margin_balance = 1.0 - min(1.0, abs(left_margin - right_margin))
    else:
        bbox_coverage = 0.0
        bbox_width_ratio = 0.0
        bbox_height_ratio = 0.0
        margin_balance = 0.0

    off_palette_ratio = color_policy_ratio(image)

    return Metrics(
        r=float(rgb[:, :, 0].mean()),
        g=float(rgb[:, :, 1].mean()),
        b=float(rgb[:, :, 2].mean()),
        luma=luma,
        saturation=float(saturation.mean()),
        contrast=contrast,
        edge_density=edge_density,
        ink_ratio=ink_ratio,
        aspect=natural_width / natural_height,
        bbox_coverage=bbox_coverage,
        bbox_width_ratio=bbox_width_ratio,
        bbox_height_ratio=bbox_height_ratio,
        margin_balance=margin_balance,
        off_palette_ratio=off_palette_ratio,
        file_size_kb=path.stat().st_size / 1024,
    )


def color_policy_ratio(image: Image.Image) -> float:
    data = np.asarray(image.convert("RGBA"), dtype=np.float32)
    rgb = data[:, :, :3]
    alpha = data[:, :, 3]
    valid_mask = alpha >= 16
    inspected = int(valid_mask.sum())
    if inspected == 0:
        return 0.0

    diff = rgb[:, :, None, :] - ALLOWED_RGB[None, None, :, :]
    min_distance = np.sqrt(np.sum(diff * diff, axis=3)).min(axis=2)
    near_allowed = min_distance <= 34.0

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

    neutral = saturation <= 0.09
    approved_blue = (hue_degrees >= 195.0) & (hue_degrees <= 224.0) & (saturation <= 0.72)
    allowed = near_allowed | neutral | approved_blue
    disallowed = valid_mask & ~allowed
    return float(disallowed.sum() / inspected)


def median_metrics(metrics: list[Metrics]) -> Metrics:
    def med(name: str) -> float:
        return float(np.median([getattr(metric, name) for metric in metrics]))

    return Metrics(
        r=med("r"),
        g=med("g"),
        b=med("b"),
        luma=med("luma"),
        saturation=med("saturation"),
        contrast=med("contrast"),
        edge_density=med("edge_density"),
        ink_ratio=med("ink_ratio"),
        aspect=med("aspect"),
        bbox_coverage=med("bbox_coverage"),
        bbox_width_ratio=med("bbox_width_ratio"),
        bbox_height_ratio=med("bbox_height_ratio"),
        margin_balance=med("margin_balance"),
        off_palette_ratio=med("off_palette_ratio"),
        file_size_kb=med("file_size_kb"),
    )


def compare_metrics(ref: Metrics, target: Metrics) -> tuple[int, dict[str, int], list[str]]:
    color_diff = distance((ref.r, ref.g, ref.b), (target.r, target.g, target.b)) / 441.7
    luma_diff = abs(ref.luma - target.luma) / 255
    sat_diff = abs(ref.saturation - target.saturation)
    contrast_diff = abs(ref.contrast - target.contrast)
    edge_diff = abs(ref.edge_density - target.edge_density)
    ink_diff = abs(ref.ink_ratio - target.ink_ratio)
    aspect_diff = min(abs(ref.aspect - target.aspect) / max(ref.aspect, 0.1), 1)

    parts = {
        "color": quality(color_diff, 0.23),
        "luma": quality(luma_diff, 0.20),
        "saturation": quality(sat_diff, 0.22),
        "contrast": quality(contrast_diff, 20),
        "edge": quality(edge_diff, 0.095),
        "ink": quality(ink_diff, 0.45),
        "aspect": quality(aspect_diff, 0.20),
    }
    score = round(
        parts["color"] * 0.20
        + parts["luma"] * 0.13
        + parts["saturation"] * 0.10
        + parts["contrast"] * 0.14
        + parts["edge"] * 0.16
        + parts["ink"] * 0.20
        + parts["aspect"] * 0.07
    )

    flags: list[str] = []
    if parts["color"] < 72:
        flags.append("色味")
    if parts["luma"] < 72:
        flags.append("明るさ")
    if parts["contrast"] < 70:
        flags.append("濃淡")
    if parts["edge"] < 70:
        flags.append("線密度")
    if parts["ink"] < 70:
        flags.append("余白")
    if parts["aspect"] < 80:
        flags.append("比率")
    if score < 70:
        flags.append("外れ値")
    return score, parts, flags


def central_padding_flag(metric: Metrics) -> bool:
    return metric.aspect > 1.9 and metric.bbox_width_ratio <= 0.58 and metric.margin_balance >= 0.82


def sparse_diagram_flag(metric: Metrics, score: int, category: str, official_asset_context: bool) -> bool:
    """Catch clean but underdrawn diagrams that the median score rewards."""
    sparse_hits = 0
    if metric.file_size_kb < 38:
        sparse_hits += 1
    if metric.ink_ratio < 0.16:
        sparse_hits += 1
    if metric.contrast < 13:
        sparse_hits += 1
    if metric.edge_density < 0.09:
        sparse_hits += 1
    if metric.saturation < 0.014:
        sparse_hits += 1

    brand_like = category in {"service", "person"} or official_asset_context
    return score >= 85 and sparse_hits >= 4 and brand_like


def off_palette_status(ratio: float) -> str:
    if ratio <= 0.010:
        return "pass"
    if ratio <= 0.020:
        return "review"
    return "fail"


def has_official_asset_context(batch_row: dict[str, str]) -> bool:
    logo_status = batch_row.get("logo_status", "")
    logo_need = batch_row.get("logo_need", "")
    official_asset = batch_row.get("official_asset", "")
    return bool(official_asset) or logo_need == "required" or logo_status in {
        "official_logo_applied",
        "official_logo_available",
        "official_overlay_ready",
        "overlay_audit",
    }


def build_rows(
    paths: list[Path],
    entries: dict[str, dict[str, str]],
    generation_rows: dict[str, dict[str, str]],
    sample_size: int,
) -> list[dict[str, str]]:
    analyzed = [(path, analyze_image(path, sample_size)) for path in paths]
    reference = median_metrics([metric for _, metric in analyzed])

    rows: list[dict[str, str]] = []
    for path, metric in analyzed:
        entry_id = path.stem
        score, parts, flags = compare_metrics(reference, metric)
        known_padding = entry_id in KNOWN_PADDING_IDS
        central_padding = central_padding_flag(metric)
        color_status = off_palette_status(metric.off_palette_ratio)
        entry = entries.get(entry_id, {})
        generation = generation_rows.get(entry_id, {})
        official_asset_context = has_official_asset_context(generation)
        sparse_diagram = sparse_diagram_flag(metric, score, entry.get("category", ""), official_asset_context)
        band = "high" if score >= 85 else "mid" if score >= 70 else "low"
        reasons = list(flags)
        if known_padding:
            reasons.append("known_padding_2to1")
        if central_padding:
            reasons.append("central_padding_shape")
        if color_status != "pass":
            reasons.append(f"color_{color_status}")
        if color_status != "pass" and official_asset_context:
            reasons.append("official_asset_color_context")
        if sparse_diagram:
            reasons.append("sparse_logo_diagram")
        if band == "mid" and not reasons:
            reasons.append("mid_score_visual_check")

        if color_status == "fail" and official_asset_context:
            recommended_action = "official_overlay_color_review"
        elif color_status == "fail":
            recommended_action = "color_or_full_regen"
        elif known_padding or central_padding:
            recommended_action = "composition_regen_review"
        elif sparse_diagram:
            recommended_action = "sparse_diagram_review"
        elif score < 70:
            recommended_action = "full_regen_review"
        elif band == "mid":
            recommended_action = "visual_review"
        else:
            recommended_action = "light_review"

        rows.append(
            {
                "entry_id": entry_id,
                "title": entry.get("title", ""),
                "category": entry.get("category", ""),
                "subtype": entry.get("subtype", ""),
                "path": rel(path),
                "score": str(score),
                "band": band,
                "flags": ";".join(flags),
                "review_reasons": ";".join(dict.fromkeys(reasons)),
                "recommended_action": recommended_action,
                "logo_need": generation.get("logo_need", ""),
                "logo_status": generation.get("logo_status", ""),
                "official_asset": generation.get("official_asset", ""),
                "official_asset_context": "yes" if official_asset_context else "no",
                "known_padding_2to1": "yes" if known_padding else "no",
                "central_padding_shape": "yes" if central_padding else "no",
                "sparse_diagram": "yes" if sparse_diagram else "no",
                "color_status": color_status,
                "off_palette_ratio": f"{metric.off_palette_ratio:.6f}",
                "file_size_kb": f"{metric.file_size_kb:.1f}",
                "part_color": str(parts["color"]),
                "part_luma": str(parts["luma"]),
                "part_saturation": str(parts["saturation"]),
                "part_contrast": str(parts["contrast"]),
                "part_edge": str(parts["edge"]),
                "part_ink": str(parts["ink"]),
                "part_aspect": str(parts["aspect"]),
                "luma": f"{metric.luma:.3f}",
                "saturation": f"{metric.saturation:.5f}",
                "contrast": f"{metric.contrast:.3f}",
                "edge_density": f"{metric.edge_density:.5f}",
                "ink_ratio": f"{metric.ink_ratio:.5f}",
                "bbox_coverage": f"{metric.bbox_coverage:.5f}",
                "bbox_width_ratio": f"{metric.bbox_width_ratio:.5f}",
                "bbox_height_ratio": f"{metric.bbox_height_ratio:.5f}",
                "margin_balance": f"{metric.margin_balance:.5f}",
            }
        )

    rows.sort(key=lambda row: natural_id_key(row["entry_id"]))
    return rows


def write_csv(rows: list[dict[str, str]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_contact_sheet(rows: list[dict[str, str]], out: Path, limit: int, title: str) -> None:
    selected = rows[:limit]
    thumb_w, thumb_h = 418, 209
    label_h = 74
    cols = 3
    row_count = max(1, (len(selected) + cols - 1) // cols)
    sheet = Image.new("RGB", (cols * thumb_w, row_count * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    outlines = {"high": (90, 150, 90), "mid": (205, 150, 45), "low": (190, 70, 70)}
    for index, row in enumerate(selected):
        source = REPO / row["path"]
        col = index % cols
        grid_row = index // cols
        x0 = col * thumb_w
        y0 = grid_row * (thumb_h + label_h)
        draw.rectangle([x0, y0, x0 + thumb_w - 1, y0 + thumb_h + label_h - 1], outline=outlines.get(row["band"], (80, 80, 80)), width=3)
        draw.text((x0 + 8, y0 + 7), f"{title} {row['entry_id']} {row['title']}", fill=(20, 20, 20))
        draw.text((x0 + 8, y0 + 27), f"score {row['score']} {row['band']} {row['recommended_action']}", fill=(70, 70, 70))
        draw.text((x0 + 8, y0 + 47), row["review_reasons"][:72], fill=(90, 90, 90))
        if source.exists():
            image = Image.open(source).convert("RGB")
            image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            sheet.paste(image, (x0 + (thumb_w - image.width) // 2, y0 + label_h + (thumb_h - image.height) // 2))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)


def write_summary(
    rows: list[dict[str, str]],
    out: Path,
    csv_path: Path,
    low_contact: Path,
    mid_contact: Path,
    known_contact: Path,
    sparse_contact: Path,
) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = {}
    actions: dict[str, int] = {}
    color_counts: dict[str, int] = {}
    for row in rows:
        counts[row["band"]] = counts.get(row["band"], 0) + 1
        actions[row["recommended_action"]] = actions.get(row["recommended_action"], 0) + 1
        color_counts[row["color_status"]] = color_counts.get(row["color_status"], 0) + 1

    low = sorted(rows, key=lambda row: int(row["score"]))[:25]
    mid_review = [
        row
        for row in sorted(rows, key=lambda row: (int(row["score"]), row["entry_id"]))
        if row["band"] == "mid" and row["recommended_action"] != "visual_review"
    ][:25]
    known = [row for row in rows if row["known_padding_2to1"] == "yes"]
    sparse = [row for row in rows if row["sparse_diagram"] == "yes"]

    lines = [
        "# Ponchi Quality Score Summary",
        "",
        "This is a mechanical outlier score for planning visual review and regeneration. It is not final approval.",
        "",
        "## Artifacts",
        "",
        f"- CSV: `{rel(csv_path)}`",
        f"- Low score contact sheet: `{rel(low_contact)}`",
        f"- Mid review contact sheet: `{rel(mid_contact)}`",
        f"- Known padding contact sheet: `{rel(known_contact)}`",
        f"- Sparse diagram contact sheet: `{rel(sparse_contact)}`",
        "",
        "## Score Bands",
        "",
        "| band | count |",
        "| --- | ---: |",
        f"| `high` | {counts.get('high', 0)} |",
        f"| `mid` | {counts.get('mid', 0)} |",
        f"| `low` | {counts.get('low', 0)} |",
        "",
        "## Recommended Actions",
        "",
        "| action | count |",
        "| --- | ---: |",
    ]
    for action, count in sorted(actions.items()):
        lines.append(f"| `{action}` | {count} |")
    lines.extend(
        [
            "",
            "## Color Gate Counts",
            "",
            "| color status | count |",
            "| --- | ---: |",
        ]
    )
    for status in ("pass", "review", "fail"):
        lines.append(f"| `{status}` | {color_counts.get(status, 0)} |")
    lines.extend(
        [
            "",
            "## Lowest Scores",
            "",
            "| entry | title | score | action | reasons |",
            "| --- | --- | ---: | --- | --- |",
        ]
    )
    for row in low:
        lines.append(f"| `{row['entry_id']}` | {row['title']} | {row['score']} | `{row['recommended_action']}` | `{row['review_reasons']}` |")
    lines.extend(
        [
            "",
            "## Mid Band With Structural Reasons",
            "",
            "| entry | title | score | action | reasons |",
            "| --- | --- | ---: | --- | --- |",
        ]
    )
    for row in mid_review:
        lines.append(f"| `{row['entry_id']}` | {row['title']} | {row['score']} | `{row['recommended_action']}` | `{row['review_reasons']}` |")
    lines.extend(
        [
            "",
            "## Sparse High-Score Diagram Candidates",
            "",
            "These score well mechanically but are likely too thin for branded/service illustrations.",
            "",
            "| entry | title | score | file KB | ink | contrast | reasons |",
            "| --- | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in sorted(sparse, key=lambda row: (float(row["file_size_kb"]), row["entry_id"])):
        lines.append(
            f"| `{row['entry_id']}` | {row['title']} | {row['score']} | "
            f"{row['file_size_kb']} | {row['ink_ratio']} | {row['contrast']} | `{row['review_reasons']}` |"
        )
    lines.extend(
        [
            "",
            "## Known Mechanical Padding Set",
            "",
            f"- known padding ids detected in final set: {len(known)} / {len(KNOWN_PADDING_IDS)}",
            "",
            "| entry | title | score | action | central shape |",
            "| --- | --- | ---: | --- | --- |",
        ]
    )
    for row in sorted(known, key=lambda row: natural_id_key(row["entry_id"])):
        lines.append(f"| `{row['entry_id']}` | {row['title']} | {row['score']} | `{row['recommended_action']}` | `{row['central_padding_shape']}` |")
    lines.extend(
        [
            "",
            "## Initial Rule Assessment",
            "",
            "- Low scores are useful for finding visual outliers, but they should be treated as review priority rather than automatic rejection.",
            "- Known mechanical padding must be an explicit rule because several padded images can still score mid or high on color and density.",
            "- Sparse high-score diagrams must be an explicit rule because clean logo/box/arrow images can look statistically normal while feeling under-produced.",
            "- Mid-band images with padding or color reasons are the important validation set: they test whether the score catches boring or weak 2:1 composition.",
            "- High-band images still need light visual review for semantic mismatch, generated logos, or policy issues that pixel metrics cannot see.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="*", type=Path)
    parser.add_argument("--out-csv", type=Path, default=DEFAULT_OUT_CSV)
    parser.add_argument("--out-md", type=Path, default=DEFAULT_OUT_MD)
    parser.add_argument("--low-contact", type=Path, default=DEFAULT_LOW_CONTACT)
    parser.add_argument("--mid-contact", type=Path, default=DEFAULT_MID_CONTACT)
    parser.add_argument("--known-contact", type=Path, default=DEFAULT_KNOWN_CONTACT)
    parser.add_argument("--sparse-contact", type=Path, default=DEFAULT_SPARSE_CONTACT)
    parser.add_argument("--contact-limit", type=int, default=30)
    parser.add_argument("--sample-size", type=int, default=96)
    args = parser.parse_args()

    paths = sorted(args.images) if args.images else sorted(FINAL_DIR.glob("*.webp"))
    if not paths:
        raise SystemExit("no images found")

    entries = load_entries(ENTRIES)
    generation_rows = load_generation_batches(GENERATION_BATCHES)
    rows = build_rows(paths, entries, generation_rows, args.sample_size)
    write_csv(rows, args.out_csv)

    low_rows = sorted(rows, key=lambda row: int(row["score"]))
    mid_rows = [
        row
        for row in sorted(rows, key=lambda row: (int(row["score"]), row["entry_id"]))
        if row["band"] == "mid"
        and (row["known_padding_2to1"] == "yes" or row["central_padding_shape"] == "yes" or row["color_status"] != "pass")
    ]
    known_rows = [row for row in rows if row["known_padding_2to1"] == "yes"]
    sparse_rows = [row for row in rows if row["sparse_diagram"] == "yes"]
    write_contact_sheet(low_rows, args.low_contact, args.contact_limit, "LOW")
    write_contact_sheet(mid_rows, args.mid_contact, args.contact_limit, "MID")
    write_contact_sheet(known_rows, args.known_contact, args.contact_limit, "KNOWN")
    write_contact_sheet(sparse_rows, args.sparse_contact, args.contact_limit, "SPARSE")
    write_summary(rows, args.out_md, args.out_csv, args.low_contact, args.mid_contact, args.known_contact, args.sparse_contact)

    band_counts: dict[str, int] = {}
    for row in rows:
        band_counts[row["band"]] = band_counts.get(row["band"], 0) + 1
    print("quality score counts: " + ", ".join(f"{key}={band_counts[key]}" for key in sorted(band_counts)))
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    print(f"wrote {args.low_contact}")
    print(f"wrote {args.mid_contact}")
    print(f"wrote {args.known_contact}")
    print(f"wrote {args.sparse_contact}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
