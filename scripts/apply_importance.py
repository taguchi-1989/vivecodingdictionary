#!/usr/bin/env python3
"""
各エントリ md の YAML フロントマターに `importance: A〜E` を一括書き込み。

実行: python3 scripts/apply_importance.py
- archived / sample はスキップ
- reader_level の直下に挿入（なければ status: の前）
- 既存の importance: 行があれば値を上書き
"""

import re
import pathlib

RANKS = {
    # ── letter A: メタ序文（11 件）全件 A
    "A-1": "A", "A-2": "A", "A-3": "A", "A-4": "A", "A-5": "A",
    "A-6": "A", "A-7": "A", "A-8": "A", "A-9": "A", "A-10": "A", "A-11": "A",

    # ── letter B: サービス・ツール（40 件）
    "B-1": "A", "B-2": "A", "B-3": "A",
    "B-4": "B", "B-5": "B", "B-7": "B", "B-8": "B", "B-10": "B", "B-12": "B",
    "B-15": "B", "B-16": "B", "B-23": "B", "B-24": "B", "B-25": "B",
    "B-32": "B", "B-33": "B", "B-50": "B", "B-51": "B", "B-52": "B",
    "B-6": "C", "B-9": "C", "B-11": "C", "B-13": "C", "B-14": "C", "B-17": "C",
    "B-19": "C", "B-20": "C", "B-21": "C", "B-22": "C", "B-26": "C", "B-27": "C",
    "B-29": "C", "B-30": "C", "B-40": "C",
    "B-18": "D", "B-28": "D", "B-31": "D", "B-41": "D", "B-60": "D",
    "B-61": "E",

    # ── letter C: 人物・組織・YouTuber（29 件）
    "C-1": "A", "C-2": "A",
    "C-3": "B", "C-4": "B", "C-7": "B", "C-9": "B",
    "C-5": "C", "C-6": "C", "C-8": "C", "C-10": "C", "C-13": "C", "C-14": "C",
    "C-50": "C", "C-51": "C", "C-52": "C", "C-58": "C", "C-59": "C",
    "C-11": "D", "C-12": "D", "C-53": "D", "C-54": "D", "C-55": "D",
    "C-56": "D", "C-57": "D", "C-60": "D",
    "C-80": "E", "C-81": "E", "C-82": "E", "C-83": "E",

    # ── letter D: モデル（38 件）
    "D-1": "B", "D-2": "B", "D-3": "B", "D-11": "B", "D-12": "B", "D-13": "B",
    "D-21": "B", "D-22": "B", "D-23": "B", "D-30": "B",
    "D-4": "C", "D-10": "C", "D-20": "C", "D-26": "C", "D-35": "C",
    "D-40": "C", "D-41": "C", "D-42": "C", "D-43": "C", "D-46": "C",
    "D-47": "C", "D-50": "C",
    "D-24": "D", "D-44": "D", "D-45": "D", "D-51": "D", "D-52": "D",
    "D-53": "D", "D-54": "D", "D-55": "D", "D-56": "D", "D-57": "D",
    "D-58": "D", "D-71": "D",
    "D-14": "E", "D-25": "E", "D-60": "E", "D-70": "E",

    # ── letter E: ベンチマーク（19 件）
    "E-50": "B",
    "E-1": "C", "E-2": "C", "E-20": "C", "E-26": "C",
    "E-3": "D", "E-4": "D", "E-21": "D", "E-22": "D", "E-23": "D",
    "E-24": "D", "E-25": "D", "E-30": "D", "E-31": "D", "E-51": "D",
    "E-27": "E", "E-32": "E", "E-33": "E", "E-34": "E",

    # ── letter F: 言語・ツール（83 件）
    "F-30": "B", "F-100": "B", "F-150": "B",
    "F-50": "C", "F-60": "C",
    "F-1": "C", "F-2": "C", "F-3": "C", "F-4": "C", "F-5": "C",
    "F-6": "C", "F-7": "C", "F-8": "C", "F-9": "C", "F-10": "C", "F-11": "C",
    "F-40": "C", "F-41": "C", "F-42": "C", "F-43": "C", "F-44": "C",
    "F-51": "C", "F-52": "C", "F-53": "C", "F-54": "C", "F-55": "C",
    "F-56": "C", "F-57": "C", "F-59": "C", "F-61": "C", "F-62": "C",
    "F-90": "C",
    "F-12": "D", "F-13": "D", "F-14": "D", "F-15": "D", "F-16": "D", "F-17": "D",
    "F-20": "D", "F-21": "D", "F-34": "D", "F-35": "D", "F-36": "D", "F-37": "D",
    "F-38": "D", "F-58": "D", "F-71": "D", "F-80": "D", "F-81": "D", "F-82": "D",
    "F-83": "D", "F-86": "D", "F-91": "D", "F-101": "D", "F-102": "D", "F-103": "D",
    "F-104": "D", "F-110": "D", "F-111": "D", "F-120": "D", "F-121": "D", "F-122": "D",
    "F-123": "D", "F-130": "D", "F-140": "D", "F-151": "D", "F-153": "D", "F-154": "D",
    "F-160": "D", "F-161": "D", "F-162": "D", "F-170": "D", "F-171": "D", "F-172": "D",
    "F-190": "D", "F-200": "D",
    "F-84": "E", "F-85": "E", "F-87": "E", "F-141": "E", "F-152": "E",
    "F-180": "E", "F-181": "E",

    # ── letter G: バイブコーディング特有（40 件）
    "G-40": "A",  # 本書のテーマ語、A 格上げ
    "G-1": "B", "G-2": "B", "G-10": "B", "G-14": "B", "G-30": "B",
    "G-35": "B", "G-36": "B",
    "G-3": "C", "G-4": "C", "G-5": "C", "G-6": "C", "G-9": "C",
    "G-13": "C", "G-15": "C", "G-16": "C", "G-17": "C", "G-18": "C",
    "G-19": "C", "G-20": "C", "G-21": "C", "G-22": "C", "G-23": "C",
    "G-7": "D", "G-8": "D", "G-11": "D", "G-12": "D", "G-31": "D",
    "G-32": "D", "G-33": "D", "G-34": "D", "G-38": "D", "G-39": "D",
    "G-41": "D", "G-42": "D",
    "G-43": "E", "G-44": "E", "G-45": "E", "G-46": "E", "G-47": "E",

    # ── letter H: 歴史・ワークフロー（22 件）
    "H-3": "B", "H-53": "B", "H-63": "B",
    "H-1": "C", "H-7": "C", "H-8": "C", "H-50": "C", "H-52": "C",
    "H-54": "C", "H-56": "C", "H-57": "C",
    "H-2": "D", "H-4": "D", "H-5": "D", "H-6": "D", "H-51": "D",
    "H-55": "D", "H-59": "D", "H-60": "D",
    "H-58": "E", "H-61": "E", "H-62": "E",

    # ── letter I: MCP（19 件）
    "I-1": "B",
    "I-2": "C", "I-3": "C", "I-10": "C", "I-11": "C", "I-20": "C",
    "I-4": "D", "I-5": "D", "I-12": "D", "I-13": "D", "I-21": "D",
    "I-22": "D", "I-23": "D", "I-24": "D", "I-30": "D", "I-50": "D",
    "I-41": "E", "I-80": "E", "I-81": "E",

    # ── letter J: 一般用語（50 件）
    "J-1": "A", "J-14": "A", "J-51": "A",
    "J-10": "B", "J-11": "B", "J-13": "B", "J-50": "B", "J-77": "B",
    "J-2": "C", "J-3": "C", "J-4": "C", "J-12": "C", "J-15": "C", "J-16": "C",
    "J-17": "C", "J-19": "C", "J-20": "C", "J-22": "C", "J-41": "C",
    "J-43": "C", "J-52": "C", "J-90": "C", "J-91": "C", "J-100": "C",
    "J-18": "D", "J-21": "D", "J-23": "D", "J-40": "D", "J-42": "D",
    "J-53": "D", "J-54": "D", "J-55": "D", "J-56": "D", "J-62": "D",
    "J-70": "D", "J-71": "D", "J-72": "D", "J-74": "D", "J-76": "D", "J-92": "D",
    "J-31": "E", "J-32": "E", "J-33": "E", "J-73": "E", "J-75": "E",
    "J-78": "E", "J-79": "E", "J-80": "E", "J-81": "E", "J-93": "E",
}


def insert_importance(text: str, rank: str) -> str:
    """frontmatter に `importance: <rank>` を入れる（既存があれば更新）。"""
    m = re.match(r"(---\n)(.*?)(\n---)", text, flags=re.DOTALL)
    if not m:
        return text
    head, body, tail = m.group(1), m.group(2), m.group(3)
    rest = text[m.end():]

    # 既存の importance: 行があれば値を差し替え
    if re.search(r"^importance:", body, flags=re.MULTILINE):
        body = re.sub(
            r"^importance:.*$",
            f"importance: {rank}",
            body,
            count=1,
            flags=re.MULTILINE,
        )
        return head + body + tail + rest

    new_line = f"importance: {rank}\n"
    # reader_level: の直後に挿入
    if re.search(r"^reader_level:", body, flags=re.MULTILINE):
        body = re.sub(
            r"(^reader_level:.*\n)",
            r"\1" + new_line,
            body,
            count=1,
            flags=re.MULTILINE,
        )
    # なければ status: の前に挿入
    elif re.search(r"^status:", body, flags=re.MULTILINE):
        body = re.sub(
            r"(^status:)",
            new_line + r"\1",
            body,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        body = body.rstrip() + "\n" + new_line
    return head + body + tail + rest


def main() -> None:
    root = pathlib.Path("content/entries")
    counts = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    skipped, missing, updated = 0, 0, 0
    for p in root.glob("**/*.md"):
        txt = p.read_text(encoding="utf-8")
        sm = re.search(r"^status:\s*(\w+)", txt, flags=re.MULTILINE)
        status = sm.group(1) if sm else ""
        if status in ("archived", "sample"):
            skipped += 1
            continue
        idm = re.search(r"^id:\s*(\S+)", txt, flags=re.MULTILINE)
        if not idm:
            missing += 1
            continue
        eid = idm.group(1)
        if eid not in RANKS:
            print(f"  [no rank] {eid} ({p})")
            missing += 1
            continue
        rank = RANKS[eid]
        new_txt = insert_importance(txt, rank)
        if new_txt != txt:
            p.write_text(new_txt, encoding="utf-8")
            updated += 1
            counts[rank] += 1
    print(f"updated: {updated}")
    print(f"skipped (archived/sample): {skipped}")
    print(f"missing (no id or no rank): {missing}")
    for r in "ABCDE":
        print(f"  {r}: {counts[r]} 件")


if __name__ == "__main__":
    main()
