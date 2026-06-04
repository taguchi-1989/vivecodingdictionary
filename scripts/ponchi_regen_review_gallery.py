#!/usr/bin/env python3
"""Build an HTML review gallery for lightweight regeneration candidates."""
from __future__ import annotations

import argparse
import csv
import html
from pathlib import Path


def rel_from_doc(path: str, docs_dir: Path) -> str:
    if not path:
        return ""
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = Path.cwd() / candidate
    try:
        return candidate.resolve().relative_to(docs_dir.resolve()).as_posix()
    except ValueError:
        try:
            return candidate.resolve().relative_to(Path.cwd().resolve()).as_posix()
        except ValueError:
            return candidate.resolve().as_posix()


def status_class(value: str) -> str:
    value = value.lower()
    if "fail" in value:
        return "fail"
    if "review" in value:
        return "review"
    if "pass" in value or "generated" in value:
        return "pass"
    return "pending"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_html(rows: list[dict[str, str]], out: Path, batch: str | None) -> None:
    docs_dir = out.parent
    selected = [row for row in rows if not batch or row["batch_id"] == batch]
    selected.sort(key=lambda row: (int(row["batch_index"]), int(row["item_index"])))

    counts: dict[str, int] = {}
    for row in selected:
        key = row.get("audit_status") or row.get("status") or "unknown"
        counts[key] = counts.get(key, 0) + 1

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("<!doctype html>\n<html lang=\"ja\">\n<head>\n")
        handle.write("<meta charset=\"utf-8\">\n")
        handle.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n")
        title = "Ponchi Lightweight Regen Review"
        handle.write(f"<title>{title}</title>\n")
        handle.write(
            "<style>\n"
            ":root{color-scheme:light;--blue:#2563eb;--ink:#111827;--muted:#6b7280;--line:#dbe3ef;--bg:#f7f9fc;--bad:#b91c1c;--warn:#b45309;--ok:#166534;}\n"
            "body{margin:0;background:var(--bg);color:var(--ink);font-family:Arial,'Yu Gothic',Meiryo,sans-serif;}\n"
            "header{position:sticky;top:0;z-index:2;background:white;border-bottom:1px solid var(--line);padding:14px 18px;}\n"
            "h1{font-size:20px;margin:0 0 8px;letter-spacing:0;}\n"
            ".meta{display:flex;gap:8px;flex-wrap:wrap;font-size:12px;color:var(--muted)}\n"
            ".pill{border:1px solid var(--line);border-radius:999px;background:#fff;padding:4px 8px;}\n"
            "main{padding:18px;}\n"
            ".grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:14px;}\n"
            ".card{background:white;border:1px solid var(--line);border-radius:8px;overflow:hidden;box-shadow:0 1px 2px rgba(15,23,42,.04);}\n"
            ".thumb{aspect-ratio:2/1;background:#eef2f7;display:flex;align-items:center;justify-content:center;border-bottom:1px solid var(--line);}\n"
            ".thumb img{width:100%;height:100%;object-fit:contain;display:block;}\n"
            ".empty{color:var(--muted);font-size:13px;}\n"
            ".body{padding:10px 12px 12px;}\n"
            ".title{font-weight:700;font-size:14px;margin-bottom:8px;display:flex;justify-content:space-between;gap:8px;}\n"
            ".row{font-size:12px;color:var(--muted);margin:4px 0;overflow-wrap:anywhere;}\n"
            ".badge{font-size:11px;border-radius:999px;padding:3px 7px;border:1px solid var(--line);white-space:nowrap;}\n"
            ".badge.pass{color:var(--ok);background:#ecfdf3;border-color:#bbf7d0;}\n"
            ".badge.review{color:var(--warn);background:#fff7ed;border-color:#fed7aa;}\n"
            ".badge.fail{color:var(--bad);background:#fef2f2;border-color:#fecaca;}\n"
            ".badge.pending{color:var(--muted);background:#f8fafc;}\n"
            "a{color:var(--blue);text-decoration:none;}\n"
            "a:hover{text-decoration:underline;}\n"
            "</style>\n"
        )
        handle.write("</head>\n<body>\n")
        handle.write("<header>\n")
        batch_label = batch or "all batches"
        handle.write(f"<h1>{html.escape(title)} - {html.escape(batch_label)}</h1>\n")
        handle.write("<div class=\"meta\">\n")
        handle.write(f"<span class=\"pill\">items: {len(selected)}</span>\n")
        for key, count in sorted(counts.items()):
            handle.write(f"<span class=\"pill\">{html.escape(key)}: {count}</span>\n")
        handle.write("</div>\n</header>\n<main>\n<div class=\"grid\">\n")
        for row in selected:
            candidate = row.get("candidate_path", "")
            src = rel_from_doc(candidate, docs_dir)
            audit = row.get("audit_status", "")
            cls = status_class(audit or row.get("status", ""))
            prompt = rel_from_doc(row.get("prompt_path", ""), docs_dir)
            handle.write("<article class=\"card\">\n")
            handle.write("<div class=\"thumb\">")
            if src:
                handle.write(f"<img src=\"{html.escape(src)}\" alt=\"{html.escape(row['entry_id'])}\">")
            else:
                handle.write("<span class=\"empty\">not generated</span>")
            handle.write("</div>\n")
            handle.write("<div class=\"body\">\n")
            handle.write(
                "<div class=\"title\">"
                f"<span>{html.escape(row['entry_id'])} {html.escape(row['title'])}</span>"
                f"<span class=\"badge {cls}\">{html.escape(audit or row.get('status',''))}</span>"
                "</div>\n"
            )
            handle.write(f"<div class=\"row\">batch: {html.escape(row['batch_id'])} / item {html.escape(row['item_index'])}</div>\n")
            handle.write(f"<div class=\"row\">regen: {html.escape(row['regen_type'])}</div>\n")
            handle.write(f"<div class=\"row\">decision: {html.escape(row.get('replacement_decision',''))}</div>\n")
            handle.write(f"<div class=\"row\">logo: {html.escape(row.get('logo_need',''))} / {html.escape(row.get('logo_status',''))}</div>\n")
            if prompt:
                handle.write(f"<div class=\"row\"><a href=\"{html.escape(prompt)}\">prompt</a></div>\n")
            if candidate:
                handle.write(f"<div class=\"row\"><a href=\"{html.escape(src)}\">candidate file</a></div>\n")
            handle.write("</div>\n</article>\n")
        handle.write("</div>\n</main>\n</body>\n</html>\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", type=Path, default=Path("ledgers/ponchi_lightweight_regen_batches.csv"))
    parser.add_argument("--out", type=Path, default=Path("docs/ponchi_lightweight_regen_review.html"))
    parser.add_argument("--batch-id")
    args = parser.parse_args()

    rows = read_rows(args.ledger)
    write_html(rows, args.out, args.batch_id)
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
