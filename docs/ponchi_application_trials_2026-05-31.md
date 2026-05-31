# Ponchi Application Trials 2026-05-31

## 目的

同じ見た目の枚数を増やすのではなく、用途別の構図ファミリーを実画像で検証する。ここで作る画像は本番差し替え前の試作であり、保存先は `assets/ponchi/experiments/regeneration/application-trials-2026-05-31/` とする。

## 試作セット

| entry_id | title | composition_family | composition_type | brand_asset | expected_status |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `F-1` | JavaScript | `concept_map` | `diagram_first` | `brand_asset_avoid` | `trial` |
| `F-2` | TypeScript | `before_after` | `single_laptop` | `brand_asset_avoid` | `trial` |
| `G-1` | Context | `timeline_scale` | `diagram_first` | `brand_asset_avoid` | `trial` |
| `J-14` | LLM | `process_flow` | `diagram_first` | `brand_asset_avoid` | `trial` |
| `F-60` | GitHub | `collaboration_hub` | `logo_clearspace` | `official_overlay_required` | `trial_logo_clearspace` |

## 共通プロンプト制約

- Canvas `1254x627`, 2:1.
- Clean simple editorial line illustration.
- White background, black/gray linework, approved blue palette only.
- No readable text, no fake UI, no code snippets, no speech bubble text.
- No logos, no official icons, no official marks, no mascots, no brand colors.
- Use recurring Character A/B/C only when helpful.
- Hands are simple. Explain with arrows, nodes, cards, checks, and flows.

## scene_briefs

```yaml
- entry_id: F-1
  title: JavaScript
  brand_asset:
    mode: brand_asset_avoid
  role_balance: solo_female_works
  composition_family: concept_map
  composition_type: diagram_first
  characters: [female]
  hands_policy:
    visible_hands_max: 1
    gesture: light reviewing gesture
  scene_goal: show a generic language core branching to browser, server, type layer, and UI layer
  main_symbols: code-file tile, abstract brackets, browser frame, server box, stacked layers
  clearspace: generous center whitespace, no logo area
  avoid: yellow JS styling, framework logos, product icons

- entry_id: F-2
  title: TypeScript
  brand_asset:
    mode: brand_asset_avoid
  role_balance: male_operates_female_checks
  composition_family: before_after
  composition_type: single_laptop
  characters: [male, female]
  hands_policy:
    visible_hands_max: 2
    gesture: one hand on laptop, one small check gesture
  scene_goal: contrast hidden runtime confusion with early type-check warning using abstract panels
  main_symbols: split panels, generic laptop, warning underline as non-text line, check mark
  clearspace: horizontal split with breathing room
  avoid: red warning color, readable code, TypeScript logo

- entry_id: G-1
  title: Context
  brand_asset:
    mode: brand_asset_avoid
  role_balance: diagram_only
  composition_family: timeline_scale
  composition_type: diagram_first
  characters: []
  hands_policy:
    visible_hands_max: 0
    gesture: none
  scene_goal: show information cards entering a context window while overflow remains outside
  main_symbols: dotted boundary, input cards, model box, overflow card, widening arrow
  clearspace: no logo area
  avoid: readable numbers, Japanese labels, dense diagram

- entry_id: J-14
  title: LLM
  brand_asset:
    mode: brand_asset_avoid
  role_balance: robot_supports
  composition_family: process_flow
  composition_type: diagram_first
  characters: [robot]
  hands_policy:
    visible_hands_max: 1
    gesture: robot points to a flow card with one simple arm
  scene_goal: show input cards passing through layered model box to output cards
  main_symbols: input cards, layered model box, arrows, output cards
  clearspace: left-to-right flow with large margins
  avoid: brain icon, product UI, readable output text

- entry_id: F-60
  title: GitHub
  brand_asset:
    mode: official_overlay_required
    asset_name: GitHub Lockup Black Clearspace
    local_path: assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png
  role_balance: both_review
  composition_family: collaboration_hub
  composition_type: logo_clearspace
  characters: [female, male, robot]
  hands_policy:
    visible_hands_max: 2
    gesture: simple review gesture only
  scene_goal: show a repository collaboration hub with issues, pull requests, checks, and automation
  main_symbols: generic folder-cloud hub, branch path, checklist, gear check, review cards
  clearspace: upper-right clean white area for a 520px official logo overlay
  avoid: fake GitHub logo, Octocat, real GitHub UI, bordered logo badge
```

## 監査メモ

生成後に、各 PNG を `1254x627` に正規化し、次を実行する。

```powershell
python scripts\audit_image_sizes.py --dir assets\ponchi\experiments\regeneration\application-trials-2026-05-31 --suffix .png
```

本番採用は別コミットで行い、この試作コミットでは `assets/ponchi/final/*.webp` を触らない。

## 生成結果

保存先:

`assets/ponchi/experiments/regeneration/application-trials-2026-05-31/`

| file | role | status | note |
| :-- | :-- | :-- | :-- |
| `F-1_javascript_concept_map_1254x627.png` | base trial | usable draft | `concept_map` として使える。黄色 JS 風ロゴなし、読める文字なし |
| `F-2_typescript_before_after_1254x627.png` | base trial | usable draft | `before_after` として使える。赤警告色を使わず、左右差が読める |
| `G-1_context_timeline_scale_1254x627.png` | base trial | usable draft | `timeline_scale` として使える。図解のみで、人物量産を避けられる |
| `J-14_llm_process_flow_1254x627.png` | base trial | usable draft | `process_flow` として使える。中央モデルと入出力の流れが読める |
| `F-60_github_collaboration_logo_clearspace_1254x627.png` | base trial | logo overlay base | 右上に公式ロゴ後合成用の白い余白を確保 |
| `F-60_github_collaboration_official_logo_1254x627.png` | composited trial | overlay verified | GitHub 公式 lockup を `width=520`, `x=686`, `y=36` で後合成 |

比較用 contact sheet:

`assets/ponchi/experiments/regeneration/application-trials-2026-05-31/contact-sheets/application_trials_contact_sheet.png`

## 監査結果

```powershell
python scripts\audit_image_sizes.py --dir assets\ponchi\experiments\regeneration\application-trials-2026-05-31 --suffix .png
```

結果:

- 6 images scanned
- `1254x627`: 6
- aspect `2:1`: 6

## 判断

このバッチでは、同じ画像風の枚数増加ではなく、次の 5 つの応用型を実物で確認できた。

- `concept_map`
- `before_after`
- `timeline_scale`
- `process_flow`
- `collaboration_hub` + `brand_clearspace`

次に本番へ進めるなら、ロゴ不要の `F-1`, `F-2`, `G-1`, `J-14` を候補にし、`F-60` は公式ロゴ合成済み画像を候補にする。
