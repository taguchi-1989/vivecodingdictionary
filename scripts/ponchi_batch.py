#!/usr/bin/env python3
"""Batch helpers for ponchi image generation.

This script does not call an image-generation API. It prepares deterministic
work batches and imports generated PNGs from Codex's generated_images folder
into assets/ponchi/final/{entry_id}.png.
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "ledgers" / "ponchi_generation_queue.csv"
ENTRIES = ROOT / "ledgers" / "entries.csv"
FINAL_DIR = ROOT / "assets" / "ponchi" / "final"
BATCH_DIR = ROOT / "assets" / "ponchi" / "batches"
PROMPT_DIR = ROOT / "assets" / "ponchi" / "batch_prompts"
DRAFT_SVG_DIR = ROOT / "drafts" / "ponchi"


ENTRY_ORDER = {
    "service": 10,
    "model": 20,
    "term_llm": 30,
    "term_tool": 40,
    "term_general": 50,
    "workflow": 60,
    "benchmark": 70,
    "mcp": 80,
    "history": 90,
    "person_org": 100,
    "common": 900,
}


@dataclass
class QueueRow:
    entry_id: str
    title: str
    category: str
    status: str
    md_path: str
    has_svg: str
    has_final_image: str
    priority: str
    notes: str

    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "QueueRow":
        return cls(**{field: row.get(field, "") for field in cls.__dataclass_fields__})

    def to_dict(self) -> dict[str, str]:
        return {
            "entry_id": self.entry_id,
            "title": self.title,
            "category": self.category,
            "status": self.status,
            "md_path": self.md_path,
            "has_svg": self.has_svg,
            "has_final_image": self.has_final_image,
            "priority": self.priority,
            "notes": self.notes,
        }


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_queue(rows: list[QueueRow]) -> None:
    QUEUE.parent.mkdir(parents=True, exist_ok=True)
    with QUEUE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(QueueRow.__dataclass_fields__))
        writer.writeheader()
        writer.writerows(row.to_dict() for row in rows)


def sync_queue() -> list[QueueRow]:
    entries = read_csv(ENTRIES)
    svg_ids = {p.stem for p in DRAFT_SVG_DIR.glob("*.svg")}
    final_ids = {p.stem for p in FINAL_DIR.glob("*.png")} if FINAL_DIR.exists() else set()
    rows: list[QueueRow] = []

    for entry in entries:
        if entry.get("status") == "archived":
            continue
        entry_id = entry.get("new_id", "")
        has_svg = entry_id in svg_ids
        has_final = entry_id in final_ids
        if has_final:
            priority = "done"
            notes = "complete" if has_svg else "final_image_without_svg"
        elif entry.get("category") == "common":
            priority = "common_review"
            notes = "needs_final_image" if has_svg else "missing_svg"
        elif entry.get("status") == "ready" and has_svg:
            priority = "ready_svg_to_image"
            notes = "needs_final_image"
        elif entry.get("status") == "ready":
            priority = "ready_missing_svg"
            notes = "missing_svg"
        else:
            priority = "later"
            notes = "needs_final_image" if has_svg else "missing_svg"

        rows.append(
            QueueRow(
                entry_id=entry_id,
                title=entry.get("title", ""),
                category=entry.get("category", ""),
                status=entry.get("status", ""),
                md_path=entry.get("path", ""),
                has_svg=str(has_svg),
                has_final_image=str(has_final),
                priority=priority,
                notes=notes,
            )
        )

    write_queue(rows)
    return rows


def load_queue(sync: bool) -> list[QueueRow]:
    if sync or not QUEUE.exists():
        return sync_queue()
    return [QueueRow.from_dict(row) for row in read_csv(QUEUE)]


def sort_key(row: QueueRow) -> tuple[int, int, str]:
    priority_rank = {
        "ready_svg_to_image": 0,
        "ready_missing_svg": 1,
        "later": 2,
        "common_review": 3,
        "done": 9,
    }.get(row.priority, 5)
    category_rank = ENTRY_ORDER.get(row.category, 500)
    return (priority_rank, category_rank, natural_id(row.entry_id))


def natural_id(entry_id: str) -> str:
    match = re.match(r"([A-Z]+)-(\d+)$", entry_id)
    if not match:
        return entry_id
    return f"{match.group(1)}-{int(match.group(2)):04d}"


def extract_ponchi_memo(path: Path) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    start = text.find("## 誌面ポンチ絵メモ")
    if start < 0:
        return ""
    rest = text[start:]
    ends = [idx for marker in ("## コミュニティ補完メモ", "## 出典メモ", "## 備考") if (idx := rest.find(marker, 1)) > 0]
    return rest[: min(ends)].strip() if ends else rest.strip()


def memo_value(memo: str, label: str) -> str:
    prefix = f"- {label}:"
    for line in memo.splitlines():
        if line.startswith(prefix):
            return line[len(prefix) :].strip()
    return ""


def prompt_for(row: QueueRow) -> str:
    memo = extract_ponchi_memo(ROOT / row.md_path)
    scene = memo_value(memo, "描く内容") or f"{row.title} を使う人の場面"
    characters = memo_value(memo, "登場人物") or "この用語に出会うユーザー 1〜2 名"
    keyword = memo_value(memo, "中央に置くキーワード/ラベル") or memo_value(memo, "中央に置くキーワード") or row.title
    svg_ref = f"drafts/ponchi/{row.entry_id}.svg" if (DRAFT_SVG_DIR / f"{row.entry_id}.svg").exists() else "none"

    return f"""Use case: illustration-story
Asset type: book editorial spot illustration for a Japanese AI/development glossary
Entry: {row.entry_id} {row.title}
Reference SVG: {svg_ref}
Primary request: Create a simple one-panel illustration that helps beginners intuitively understand "{row.title}" through people using it in context.
Scene/backdrop: {scene}
Subject: {characters}
Supporting idea: {keyword}
Style/medium: soft hand-drawn editorial illustration, clean expressive linework, gentle paper texture, minimal detail, friendly but not childish, suitable for a printed technical glossary.
Composition/framing: square composition, one clear scene, readable when reduced to a small book illustration, generous margins, no crowded UI details.
Color palette: mostly black linework with white and very pale blue-gray paper tones; at most one subtle blue accent.
Text: No readable text inside the image. If speech bubbles appear, use only tiny abstract scribble marks.
If the source scene mentions labels, UI text, column names, or speech words, represent them as abstract blocks, icon marks, checkmarks, dots, or short illegible scribbles instead of readable text; the printed page caption will carry the wording.
Constraints: Do not draw official logos, trademarks, product UI screenshots, brand marks, model provider marks, or real people's likenesses. Do not make it look like an advertisement. Keep the concept human-centered.
Avoid: photorealism, 3D render, glossy icons, dense diagrams, fake readable Japanese text, brand marks, watermarks.
"""


def create_batch(args: argparse.Namespace) -> None:
    rows = load_queue(sync=args.sync)
    selected = [row for row in rows if row.has_final_image != "True" and row.priority in set(args.priority)]
    selected.sort(key=sort_key)
    selected = selected[: args.count]
    if not selected:
        print("No pending entries matched the requested priority.")
        return

    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    PROMPT_DIR.mkdir(parents=True, exist_ok=True)
    batch_path = BATCH_DIR / f"{args.name}.csv"
    prompt_path = PROMPT_DIR / f"{args.name}.md"

    with batch_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["order", "lane", "entry_id", "title", "category", "status", "md_path", "priority"])
        writer.writeheader()
        for idx, row in enumerate(selected, start=1):
            writer.writerow(
                {
                    "order": idx,
                    "lane": ((idx - 1) % args.lanes) + 1,
                    "entry_id": row.entry_id,
                    "title": row.title,
                    "category": row.category,
                    "status": row.status,
                    "md_path": row.md_path,
                    "priority": row.priority,
                }
            )

    sections = []
    for idx, row in enumerate(selected, start=1):
        sections.append(f"## {idx}. {row.entry_id} {row.title}\n\n```text\n{prompt_for(row).strip()}\n```\n")
    prompt_path.write_text(f"# Ponchi Batch: {args.name}\n\n" + "\n".join(sections), encoding="utf-8")

    print(f"Wrote {batch_path.relative_to(ROOT)}")
    print(f"Wrote {prompt_path.relative_to(ROOT)}")
    print(f"Entries: {', '.join(row.entry_id for row in selected)}")


def import_batch(args: argparse.Namespace) -> None:
    batch_path = BATCH_DIR / f"{args.name}.csv"
    if not batch_path.exists():
        raise SystemExit(f"Batch not found: {batch_path}")
    batch_rows = read_csv(batch_path)
    source_dir = Path(args.source).expanduser()
    if not source_dir.exists():
        raise SystemExit(f"Source directory not found: {source_dir}")
    images = sorted(source_dir.glob("*.png"), key=lambda p: p.stat().st_mtime)
    if args.skip:
        images = images[args.skip :]
    if len(images) < len(batch_rows):
        raise SystemExit(f"Need {len(batch_rows)} PNGs, found {len(images)} after skip={args.skip}")

    FINAL_DIR.mkdir(parents=True, exist_ok=True)
    for row, image in zip(batch_rows, images):
        dest = FINAL_DIR / f"{row['entry_id']}.png"
        if dest.exists() and not args.force:
            raise SystemExit(f"Refusing to overwrite existing file without --force: {dest}")
        shutil.copy2(image, dest)
        print(f"{image.name} -> {dest.relative_to(ROOT)}")

    sync_queue()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_sync = sub.add_parser("sync", help="refresh ledgers/ponchi_generation_queue.csv from current files")
    p_sync.set_defaults(func=lambda args: print(f"Rows: {len(sync_queue())}"))

    p_next = sub.add_parser("next", help="create a generation batch and prompt bundle")
    p_next.add_argument("--name", required=True, help="batch name, e.g. batch_20260516_01")
    p_next.add_argument("--count", type=int, default=12)
    p_next.add_argument("--lanes", type=int, default=4, help="logical lanes for manual parallel dispatch")
    p_next.add_argument("--priority", nargs="+", default=["ready_svg_to_image", "ready_missing_svg"])
    p_next.add_argument("--sync", action="store_true")
    p_next.set_defaults(func=create_batch)

    p_import = sub.add_parser("import", help="copy generated PNGs into assets/ponchi/final by batch order")
    p_import.add_argument("--name", required=True)
    p_import.add_argument("--source", required=True, help="directory containing generated PNGs")
    p_import.add_argument("--skip", type=int, default=0, help="skip oldest N PNGs in source directory")
    p_import.add_argument("--force", action="store_true")
    p_import.set_defaults(func=import_batch)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
