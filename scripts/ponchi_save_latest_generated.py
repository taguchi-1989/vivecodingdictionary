#!/usr/bin/env python3
"""Copy the latest built-in imagegen PNG into a ponchi experiment batch."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


DEFAULT_GENERATED_DIR = Path(
    r"C:\Users\tgch1\.codex\generated_images\019e8dd4-74ba-7e03-bd37-97fca9db2dfe"
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("entry_id")
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--generated-dir", type=Path, default=DEFAULT_GENERATED_DIR)
    parser.add_argument("--out-root", type=Path, default=Path("assets/ponchi/experiments/batches"))
    parser.add_argument("--width", type=int, default=1254)
    parser.add_argument("--height", type=int, default=627)
    args = parser.parse_args()

    candidates = list(args.generated_dir.glob("*.png"))
    if not candidates:
        raise SystemExit(f"no generated PNG files found in {args.generated_dir}")

    source = max(candidates, key=lambda path: path.stat().st_mtime)
    out_dir = args.out_root / args.batch_id
    out_dir.mkdir(parents=True, exist_ok=True)

    raw = out_dir / f"{args.entry_id}_base_raw.png"
    normalized = out_dir / f"{args.entry_id}_base_1254x627.png"

    image = Image.open(source).convert("RGB")
    image.save(raw)
    image.resize((args.width, args.height), Image.Resampling.LANCZOS).save(normalized, optimize=True)

    print(f"source={source}")
    print(f"raw={raw}")
    print(f"normalized={normalized}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
