#!/usr/bin/env python3
"""Score blind ponchi identification quiz responses."""
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def confidence(value: str) -> int:
    try:
        return max(0, min(100, int(float(value))))
    except (TypeError, ValueError):
        return 0


def decision(top1_correct: bool, top3_correct: bool, conf: int) -> str:
    if top1_correct and conf >= 70:
        return "semantic_ok"
    if top1_correct:
        return "weak_but_identifiable"
    if top3_correct:
        return "ambiguous"
    if conf >= 70:
        return "misleading"
    return "generic"


def normalize_guess(value: str, aliases: dict[str, str]) -> str:
    value = (value or "").strip()
    return aliases.get(value, value)


def load_aliases(candidates: Path | None) -> dict[str, str]:
    aliases: dict[str, str] = {}
    if not candidates:
        return aliases
    for row in read_csv(candidates):
        entry_id = row.get("entry_id", "").strip()
        title = row.get("title", "").strip()
        if entry_id:
            aliases[entry_id] = entry_id
        if title and entry_id:
            aliases[title] = entry_id
    return aliases


def score(answer_key: Path, responses: Path, candidates: Path | None = None) -> list[dict[str, str]]:
    key_rows = {row["blind_image_id"]: row for row in read_csv(answer_key)}
    response_rows = read_csv(responses)
    aliases = load_aliases(candidates)
    scored: list[dict[str, str]] = []

    for row in response_rows:
        blind_id = row["blind_image_id"]
        key = key_rows.get(blind_id, {})
        expected = key.get("entry_id", "")
        raw_guesses = [row.get("top1_guess", ""), row.get("top2_guess", ""), row.get("top3_guess", "")]
        guesses = [normalize_guess(guess, aliases) for guess in raw_guesses]
        conf = confidence(row.get("top1_confidence", ""))
        top1_correct = guesses[0] == expected
        top3_correct = expected in guesses
        scored.append(
            {
                "blind_image_id": blind_id,
                "expected_entry_id": expected,
                "expected_title": key.get("title", ""),
                "top1_guess": guesses[0],
                "top1_guess_raw": raw_guesses[0],
                "top1_confidence": str(conf),
                "top2_guess": guesses[1],
                "top2_guess_raw": raw_guesses[1],
                "top3_guess": guesses[2],
                "top3_guess_raw": raw_guesses[2],
                "top1_correct": str(top1_correct).lower(),
                "top3_correct": str(top3_correct).lower(),
                "semantic_decision": decision(top1_correct, top3_correct, conf),
                "visual_evidence": row.get("visual_evidence", ""),
                "confused_with": row.get("confused_with", ""),
                "semantic_comment": row.get("semantic_comment", ""),
            }
        )
    return scored


def write_summary(path: Path, scored: list[dict[str, str]], chapter: str) -> None:
    total = len(scored)
    top1 = sum(row["top1_correct"] == "true" for row in scored)
    top3 = sum(row["top3_correct"] == "true" for row in scored)
    decisions = Counter(row["semantic_decision"] for row in scored)
    wrong = [row for row in scored if row["top1_correct"] != "true"]

    lines = [
        f"# Ponchi Blind Quiz Score {chapter}",
        "",
        "## Summary",
        "",
        f"- total: {total}",
        f"- top1_correct: {top1} / {total}",
        f"- top3_correct: {top3} / {total}",
        "",
        "## Decisions",
        "",
        "| decision | count |",
        "| --- | ---: |",
    ]
    for name, count in sorted(decisions.items()):
        lines.append(f"| `{name}` | {count} |")

    lines.extend(["", "## Non-Top1 Items", "", "| blind | expected | guess | confidence | decision | confused/comment |", "| --- | --- | --- | ---: | --- | --- |"])
    for row in wrong:
        note = row["confused_with"] or row["semantic_comment"]
        lines.append(
            f"| `{row['blind_image_id']}` | `{row['expected_entry_id']}` {row['expected_title']} | "
            f"`{row['top1_guess']}` | {row['top1_confidence']} | `{row['semantic_decision']}` | {note} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", required=True)
    parser.add_argument("--answer-key", type=Path, required=True)
    parser.add_argument("--candidates", type=Path)
    parser.add_argument("--responses", type=Path, required=True)
    parser.add_argument("--out-csv", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    scored = score(args.answer_key, args.responses, args.candidates)
    fieldnames = [
        "blind_image_id",
        "expected_entry_id",
        "expected_title",
        "top1_guess",
        "top1_guess_raw",
        "top1_confidence",
        "top2_guess",
        "top2_guess_raw",
        "top3_guess",
        "top3_guess_raw",
        "top1_correct",
        "top3_correct",
        "semantic_decision",
        "visual_evidence",
        "confused_with",
        "semantic_comment",
    ]
    write_csv(args.out_csv, scored, fieldnames)
    write_summary(args.out_md, scored, args.chapter)
    print(f"wrote {args.out_csv}")
    print(f"wrote {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
