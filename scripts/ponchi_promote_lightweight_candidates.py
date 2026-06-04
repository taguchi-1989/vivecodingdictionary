#!/usr/bin/env python3
"""Promote lightweight regeneration candidates into the main final ponchi images."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

from PIL import Image


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "entry_id",
        "title",
        "candidate_path",
        "final_path",
        "replacement_decision",
        "audit_status",
        "old_size_bytes",
        "new_size_bytes",
        "status",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def promote(args: argparse.Namespace) -> list[dict[str, str]]:
    rows = read_rows(args.ledger)
    report: list[dict[str, str]] = []

    for row in rows:
        entry_id = row["entry_id"]
        candidate_path = Path(row["candidate_path"])
        final_path = args.final_dir / f"{entry_id}.webp"
        status = "promoted"
        old_size = str(final_path.stat().st_size) if final_path.exists() else ""

        if not candidate_path.exists():
            status = "missing_candidate"
        elif not final_path.exists():
            status = "missing_final"
        elif not args.dry_run:
            image = Image.open(candidate_path).convert("RGB")
            if image.size != (args.width, args.height):
                image = image.resize((args.width, args.height), Image.Resampling.LANCZOS)
            image.save(final_path, "WEBP", quality=args.quality, method=6)

        report.append(
            {
                "entry_id": entry_id,
                "title": row.get("title", ""),
                "candidate_path": candidate_path.as_posix(),
                "final_path": final_path.as_posix(),
                "replacement_decision": row.get("replacement_decision", ""),
                "audit_status": row.get("audit_status", ""),
                "old_size_bytes": old_size,
                "new_size_bytes": str(final_path.stat().st_size) if final_path.exists() and not args.dry_run else "",
                "status": status,
            }
        )

    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", type=Path, default=Path("ledgers/ponchi_lightweight_regen_batches.csv"))
    parser.add_argument("--final-dir", type=Path, default=Path("assets/ponchi/final"))
    parser.add_argument("--out", type=Path, default=Path("ledgers/ponchi_lightweight_promotion.csv"))
    parser.add_argument("--width", type=int, default=1254)
    parser.add_argument("--height", type=int, default=627)
    parser.add_argument("--quality", type=int, default=92)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    report = promote(args)
    write_rows(args.out, report)
    counts: dict[str, int] = {}
    for row in report:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    for status, count in sorted(counts.items()):
        print(f"{status}={count}")
    print(f"wrote {args.out}")
    return 1 if any(row["status"].startswith("missing_") for row in report) else 0


if __name__ == "__main__":
    raise SystemExit(main())
