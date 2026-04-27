#!/usr/bin/env python3
"""
preview HTML → PDF 変換と「1 見開き 2 ページに収まっているか」の自動判定。

Chrome の headless 印刷を呼び出して、各エントリの preview HTML を本サイズ
（150mm × 212mm 縦向き）の PDF に書き出す。出力 PDF の物理ページ数を数えて
2 ページに収まっていないエントリ（＝コンテンツがはみ出している可能性）を
警告として表示する。

ブラウザ印刷ダイアログの UI 設定（用紙向き・サイズ）に左右されないため、
本のサイズ確認はこちらが正。

依存: Windows 上の Google Chrome（標準インストール先を自動検出、なければ
$CHROME 環境変数で指定可）。Python 追加ライブラリは不要。

Usage:
    python scripts/preview_to_pdf.py
    python scripts/preview_to_pdf.py --keep-bg-color  # 背景塗り維持
"""

from __future__ import annotations

import argparse
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.platform == "win32" and hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)

ROOT = Path(__file__).resolve().parent.parent
PREVIEW_DIR = ROOT / "drafts" / "prototypes" / "preview"
PDF_DIR = PREVIEW_DIR / "pdf"

# Chrome のインストール先候補（Windows）
CHROME_CANDIDATES = [
    Path(r"C:/Program Files/Google/Chrome/Application/chrome.exe"),
    Path(r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
    Path(r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"),
    Path(r"C:/Program Files/Microsoft/Edge/Application/msedge.exe"),
]


def find_browser() -> Path:
    """Chrome / Edge の実行ファイルを探す。$CHROME 環境変数が最優先。"""
    env = os.environ.get("CHROME")
    if env and Path(env).exists():
        return Path(env)
    for cand in CHROME_CANDIDATES:
        if cand.exists():
            return cand
    found = shutil.which("chrome") or shutil.which("msedge")
    if found:
        return Path(found)
    raise FileNotFoundError(
        "Chrome / Edge が見つかりません。$CHROME を設定するか、標準インストール先に置いてください。"
    )


def count_pdf_pages(pdf_path: Path) -> int:
    """PDF のページ数を pure Python で数える。

    PDF オブジェクト内 `/Type /Page` の出現を数えるが、`/Type /Pages`（複数形、
    ページ木のルート）にもマッチしてしまうので除外する。
    """
    data = pdf_path.read_bytes()
    return len(re.findall(rb"/Type\s*/Page(?!s)", data))


def render_pdf(browser: Path, html_path: Path, pdf_path: Path) -> None:
    """Chrome headless で 1 ファイルだけ PDF 化する。

    --print-to-pdf-no-header を付けてヘッダ・フッタを抑制。@page CSS が効くので
    用紙サイズは preview_gen.py の `@page { size: 150mm 212mm }` がそのまま反映される。
    """
    # ユーザープロファイルを汚さないよう、毎回テンポラリディレクトリを使う
    with tempfile.TemporaryDirectory(prefix="vbcd_print_") as tmp:
        cmd = [
            str(browser),
            "--headless=new",
            "--disable-gpu",
            f"--user-data-dir={tmp}",
            "--no-pdf-header-footer",
            "--virtual-time-budget=4000",  # 描画完了を待つ
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ]
        result = subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            timeout=60,
            check=False,
        )
        if result.returncode != 0 and not pdf_path.exists():
            raise RuntimeError(
                f"Chrome の PDF 出力に失敗: rc={result.returncode}\n"
                f"stderr: {result.stderr.decode('utf-8', errors='replace')[:500]}"
            )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--only",
        help="特定エントリだけ処理（例: --only G-1,J-14）",
        default="",
    )
    args = ap.parse_args()

    try:
        browser = find_browser()
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 2

    only_set = {s.strip() for s in args.only.split(",") if s.strip()}

    html_files = sorted(PREVIEW_DIR.glob("*.html"))
    html_files = [
        f for f in html_files
        if f.name != "index.html" and (not only_set or f.stem in only_set)
    ]
    if not html_files:
        print("対象 preview HTML がありません。先に scripts/preview_gen.py を実行してください。", file=sys.stderr)
        return 2

    PDF_DIR.mkdir(parents=True, exist_ok=True)

    print(f"=== preview → PDF 変換 ({len(html_files)} 件) ===")
    print(f"ブラウザ: {browser}")
    print()

    overflow: list[tuple[str, int]] = []
    failed: list[str] = []

    for f in html_files:
        pdf_path = PDF_DIR / f"{f.stem}.pdf"
        try:
            render_pdf(browser, f, pdf_path)
        except Exception as exc:
            print(f"  ✗ {f.stem}  PDF 出力失敗: {exc}")
            failed.append(f.stem)
            continue

        pages = count_pdf_pages(pdf_path)
        if pages == 2:
            mark = "✓"
        elif pages > 2:
            mark = f"⚠ {pages}p（はみ出し）"
            overflow.append((f.stem, pages))
        else:
            mark = f"⚠ {pages}p（足りない）"
            overflow.append((f.stem, pages))
        print(f"  {mark:24}  {pdf_path.relative_to(ROOT)}")

    print()
    if overflow:
        print(f"=== 1 見開き(2p) に収まっていないエントリ {len(overflow)} 件 ===")
        for eid, pc in overflow:
            print(f"  - {eid}: {pc} pages（本文圧縮 or pages 拡張で対応）")
    else:
        print("=== すべて 2 ページに収まっています ===")
    if failed:
        print(f"\n=== PDF 化に失敗 {len(failed)} 件 ===")
        for eid in failed:
            print(f"  - {eid}")

    return 1 if overflow or failed else 0


if __name__ == "__main__":
    sys.exit(main())
