# Ponchi Generation Audit 2026-05-31

## Scope

This audit records the current state before continuing semantic 2:1 image
regeneration. It focuses on dimensions, brand asset safety, and character
continuity rules.

## Dimension Audit

Command:

```powershell
python scripts\audit_image_sizes.py --suffix .webp
```

Result:

| Target | Scanned | Common sizes | Aspect classes |
| :-- | --: | :-- | :-- |
| `assets/ponchi/final/*.webp` | 350 | `1254x627`: 349, `1024x512`: 1 | `2:1`: 350 |

Status: pass for WebP aspect ratio.

PNG local working copies are not the final committed target, but were also
checked:

```powershell
python scripts\audit_image_sizes.py --suffix .png
```

Result:

- 347 PNG files scanned.
- `2:1`: 327.
- `1:1`: 20.
- Invalid PNG reads: `B-2.png`, `B-3.png`, `B-4.png`.
- Remaining 1:1 local PNG IDs: `E-25`, `E-26`, `E-27`, `E-30`, `E-50`,
  `H-1`, `H-5`, `H-6`, `H-7`, `H-8`, `I-2`, `I-3`, `I-4`, `I-5`, `J-100`,
  `J-81`, `J-90`, `J-91`, `J-92`, `J-93`.

Status: informational. WebP remains the publishing target for this audit.

## Policy Sources

Current source-of-truth files:

- `drafts/IMAGE_GEN_POLICY_v2.md`
- `docs/ponchi_image_generation_rules.md`
- `docs/ponchi_brand_asset_rules.md`
- `docs/ponchi_character_bible.md`
- `docs/brand_usage_audit.md`
- `docs/ponchi_regeneration_logo_todo.md`

## Brand Asset Rule

AI generation must not create:

- company logos
- service logos
- app icons
- product icons
- official marks
- official mascots
- brand-color substitutes
- real product UI

If brand identification is required, the generated base illustration must leave
clean white clearspace and a verified official asset must be composited
afterward.

Primary official lockups on the standard `1254x627` canvas should be composited
at about `500-520px` wide. This is intentionally large: the logo should remain
identifiable in book previews and thumbnails, while the generated base image
stays free of fake logos, fake icons, and brand-color substitutes.

## Character Rule

The fixed cast is:

- Character A: reader/listener woman
- Character B: teacher/developer man
- Character C: pet robot for AI

Prompts should reference `docs/ponchi_character_bible.md` and avoid introducing
new one-off people, robots, mascots, or animal-like designs.

## Prompt Audit

Updated and safe to use as current pilot prompt sources:

| Prompt | Status | Note |
| :-- | :-- | :-- |
| `assets/ponchi/prompts/B-5.md` | usable with official asset overlay | GitHub/Copilot base image; official logo composited afterward |
| `assets/ponchi/prompts/F-1.md` | usable without brand asset overlay | JavaScript ecosystem, generic icons only |
| `assets/ponchi/prompts/F-60.md` | usable with official asset overlay | GitHub base image; official logo composited afterward |
| `assets/ponchi/prompts/J-14.md` | usable without brand asset overlay | LLM conceptual flow, generic data/model icons only |

Known older prompts that must not be used without revision:

| Prompt | Risk |
| :-- | :-- |
| `assets/ponchi/prompts/B-1.md` | Mentions Gemini star, Android, Docs, Gmail, and Google Cloud icon concepts |
| `assets/ponchi/prompts/B-2.md` | Service brand asset handling not yet updated |
| `assets/ponchi/prompts/B-3.md` | Mentions a ChatGPT logo node |
| `assets/ponchi/prompts/B-4.md` | Service brand asset handling not yet updated |
| `assets/ponchi/prompts/B-6.md` | Service brand asset handling not yet updated |
| `assets/ponchi/prompts/B-7.md` | Service brand asset handling not yet updated |
| `assets/ponchi/prompts/B-8.md` | Mentions ChatGPT/Codex/GitHub PR concepts and must be rewritten to reserve official asset clearspace |

## Next Audit Steps

1. Run visual review in `drafts/tools/ponchi_quality_review.html`.
2. Classify images as `OK`, `minor_fix`, `regenerate`, or
   `blocked_brand_asset`.
3. Rewrite all service prompts before generating new images.
4. Regenerate only from prompts that include color, brand asset, character, and
   no-readable-text rules.
5. After each replacement, run:

```powershell
python scripts\audit_image_sizes.py --suffix .webp
```
