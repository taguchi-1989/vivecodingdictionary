#!/usr/bin/env python3
"""assets/ponchi/final/*.png を WebP に変換する。

- 元 PNG はそのまま残します（ローカル保管用）。
- 既に .webp がある場合はスキップ（--force で再生成）。
- 既定品質 80、メソッド 6（じっくり圧縮）。
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image

PONCHI_DIR = Path(__file__).resolve().parents[1] / "assets" / "ponchi" / "final"


def convert_one(png: Path, quality: int, force: bool) -> tuple[str, int, int]:
    webp = png.with_suffix(".webp")
    if webp.exists() and not force:
        return ("skip", png.stat().st_size, webp.stat().st_size)
    with Image.open(png) as im:
        im.save(webp, "WEBP", quality=quality, method=6)
    return ("done", png.stat().st_size, webp.stat().st_size)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quality", type=int, default=80)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--pattern", default="*.png")
    args = ap.parse_args()

    pngs = sorted(PONCHI_DIR.glob(args.pattern))
    if not pngs:
        print(f"no png in {PONCHI_DIR}")
        return 0

    total_png = total_webp = 0
    done = skipped = 0
    for p in pngs:
        status, png_size, webp_size = convert_one(p, args.quality, args.force)
        total_png += png_size
        total_webp += webp_size
        if status == "done":
            done += 1
            print(f"  {p.name}: {png_size/1024:.0f}KB -> {webp_size/1024:.0f}KB")
        else:
            skipped += 1

    print()
    print(f"converted: {done}, skipped: {skipped}")
    print(f"total PNG : {total_png/1024/1024:.1f} MB")
    print(f"total WebP: {total_webp/1024/1024:.1f} MB")
    if total_png:
        print(f"reduction : {(1 - total_webp/total_png)*100:.1f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
