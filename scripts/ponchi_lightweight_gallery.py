#!/usr/bin/env python3
"""Build an HTML gallery sorted by smallest ponchi final image file size."""
from __future__ import annotations

import csv
import html
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCORES = REPO / "ledgers" / "ponchi_quality_scores.csv"
OUT = REPO / "docs" / "ponchi_lightweight_gallery.html"


def rel_from_docs(path: Path) -> str:
    return "../" + path.resolve().relative_to(REPO).as_posix()


def load_rows() -> list[dict[str, str]]:
    if not SCORES.exists():
        raise SystemExit(f"missing score CSV: {SCORES}")
    with SCORES.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        image = REPO / row["path"]
        row["file_size_kb"] = f"{image.stat().st_size / 1024:.1f}"
        row["image_src"] = rel_from_docs(image)
        row["score_num"] = int(row["score"])
        row["file_size_num"] = float(row["file_size_kb"])
    rows.sort(key=lambda row: (row["file_size_num"], row["entry_id"]))
    return rows


def write_html(rows: list[dict[str, str]]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(rows, ensure_ascii=False)
    html_text = f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ponchi Lightweight Gallery</title>
  <style>
    :root {{
      --bg: #f7f9fc;
      --panel: #ffffff;
      --ink: #1a1a1a;
      --muted: #6b7280;
      --line: #d6e6fa;
      --blue: #3f7fd1;
      --dark-blue: #123e82;
      --warn: #b7791f;
      --bad: #b42318;
      --ok: #177245;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.45;
    }}
    header {{
      position: sticky;
      top: 0;
      z-index: 5;
      border-bottom: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(10px);
    }}
    .top {{
      max-width: 1480px;
      margin: 0 auto;
      padding: 14px 18px;
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 14px;
      align-items: center;
    }}
    h1 {{
      margin: 0;
      font-size: 18px;
      letter-spacing: 0;
    }}
    .summary {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      color: var(--muted);
      font-size: 12px;
    }}
    .pill {{
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 4px 9px;
      background: #fff;
    }}
    .controls {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: flex-end;
      align-items: center;
    }}
    input, select {{
      height: 34px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      padding: 0 10px;
      font: inherit;
      font-size: 13px;
    }}
    main {{
      max-width: 1480px;
      margin: 0 auto;
      padding: 18px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
      gap: 12px;
    }}
    .card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      overflow: hidden;
      min-width: 0;
    }}
    .card.review {{ border-color: #e2a13a; }}
    .card.bad {{ border-color: #df7a70; }}
    .card.sparse {{ box-shadow: inset 4px 0 0 var(--warn); }}
    .image-wrap {{
      aspect-ratio: 2 / 1;
      background: #fff;
      border-bottom: 1px solid var(--line);
      display: grid;
      place-items: center;
    }}
    .image-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
    }}
    .body {{
      padding: 10px 11px 12px;
    }}
    .title-row {{
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 8px;
      align-items: start;
    }}
    .entry {{
      font-weight: 700;
      font-size: 14px;
      min-width: 0;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .kb {{
      font-weight: 800;
      color: var(--dark-blue);
      font-size: 15px;
      white-space: nowrap;
    }}
    .meta {{
      margin-top: 7px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
    }}
    .metric {{
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 5px 6px;
      min-width: 0;
    }}
    .metric span {{
      display: block;
      color: var(--muted);
      font-size: 10px;
    }}
    .metric strong {{
      display: block;
      font-size: 12px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .tags {{
      margin-top: 8px;
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
    }}
    .tag {{
      border-radius: 999px;
      background: #eaf1fb;
      color: var(--dark-blue);
      padding: 3px 7px;
      font-size: 11px;
      max-width: 100%;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .tag.warn {{ background: #fff4d6; color: #7a4b00; }}
    .tag.bad {{ background: #ffe7e3; color: var(--bad); }}
    .tag.ok {{ background: #e7f6ed; color: var(--ok); }}
    .reason {{
      margin-top: 7px;
      color: var(--muted);
      font-size: 11px;
      min-height: 16px;
      overflow-wrap: anywhere;
    }}
    .hidden {{ display: none !important; }}
    @media (max-width: 720px) {{
      .top {{ grid-template-columns: 1fr; }}
      .controls {{ justify-content: flex-start; }}
      .grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="top">
      <div>
        <h1>Ponchi Lightweight Gallery</h1>
        <div class="summary" id="summary"></div>
      </div>
      <div class="controls">
        <input id="search" type="search" placeholder="ID / title">
        <select id="filter">
          <option value="all">all</option>
          <option value="sparse">sparse only</option>
          <option value="review">review lanes</option>
          <option value="lt20">under 20KB</option>
          <option value="lt30">under 30KB</option>
          <option value="lt40">under 40KB</option>
        </select>
        <select id="limit">
          <option value="50">top 50</option>
          <option value="100" selected>top 100</option>
          <option value="200">top 200</option>
          <option value="350">all 350</option>
        </select>
      </div>
    </div>
  </header>
  <main>
    <div class="grid" id="grid"></div>
  </main>
  <script>
    const rows = {data};
    const grid = document.getElementById("grid");
    const search = document.getElementById("search");
    const filter = document.getElementById("filter");
    const limit = document.getElementById("limit");
    const summary = document.getElementById("summary");

    function tagClass(value) {{
      if (value === "sparse_diagram_review" || value === "composition_regen_review") return "warn";
      if (value === "full_regen_review" || value === "official_overlay_color_review") return "bad";
      if (value === "light_review") return "ok";
      return "";
    }}

    function cardClass(row) {{
      const classes = ["card"];
      if (row.sparse_diagram === "yes") classes.push("sparse");
      if (row.recommended_action.includes("review")) classes.push("review");
      if (row.recommended_action === "full_regen_review") classes.push("bad");
      return classes.join(" ");
    }}

    function render() {{
      const q = search.value.trim().toLowerCase();
      const f = filter.value;
      const max = Number(limit.value);
      let filtered = rows.filter(row => {{
        const hay = `${{row.entry_id}} ${{row.title}} ${{row.recommended_action}} ${{row.review_reasons}}`.toLowerCase();
        if (q && !hay.includes(q)) return false;
        if (f === "sparse" && row.sparse_diagram !== "yes") return false;
        if (f === "review" && row.recommended_action === "light_review") return false;
        if (f === "lt20" && row.file_size_num >= 20) return false;
        if (f === "lt30" && row.file_size_num >= 30) return false;
        if (f === "lt40" && row.file_size_num >= 40) return false;
        return true;
      }}).slice(0, max);

      summary.innerHTML = [
        `<span class="pill">showing ${{filtered.length}} / ${{rows.length}}</span>`,
        `<span class="pill">smallest ${{rows[0].file_size_kb}}KB: ${{rows[0].entry_id}}</span>`,
        `<span class="pill">sparse ${{rows.filter(row => row.sparse_diagram === "yes").length}}</span>`,
        `<span class="pill">review lanes ${{rows.filter(row => row.recommended_action !== "light_review").length}}</span>`
      ].join("");

      grid.innerHTML = filtered.map(row => `
        <article class="${{cardClass(row)}}">
          <div class="image-wrap"><img src="${{row.image_src}}" alt="${{escapeHtml(row.entry_id + " " + row.title)}}" loading="lazy"></div>
          <div class="body">
            <div class="title-row">
              <div class="entry" title="${{escapeHtml(row.title)}}">${{escapeHtml(row.entry_id)}} ${{escapeHtml(row.title)}}</div>
              <div class="kb">${{row.file_size_kb}}KB</div>
            </div>
            <div class="meta">
              <div class="metric"><span>score</span><strong>${{row.score}}</strong></div>
              <div class="metric"><span>ink</span><strong>${{row.ink_ratio}}</strong></div>
              <div class="metric"><span>contrast</span><strong>${{row.contrast}}</strong></div>
              <div class="metric"><span>edge</span><strong>${{row.edge_density}}</strong></div>
            </div>
            <div class="tags">
              <span class="tag ${{tagClass(row.recommended_action)}}">${{escapeHtml(row.recommended_action)}}</span>
              <span class="tag">${{escapeHtml(row.band)}}</span>
              <span class="tag ${{row.sparse_diagram === "yes" ? "warn" : ""}}">sparse: ${{row.sparse_diagram || "no"}}</span>
              <span class="tag ${{row.color_status === "fail" ? "bad" : row.color_status === "review" ? "warn" : "ok"}}">color: ${{row.color_status}}</span>
            </div>
            <div class="reason">${{escapeHtml(row.review_reasons || "")}}</div>
          </div>
        </article>
      `).join("");
    }}

    function escapeHtml(value) {{
      return String(value).replace(/[&<>"']/g, char => ({{
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
      }}[char]));
    }}

    search.addEventListener("input", render);
    filter.addEventListener("change", render);
    limit.addEventListener("change", render);
    render();
  </script>
</body>
</html>
"""
    OUT.write_text(html_text, encoding="utf-8", newline="\n")


def main() -> int:
    rows = load_rows()
    write_html(rows)
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
