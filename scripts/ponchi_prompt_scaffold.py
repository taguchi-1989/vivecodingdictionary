#!/usr/bin/env python3
"""Scaffold subject-stack ponchi prompt files from the batch ledger."""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
BATCH_LEDGER = REPO / "ledgers" / "ponchi_generation_batches.csv"
PROMPTS = REPO / "assets" / "ponchi" / "pipeline_prompts"


TYPE_BY_CATEGORY = {
    "common": "front_matter",
    "service": "brand_or_service",
    "model": "model_family",
    "benchmark": "benchmark_or_eval",
    "language": "tool_or_language",
    "concept": "concept",
    "history": "history_or_event",
    "mcp": "tool_or_language",
}


def read_entry(path_value: str) -> str:
    path = REPO / path_value
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def extract_section(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)",
        flags=re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def extract_bullets(section: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        body = line[2:]
        if ":" in body:
            key, value = body.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def clean(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    return value.replace("|", "/")


def remove_readable_text_hints(value: str) -> str:
    value = re.sub(r"「[^」]+」", "blank abstract marks", value)
    value = re.sub(r"『[^』]+』", "blank abstract marks", value)
    value = re.sub(r"(?:blank abstract marks){2,}", "unlabeled workflow stages", value)
    value = re.sub(r"blank abstract marks(?:の)?(?:ロゴ枠|ロゴノード)", "a neutral unlabeled service hub", value)
    value = value.replace("ロゴ枠", "neutral service hub")
    value = value.replace("ロゴノード", "neutral service hub")
    value = value.replace("blank abstract marks", "an unlabeled visual block")
    value = value.replace("v0 のチャット画面", "a generic UI-generation chat panel")
    value = value.replace("v0", "the service concept")
    return clean(value)


def neutralize_entry_name(value: str, title: str) -> str:
    if not title:
        return value
    escaped = re.escape(title)
    value = re.sub(rf"{escaped}\s*(?:アイコン|ロゴ|logo|icon)", "a neutral service symbol", value, flags=re.IGNORECASE)
    value = re.sub(rf"{escaped}\s*(?:画面|コンソール|UI)", "a generic service screen", value, flags=re.IGNORECASE)
    value = re.sub(escaped, "the service concept", value, flags=re.IGNORECASE)
    return clean(value)


def subject_type(row: dict[str, str]) -> str:
    return TYPE_BY_CATEGORY.get(row.get("category", ""), "concept")


def brand_mode(row: dict[str, str]) -> str:
    stage = row.get("pipeline_stage", "")
    if stage == "blocked_brand_asset":
        return "blocked_brand_asset"
    if stage == "overlay_wait":
        return "official_overlay_required"
    if stage in {"overlay_ready", "overlay_audit"}:
        return "official_overlay_ready"
    return "none"


def role_balance(row: dict[str, str]) -> str:
    if row.get("category") == "common":
        return "both_review"
    if row.get("category") == "service":
        return "solo_female_works"
    return "diagram_first"


def composition_family(row: dict[str, str]) -> str:
    category = row.get("category", "")
    subtype = row.get("subtype", "")
    title = row.get("title", "")
    if category == "common":
        return "concept_map"
    if "assistant" in subtype or category == "service":
        return "brand_clearspace" if row.get("pipeline_stage") in {"overlay_wait", "overlay_ready", "overlay_audit"} else "process_flow"
    if "Context" in title or category == "concept":
        return "timeline_scale"
    return "process_flow"


def composition_type(row: dict[str, str]) -> str:
    if row.get("pipeline_stage") in {"overlay_wait", "overlay_ready", "overlay_audit"}:
        return "logo_clearspace"
    if row.get("category") == "common":
        return "diagram_first"
    return "diagram_first"


def has_before_after(memo: str) -> bool:
    return bool(re.search(r"Before\s*/\s*After|Before\s*／\s*After|対比|ビフォー|アフター", memo, re.IGNORECASE))


def view_mode(row: dict[str, str], memo: str, visual_subject_source: str, mode: str) -> str:
    if has_before_after(memo):
        return "before_after"
    if re.search(r"時系列|順番|流れ|フロー|Step|ステップ|push|deploy|デプロイ", visual_subject_source, re.IGNORECASE):
        return "operation_flow"
    if mode != "none":
        return "logo_clearspace"
    if row.get("category") == "common":
        return "structure_map"
    return "diagram_only"


def character_block(row: dict[str, str], memo: str) -> tuple[str, str, str]:
    text = f"{row.get('title','')} {memo}"
    robot = "use" if re.search(r"ロボット|AI|assistant|アシスタント", text, re.IGNORECASE) else "omit"
    male = "use" if re.search(r"エンジニア|開発|男性|技術者", text) else "omit"
    female = "use" if re.search(r"人物|読者|担当者|ユーザー|非エンジニア|企画|デザイン", text) else "omit"
    if female == "omit" and male == "omit" and row.get("category") == "common":
        female = "use"
        male = "use"
    return female, male, robot


def temporary_people_block(memo: str) -> tuple[str, str, str, str]:
    text = memo
    multi = bool(re.search(r"複数|チーム|メンバー|全員|グループ|レビュアー|レビュー|ユーザー|担当者|3 人|3人|2 名|2名", text))
    if not multi:
        return "no", "", "", "temporary people are not needed"

    count = "2-4"
    match = re.search(r"([2-6])\s*(?:人|名)", text)
    if match:
        count = match.group(1)
    role = "background_team"
    if re.search(r"レビュアー|レビュー|確認", text):
        role = "reviewers"
    elif re.search(r"ユーザー|利用者|担当者", text):
        role = "users"
    return (
        "yes",
        count,
        role,
        "allowed only when the entry needs coordination; keep them smaller than Character A/B/C and do not turn them into the main cast",
    )


def make_prompt(row: dict[str, str]) -> str:
    entry_text = read_entry(row["md_path"])
    memo = extract_section(entry_text, "誌面ポンチ絵メモ")
    bullets = extract_bullets(memo)
    main_figure = extract_section(entry_text, "メイン図")
    main_figure_lines = [line.strip() for line in main_figure.splitlines() if line.strip()]
    visual_subject_source = (
        bullets.get("描く内容")
        or bullets.get("中心に置く概念")
        or bullets.get("中央キーワード")
        or (main_figure_lines[0] if main_figure_lines else "")
        or f"{row['title']} concept explained as a simple workflow"
    )
    visual_subject = neutralize_entry_name(remove_readable_text_hints(visual_subject_source), row["title"])
    supporting = clean(
        bullets.get("周辺の要素")
        or bullets.get("登場人物")
        or "generic cards, arrows, simple UI-neutral symbols"
    )
    supporting = neutralize_entry_name(remove_readable_text_hints(supporting), row["title"])
    avoid = "readable text, fake logos, official icons, brand colors, real product UI, watermarks"
    mode = brand_mode(row)
    logo_subject = "none"
    if mode != "none":
        logo_subject = f"official {row['title']} brand overlay after source review"
    female, male, robot = character_block(row, memo)
    clearspace = "no logo clearspace needed"
    if mode in {"official_overlay_ready", "official_overlay_required", "blocked_brand_asset"}:
        clearspace = f"rightmost 40% of top 25% kept completely blank for official {row['title']} logo"
    temp_allowed, temp_count, temp_role, temp_rule = temporary_people_block(memo)
    comparison_mode = "before_after" if has_before_after(memo) else "not_applicable"
    resolved_view_mode = view_mode(row, memo, visual_subject_source, mode)

    return f"""# {row['entry_id']} {row['title']} ponchi prompt

## Scene Brief

```yaml
entry_id: {row['entry_id']}
title: {row['title']}
subject_type: {subject_type(row)}
subject_stack:
  entry_subject: {row['title']}
  visual_subject: {visual_subject}
  supporting_subjects: {supporting}
  logo_subject: {logo_subject}
  excluded_subjects: {avoid}
brand_asset:
  mode: {mode}
  asset_name: {row.get('title', '') if mode != 'none' else ''}
  local_path: {row.get('official_asset', '')}
  source_url:
visual_references:
  character_a: assets/ponchi/references/character-a-reader-woman.png
  character_b: assets/ponchi/references/character-b-teacher-man.png
  character_c: assets/ponchi/references/character-c-pet-robot.png
role_balance: {role_balance(row)}
composition_family: {composition_family(row)}
composition_type: {composition_type(row)}
composition_density: balanced
comparison_mode: {comparison_mode}
view_mode: {resolved_view_mode}
characters:
  female: {female}
  male: {male}
  robot: {robot}
temporary_people:
  allowed: {temp_allowed}
  count: {temp_count}
  role: {temp_role}
  rule: {temp_rule}
hands_policy:
  visible_hands_max: 2
  gesture: simple pointing or operating gesture only if needed
canvas:
  ratio: 2:1
  standard_size: 1254x627
  main_subject_scale: main subject occupies more than half of canvas width
  density_gate: bbox coverage should be at least 0.50 unless visually justified
clearspace:
  required: {'yes' if mode != 'none' else 'no'}
  location: {clearspace}
  size_hint: controlled, not an empty half-page
  forbidden_under_clearspace: characters, faces, hands, cards, icons, arrows, dots, connectors, labels, borders, shadows, placeholders
scene_goal: make {row['title']} understandable as a simple book diagram
main_symbols: {visual_subject}
avoid: {avoid}
```

## Generation Prompt

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for {row['entry_id']} {row['title']}.

Subject: The entry subject is {row['title']}, but the visual subject is {visual_subject}. Show {supporting} only as supporting elements.

Composition: Use {composition_family(row)} / {composition_type(row)} with balanced density. The main subject must occupy more than half of the canvas width. Use 2-4 large visual blocks rather than many tiny cards.

Comparison: {comparison_mode}. If before_after, make the before and after states visibly different without relying on readable text.

Characters: female={female}, male={male}, robot={robot}. Use the recurring Character A/B/C visual references whenever those characters appear. Temporary people allowed={temp_allowed}; if used, keep them secondary and smaller than the recurring characters.

Logo and brand rule: {'Keep the upper-right logo clearspace completely blank white, about the rightmost 40% of the top 25% of the image. Do not generate, imitate, redraw, or approximate any company or service logo. Outside that clearspace, keep the main subject large and complete.' if mode != 'none' else 'No official logo is needed. Do not draw, imitate, or hint at any company or service logo, app icon, product UI, brand mark, or brand color scheme.'}

Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.

Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading, no hatching, no pencil sketch, no painterly texture.

Avoid: {avoid}. No readable text, no watermark.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_id")
    parser.add_argument("--ledger", type=Path, default=BATCH_LEDGER)
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    with args.ledger.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["batch_id"] == args.batch_id]
    if not rows:
        raise SystemExit(f"batch not found: {args.batch_id}")

    out_dir = args.out_dir or PROMPTS / args.batch_id
    out_dir.mkdir(parents=True, exist_ok=True)
    wrote = 0
    skipped = 0
    for row in rows:
        if row["pipeline_stage"] not in {
            "brief_needed",
            "blocked_brand_asset",
            "overlay_wait",
            "overlay_ready",
            "prompt_review",
        }:
            continue
        path = out_dir / f"{row['entry_id']}.md"
        if path.exists() and not args.overwrite:
            skipped += 1
            continue
        path.write_text(make_prompt(row), encoding="utf-8")
        wrote += 1
    print(f"wrote={wrote} skipped={skipped} batch={args.batch_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
