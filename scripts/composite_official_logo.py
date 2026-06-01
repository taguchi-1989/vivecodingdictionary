#!/usr/bin/env python3
"""Composite an official logo asset onto a ponchi image with ImageMagick.

The script is intentionally small and deterministic: it never asks image
generation to draw the logo, and it does not crop, recolor, or distort the
official asset. ImageMagick handles PNG/WebP/SVG/PDF input formats available in
the local install.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path
from typing import Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path, help="Base 2:1 image")
    parser.add_argument("--logo", required=True, type=Path, help="Official logo asset")
    parser.add_argument("--out", required=True, type=Path, help="Output image path")
    parser.add_argument("--width", type=int, default=520, help="Logo width in px")
    parser.add_argument("--x", type=int, default=None, help="Overlay x position in px")
    parser.add_argument("--y", type=int, default=36, help="Overlay y position in px")
    parser.add_argument(
        "--right-margin",
        type=int,
        default=48,
        help="Right margin used when --x is omitted",
    )
    parser.add_argument(
        "--canvas-width",
        type=int,
        default=1254,
        help="Canvas width used for right-aligned placement",
    )
    parser.add_argument(
        "--audit-density",
        action="store_true",
        help="Audit base image subject coverage before compositing",
    )
    parser.add_argument(
        "--min-bbox-coverage",
        type=float,
        default=0.50,
        help="Minimum non-white bounding-box coverage for --audit-density",
    )
    parser.add_argument(
        "--warn-only-density",
        action="store_true",
        help="Print density warnings without failing the command",
    )
    parser.add_argument("--magick", default="magick", help="ImageMagick executable")
    return parser.parse_args()


def require_file(path: Path, label: str) -> None:
    if not path.exists():
        raise SystemExit(f"{label} not found: {path}")
    if not path.is_file():
        raise SystemExit(f"{label} is not a file: {path}")


def image_density_with_magick(path: Path, magick: str) -> Tuple[Tuple[int, int], float]:
    identify = subprocess.run(
        [magick, "identify", "-format", "%w %h", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    width, height = [int(part) for part in identify.stdout.split()]
    trimmed = subprocess.run(
        [magick, str(path), "-fuzz", "7%", "-trim", "-format", "%w %h", "info:"],
        check=True,
        capture_output=True,
        text=True,
    )
    trim_width, trim_height = [int(part) for part in trimmed.stdout.split()]
    return (width, height), (trim_width * trim_height) / (width * height)


def image_density(path: Path, magick: str) -> Tuple[Tuple[int, int], float]:
    try:
        from PIL import Image
    except ImportError:
        return image_density_with_magick(path, magick)

    image = Image.open(path).convert("RGB")
    width, height = image.size
    pixels = image.load()
    xs: list[int] = []
    ys: list[int] = []

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # White paper can include antialiased off-white edges. Count only
            # visible ink/fill so large blank logo spaces are caught.
            if min(255 - r, 255 - g, 255 - b) > 18 or (255 - r) + (255 - g) + (255 - b) > 55:
                xs.append(x)
                ys.append(y)

    if not xs:
        return (width, height), 0.0

    bbox_area = (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)
    return (width, height), bbox_area / (width * height)


def audit_density(path: Path, minimum: float, warn_only: bool, magick: str) -> None:
    size, coverage = image_density(path, magick)
    message = (
        f"base_density_bbox_coverage={coverage:.3f} "
        f"size={size[0]}x{size[1]} minimum={minimum:.3f}"
    )
    if coverage < minimum:
        if warn_only:
            print(f"warning: {message}")
            return
        raise SystemExit(
            f"{message}; base image is likely too sparse for logo overlay. "
            "Rerun the base with larger subject mass or pass --warn-only-density "
            "only for an intentional spacious composition."
        )
    print(message)


def main() -> int:
    args = parse_args()
    require_file(args.input, "input")
    require_file(args.logo, "logo")

    if args.width <= 0:
        raise SystemExit("--width must be positive")
    if args.y < 0:
        raise SystemExit("--y must be zero or positive")
    if not 0 < args.min_bbox_coverage <= 1:
        raise SystemExit("--min-bbox-coverage must be greater than 0 and <= 1")

    x = args.x
    if x is None:
        x = args.canvas_width - args.right_margin - args.width
    if x < 0:
        raise SystemExit("computed x is negative; reduce --width or margins")

    if shutil.which(args.magick) is None:
        raise SystemExit(f"ImageMagick executable not found: {args.magick}")

    if args.audit_density:
        audit_density(
            args.input,
            args.min_bbox_coverage,
            args.warn_only_density,
            args.magick,
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        args.magick,
        str(args.input),
        "(",
        str(args.logo),
        "-resize",
        f"{args.width}x",
        ")",
        "-geometry",
        f"+{x}+{args.y}",
        "-composite",
        str(args.out),
    ]
    subprocess.run(cmd, check=True)
    print(f"wrote {args.out}")
    print(f"logo_width={args.width} x={x} y={args.y}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
