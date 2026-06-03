# ponchi-batch-018 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- `color_audit` means a non-brand base candidate is staged and has passed the mechanical color gate; it still needs visual review before final promotion.
- Generate or update scene briefs only for rows that truly lack prompts or need a rerun.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `J-77` | GPU (概念) | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 2 | `J-78` | HDD | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 3 | `J-79` | SSD | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 4 | `J-80` | SATA | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 5 | `J-81` | M.2 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 6 | `J-90` | GUI | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 7 | `J-91` | CLI | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 8 | `J-92` | Linux | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 9 | `J-93` | Ubuntu | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 10 | `J-100` | 識字（リテラシー） | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_report.py ponchi-batch-018
python scripts\ponchi_prompt_lint.py <prompt-files>
python scripts\ponchi_color_audit.py --manifest-root assets\ponchi\final_candidates
```
