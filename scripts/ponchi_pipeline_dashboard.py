#!/usr/bin/env python3
"""Generate a local HTML dashboard for the ponchi generation pipeline."""
from __future__ import annotations

import argparse
import csv
import html
from collections import Counter, defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
LEDGER = REPO / "ledgers" / "ponchi_generation_batches.csv"
PIPELINE_PROMPTS = REPO / "assets" / "ponchi" / "pipeline_prompts"
FINAL_CANDIDATES = REPO / "assets" / "ponchi" / "final_candidates"
EXPERIMENTS = REPO / "assets" / "ponchi" / "experiments" / "batches"
AUDITS = REPO / "docs" / "ponchi_batch_audits"
OUT = REPO / "docs" / "ponchi_pipeline_dashboard.html"


STAGE_ORDER = [
    "brief_needed",
    "prompt_review",
    "overlay_wait",
    "overlay_ready",
    "overlay_audit",
    "blocked_brand_asset",
]


def esc(value: str) -> str:
    return html.escape(value or "")


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def prompt_count(batch_id: str) -> int:
    path = PIPELINE_PROMPTS / batch_id
    if not path.exists():
        return 0
    return len(list(path.glob("*.md")))


def final_candidate_count(batch_id: str) -> int:
    path = FINAL_CANDIDATES / batch_id / "manifest.csv"
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def base_image_count(batch_id: str) -> int:
    path = EXPERIMENTS / batch_id
    if not path.exists():
        return 0
    return len(list(path.glob("*_base_1254x627.png")))


def base_audit_summary(batch_id: str) -> str:
    path = REPO / "ledgers" / f"{batch_id.replace('-', '_')}_base_audit.csv"
    if not path.exists():
        return ""
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        counts = Counter(row.get("status", "missing") for row in csv.DictReader(handle))
    if not counts:
        return ""
    return " / " + " ".join(f"{esc(status)} {count}" for status, count in sorted(counts.items()))


def optional_link(href: str, label: str, exists: bool) -> str:
    if not exists:
        return ""
    return f'<a href="{esc(href)}">{esc(label)}</a>'


def render(rows: list[dict[str, str]]) -> str:
    stage_counts = Counter(row["pipeline_stage"] for row in rows)
    logo_counts = Counter(row["logo_status"] for row in rows)
    batches: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        batches[row["batch_id"]].append(row)

    batch_cards = []
    for batch_id in sorted(batches):
        items = batches[batch_id]
        counts = Counter(item["pipeline_stage"] for item in items)
        prompt_total = prompt_count(batch_id)
        base_total = base_image_count(batch_id)
        base_audit = base_audit_summary(batch_id)
        candidate_total = final_candidate_count(batch_id)
        report_path = REPO / "ledgers" / "ponchi_batches" / f"{batch_id}.md"
        audit_path = REPO / "docs" / "ponchi_batch_audits" / f"{batch_id}.md"
        base_contact_path = AUDITS / f"{batch_id}-base-contact-sheet.png"
        prompt_path = PIPELINE_PROMPTS / batch_id
        final_candidates_path = FINAL_CANDIDATES / batch_id / "final_candidates_contact_sheet.png"
        report_rel = f"../ledgers/ponchi_batches/{batch_id}.md"
        audit_rel = f"ponchi_batch_audits/{batch_id}.md"
        base_contact_rel = f"ponchi_batch_audits/{batch_id}-base-contact-sheet.png"
        prompt_rel = f"../assets/ponchi/pipeline_prompts/{batch_id}/"
        final_candidates_rel = f"../assets/ponchi/final_candidates/{batch_id}/final_candidates_contact_sheet.png"
        links_html = "".join(
            [
                optional_link(report_rel, "report", report_path.exists()),
                optional_link(audit_rel, "audit", audit_path.exists()),
                optional_link(base_contact_rel, "base sheet", base_contact_path.exists()),
                optional_link(prompt_rel, "prompts", prompt_path.exists()),
                optional_link(final_candidates_rel, "final candidates", final_candidates_path.exists()),
            ]
        )
        badge_html = "".join(
            f'<span class="mini {esc(stage)}">{esc(stage)} {counts.get(stage, 0)}</span>'
            for stage in STAGE_ORDER
            if counts.get(stage, 0)
        )
        item_rows = "\n".join(
            "<tr>"
            f"<td>{esc(item['item_index'])}</td>"
            f"<td><code>{esc(item['entry_id'])}</code></td>"
            f"<td>{esc(item['title'])}</td>"
            f"<td><span class=\"stage {esc(item['pipeline_stage'])}\">{esc(item['pipeline_stage'])}</span></td>"
            f"<td>{esc(item['logo_status'])}</td>"
            f"<td>{esc(item['confirmation_status'])}</td>"
            "</tr>"
            for item in items
        )
        batch_cards.append(
            f"""
      <section class="batch-card" id="{esc(batch_id)}">
        <div class="batch-head">
          <div>
            <h2>{esc(batch_id)}</h2>
            <p>{len(items)} items / pipeline prompts {prompt_total} / base images {base_total}{base_audit} / final candidates {candidate_total}</p>
          </div>
          <div class="links">
            {links_html}
          </div>
        </div>
        <div class="badges">{badge_html}</div>
        <table>
          <thead><tr><th>#</th><th>entry</th><th>title</th><th>stage</th><th>logo</th><th>confirm</th></tr></thead>
          <tbody>{item_rows}</tbody>
        </table>
      </section>
"""
        )

    stage_summary = "".join(
        f'<article><strong>{esc(stage)}</strong><span>{stage_counts.get(stage, 0)}</span></article>'
        for stage in STAGE_ORDER
    )
    logo_summary = "".join(
        f'<tr><td>{esc(status)}</td><td>{count}</td></tr>'
        for status, count in sorted(logo_counts.items())
    )
    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ponchi Pipeline Dashboard</title>
  <style>
    :root {{
      --ink: #1a1a1a;
      --muted: #6b7280;
      --line: #d8dee8;
      --blue: #3f7fd1;
      --paper: #f7f9fc;
      --warn: #8a5a00;
      --block: #8a1f1f;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--ink);
      background: #fff;
      line-height: 1.55;
    }}
    main {{ max-width: 1180px; margin: 0 auto; padding: 28px 20px 56px; }}
    header {{ border-bottom: 1px solid var(--line); padding-bottom: 18px; margin-bottom: 20px; }}
    h1 {{ margin: 0 0 8px; font-size: 28px; }}
    h2 {{ margin: 0; font-size: 18px; }}
    p {{ margin: 4px 0; color: var(--muted); }}
    .summary {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin: 18px 0; }}
    .summary article {{ border: 1px solid var(--line); border-radius: 8px; padding: 12px; background: var(--paper); }}
    .summary strong {{ display: block; font-size: 12px; color: var(--muted); }}
    .summary span {{ display: block; font-size: 24px; font-weight: 700; margin-top: 4px; }}
    .layout {{ display: grid; grid-template-columns: 1fr; gap: 16px; }}
    .batch-card {{ border: 1px solid var(--line); border-radius: 8px; padding: 14px; }}
    .batch-head {{ display: flex; justify-content: space-between; gap: 16px; align-items: start; margin-bottom: 10px; }}
    .links a {{ color: var(--blue); margin-left: 12px; text-decoration: none; font-weight: 650; }}
    .badges {{ display: flex; flex-wrap: wrap; gap: 6px; margin: 8px 0 12px; }}
    .mini, .stage {{ display: inline-block; border-radius: 999px; padding: 2px 8px; font-size: 12px; border: 1px solid var(--line); background: #fff; }}
    .brief_needed {{ color: #445; }}
    .prompt_review {{ color: var(--blue); }}
    .overlay_wait {{ color: var(--warn); border-color: #d9b45f; }}
    .overlay_ready, .overlay_audit {{ color: #1f5f3a; border-color: #9fceb0; }}
    .blocked_brand_asset {{ color: var(--block); border-color: #d9a3a3; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
    th, td {{ border-top: 1px solid var(--line); padding: 7px 8px; text-align: left; vertical-align: top; }}
    th {{ color: var(--muted); font-weight: 650; background: #fbfcfe; }}
    code {{ font-family: ui-monospace, SFMono-Regular, Consolas, monospace; }}
    .logo-table {{ max-width: 620px; margin: 10px 0 22px; }}
    @media (max-width: 760px) {{
      .summary {{ grid-template-columns: repeat(2, 1fr); }}
      .batch-head {{ display: block; }}
      .links a {{ margin-left: 0; margin-right: 12px; }}
      table {{ font-size: 12px; }}
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Ponchi Pipeline Dashboard</h1>
      <p>20件単位で scene brief、prompt、生成、監査、確認、final候補化を進めるための観察ページ。</p>
      <p>Source: <code>ledgers/ponchi_generation_batches.csv</code></p>
    </header>
    <section class="summary">{stage_summary}</section>
    <section>
      <h2>Logo Status</h2>
      <table class="logo-table"><tbody>{logo_summary}</tbody></table>
    </section>
    <section class="layout">
      {''.join(batch_cards)}
    </section>
  </main>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", type=Path, default=LEDGER)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args()

    if not args.ledger.exists():
        raise SystemExit(f"missing ledger: {args.ledger}")
    rows = load_rows(args.ledger)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render(rows), encoding="utf-8")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
