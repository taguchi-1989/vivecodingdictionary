# Ponchi 2:1 semantic regeneration and brand asset TODO

This document tracks the real regeneration task. It is separate from the
mechanical 1:1 to 2:1 conversion work.

## Intent

- Regenerate ponchi images as meaningful 2:1 book illustrations.
- Do not only crop, pad, or re-encode existing 1:1 images.
- Keep the image-generation policy: clean editorial illustration, no fake UI,
  no readable in-image text, no real-person likenesses.
- Do not ask image generation to invent or imitate company logos.
- Do not ask image generation to invent or imitate official icons, official
  marks, mascots, or brand-colored substitutes.
- For entries where a logo or official icon materially improves reader
  comprehension, use an official asset as a deterministic overlay, unchanged in
  color and shape.
- If the entry is itself a brand, product, service, or model family, treat the
  logo as required once an official source exists. Do not avoid a logo only
  because the name also appears in surrounding text.
- If an official asset or usage permission is not confirmed, leave the brand
  asset out and record the item as blocked instead of generating a fake logo or
  fake icon.

## Workflow

1. Classify each entry as `no_brand_asset`, `official_brand_asset_required`, or
   `brand_asset_avoid`.
2. For `official_brand_asset_required`, record source, usage guidance, local asset
   path, and any restrictions.
3. Generate a 2:1 illustration with a deliberate blank/neutral placement area
   for the brand mark when an official asset will be overlaid.
4. Composite the official brand asset deterministically after generation.
5. Verify dimensions, legibility at small size, absence of fake text/logos/icons,
   and policy fit before replacing `assets/ponchi/final/*.webp`.

The current per-entry logo requirement matrix is recorded in
`docs/ponchi_logo_requirement_matrix_2026-06-01.md`. Brand entries must first
have a meaningful 2:1 base illustration before any official logo overlay is
attempted. The current base regeneration audit is recorded in
`docs/ponchi_brand_base_regeneration_2026-06-01.md`.

## Unified visual policy

Use `docs/ponchi_image_generation_rules.md` as the source of truth for image
regeneration prompts. In particular:

- Allowed colors are `#FFFFFF`, `#F7F9FC`, `#1A1A1A`, `#6B7280`, plus the
  approved blue palette only: `#EAF1FB`, `#D6E6FA`, `#8DB7E8`, `#3F7FD1`,
  and rare `#123E82` accents.
- Pale blue is semantic, not decorative: use it only for active AI suggestions,
  selected paths, current focus, or a similar meaning-bearing state.
- Do not use brand colors inside generated illustration content. Brand identity
  is handled by official logo overlays only.
- Do not generate logos, official icons, official marks, mascots, or brand-style
  substitutes. Reserve clean white clearspace and composite official assets
  afterward.
- For a primary service logo on a `1254x627` ponchi image, reserve enough
  upper-right clearspace for an unchanged official lockup about `500-520px`
  wide.
- Do not put a custom box, card, border, badge, glow, or shadow around the
  logo. The logo must sit on clean white space.

## Current state

- 350 final WebP files were mechanically converted to 2:1.
- That conversion does not satisfy this regeneration task.
- Local official brand asset inventory currently contains AWS and GitHub assets.
- Main service logos such as Gemini, ChatGPT/OpenAI, Codex, and Windsurf still
  need official source review before use. Claude-family and Cursor official
  sources have been confirmed and now need local asset import before overlay.

## Pilot queue

| entry_id | title | brand asset status | regeneration intent | status |
| --- | --- | --- | --- | --- |
| B-1 | Gemini | official_brand_asset_required | Four entry points into one AI service: browser, Android phone, Docs/Gmail, cloud/developer context. | official_logo_source_review_required |
| B-2 | Claude | official_brand_asset_required | One assistant brand used by planner, developer, and operations worker. | official_logo_source_available_needs_import |
| B-3 | ChatGPT | official_brand_asset_required | Conversational AI as a general-purpose everyday workbench, not a fake chat screenshot. | official_logo_source_review_required |
| B-4 | Cursor | official_brand_asset_required | AI-first editor helping a developer move between code, intent, and review. | official_logo_source_available_needs_import |
| B-5 | GitHub Copilot | official_brand_asset_available | Pair-programming support inside a repository workflow; use current GitHub Copilot visual guidance. | pilot_regenerated |
| B-6 | Windsurf | official_brand_asset_required | AI coding environment that connects prompt, editor, and running app. | blocked_brand_asset |
| B-7 | Claude Code | official_brand_asset_required | CLI agent working with files, terminal, and review loop; avoid fake terminal text. | official_logo_source_available_needs_import |
| B-8 | Codex | official_brand_asset_required | Coding agent loop: task, local workspace, diff, tests, review. | official_logo_source_review_required |
| F-1 | JavaScript | brand_asset_avoid | Explain language/runtime ecosystem with generic JS/TS/browser/server symbols, not official logos or icons. | ready_for_regen |
| F-60 | GitHub | official_brand_asset_available | Repository as collaboration hub: issues, PR, actions, and AI support. | official_logo_applied |

## Notes from source policy review

- OpenAI brand guidance allows logo use only when directly related to OpenAI
  services and says to use marks exactly as provided, without implying
  endorsement.
- Anthropic has an official newsroom/press-kit path, so Claude and Claude 4 系
  should move from optional/no-logo treatment to official-source import before
  overlay.
- Cursor has an official brand assets page, so B-4 should move to official
  source import before overlay.
- Google Brand Resource Center exists, but Gemini needs a concrete
  product-icon/lockup choice and any required permission review before overlay.
- GitHub Copilot guidance says that since 2025 Copilot no longer has a
  standalone logo centered on the old Copilot icon.
- GitHub logo guidance permits secondary placement in news/blog/contextual
  reference but forbids modification and endorsement confusion.

## Pilot result

- `B-5` was regenerated as a real 2:1 composition and saved to
  `assets/ponchi/final/B-5.webp`.
- The base illustration was generated without any logo or trademark prompt.
- The GitHub Copilot mark was overlaid afterward from the official GitHub logo
  ZIP downloaded from `https://brand.github.com/GitHub_Logos.zip`.
- Experiment files are in `assets/ponchi/experiments/regeneration/`.
- Final audit after replacement: 350 WebP files are still 2:1.

## F-60 result

- `F-60 GitHub` was regenerated as a `collaboration_hub` composition and saved
  to `assets/ponchi/final/F-60.webp`.
- The base illustration reserved clean upper-right white clearspace.
- The official GitHub lockup was overlaid afterward from
  `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png`.
- Overlay parameters: `width=520`, `x=686`, `y=36`.
- Final audit after replacement: 350 WebP files are still 2:1.

## B-5 quality revision notes

- The first pilot used a bordered logo badge. That made the logo area read as an
  unexplained UI object, so the revised prompt forbids drawing any box, border,
  placeholder, or badge around reserved logo clearspace.
- The logo overlay size is now specified as about `500-520px` wide on the
  `1254x627` canvas, so the official mark is clearly identifiable in preview.
- The first pilot used scattered blue highlights. The revised prompt restricts
  pale blue to the active completion suggestion on the right side only.
- The first pilot emphasized a repository workflow. The entry text calls for a
  before/after Tab-completion explanation, so the revised prompt now requires a
  left/right before-after structure.
- The illustration touch is tightened to medium-weight black line art, flat
  light fills, restrained paper texture, and no scratchy hatching.
- The style policy was further revised away from pencil/sketch lines toward a
  clean simple editorial diagram style: smooth uniform black lines, flat gray
  fills, minimal shading, no hatching, and no scratchy hand-drawn texture.
- The revised prompt is stored at `assets/ponchi/prompts/B-5.md`.
