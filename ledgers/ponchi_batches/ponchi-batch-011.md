# ponchi-batch-011 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- `color_audit` means a non-brand base candidate is staged and has passed the mechanical color gate; it still needs visual review before final promotion.
- Generate or update scene briefs only for rows that truly lack prompts or need a rerun.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `F-123` | ORM | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 2 | `F-130` | OAuth | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 3 | `F-140` | Mermaid | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 4 | `F-141` | PlantUML | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 5 | `F-150` | MIT ライセンス | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 6 | `F-151` | Apache 2.0 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 7 | `F-152` | GPL | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 8 | `F-153` | Creative Commons | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 9 | `F-154` | OSS | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 10 | `F-160` | DOM | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 11 | `F-161` | SSR | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 12 | `F-162` | SSG | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 13 | `F-170` | EC2 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 14 | `F-171` | S3 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 15 | `F-172` | IAM | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 16 | `F-180` | OpenGL | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 17 | `F-181` | WebGL | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 18 | `F-190` | サブルーチン | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 19 | `F-200` | Rust | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 20 | `G-1` | Context (コンテキスト) | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_report.py ponchi-batch-011
python scripts\ponchi_prompt_lint.py <prompt-files>
python scripts\ponchi_color_audit.py --manifest-root assets\ponchi\final_candidates
```
