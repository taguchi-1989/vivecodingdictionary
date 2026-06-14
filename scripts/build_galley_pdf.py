#!/usr/bin/env python3
"""
サンプルゲラ PDF ビルダー（内容・流れの通読校正用）

目的:
- 「本として通したときの全体像」を 1 本の PDF で見られるようにする。
- A 章（前付け）は専用デザイン（drafts/front_section/）をそのまま使う。A は辞書
  エントリではないため、エントリ用テンプレ（preview）では描けない。
- B〜J は各 letter の先頭 1〜2 件だけ preview から抜粋（既定 2 件）。章の入り・終わり
  のリズム、同型レイアウトの単調さ、隣接エントリの重複などを実紙で確認する用途。

方式（CSS 体系が前付けとエントリで違うため、混ぜずに個別 PDF 化してから結合）:
- 表紙・章扉      → その場で生成した HTML を PDF 化
- A 章            → front_section/*.html を印刷用 style を注入して PDF 化
- B〜J            → preview/{id}.html をそのまま PDF 化（@media print 済み）
- 全部を pdfunite（無ければ Ghostscript）で 1 本に結合

注意:
- これは「内容・流れ校正用」の簡易ゲラであって入稿用ではない（塗り足し・CMYK・トンボなし）。
- 物理ページは 199×281mm（750×1061px の物理換算）。本来の trim（A5 等）への縮小は
  本番 Paged.js 側の仕事（docs/component_spec_v2.md §4-3）。

依存: Chrome / Edge（headless 印刷）＋ pdfunite か Ghostscript（gswin64c）。Python 追加ライブラリ不要。

Usage:
    python scripts/build_galley_pdf.py
    python scripts/build_galley_pdf.py --per-letter 1
    python scripts/build_galley_pdf.py --skip-gen
    python scripts/build_galley_pdf.py --open
"""

from __future__ import annotations

import argparse
import csv
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import webbrowser
from pathlib import Path

if sys.platform == "win32" and hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "ledgers" / "entries.csv"
CHAPTERS_PATH = ROOT / "ledgers" / "chapters.yaml"
PREVIEW_DIR = ROOT / "drafts" / "prototypes" / "preview"
FRONT_DIR = ROOT / "drafts" / "front_section"
PDF_DIR = PREVIEW_DIR / "pdf"
OUT_PDF = PDF_DIR / "galley_sample.pdf"
BASE_CSS = ROOT / "drafts" / "prototypes" / "mockups" / "design_philosophy_v2" / "base.css"

# 判型ごとの trim 寸法（mm）。199×281mm の版を Ghostscript でこのサイズに縮小すると、
# 本番（Paged.js で 750×1061px を trim に縮小）と同じ文字サイズになる。
# A5=ISO、B5=JIS（日本の書籍標準）。「実際のサイズ」で A4 に印刷して手で比較する用途。
TRIM_SIZES = {
    "a5": (148, 210),   # ISO A5
    "b5": (182, 257),   # JIS B5
}

# A 章の前付け（圧縮案 5 見開き / docs/front_section_layout.md §2）。
# 扉(旧0)とまえがき(旧1)は 1_concept_preface.html に統合済み。
FRONT_SECTION_ORDER = [
    "1_concept_preface.html",       # FR-01 扉＋まえがき（統合）
    "2_a2_anatomy.html",            # FR-02 見開きの読み方（分解図）
    "3_a3_a9_map_index.html",       # FR-03 歩き方＋語の探し方
    "4_legend_all.html",            # FR-04 記号と凡例（旧 FR-04+FR-05 を 1 見開きに集約）
]

# 巻末（圧縮案で前付けから移動した A-10/A-11 ＋ 全件索引）
BACK_SECTION_ORDER = [
    "6_a10_a11_log_glossary.html",  # 更新履歴と略称
    "9_full_index.html",            # 全件索引（旧 A-9 ミニ索引の置き換え。scripts/build_full_index.py で生成）
]

SKIP_STATUSES = {"archived", "sample"}

CHROME_CANDIDATES = [
    Path(r"C:/Program Files/Google/Chrome/Application/chrome.exe"),
    Path(r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
    Path(r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"),
    Path(r"C:/Program Files/Microsoft/Edge/Application/msedge.exe"),
]

# 前付け（front_section）は @media print を持たないので注入する。
# 通常ページ: 左右ページを各 1 物理ページ（縦 199×281mm = 750×1061px の物理換算）に割り付け。
# _common.css の .page は px 指定で、物理単位を入れないと縮小表示になるため width/height を上書き。
FRONT_PRINT_STYLE = """
<style id="galley-print">
@page { size: 199mm 281mm; margin: 0; }
@media print {
  html, body { background:#fff !important; margin:0 !important; padding:0 !important; }
  .reader-nav, .draft-stamp, .proto-nav { display:none !important; }
  .spread { display:block !important; width:auto !important; max-width:none !important; margin:0 !important; box-shadow:none !important; }
  .page {
    width:199mm !important; height:281mm !important;
    min-height:281mm !important; max-height:281mm !important; overflow:hidden !important;
    box-shadow:none !important; margin:0 !important; border-radius:0 !important;
    page-break-after: always; page-break-inside: avoid;
  }
  .page:last-of-type { page-break-after: auto; }
}
</style>
"""

# 解剖図（A-2）は 1500×1061px の見開き一枚絵。縦 1 ページには割れないので横（398×281mm）で 1 枚に。
ANATOMY_PRINT_STYLE = """
<style id="galley-print">
@page { size: 398mm 281mm; margin: 0; }
@media print {
  html, body { background:#fff !important; margin:0 !important; padding:0 !important; }
  .reader-nav, .draft-stamp, .proto-nav { display:none !important; }
  .spread.anatomy {
    width:1500px !important; height:1061px !important;
    margin:0 !important; box-shadow:none !important; transform:none !important;
    page-break-inside: avoid;
  }
}
</style>
"""

SIMPLE_PAGE = """<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8">
<link rel="stylesheet" href="{base_css}">
<style>
@page {{ size: 199mm 281mm; margin: 0; }}
html, body {{ margin:0; padding:0; background:#fff; font-family: var(--font-jp); }}
.page {{ width:750px; height:1061px; box-sizing:border-box; display:flex; flex-direction:column;
        align-items:center; justify-content:center; text-align:center; }}
.kicker {{ font-size:18px; color:var(--ink-blue-700); letter-spacing:.15em; margin-bottom:24px; }}
.title {{ font-size:56px; font-weight:900; color:var(--ink-blue-900); margin:0 0 32px; }}
.note {{ font-size:16px; color:var(--ink-2); line-height:2; max-width:560px; }}
.big {{ font-size:180px; font-weight:900; color:var(--ink-blue); line-height:1; }}
.lab {{ font-size:34px; font-weight:700; color:var(--ink-blue-900); margin-top:16px; letter-spacing:.08em; }}
</style></head><body>
<div class="page">{inner}</div>
</body></html>
"""


def find_browser() -> Path:
    env = os.environ.get("CHROME")
    if env and Path(env).exists():
        return Path(env)
    for cand in CHROME_CANDIDATES:
        if cand.exists():
            return cand
    found = shutil.which("chrome") or shutil.which("msedge")
    if found:
        return Path(found)
    raise FileNotFoundError("Chrome / Edge が見つかりません。$CHROME を設定してください。")


def count_pdf_pages(pdf_path: Path) -> int:
    return len(re.findall(rb"/Type\s*/Page(?!s)", pdf_path.read_bytes()))


def render_html_to_pdf(browser: Path, html_path: Path, pdf_path: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="vbcd_galley_") as tmp:
        cmd = [
            str(browser), "--headless=new", "--disable-gpu", f"--user-data-dir={tmp}",
            "--no-pdf-header-footer", "--virtual-time-budget=8000",
            f"--print-to-pdf={pdf_path}", html_path.as_uri(),
        ]
        r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                          timeout=90, check=False)
        if r.returncode != 0 and not pdf_path.exists():
            raise RuntimeError(f"rc={r.returncode}: {r.stderr.decode('utf-8','replace')[:400]}")


def render_front_file(browser: Path, src: Path, pdf_path: Path) -> None:
    """front_section の HTML に印刷 style を注入し、同じディレクトリの一時ファイルから PDF 化
    （相対参照の画像・CSS を壊さないため同ディレクトリに置く）。"""
    html = src.read_text(encoding="utf-8")
    style = ANATOMY_PRINT_STYLE if "spread anatomy" in html else FRONT_PRINT_STYLE
    if "</head>" in html:
        html = html.replace("</head>", style + "</head>", 1)
    else:
        html = style + html
    tmp = src.parent / f"_galley_tmp_{src.stem}.html"
    tmp.write_text(html, encoding="utf-8")
    try:
        render_html_to_pdf(browser, tmp, pdf_path)
    finally:
        tmp.unlink(missing_ok=True)


def render_simple(browser: Path, inner: str, pdf_path: Path, workdir: Path) -> None:
    html = SIMPLE_PAGE.format(base_css=BASE_CSS.as_uri(), inner=inner)
    tmp = workdir / f"_simple_{pdf_path.stem}.html"
    tmp.write_text(html, encoding="utf-8")
    render_html_to_pdf(browser, tmp, pdf_path)


def merge_pdfs(parts: list[Path], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    pdfunite = shutil.which("pdfunite")
    if pdfunite:
        r = subprocess.run([pdfunite, *[str(p) for p in parts], str(out)],
                          stderr=subprocess.PIPE, check=False)
        if r.returncode == 0 and out.exists():
            return
        print(f"  pdfunite 失敗、Ghostscript で再試行: {r.stderr.decode('utf-8','replace')[:200]}")
    gs = shutil.which("gswin64c") or shutil.which("gs")
    if not gs:
        raise RuntimeError("pdfunite も Ghostscript も見つかりません。")
    cmd = [gs, "-dBATCH", "-dNOPAUSE", "-q", "-sDEVICE=pdfwrite",
           f"-sOutputFile={out}", *[str(p) for p in parts]]
    r = subprocess.run(cmd, stderr=subprocess.PIPE, check=False)
    if r.returncode != 0 or not out.exists():
        raise RuntimeError(f"Ghostscript 結合に失敗: {r.stderr.decode('utf-8','replace')[:300]}")


def scale_pdf_to_trim(src: Path, dst: Path, w_mm: float, h_mm: float) -> bool:
    """199×281mm 版を Ghostscript で指定 trim に等比縮小（本番と同じ縮小結果）。"""
    gs = shutil.which("gswin64c") or shutil.which("gs")
    if not gs:
        return False
    w_pt = round(w_mm / 25.4 * 72, 1)
    h_pt = round(h_mm / 25.4 * 72, 1)
    cmd = [
        gs, "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=pdfwrite",
        "-dFIXEDMEDIA", "-dPDFFitPage", "-dAutoRotatePages=/None",
        f"-dDEVICEWIDTHPOINTS={w_pt}", f"-dDEVICEHEIGHTPOINTS={h_pt}",
        f"-sOutputFile={dst}", str(src),
    ]
    r = subprocess.run(cmd, stderr=subprocess.PIPE, check=False)
    return r.returncode == 0 and dst.exists()


def load_chapter_labels() -> dict[str, str]:
    labels: dict[str, str] = {}
    if not CHAPTERS_PATH.exists():
        return labels
    cur = None
    for line in CHAPTERS_PATH.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*-?\s*letter:\s*([A-J])\s*$", line)
        if m:
            cur = m.group(1)
            continue
        m = re.match(r"\s*label:\s*(.+?)\s*$", line)
        if m and cur:
            labels[cur] = m.group(1)
            cur = None
    return labels


def load_entries() -> list[dict]:
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def select_bj(rows: list[dict], per_letter: int) -> list[dict]:
    counts: dict[str, int] = {}
    picked: list[dict] = []
    for row in rows:
        eid = (row.get("new_id") or "").strip()
        if not eid or "-" not in eid:
            continue
        letter = eid.split("-", 1)[0]
        if letter == "A":
            continue
        if (row.get("status") or "").strip() in SKIP_STATUSES:
            continue
        if counts.get(letter, 0) < per_letter:
            picked.append(row)
            counts[letter] = counts.get(letter, 0) + 1
    return picked


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-letter", type=int, default=2, help="B〜J で各 letter から拾う件数（既定 2）")
    ap.add_argument("--skip-gen", action="store_true", help="preview_gen.py を走らせず既存 HTML を使う")
    ap.add_argument("--trims", default="a5,b5",
                   help="判型縮小版も出す（カンマ区切り。例 a5,b5 / none で出さない）")
    ap.add_argument("--open", action="store_true", help="生成後に PDF を開く")
    args = ap.parse_args()

    try:
        browser = find_browser()
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 2

    if not args.skip_gen:
        print("==> preview HTML を再生成（scripts/preview_gen.py）")
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "preview_gen.py")],
                          cwd=str(ROOT), check=False)
        if r.returncode != 0:
            print("preview_gen.py が失敗。--skip-gen で既存 HTML を使えます。", file=sys.stderr)
            return 2

    labels = load_chapter_labels()
    bj = select_bj(load_entries(), args.per_letter)
    print(f"==> A 章 = front_section {len(FRONT_SECTION_ORDER)} ファイル、B〜J = 各 {args.per_letter} 件（{len(bj)} 件）")

    workdir = Path(tempfile.mkdtemp(prefix="vbcd_galley_parts_"))
    parts: list[Path] = []
    missing: list[str] = []
    idx = 0

    def add(pdf: Path):
        nonlocal idx
        parts.append(pdf)
        idx += 1

    try:
        # 表紙
        cover_pdf = workdir / f"{idx:03d}_cover.pdf"
        render_simple(browser, (
            '<div class="kicker">サンプルゲラ — 全体像確認用</div>'
            '<h1 class="title">バイブコーディング図鑑</h1>'
            f'<div class="note">A 章（前付け）は専用デザイン（front_section）全 {len(FRONT_SECTION_ORDER)} 見開き、'
            f'B〜J は各 letter の先頭 {args.per_letter} 件を抜粋。<br>'
            '各ページ番号は本での想定ノンブル（このサンプルでは飛び番号）。<br>'
            'これは内容・流れ校正用の簡易ゲラです（塗り足し・CMYK・トンボなし）。</div>'
        ), cover_pdf, workdir)
        add(cover_pdf)
        print("  ✓ 表紙")

        # A 章扉 + front_section
        a_div = workdir / f"{idx:03d}_div_A.pdf"
        render_simple(browser, f'<div class="big">A</div><div class="lab">{labels.get("A","はじめに・読み方")}</div>',
                     a_div, workdir)
        add(a_div)
        print(f"  [章扉] A  {labels.get('A','')}")
        for name in FRONT_SECTION_ORDER:
            src = FRONT_DIR / name
            if not src.exists():
                print(f"  ✗ front_section/{name} が無い（スキップ）")
                missing.append(name)
                continue
            p = workdir / f"{idx:03d}_front_{src.stem}.pdf"
            render_front_file(browser, src, p)
            add(p)
            print(f"  ✓ A  {name}")

        # B〜J: 章扉 + preview エントリ
        seen: set[str] = set()
        for row in bj:
            eid = row["new_id"].strip()
            letter = eid.split("-", 1)[0]
            if letter not in seen:
                seen.add(letter)
                dp = workdir / f"{idx:03d}_div_{letter}.pdf"
                render_simple(browser, f'<div class="big">{letter}</div><div class="lab">{labels.get(letter,"")}</div>',
                             dp, workdir)
                add(dp)
                print(f"  [章扉] {letter}  {labels.get(letter,'')}")
            html_path = PREVIEW_DIR / f"{eid}.html"
            if not html_path.exists():
                print(f"  ✗ {eid}  preview HTML が無い（スキップ）")
                missing.append(eid)
                continue
            p = workdir / f"{idx:03d}_{eid}.pdf"
            render_html_to_pdf(browser, html_path, p)
            add(p)
            print(f"  ✓ {eid}  {row.get('title','')}")

        # 巻末（圧縮案で前付けから移動した A-10/A-11 ＋ 後付け候補）
        if BACK_SECTION_ORDER:
            bk_div = workdir / f"{idx:03d}_div_back.pdf"
            render_simple(browser, '<div class="big" style="font-size:120px;">巻末</div>'
                         '<div class="lab">更新履歴・略称ほか</div>', bk_div, workdir)
            add(bk_div)
            print("  [章扉] 巻末")
            for name in BACK_SECTION_ORDER:
                src = FRONT_DIR / name
                if not src.exists():
                    print(f"  ✗ back/{name} が無い（スキップ）")
                    missing.append(name)
                    continue
                p = workdir / f"{idx:03d}_back_{src.stem}.pdf"
                render_front_file(browser, src, p)
                add(p)
                print(f"  ✓ 巻末  {name}")

        print(f"\n==> {len(parts)} 個の PDF を結合中…")
        merge_pdfs(parts, OUT_PDF)
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    pages = count_pdf_pages(OUT_PDF)
    size_kb = OUT_PDF.stat().st_size // 1024
    print(f"\n==> 完成: {OUT_PDF.relative_to(ROOT)}  ({pages} 物理ページ / {size_kb} KB) [199×281mm 原寸版]")
    if missing:
        print(f"   ※ 取り込めなかった {len(missing)} 件: {', '.join(missing)}")

    trims = [t.strip().lower() for t in args.trims.split(",") if t.strip() and t.strip().lower() != "none"]
    for t in trims:
        if t not in TRIM_SIZES:
            print(f"   ! 未知の判型 '{t}' をスキップ（既知: {', '.join(TRIM_SIZES)}）")
            continue
        w, h = TRIM_SIZES[t]
        dst = PDF_DIR / f"galley_{t.upper()}.pdf"
        if scale_pdf_to_trim(OUT_PDF, dst, w, h):
            print(f"==> 判型版: {dst.relative_to(ROOT)}  （{w}×{h}mm、本番と同じ縮小・「実際のサイズ」で A4 印刷して比較）")
        else:
            print(f"   ✗ {t.upper()} 版の生成に失敗（Ghostscript 不在？）")

    if args.open:
        webbrowser.open(OUT_PDF.as_uri())
    return 0


if __name__ == "__main__":
    sys.exit(main())
