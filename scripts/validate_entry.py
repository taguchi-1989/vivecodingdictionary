#!/usr/bin/env python3
"""
VibeCodingDictionary エントリ検証スクリプト

Usage:
    # 単体実行：ファイルパスを引数に
    python3 scripts/validate_entry.py content/entries/service/B-1_gemini.md

    # Hook 実行：PostToolUse JSON payload を stdin から受け取る
    echo '{"tool_input":{"file_path":"..."}}' | python3 scripts/validate_entry.py

Exit codes:
    0  全パス
    1  警告のみ（☆ 違反なし。transcript に表示される想定）
    2  ☆ 違反あり（PostToolUse で stderr を Claude に見せる）

設計メモ:
    - docs/quality_checklist.md の ☆ 項目を機械的にチェック
    - archived / sample ステータスはチェック対象外
    - 左ページ 700-800 字、右ページ 250-400 字（100 字超過で ☆ 違反）
    - 標準ライブラリのみ（PyYAML なし、手書き frontmatter parser）
"""

import io
import json
import re
import sys
from pathlib import Path

# Windows cp932 でも絵文字を出力できるように stdout/stderr を UTF-8 に統一
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


# ─── 設定 ─────────────────────────────────────────

REQUIRED_YAML = [
    "id",
    "title",
    "category",
    "figure_type",
    "page_layout",
    "evaluation_date",
    "status",
]

REQUIRED_SECTIONS = [
    "## tagline",
    "## 何をしてくれるか",
    "## どこで出会うか",
    "## メイン図",
    "## 関連用語",
    "## この用語の見どころ",
    "## 開発フローでの位置（必須）",
    "## 非エンジニアのつまずき",
    "## 私のコメント",
]

MIHIDOKORO_SUBS = [
    "### 1. 役割",
    "### 2. うれしさ",
    "### 3. 注意点",
    "### 4. どこで役立つか",
    "### 5. はじめに",
    "### 6. 深掘り先",
]

# 旧テンプレで書かれた箇所を検出して移行を促す（警告のみ）
DEPRECATED_HEADINGS = [
    ("どこで効くか", "「どこで効くか」→「どこで役立つか」（AI 臭回避、2026-04-24 決定）"),
    ("## ひとことで", "「ひとことで」は v2 で廃止。内容は tagline に合流してください"),
    ("## バイブコーディングでの位置づけ", "「バイブコーディングでの位置づけ」→「どこで出会うか」（v2 改名）"),
    ("### 5. 最初に理解する範囲", "「最初に理解する範囲」→「はじめに」（v2 改名）"),
    ("🎯 誰向けか", "「🎯 誰向けか」→「👥 誰向けか」（v2 絵文字変更）"),
]

# 強い断定語（本文に入ると減点）
STRONG_ASSERTION_WORDS = ["最新", "最強", "完全に", "絶対に", "必ず"]

# です・ます調から外れるパターン（語尾検出）
NON_DESU_MASU_PATTERNS = [
    re.compile(r"である[。\s]"),
    re.compile(r"(?<![すまりぞ])だ[。\s]"),  # "です"や"ます"に続く「だ」は除外
]


# ─── 字数目安（quality_checklist.md §H と一致、v2 誌面ベース） ─────────────────

# セクションごとの [key, display_name, min, max, page]
# 個別セクションは超過/下回りとも「⚠️ 警告」のみ。
# ☆（ブロッキング）は左右ページ合計が 100 字超過したときのみ。
# v2_rules_summary.md §2 の決定版ルールを写したもの。数値変更時は v2_rules_summary を先に動かす。
# min/max の「推奨範囲」。超過は ⚠️ 警告（☆ は左右合計 + 100 字超でのみ）
SECTION_TARGETS = [
    ("tagline",        "tagline",            25,  45, "left"),   # 許容 25-45, 推奨 30-38
    ("nanishiteku",    "何をしてくれるか",   60, 200, "left"),   # 許容 60-200, 推奨 80-150
    ("dokode_deau",    "どこで出会うか",     60, 200, "left"),   # 許容 60-200, 推奨 80-150
    ("mihidokoro",     "見どころ 6 視点",   120, 240, "right"),  # 6 視点合計（各 15-40、深掘り 15-50）
    ("kaihatsu_flow",  "開発フローでの位置", 80, 180, "right"),
    # iter 22（2026-04-25）: 関連用語を左ページから右ページ下段（開発フロー直下）へ移動
    ("related_terms",  "関連用語",           20,  50, "right"),
]

# 著者記入欄は誌面に出るが、著者本人が後で書く領域。文字数は情報表示のみ（判定しない）。
AUTHOR_INFO_SECTIONS = [
    ("tsumazuki",         "非エンジニアのつまずき"),
    ("watashino_comment", "私のコメント"),
]

# 左右ページ合計の目安と ☆ 閾値（著者欄は合計に含めない）
# iter 22（2026-04-25）: 関連用語（20-50 字）が左→右へ移動したため、左は -20/-50、右は +20/+50 シフト
LEFT_TOTAL_MIN, LEFT_TOTAL_MAX = 155, 250
RIGHT_TOTAL_MIN, RIGHT_TOTAL_MAX = 220, 430
TOTAL_STARS_OVER = 100   # 合計がこの字数を超えて超過すると ☆


# ─── 結果ラッパ ─────────────────────────────────────────

class Report:
    def __init__(self, path: Path):
        self.path = path
        self.star_fails: list[str] = []  # ☆ 違反（exit 2）
        self.warnings: list[str] = []    # 警告（exit 1）
        self.char_table: list[tuple[str, int, int, int, str, str]] = []
        # 各行: (セクション名, min, max, actual, page, judgement)

    def star(self, msg: str):
        self.star_fails.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)

    def add_char_row(self, display: str, mn: int, mx: int, actual: int, page: str, judge: str):
        self.char_table.append((display, mn, mx, actual, page, judge))

    @property
    def exit_code(self) -> int:
        if self.star_fails:
            return 2
        if self.warnings:
            return 1
        return 0

    def render_char_table(self) -> str:
        if not self.char_table:
            return ""
        out = [
            "### 文字数チェック\n",
            "| セクション | 目安 | 実測 | 差分 | 判定 |",
            "| :-- | --: | --: | --: | :-- |",
        ]
        for display, mn, mx, actual, page, judge in self.char_table:
            # 著者記入欄は target なし（min=max=0 で表現）
            if mn == 0 and mx == 0:
                target_str = "—"
                diff = "—"
            else:
                target_str = f"{mn}-{mx}"
                if actual < mn:
                    diff = f"-{mn - actual}"
                elif actual > mx:
                    diff = f"+{actual - mx}"
                else:
                    diff = "—"
            row = f"| {display} | {target_str} | {actual} | {diff} | {judge} |"
            out.append(row)
        out.append("")
        return "\n".join(out)

    def render(self) -> str:
        lines = [f"## Validator: {self.path.as_posix()}\n"]
        table = self.render_char_table()
        if table:
            lines.append(table)
        if self.star_fails:
            lines.append("### ❌ ☆ 違反（修正必須）\n")
            for m in self.star_fails:
                lines.append(f"- {m}")
            lines.append("")
        if self.warnings:
            lines.append("### ⚠️ 警告\n")
            for m in self.warnings:
                lines.append(f"- {m}")
            lines.append("")
        if not self.star_fails and not self.warnings:
            lines.append("### ✅ 全チェックパス\n")
        return "\n".join(lines)


# ─── Parser（YAML frontmatter の最小実装） ─────────────────

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """YAML frontmatter と本文を分離する。必要最小限の key:value パーサ。"""
    if not content.startswith("---\n"):
        return {}, content
    end = content.find("\n---\n", 4)
    if end == -1:
        return {}, content
    fm_text = content[4:end]
    body = content[end + 5:]
    data: dict = {}
    current_list_key: str | None = None
    for raw in fm_text.split("\n"):
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        if raw.startswith("  - "):
            if current_list_key:
                data.setdefault(current_list_key, []).append(raw[4:].strip())
            continue
        m = re.match(r"^([A-Za-z_]\w*):\s*(.*)$", raw)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if v == "":
                data[k] = []
                current_list_key = k
            else:
                data[k] = v
                current_list_key = None
    return data, body


# ─── 文字数カウント ─────────────────────────────────

def count_chars(text: str) -> int:
    """見出し・HTML コメント・Markdown 装飾・空白を除いた実文字数。"""
    t = re.sub(r"^#+\s.*$", "", text, flags=re.MULTILINE)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.DOTALL)
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"^\s*(\d+\.|-)\s*", "", t, flags=re.MULTILINE)
    t = re.sub(r"[\s\n]+", "", t)
    return len(t)


# ─── チェック関数群 ─────────────────────────────────

def check_yaml(fm: dict, r: Report) -> None:
    for key in REQUIRED_YAML:
        if key not in fm or not str(fm[key]).strip():
            r.star(f"A. YAML: 必須キー `{key}` が欠落")
    if fm.get("page_layout") and fm["page_layout"] != "spread_v1":
        r.warn(f"A. YAML: `page_layout` が `spread_v1` 以外（{fm['page_layout']}）")

    # evaluation_date の書式
    eval_date = str(fm.get("evaluation_date", "")).strip()
    if eval_date and not re.match(r"^\d{4}-\d{2}-\d{2}$", eval_date):
        r.warn(f"A. YAML: `evaluation_date` が YYYY-MM-DD 形式でない（{eval_date}）")


def check_structure(body: str, r: Report) -> None:
    for sec in REQUIRED_SECTIONS:
        if sec not in body:
            r.star(f"B/C 構造: 必須セクション `{sec}` が無い")
    found_subs = [s for s in MIHIDOKORO_SUBS if s in body]
    if len(found_subs) < 6:
        missing = [s for s in MIHIDOKORO_SUBS if s not in body]
        r.star(f"C. 見どころ 6 視点: {', '.join(missing)} が無い")


def check_author_fields_empty(body: str, status: str, r: Report) -> None:
    """著者欄が空スケルトンのままか。

    - status が `drafting` のときは ☆ 違反（AI がまだ書いている段階なので空が正）
    - status が `needs_review` 以降は情報表示のみ（著者が記入している可能性）
    """
    is_strict = status in ("drafting", "candidate", "", None)

    # 非エンジニアのつまずき：`-` のみで、語句なしか
    m = re.search(r"## 非エンジニアのつまずき\n(.*?)(?=\n## |\n<!--)", body, re.DOTALL)
    if m:
        block = m.group(1).strip()
        for line in block.split("\n"):
            line = line.strip()
            if line.startswith("-") and len(line) > 1 and line[1:].strip():
                msg = f"D. 著者欄: 「非エンジニアのつまずき」に記入あり（{line[:40]}…）"
                if is_strict:
                    r.star(msg + " — drafting 中は空スケルトンのままに")
                else:
                    r.warn(msg + " — 著者の記入なら OK")
                break

    # 私のコメント：4 ラベル（🎯 / 👥 どちらも許容）
    label_keys = ["第一印象", "良い点", "ダメな点", "誰向けか"]
    m = re.search(r"## 私のコメント\n(.*?)(?=\n## |\n<!--)", body, re.DOTALL)
    if m:
        block = m.group(1)
        for lbl in label_keys:
            for line in block.split("\n"):
                if lbl in line and ":" in line:
                    after = line.split(":", 1)[-1].strip()
                    if after:
                        msg = f"D. 著者欄: 「私のコメント」の {lbl} に記入あり（{after[:40]}）"
                        if is_strict:
                            r.star(msg + " — drafting 中は空ラベルのままに")
                        else:
                            r.warn(msg + " — 著者の記入なら OK")
                        break


def extract_section(body: str, heading: str) -> str:
    """`## <heading>` の本文を取り出す。次の `## ` またはファイル終端まで。"""
    m = re.search(re.escape("## " + heading) + r"\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    return m.group(1) if m else ""


def extract_mihidokoro_body(body: str) -> str:
    """見どころセクション（### 1〜6 の合計）を取り出す。"""
    section = extract_section(body, "この用語の見どころ")
    return section


def extract_kaihatsu_flow_body(body: str) -> str:
    """開発フローセクションを取り出す。"""
    section = extract_section(body, "開発フローでの位置（必須）")
    return section


def judge_section(actual: int, mn: int, mx: int) -> tuple[str, str]:
    """個別セクション判定（✅ / ⚠️ のみ）。"""
    if mn <= actual <= mx:
        return "✅", ""
    if actual > mx:
        return "⚠️", f"+{actual - mx} 字超過"
    return "⚠️", f"-{mn - actual} 字不足"


def judge_total(actual: int, mn: int, mx: int) -> tuple[str, str]:
    """合計判定（☆ 違反あり）。100 字超過で ❌ ☆。"""
    if mn <= actual <= mx:
        return "✅", ""
    if actual > mx:
        over = actual - mx
        if over > TOTAL_STARS_OVER:
            return "❌ ☆", f"+{over} 字超過（{TOTAL_STARS_OVER} 字超で ☆）"
        return "⚠️", f"+{over} 字超過"
    return "⚠️", f"-{mn - actual} 字不足"


def check_char_counts(body: str, r: Report) -> None:
    """各セクションと左右ページ合計を個別に判定。著者欄は情報表示のみ。"""

    heading_map = {
        "tagline": "tagline",
        "nanishiteku": "何をしてくれるか",
        "dokode_deau": "どこで出会うか",
        "related_terms": "関連用語",
    }
    author_heading_map = {
        "tsumazuki": "非エンジニアのつまずき",
        "watashino_comment": "私のコメント",
    }

    left_total = 0
    right_total = 0

    # 採点対象セクション
    for key, display, mn, mx, page in SECTION_TARGETS:
        if key in heading_map:
            text = extract_section(body, heading_map[key])
        elif key == "mihidokoro":
            text = extract_mihidokoro_body(body)
        elif key == "kaihatsu_flow":
            text = extract_kaihatsu_flow_body(body)
        else:
            text = ""

        actual = count_chars(text)
        if page == "left":
            left_total += actual
        else:
            right_total += actual

        mark, reason = judge_section(actual, mn, mx)
        judgement = mark + ((" " + reason) if reason else "")
        r.add_char_row(display, mn, mx, actual, page, judgement)

        if mark.startswith("⚠️"):
            r.warn(f"H. {display}: {actual} 字（目安 {mn}-{mx}、{reason}）")

    # 著者記入欄は情報表示のみ（著者が書く領域なので判定しない）
    for key, display in AUTHOR_INFO_SECTIONS:
        heading = author_heading_map.get(key)
        if not heading:
            continue
        text = extract_section(body, heading)
        actual = count_chars(text)
        r.add_char_row(display, 0, 0, actual, "right", "ℹ️ 著者記入欄")

    # 左右ページ合計（著者欄は含めない）
    left_mark, left_reason = judge_total(left_total, LEFT_TOTAL_MIN, LEFT_TOTAL_MAX)
    left_judge = left_mark + ((" " + left_reason) if left_reason else "")
    r.add_char_row("**左ページ合計**", LEFT_TOTAL_MIN, LEFT_TOTAL_MAX, left_total, "left", left_judge)
    if left_mark.startswith("❌"):
        r.star(f"H. 左ページ合計: {left_total} 字（目安 {LEFT_TOTAL_MIN}-{LEFT_TOTAL_MAX}、{left_reason}）")
    elif left_mark.startswith("⚠️"):
        r.warn(f"H. 左ページ合計: {left_total} 字（目安 {LEFT_TOTAL_MIN}-{LEFT_TOTAL_MAX}、{left_reason}）")

    right_mark, right_reason = judge_total(right_total, RIGHT_TOTAL_MIN, RIGHT_TOTAL_MAX)
    right_judge = right_mark + ((" " + right_reason) if right_reason else "")
    r.add_char_row("**右ページ合計**", RIGHT_TOTAL_MIN, RIGHT_TOTAL_MAX, right_total, "right", right_judge)
    if right_mark.startswith("❌"):
        r.star(f"H. 右ページ合計: {right_total} 字（目安 {RIGHT_TOTAL_MIN}-{RIGHT_TOTAL_MAX}、{right_reason}）")
    elif right_mark.startswith("⚠️"):
        r.warn(f"H. 右ページ合計: {right_total} 字（目安 {RIGHT_TOTAL_MIN}-{RIGHT_TOTAL_MAX}、{right_reason}）")


def check_tone(body: str, r: Report) -> None:
    # 旧テンプレの残骸（v1 → v2 移行ヘルパ）。警告のみ（☆ にはしない）
    for pat, msg in DEPRECATED_HEADINGS:
        if pat in body:
            r.warn(f"F. v1 テンプレの名残: `{pat}` — {msg}")

    # である調／だ調の検出
    for rx in NON_DESU_MASU_PATTERNS:
        matches = rx.findall(body)
        if matches:
            # 誤検出しやすいのでサンプルだけ警告
            sample = str(rx.pattern)
            r.warn(f"F. トーン: です・ます外れの疑いあり（{sample} のパターン、要目視確認）")
            break

    # 強い断定語
    for w in STRONG_ASSERTION_WORDS:
        if re.search(rf"(?<![「『\w]){re.escape(w)}", body):
            r.warn(f"F. トーン: 強い断定語「{w}」が入っている可能性（要確認）")


def check_sources_date(body: str, fm: dict, r: Report) -> None:
    """出典メモの `checked YYYY-MM-DD` 形式を確認。time-varying entry のみ。"""
    pricing = str(fm.get("pricing_note", "")).strip()
    version = str(fm.get("version_status", "")).strip()
    time_varying = bool(pricing or version)
    if not time_varying:
        return

    m = re.search(r"## 出典メモ\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    if not m:
        r.star("E. 出典メモ: 時変情報を扱うのに `## 出典メモ` セクションが無い")
        return
    sources = m.group(1)
    if not re.search(r"checked\s+\d{4}-\d{2}-\d{2}", sources):
        r.star("E. 出典メモ: `checked YYYY-MM-DD` 形式の記載が無い（時変情報を扱っているのに）")


# ─── メイン ─────────────────────────────────────────

def resolve_path_from_stdin_or_argv() -> Path | None:
    """Hook (JSON on stdin) か CLI 引数 か。"""
    # 引数優先
    if len(sys.argv) > 1:
        return Path(sys.argv[1])

    # stdin JSON
    if not sys.stdin.isatty():
        try:
            data = sys.stdin.read()
            if not data.strip():
                return None
            payload = json.loads(data)
            tool_input = payload.get("tool_input", {})
            file_path = tool_input.get("file_path") or payload.get("tool_response", {}).get("filePath")
            if file_path:
                return Path(file_path)
        except Exception:
            return None
    return None


def should_validate(path: Path) -> bool:
    """content/entries/**/*.md のみ対象。"""
    posix = path.as_posix()
    return bool(re.search(r"(^|/)content/entries/[^/]+/[^/]+\.md$", posix))


def main() -> int:
    path = resolve_path_from_stdin_or_argv()
    if path is None:
        # ファイルが特定できなければ静かに終了（他の Edit/Write には干渉しない）
        return 0

    if not should_validate(path):
        return 0

    if not path.exists():
        print(f"validator: file not found: {path}", file=sys.stderr)
        return 0

    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"validator: read error: {e}", file=sys.stderr)
        return 0

    fm, body = parse_frontmatter(content)

    # archived / sample はチェック対象外
    status = str(fm.get("status", "")).strip()
    if status in ("archived", "sample"):
        return 0

    r = Report(path)
    check_yaml(fm, r)
    check_structure(body, r)
    check_author_fields_empty(body, status, r)
    check_char_counts(body, r)
    check_tone(body, r)
    check_sources_date(body, fm, r)

    # 出力：☆ 違反は stderr（Claude に見せる）、警告は stdout
    rendered = r.render()
    if r.star_fails:
        print(rendered, file=sys.stderr)
    else:
        print(rendered)
    return r.exit_code


if __name__ == "__main__":
    sys.exit(main())
