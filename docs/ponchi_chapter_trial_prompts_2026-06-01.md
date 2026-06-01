# Ponchi Chapter Trial Prompts 2026-06-01

各章から 1 件ずつ、現在の 2:1 画像生成ルールで試作するための scene brief と生成プロンプト。

共通ルール:

- 2:1 horizontal landscape book illustration.
- Clean simple editorial line illustration, white background, uniform black linework, light gray fills.
- Use only `#FFFFFF`, `#F7F9FC`, `#1A1A1A`, `#6B7280`, `#EAF1FB`, `#D6E6FA`, `#8DB7E8`, `#3F7FD1`, `#123E82`.
- Do not generate readable text, logos, official icons, real product UI, brand colors, real-person likenesses, mascots, or watermarks.
- Use recurring Character A/B/C visual references:
  - `assets/ponchi/references/character-a-reader-woman.png`
  - `assets/ponchi/references/character-b-teacher-man.png`
  - `assets/ponchi/references/character-c-pet-robot.png`
- Temporary people are allowed only for crowd/team scenes, and must remain secondary.
- Brand entries reserve quiet upper-right logo clearspace; no drawing under that future logo area.
- Do not over-reserve blank space. The main subject should occupy more than half of the canvas width; logo clearspace must be controlled and intentional, not an empty half-page.
- For brand entries, keep the rightmost 40% of the top 25% of the image completely blank white for the future logo. Outside that area, use left, center, lower center, and lower right space for the main subject.
- Use `composition_density: balanced` by default. Use `spacious` only when the empty area is part of the concept, not just a logo placeholder.

## A-1 まえがき

Scene brief:

```yaml
entry_id: A-1
title: まえがき
subject_type: front_matter
subject_stack:
  entry_subject: まえがき
  visual_subject: shared vocabulary bridge between non-engineer and engineer
  supporting_subjects: Character A, Character B, abstract paper cards
  logo_subject: none
  excluded_subjects: readable Japanese text, brand marks, product UI
brand_asset:
  mode: none
visual_references:
  character_a: assets/ponchi/references/character-a-reader-woman.png
  character_b: assets/ponchi/references/character-b-teacher-man.png
  character_c: omit
role_balance: both_review
composition_family: concept_map
composition_type: standing_board
view_mode: structure_map
character_base:
  female: use
  male: use
  robot: omit
temporary_people:
  allowed: no
scene_goal: 非エンジニアとエンジニアの言葉を小さな橋でつなぐ
main_symbols: small bridge, two abstract word cards, shared glossary path
clearspace: natural whitespace around bridge
avoid: readable Japanese text, logos, dark background
```

Prompt:

```text
Create a 2:1 horizontal book ponchi illustration for A-1 Preface.
Show Character A and Character B facing each other across a small simple bridge made of abstract paper cards, representing a shared vocabulary bridge between non-engineer and engineer. Use the recurring character references for their hair, clothing, proportions, and line style. No robot in this image. The bridge and cards must have no readable text; use simple blank marks and dots only. Clean white background, generous whitespace, calm editorial composition.
```

## B-1 Gemini

Scene brief:

```yaml
entry_id: B-1
title: Gemini
subject_type: brand_or_service
subject_stack:
  entry_subject: Gemini
  visual_subject: multi-entry AI assistant hub
  supporting_subjects: browser card, phone card, document card, developer cloud card, Character A, Character C
  logo_subject: official Gemini/Google overlay after source review
  excluded_subjects: Gemini logo, Google logo, Google app icons, Google colors, real Google UI
brand_asset:
  mode: official_overlay_required
role_balance: solo_female_works
composition_family: brand_clearspace
composition_type: logo_clearspace
composition_density: balanced
view_mode: logo_clearspace
character_base:
  female: use
  male: omit
  robot: use
temporary_people:
  allowed: no
scene_goal: 複数入口を持つ AI アシスタントとして見せる
main_symbols: browser card, phone card, document card, cloud developer card
clearspace: rightmost 40% of top 25% kept completely blank for official Gemini logo
main_subject_scale: Character A and the AI hub must occupy left, center, and lower-right width; do not leave the entire right half empty
avoid: Gemini logo, Google colors, Google app icons, readable UI
```

Prompt:

```text
Create a 2:1 horizontal book ponchi illustration for B-1 Gemini.
Keep the upper-right logo clearspace completely blank white, about the rightmost 40% of the top 25% of the image. Do not place any card, icon, connector, character, robot, dot, line, or pattern under that area, but do not leave the whole right half empty. Make Character A, Character C, the neutral AI hub, and four generic entry-point cards occupy a strong left, center, and lower-right composition across more than half the canvas width. Use larger cards and connectors than a thumbnail-sized diagram. Do not draw the Gemini logo, Google logo, Google app icons, brand colors, or real UI. Use only generic cards, nodes, arrows, and approved blue accents.
```

## C-1 OpenAI

Scene brief:

```yaml
entry_id: C-1
title: OpenAI
subject_type: brand_or_service
subject_stack:
  entry_subject: OpenAI
  visual_subject: neutral central AI company hub branching to capability cards
  supporting_subjects: chat card, image card, video card, developer API card
  logo_subject: official OpenAI wordmark overlay
  excluded_subjects: OpenAI knot, ChatGPT logo, DALL-E logo, Sora logo, product UI, brand colors
brand_asset:
  mode: official_overlay_ready
  asset_name: OpenAI wordmark
  local_path: assets/logos/openai/openai_wordmark_black_official_template_layer.png
  source_url: https://cdn.openai.com/brand/OpenAI-Partnership-Templates-2025.zip
role_balance: diagram_only
composition_family: brand_clearspace
composition_type: logo_clearspace
composition_density: balanced
view_mode: structure_map
character_base:
  female: omit
  male: omit
  robot: omit
temporary_people:
  allowed: no
scene_goal: 企業から複数の AI サービスが伸びる構造
main_symbols: central company building block, chat, image, video, API cards
clearspace: rightmost 40% of top 25% kept completely blank for official OpenAI logo
main_subject_scale: central hub and capability cards must be large enough to read at thumbnail size
avoid: OpenAI mark, ChatGPT logo, product UI, readable labels
```

Prompt:

```text
Create a 2:1 horizontal book ponchi illustration for C-1 OpenAI.
Keep the upper-right logo clearspace completely blank white, about the rightmost 40% of the top 25% of the image. Do not place any card, icon, connector, dot, symbol, or pattern under that area. Make a diagram-first composition with a large neutral central company block and four large generic capability cards for chat, image generation, video generation, and API/developer access. The main hub and cards should occupy the center-left, lower center, and lower-right enough that the image feels complete before the logo is added. No people. Do not draw OpenAI, ChatGPT, DALL-E, Sora, knots, official marks, product UI, readable labels, or brand colors. Use only generic shapes and approved blue semantic highlights.
```

## D-12 Claude 4 系

Scene brief:

```yaml
entry_id: D-12
title: Claude 4 系
subject_type: model_family
subject_stack:
  entry_subject: Claude 4 系
  visual_subject: three simplified model-family lanes with tool and outcome symbols
  supporting_subjects: lane cards, quality marker, speed marker, tool-use node
  logo_subject: official Claude/Anthropic overlay after source review
  excluded_subjects: Claude logo, Anthropic mark, model names as readable text, brand colors
brand_asset:
  mode: official_overlay_required
role_balance: diagram_only
composition_family: timeline_scale
composition_type: diagram_only
composition_density: balanced
view_mode: logo_clearspace
character_base:
  female: omit
  male: omit
  robot: omit
temporary_people:
  allowed: no
scene_goal: Opus/Sonnet/Haiku の層とモデル世代の進化
main_symbols: three large tier lanes, model generation timeline, tool-use nodes
clearspace: rightmost 40% of top 25% kept completely blank for official Claude/Anthropic logo
main_subject_scale: fewer larger cards; three lanes must read as large blocks, not many tiny steps
avoid: Claude logo, Anthropic mark, readable model names, brand colors
```

Prompt:

```text
Create a 2:1 horizontal book ponchi illustration for D-12 Claude 4 series.
Keep the upper-right logo clearspace completely blank white, about the rightmost 40% of the top 25% of the image. Do not place any card, icon, connector, timeline marker, dot, symbol, or pattern under that area. Use a diagram-only timeline and tier structure: three large horizontal model lanes with only a few large neutral cards moving forward, plus simple tool-use nodes and quality/speed markers. Avoid many tiny boxes; the three lanes must remain readable at thumbnail size. Do not write Opus, Sonnet, Haiku, Claude, or any readable text in the image. Do not draw the Claude or Anthropic logo, brand colors, or product UI.
```

## E-1 SWE-Bench

Scene brief:

```yaml
entry_id: E-1
title: SWE-Bench
subject_type: benchmark_or_eval
subject_stack:
  entry_subject: SWE-Bench
  visual_subject: benchmark workflow from issue to patch to hidden tests to score
  supporting_subjects: Character B, Character C, issue card, repo folder, patch card, test gate, score meter
  logo_subject: none
  excluded_subjects: GitHub logo, real repository UI, readable code, brand colors
brand_asset:
  mode: none
role_balance: robot_supports
composition_family: process_flow
composition_type: robot_console
view_mode: operation_flow
character_base:
  female: omit
  male: use
  robot: use
temporary_people:
  allowed: no
scene_goal: OSS issue から patch と test pass までの評価フロー
main_symbols: issue card, repository folder, patch card, hidden test gate, score meter
clearspace: no logo clearspace needed
avoid: GitHub logo, real repo UI, readable code, brand colors
```

Prompt:

```text
Create a 2:1 horizontal book ponchi illustration for E-1 SWE-Bench.
Show Character B working with Character C through a generic benchmark workflow: an issue card flows into a repository folder, then a patch card, then a hidden test gate, then a simple score meter. Use generic cards and arrows only. Do not draw GitHub logos, real repository UI, readable code, or text. Keep Character C small and supportive. Clean editorial line illustration with approved blue for the active path.
```

## F-1 JavaScript

Scene brief:

```yaml
entry_id: F-1
title: JavaScript
subject_type: tool_or_language
subject_stack:
  entry_subject: JavaScript
  visual_subject: script node connecting browser interaction, validation, server, and UI state
  supporting_subjects: browser frame, button action, input-check card, server card, UI state card
  logo_subject: none
  excluded_subjects: JavaScript logo, yellow square, framework logos, readable code
brand_asset:
  mode: none
role_balance: diagram_only
composition_family: concept_map
composition_type: diagram_first
view_mode: structure_map
character_base:
  female: omit
  male: omit
  robot: omit
temporary_people:
  allowed: no
scene_goal: Web の動きを作る言語としての位置
main_symbols: browser frame, button action, input check, server card, UI card
clearspace: no logo clearspace needed
avoid: JS logo, yellow, framework logos, readable code
```

Prompt:

```text
Create a 2:1 horizontal book ponchi illustration for F-1 JavaScript.
Use a diagram-first concept map. A neutral central script node connects to a browser frame, a button interaction, an input-check card, a small server card, and a UI state card. No people. Do not draw the JavaScript logo, yellow color, framework logos, readable code, or real UI. Use white, black, gray, and approved blue accents only.
```

## G-1 Context

Scene brief:

```yaml
entry_id: G-1
title: Context
subject_type: concept
subject_stack:
  entry_subject: Context
  visual_subject: context-window container showing selected and dropped information
  supporting_subjects: Character A, Character B, selected cards, dropped cards, active path
  logo_subject: none
  excluded_subjects: readable text, real chat UI, brand marks
brand_asset:
  mode: none
role_balance: both_review
composition_family: timeline_scale
composition_type: diagram_first
view_mode: structure_map
character_base:
  female: use
  male: use
  robot: omit
temporary_people:
  allowed: no
scene_goal: LLM に渡す情報の入れすぎ/不足/適量を見せる
main_symbols: context window container, selected cards, dropped cards, active path
clearspace: no logo clearspace needed
avoid: readable text, logos, real chat UI
```

Prompt:

```text
Create a 2:1 horizontal book ponchi illustration for G-1 Context.
Show Character A and Character B reviewing a large context-window container. Several generic cards flow into it; a few selected cards fit inside, and a few faded cards sit outside to show information dropped or excluded. Use no readable text. Avoid real chat UI, logos, or brand colors. Make the context boundary and active selected path clear with approved blue accents.
```

## H-53 ChatGPT 登場

Scene brief:

```yaml
entry_id: H-53
title: ChatGPT 登場
subject_type: history_or_event
subject_stack:
  entry_subject: ChatGPT 登場
  visual_subject: generic chat launch spreading to many users
  supporting_subjects: Character A, generic chat card, launch point, temporary user silhouettes
  logo_subject: official OpenAI wordmark overlay; ChatGPT-specific asset still subject to review
  excluded_subjects: ChatGPT logo, OpenAI mark generated by AI, readable dates, product UI, brand colors
brand_asset:
  mode: official_overlay_ready
  asset_name: OpenAI wordmark
  local_path: assets/logos/openai/openai_wordmark_black_official_template_layer.png
  source_url: https://cdn.openai.com/brand/OpenAI-Partnership-Templates-2025.zip
role_balance: solo_female_works
composition_family: timeline_scale
composition_type: standing_board
composition_density: balanced
view_mode: structure_map
character_base:
  female: use
  male: omit
  robot: omit
temporary_people:
  allowed: yes
  count: small crowd silhouettes
  role: users
scene_goal: 2022 年以降に一般利用者へ AI チャットが広がった出来事
main_symbols: launch point, expanding user groups, simple chat card
clearspace: rightmost 40% of top 25% kept completely blank for official OpenAI/ChatGPT logo
main_subject_scale: keep Character A visible and make the user spread dense enough to feel intentional
avoid: ChatGPT logo, OpenAI mark, readable dates/text, real UI
```

Prompt:

```text
Create a 2:1 horizontal book ponchi illustration for H-53 ChatGPT launch.
Keep the upper-right logo clearspace completely blank white, about the rightmost 40% of the top 25% of the image. Do not place any silhouette, dot, line, connector, card, character, or pattern under that area. Show Character A near a simple launch point where a generic chat card expands into several visible groups of temporary user silhouettes/dots across a timeline-like path. The crowd can be secondary, but it should be dense enough that the right and lower-right side does not feel empty. Do not draw ChatGPT logo, OpenAI mark, readable dates, product UI, or brand colors.
```

## I-1 MCP

Scene brief:

```yaml
entry_id: I-1
title: MCP
subject_type: tool_or_language
subject_stack:
  entry_subject: MCP
  visual_subject: common connector from LLM box to external server tools
  supporting_subjects: Character B, Character C, client adapter, transport cable, server tool boxes
  logo_subject: none
  excluded_subjects: USB-C logo, Anthropic logo, tool logos, readable labels
brand_asset:
  mode: none
role_balance: robot_supports
composition_family: layer_stack
composition_type: diagram_first
view_mode: structure_map
character_base:
  female: omit
  male: use
  robot: use
temporary_people:
  allowed: no
scene_goal: LLM と外部ツールを共通規格でつなぐ
main_symbols: LLM box, client adapter, server tools, transport cable
clearspace: no logo clearspace needed
avoid: USB-C logo, Anthropic logo, tool logos, readable labels
```

Prompt:

```text
Create a 2:1 horizontal book ponchi illustration for I-1 MCP.
Show Character B and Character C looking at a clean structure diagram: a generic LLM box connects through a small client adapter and transport cable to several server tool boxes. No readable labels. Do not draw USB-C logos, Anthropic logos, product logos, or brand colors. The visual metaphor can feel like a universal connector, but use only generic ports, cables, boxes, and arrows.
```

## J-14 LLM

Scene brief:

```yaml
entry_id: J-14
title: LLM
subject_type: concept
subject_stack:
  entry_subject: LLM
  visual_subject: input cards flowing through a model-layer grid to output cards
  supporting_subjects: Character C, active path, generic output cards
  logo_subject: none
  excluded_subjects: brain mascot, logos, readable text, real chat UI
brand_asset:
  mode: none
role_balance: diagram_only
composition_family: process_flow
composition_type: diagram_first
view_mode: operation_flow
character_base:
  female: omit
  male: omit
  robot: use
temporary_people:
  allowed: no
scene_goal: 入力テキストからモデル層を通り出力へ流れる
main_symbols: input cards, model layer grid, output cards, active path
clearspace: no logo clearspace needed
avoid: brain mascot, logos, readable text, real chat UI
```

Prompt:

```text
Create a 2:1 horizontal book ponchi illustration for J-14 LLM.
Use a diagram-first process flow: generic input cards enter a large model-layer grid, an approved-blue active path passes through nodes, and generic output cards come out. Character C can stand small near the output path as a helper, using the recurring robot reference. Do not draw readable text, logos, real chat UI, brain mascots, or brand colors.
```
