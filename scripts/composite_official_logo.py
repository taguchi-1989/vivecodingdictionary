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
    parser.add_argument("--magick", default="magick", help="ImageMagick executable")
    return parser.parse_args()


def require_file(path: Path, label: str) -> None:
    if not path.exists():
        raise SystemExit(f"{label} not found: {path}")
    if not path.is_file():
        raise SystemExit(f"{label} is not a file: {path}")


def main() -> int:
    args = parse_args()
    require_file(args.input, "input")
    require_file(args.logo, "logo")

    if args.width <= 0:
        raise SystemExit("--width must be positive")
    if args.y < 0:
        raise SystemExit("--y must be zero or positive")

    x = args.x
    if x is None:
        x = args.canvas_width - args.right_margin - args.width
    if x < 0:
        raise SystemExit("computed x is negative; reduce --width or margins")

    if shutil.which(args.magick) is None:
        raise SystemExit(f"ImageMagick executable not found: {args.magick}")

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
