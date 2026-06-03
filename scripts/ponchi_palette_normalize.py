#!/usr/bin/env python3
"""Normalize ponchi body colors to the approved palette.

When both a base and overlay are provided, the overlay output preserves pixels
that differ from the original base. This keeps deterministic official logo
pixels intact while normalizing the generated illustration body.
"""
from __future__ import annotations

import argparse
import colorsys
from pathlib import Path

try:
    import numpy as np
    from PIL import Image
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("This script requires Pillow and NumPy. Use the bundled Codex Python runtime.") from exc


APPROVED = {
    "white": (255, 255, 255),
    "paper": (247, 249, 252),
    "black": (26, 26, 26),
    "gray": (107, 114, 128),
    "blue_1": (234, 241, 251),
    "blue_2": (214, 230, 250),
    "blue_3": (141, 183, 232),
    "blue_4": (63, 127, 209),
    "navy": (18, 62, 130),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, type=Path, help="Generated base image")
    parser.add_argument("--out-base", type=Path, default=None, help="Normalized base output; defaults to --base")
    parser.add_argument("--overlay", type=Path, default=None, help="Overlay image to preserve official asset pixels")
    parser.add_argument("--out-overlay", type=Path, default=None, help="Normalized overlay output; defaults to --overlay")
    parser.add_argument(
        "--overlay-diff-threshold",
        type=int,
        default=10,
        help="RGB difference threshold used to preserve official overlay pixels",
    )
    return parser.parse_args()


def require(path: Path, label: str) -> None:
    if not path.exists():
        raise SystemExit(f"{label} not found: {path}")
    if not path.is_file():
        raise SystemExit(f"{label} is not a file: {path}")


def nearest_palette(rgb: np.ndarray, palette: list[tuple[int, int, int]]) -> np.ndarray:
    colors = np.asarray(palette, dtype=np.float32)
    diff = rgb[:, :, None, :].astype(np.float32) - colors[None, None, :, :]
    indices = np.sum(diff * diff, axis=3).argmin(axis=2)
    return colors[indices].astype(np.uint8)


def normalize_rgb(rgb: np.ndarray) -> np.ndarray:
    values = rgb.astype(np.float32) / 255.0
    r = values[:, :, 0]
    g = values[:, :, 1]
    b = values[:, :, 2]
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

    luminance = (0.2126 * rgb[:, :, 0] + 0.7152 * rgb[:, :, 1] + 0.0722 * rgb[:, :, 2]).astype(np.float32)
    out = np.empty_like(rgb)

    very_light = luminance >= 249
    paper = (luminance >= 239) & ~very_light
    light = (luminance >= 214) & ~(very_light | paper)
    mid_light = (luminance >= 170) & ~(very_light | paper | light)
    mid = (luminance >= 115) & ~(very_light | paper | light | mid_light)
    dark = ~(very_light | paper | light | mid_light | mid)

    blueish = (hue_degrees >= 185) & (hue_degrees <= 255) & (saturation > 0.08)

    out[very_light] = APPROVED["white"]
    out[paper] = APPROVED["paper"]
    out[light] = APPROVED["blue_1"]
    out[mid_light] = APPROVED["blue_2"]
    out[mid] = APPROVED["gray"]
    out[dark] = APPROVED["black"]

    out[blueish & light] = APPROVED["blue_2"]
    out[blueish & mid_light] = APPROVED["blue_3"]
    out[blueish & mid] = APPROVED["blue_4"]
    out[blueish & dark] = APPROVED["navy"]

    # Snap the result to exact approved colors. This also catches antialiasing
    # introduced by prior resampling.
    return nearest_palette(out, list(APPROVED.values()))


def normalize_image(path: Path) -> tuple[Image.Image, np.ndarray]:
    image = Image.open(path).convert("RGBA")
    data = np.asarray(image, dtype=np.uint8).copy()
    normalized = normalize_rgb(data[:, :, :3])
    data[:, :, :3] = normalized
    return Image.fromarray(data, "RGBA"), np.asarray(image, dtype=np.uint8)


def main() -> int:
    args = parse_args()
    require(args.base, "base")
    out_base = args.out_base or args.base

    normalized_base, original_base = normalize_image(args.base)
    out_base.parent.mkdir(parents=True, exist_ok=True)
    normalized_base.convert("RGB").save(out_base)
    print(f"wrote {out_base}")

    if args.overlay:
        require(args.overlay, "overlay")
        overlay = Image.open(args.overlay).convert("RGBA")
        overlay_data = np.asarray(overlay, dtype=np.uint8).copy()
        if overlay_data.shape != original_base.shape:
            raise SystemExit("overlay and base sizes differ")
        normalized_data = np.asarray(normalized_base, dtype=np.uint8).copy()
        diff = np.abs(overlay_data[:, :, :3].astype(np.int16) - original_base[:, :, :3].astype(np.int16)).sum(axis=2)
        preserve = diff > args.overlay_diff_threshold
        normalized_data[preserve] = overlay_data[preserve]
        out_overlay = args.out_overlay or args.overlay
        out_overlay.parent.mkdir(parents=True, exist_ok=True)
        Image.fromarray(normalized_data, "RGBA").convert("RGB").save(out_overlay)
        print(f"wrote {out_overlay}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
