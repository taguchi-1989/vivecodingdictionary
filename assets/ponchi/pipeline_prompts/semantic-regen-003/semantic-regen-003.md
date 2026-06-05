# semantic-regen-003 ponchi prompts

Wave 3 targets B-chapter P1 semantic failures where the legacy image looked like a generic AI/coding workspace. Generate base images only. Keep official-logo clearspace blank for deterministic overlays.

## B-1 Gemini

```yaml
entry_id: B-1
title: Gemini
subject_type: ai_assistant_brand
subject_stack:
  entry_subject: Gemini
  visual_subject: Google Gemini as one brand with four distinct entry points: consumer chat, Android assistant, Workspace documents/mail, and developer/API/cloud access
  supporting_subjects: four user roles around one hub; browser chat, phone voice assistant, document/mail workspace, API/cloud connector
  logo_subject: official Gemini brand overlay after source review
  excluded_subjects: readable text, fake logos, official icons, brand colors, real product UI, whiteboard diagram tool, Figma/Canva canvas, Excalidraw-style board, pricing ladder
brand_asset:
  mode: official_overlay_required
  asset_name: Gemini
composition_family: semantic_regen
composition_type: multi_entry_brand_map_with_logo_clearspace
view_mode: logo_clearspace
clearspace:
  required: yes
  location: rightmost 40% of top 25% kept completely blank
scene_goal: make Gemini identifiable as Google's multi-entry AI assistant brand, not a diagramming/design tool or pricing page
main_symbols: central assistant hub splitting into four entry points: chat laptop, Android phone, Docs/Gmail-like document cards, developer API/cloud connector
avoid: readable text, fake logos, official icons, brand colors, real product UI, whiteboard diagram tool, Figma/Canva canvas, Excalidraw-style board, pricing ladder
```

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for B-1 Gemini. Show one central AI assistant hub branching to four clearly different entry points: a consumer chat laptop, an Android-style phone assistant, workspace document/mail cards, and a developer API/cloud connector. It must look like a Google AI assistant brand map, not a design canvas or diagramming board. Keep the upper-right logo clearspace blank white.
Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.
Do not use yellow, green, red, purple, brown, orange, rainbow colors, cyan, teal, purple-blue, arbitrary blue variants, decorative blue sparkles, blue background fills, product UI colors, photo thumbnails, colorful charts, or brand colors.
Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading. No readable text, no watermark.

## B-2 Claude

```yaml
entry_id: B-2
title: Claude
subject_type: ai_assistant_brand
subject_stack:
  entry_subject: Claude
  visual_subject: Claude as one Anthropic assistant across Claude.ai conversation, long document work, artifacts, Claude Code, and API integration
  supporting_subjects: planning person, long document stack, artifact preview card, developer terminal as one branch, business API workflow
  logo_subject: official Claude brand overlay after source review
  excluded_subjects: readable text, fake logos, official icons, brand colors, real product UI, GitHub Copilot completion, repository-only workflow, coding assistant as the only subject
brand_asset:
  mode: official_overlay_required
  asset_name: Claude
composition_family: semantic_regen
composition_type: assistant_entry_map_with_logo_clearspace
view_mode: logo_clearspace
clearspace:
  required: yes
  location: rightmost 40% of top 25% kept completely blank
scene_goal: make Claude identifiable as a general Anthropic assistant with long-context/document/artifact strengths, not GitHub Copilot or a coding-only assistant
main_symbols: conversation hub, long document stack, artifact preview panel, small coding branch, API integration branch, human review loop
avoid: readable text, fake logos, official icons, brand colors, real product UI, GitHub Copilot completion, repository-only workflow, coding assistant as the only subject
```

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for B-2 Claude. Show a general assistant workflow centered on conversation, long documents, artifacts, a small code branch, and API integration. The document/artifact reasoning surface should dominate more than coding. Keep the upper-right logo clearspace blank white.
Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.
Do not use yellow, green, red, purple, brown, orange, rainbow colors, cyan, teal, purple-blue, arbitrary blue variants, decorative blue sparkles, blue background fills, product UI colors, photo thumbnails, colorful charts, or brand colors.
Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading. No readable text, no watermark.

## B-3 ChatGPT

```yaml
entry_id: B-3
title: ChatGPT
subject_type: ai_assistant_brand
subject_stack:
  entry_subject: ChatGPT
  visual_subject: ChatGPT as the mainstream OpenAI chat service with three entry points: chatgpt.com, Custom GPT, and API
  supporting_subjects: everyday user drafting text, business custom assistant card, developer API connector, model block underneath supporting all three
  logo_subject: official OpenAI/ChatGPT brand overlay after source review
  excluded_subjects: readable text, fake logos, official icons, brand colors, real product UI, GitHub Copilot coding flow, IDE-only screen, pull request review, repository branch graph
brand_asset:
  mode: official_overlay_required
  asset_name: OpenAI
composition_family: semantic_regen
composition_type: mainstream_chat_service_map_with_logo_clearspace
view_mode: logo_clearspace
clearspace:
  required: yes
  location: rightmost 40% of top 25% kept completely blank
scene_goal: make ChatGPT identifiable as the general OpenAI chat service and Custom GPT/API entry map, not GitHub Copilot or a coding tool
main_symbols: large chat conversation, document drafting card, custom assistant builder card, API integration branch, shared model foundation block
avoid: readable text, fake logos, official icons, brand colors, real product UI, GitHub Copilot coding flow, IDE-only screen, pull request review, repository branch graph
```

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for B-3 ChatGPT. Show the mainstream OpenAI chat service: everyday chat and document drafting on one side, a Custom GPT-style special assistant card in the middle, and API integration on the other side, all supported by a model block underneath. Coding may appear only as a tiny secondary cue. Keep the upper-right logo clearspace blank white.
Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.
Do not use yellow, green, red, purple, brown, orange, rainbow colors, cyan, teal, purple-blue, arbitrary blue variants, decorative blue sparkles, blue background fills, product UI colors, photo thumbnails, colorful charts, or brand colors.
Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading. No readable text, no watermark.

## B-10 Devin

```yaml
entry_id: B-10
title: Devin
subject_type: autonomous_engineering_agent
subject_stack:
  entry_subject: Devin
  visual_subject: autonomous AI software engineer that takes an issue, researches, edits code, runs tests, opens a pull request, and reports back while the human waits at the edges
  supporting_subjects: human task handoff on left, autonomous loop in center, repo files, test results, PR review card on right
  logo_subject: official Devin brand overlay after source review
  excluded_subjects: readable text, fake logos, official icons, brand colors, real product UI, coworking pair, human-AI collaboration meeting, generic assistant chat, coding helper beside a user
brand_asset:
  mode: official_overlay_required
  asset_name: Devin
composition_family: semantic_regen
composition_type: autonomous_agent_loop_with_logo_clearspace
view_mode: logo_clearspace
clearspace:
  required: yes
  location: rightmost 40% of top 25% kept completely blank
scene_goal: make Devin identifiable as an autonomous AI engineer completing a repo task through PR, not Claude Cowork or a generic coding assistant
main_symbols: issue handoff, autonomous investigate-edit-test loop, repo files, terminal/test run, pull request review card, human only at task start and review end
avoid: readable text, fake logos, official icons, brand colors, real product UI, coworking pair, human-AI collaboration meeting, generic assistant chat, coding helper beside a user
```

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for B-10 Devin. Show autonomy: a human hands off one task card on the far left, then an AI engineering agent independently loops through investigation, code edits, test run, and pull request, returning a review card to the human on the far right. Human collaboration must be at the edges only. Keep the upper-right logo clearspace blank white.
Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.
Do not use yellow, green, red, purple, brown, orange, rainbow colors, cyan, teal, purple-blue, arbitrary blue variants, decorative blue sparkles, blue background fills, product UI colors, photo thumbnails, colorful charts, or brand colors.
Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading. No readable text, no watermark.

## B-14 Genspark

```yaml
entry_id: B-14
title: Genspark
subject_type: research_output_service
subject_stack:
  entry_subject: Genspark
  visual_subject: Genspark as a multi-LLM and web-search service that generates Sparkpage summaries and branches into slides or task outputs
  supporting_subjects: search query input, parallel model/search lanes, assembled Sparkpage, output branch to slide deck and super-agent task card
  logo_subject: official Genspark brand overlay after source review
  excluded_subjects: readable text, fake logos, official icons, brand colors, real product UI, autonomous coding agent, repo PR loop, Devin-like software task workflow, generic chat assistant
brand_asset:
  mode: official_overlay_required
  asset_name: Genspark
composition_family: semantic_regen
composition_type: research_to_outputs_flow_with_logo_clearspace
view_mode: logo_clearspace
clearspace:
  required: yes
  location: rightmost 40% of top 25% kept completely blank
scene_goal: make Genspark identifiable as search/multi-LLM-to-Sparkpage-and-slides, not Devin, Codex, or a software engineering agent
main_symbols: query card, web-search lanes, multiple model lanes, Sparkpage assembled as a report page, branch into slide deck and agent task output
avoid: readable text, fake logos, official icons, brand colors, real product UI, autonomous coding agent, repo PR loop, Devin-like software task workflow, generic chat assistant
```

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for B-14 Genspark. Show a research-to-output flow: a question enters web search and multiple model lanes, an assembled Sparkpage/report page appears, then the output branches to a slide deck and a task output card. Do not show repository code, tests, or pull requests. Keep the upper-right logo clearspace blank white.
Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.
Do not use yellow, green, red, purple, brown, orange, rainbow colors, cyan, teal, purple-blue, arbitrary blue variants, decorative blue sparkles, blue background fills, product UI colors, photo thumbnails, colorful charts, or brand colors.
Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading. No readable text, no watermark.
