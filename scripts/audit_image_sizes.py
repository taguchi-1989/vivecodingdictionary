#!/usr/bin/env python3
"""Audit ponchi final image dimensions without external dependencies."""
from __future__ import annotations

import argparse
import struct
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FINAL_DIR = ROOT / "assets" / "ponchi" / "final"


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as f:
        header = f.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    return struct.unpack(">II", header[16:24])


def webp_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:64]
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise ValueError("not a WebP")

    fmt = data[12:16]
    if fmt == b"VP8X":
        width = 1 + int.from_bytes(data[24:27], "little")
        height = 1 + int.from_bytes(data[27:30], "little")
        return width, height
    if fmt == b"VP8 ":
        width = struct.unpack_from("<H", data, 26)[0] & 0x3FFF
        height = struct.unpack_from("<H", data, 28)[0] & 0x3FFF
        return width, height
    if fmt == b"VP8L":
        b0, b1, b2, b3 = data[21:25]
        width = 1 + (((b1 & 0x3F) << 8) | b0)
        height = 1 + (((b3 & 0x0F) << 10) | (b2 << 2) | ((b1 & 0xC0) >> 6))
        return width, height

    raise ValueError(f"unsupported WebP chunk: {fmt!r}")


def image_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as f:
        magic = f.read(12)
    if magic[:8] == b"\x89PNG\r\n\x1a\n":
        return png_size(path)
    if magic[:4] == b"RIFF" and magic[8:12] == b"WEBP":
        return webp_size(path)
    raise ValueError(f"unsupported image type: {path.suffix.lower()}")


def classify(width: int, height: int) -> str:
    ratio = width / height
    if width == height:
        return "1:1"
    if abs(ratio - 2) < 0.01:
        return "2:1"
    return f"{ratio:.3f}:1"


def audit(directory: Path, suffix: str | None) -> int:
    patterns = [f"*{suffix}"] if suffix else ["*.png", "*.webp"]
    paths: list[Path] = []
    for pattern in patterns:
        paths.extend(sorted(directory.glob(pattern)))

    if not paths:
        print(f"No images found in {directory}")
        return 0

    rows = []
    for path in paths:
        try:
            width, height = image_size(path)
        except Exception as exc:  # noqa: BLE001 - audit should report and continue.
            print(f"Error reading {path.name}: {exc}")
            continue
        rows.append((path.name, width, height, classify(width, height)))

    size_counter = Counter((width, height) for _, width, height, _ in rows)
    class_counter = Counter(kind for *_, kind in rows)

    print("=== Image Size Audit ===")
    print(f"Directory: {directory}")
    print(f"Images scanned: {len(rows)}")

    print("\nCommon sizes:")
    for (width, height), count in size_counter.most_common():
        print(f"  {width}x{height}: {count}")

    print("\nAspect classes:")
    for kind, count in class_counter.most_common():
        print(f"  {kind}: {count}")

    square = [name for name, _, _, kind in rows if kind == "1:1"]
    if square:
        print("\n1:1 image IDs:")
        print("  " + ", ".join(Path(name).stem for name in square))

    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=Path, default=FINAL_DIR, help="Image directory to audit")
    parser.add_argument("--suffix", choices=[".png", ".webp"], help="Limit audit to one file type")
    args = parser.parse_args()
    return audit(args.dir, args.suffix)


if __name__ == "__main__":
    raise SystemExit(main())
