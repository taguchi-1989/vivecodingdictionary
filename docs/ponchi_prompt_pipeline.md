# Ponchi Prompt Pipeline

ポンチ絵を量産するときに、毎回の判断を場当たりにしないためのプロンプト設計パイプライン。

## 進化方針

これまでの試作で分かったこと:

- `2:1` は寸法だけでは不十分。横長の誌面全体に意味が必要。
- ロゴ用 clearspace を強く指示すると、右側が空きすぎる。
- ブランド回はロゴを AI に描かせず、公式素材の後合成に分ける必要がある。
- キャラはプロンプトだけでは安定しないため、A/B/C の視覚参照を毎回使う。
- 多人数が必要な場面では、一時キャラを許可しないと説明できない。
- 章ごとに「題材」と「絵の主役」を分けないと、ロゴやサービス名が主役になりすぎる。

次の段階では、各画像を次の順に処理する。

1. 題材を分類する。
2. 絵の主役を決める。
3. ロゴ状態を決める。
4. キャラの必要性を決める。
5. 構図ファミリーと密度を決める。
6. scene brief を作る。
7. プロンプトを生成する。
8. 2:1 ベース画像を生成する。
9. 密度監査を通す。
10. 公式ロゴが必要なら後合成する。
11. contact sheet で目視監査する。
12. final へ昇格するか、再生成理由を記録する。

## Subject Stack

`title` をそのまま絵にしない。必ず subject stack に分解する。

```yaml
subject_stack:
  entry_subject: 用語・サービス・章タイトルそのもの
  visual_subject: 絵で一番大きく見せる概念
  supporting_subjects: 補助的に出す小物・人・流れ
  logo_subject: 後合成する公式ブランド素材。不要なら none
  excluded_subjects: 似てしまうと危険なロゴ、UI、色、文字
```

例:

```yaml
entry_subject: OpenAI
visual_subject: neutral central AI company hub branching to capability cards
supporting_subjects: chat card, image card, video card, developer API card
logo_subject: official OpenAI wordmark overlay
excluded_subjects: OpenAI knot, ChatGPT logo, DALL-E logo, Sora logo, product UI
```

`visual_subject` が空のままなら生成しない。ロゴやタイトルではなく、読者が見て意味を取る主図解を先に決める。

## Classification

### 題材タイプ

| type | 使う場面 | 絵の主役 |
| --- | --- | --- |
| `brand_or_service` | Gemini, OpenAI, Claude, GitHub など | そのサービスが担う仕事の構造 |
| `model_family` | Claude 4 系, GPT 系など | 世代、層、性能差、使い分け |
| `tool_or_language` | JavaScript, MCP, CLI など | 入出力、接続、実行、検証の流れ |
| `benchmark_or_eval` | SWE-Bench など | 問題から評価結果までの流れ |
| `concept` | Context, LLM など | 抽象概念の構造またはプロセス |
| `history_or_event` | ChatGPT 登場など | 出来事が広がる流れ |
| `front_matter` | まえがき、導入など | 読者と技術者をつなぐ比喩 |

### ロゴ状態

| state | 進め方 |
| --- | --- |
| `none` | ロゴ不要。通常の2:1生成へ進む。 |
| `official_overlay_ready` | 公式素材、出典、ローカルパスがある。ベース生成後に後合成する。 |
| `official_overlay_required` | ロゴが必要だが素材未取得。ベースは作れるが final 昇格は止める。 |
| `blocked_brand_asset` | 公式素材や利用条件が不明。AI 代替生成は禁止。 |

### 構図密度

| density | 使う場面 | 注意 |
| --- | --- | --- |
| `compact` | 小さな手順や単一操作 | 詰め込みすぎない |
| `balanced` | 標準 | まずこれを使う |
| `spacious` | 意図的に距離や広がりを見せる | ロゴ用空白の言い訳にしない |

ブランド回でも `balanced` を基本にする。`spacious` は H-53 のように「広がる現象」自体が主題のときだけ使う。

## Scene Brief Template

```yaml
entry_id:
title:
subject_type: brand_or_service | model_family | tool_or_language | benchmark_or_eval | concept | history_or_event | front_matter
subject_stack:
  entry_subject:
  visual_subject:
  supporting_subjects:
  logo_subject:
  excluded_subjects:
brand_asset:
  mode: none | official_overlay_ready | official_overlay_required | blocked_brand_asset
  asset_name:
  local_path:
  source_url:
visual_references:
  character_a: assets/ponchi/references/character-a-reader-woman.png
  character_b: assets/ponchi/references/character-b-teacher-man.png
  character_c: assets/ponchi/references/character-c-pet-robot.png
role_balance:
composition_family:
composition_type:
composition_density: compact | balanced | spacious
view_mode: before_after | operation_flow | structure_map | logo_clearspace | diagram_only
characters:
  female: use | omit
  male: use | omit
  robot: use | omit
temporary_people:
  allowed: yes | no
  count:
  role: background_team | crowd | reviewers | users
  rule:
hands_policy:
  visible_hands_max:
  gesture:
canvas:
  ratio: 2:1
  standard_size: 1254x627
  main_subject_scale:
  density_gate:
clearspace:
  required: yes | no
  location:
  size_hint:
  forbidden_under_clearspace:
scene_goal:
main_symbols:
avoid:
```

## Prompt Template

```text
Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for <entry_id> <title>.

Subject: The entry subject is <entry_subject>, but the visual subject is <visual_subject>.
Show <supporting_subjects> only as supporting elements.

Composition: Use <composition_family> / <composition_type> with <composition_density> density.
The main subject must occupy more than half of the canvas width unless the scene brief explicitly says otherwise.
Use 2-4 large visual blocks rather than many tiny cards.

Characters: <character instructions from scene brief>.
Use the recurring Character A/B/C visual references whenever those characters appear.
Temporary people are allowed only if the scene brief says yes, and must remain secondary.

Logo and brand rule: <logo block based on brand_asset.mode>.

Color palette: strict white/black/gray plus approved blue accents only:
#FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.
Do not use yellow, green, red, purple, brown, orange, rainbow colors, decorative blue sparkles, blue background fills, or brand colors.

Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading, no hatching, no pencil sketch, no painterly texture.

Avoid: <avoid list>. No readable text, no watermark.
```

### Logo Block: none

```text
Logo rule: no official logo is needed. Do not draw, imitate, or hint at any company or service logo, app icon, product UI, brand mark, or brand color scheme.
```

### Logo Block: official overlay ready/required

```text
Logo rule: do not generate, imitate, redraw, or approximate any company or service logo.
Keep the upper-right logo clearspace completely blank white, about the rightmost 40% of the top 25% of the image.
Do not place any card, icon, connector, dot, line, character, face, hand, symbol, pattern, label, border, shadow, or placeholder under that area.
Outside that clearspace, keep the main subject large and complete. Do not leave an empty half-page for the logo.
```

## Audit Gates

### Generated Base

Required:

- `1254x627` or cleanly normalizable to `1254x627`.
- No generated logos, icons, official marks, brand colors, real UI, or readable text.
- Subject is visible as a few large blocks at 200px thumbnail size.
- Main subject is not pushed into a corner.
- For logo images, upper-right clearspace is blank but not oversized.
- Character A/B/C remain visually consistent if used.

Recommended automated gate:

```powershell
C:\Users\tgch1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe `
  scripts\ponchi_image_audit.py `
  <base_1254x627.png> `
  --min-bbox-coverage 0.50 `
  --max-clearspace-ink 0.015
```

This gate checks both:

- `bbox_coverage >= 0.50`: the subject is not too small or sparse.
- `clearspace_ink_ratio <= 0.015`: the upper-right logo area is effectively blank.

Use the density-only `composite_official_logo.py --audit-density` gate only when an official logo overlay is being produced at the same time.

### Overlay

Required:

- Official source is recorded in `docs/brand_usage_audit.md`.
- Logo shape, color, aspect ratio, and built-in clearspace are unchanged.
- Logo does not cover or touch important diagram elements.
- Logo does not make the image look like an advertisement banner.
- Overlay output is still `1254x627`.

## Batch Workflow

For a 20 image batch:

1. Build one `scene_brief` per entry.
2. Check that at least 3 composition families appear in the batch.
3. Check that `role_balance` is not repeated for every image.
4. If legacy final images already exist, audit them first as evidence only; do not promote them automatically.
5. Generate base images only.
6. Copy generated outputs into `assets/ponchi/experiments/regeneration/<batch-name>/`.
7. Normalize to `1254x627`.
8. Create a contact sheet.
9. Run density audit.
10. Update an audit markdown with `accept`, `rerun`, `overlay_wait`, or `reject`.
11. Only then run official logo overlays.

## Status Labels

| label | Meaning |
| --- | --- |
| `base_candidate` | Base image passed visual review but no logo overlay yet. |
| `needs_rerun_density` | Subject is too small, too sparse, or too fine. |
| `needs_rerun_clearspace` | Logo area is polluted or too large. |
| `overlay_wait` | Base is usable but official logo asset is missing. |
| `overlay_candidate` | Official logo overlay exists and needs final preview review. |
| `final_ready` | Ready to promote to `assets/ponchi/final/`. |
| `blocked_brand_asset` | Must not proceed until official asset is confirmed. |
