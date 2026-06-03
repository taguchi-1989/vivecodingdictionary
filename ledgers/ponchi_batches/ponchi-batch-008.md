# ponchi-batch-008 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- `color_audit` means a non-brand base candidate is staged and has passed the mechanical color gate; it still needs visual review before final promotion.
- Generate or update scene briefs only for rows that truly lack prompts or need a rerun.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `F-4` | HTML | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 2 | `F-5` | CSS | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 3 | `F-6` | Markdown | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 4 | `F-7` | YAML | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 5 | `F-8` | JSON | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 6 | `F-9` | SVG | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 7 | `F-10` | React | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 8 | `F-11` | Next.js | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 9 | `F-12` | Electron | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 10 | `F-13` | Tauri | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 11 | `F-14` | three.js | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 12 | `F-15` | shadcn/ui | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 13 | `F-16` | Tailwind CSS | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 14 | `F-17` | Astro | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 15 | `F-20` | ESLint | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 16 | `F-21` | Prettier | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 17 | `F-30` | VS Code | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 18 | `F-34` | VS Code 拡張機能 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 19 | `F-35` | Markdown Preview Enhanced | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 20 | `F-36` | Git Graph | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_report.py ponchi-batch-008
python scripts\ponchi_prompt_lint.py <prompt-files>
python scripts\ponchi_color_audit.py --manifest-root assets\ponchi\final_candidates
```
