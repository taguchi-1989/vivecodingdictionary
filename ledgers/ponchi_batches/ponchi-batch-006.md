# ponchi-batch-006 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- `color_audit` means a non-brand base candidate is staged and has passed the mechanical color gate; it still needs visual review before final promotion.
- Generate or update scene briefs only for rows that truly lack prompts or need a rerun.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `D-42` | Gemma 系 | `overlay_audit` | `official_logo_applied` | review official Google DeepMind icon overlay before final promotion | `not_reviewed` |
| 2 | `D-43` | Qwen 系 | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 3 | `D-44` | Kimi | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 4 | `D-45` | GLM | `overlay_audit` | `official_logo_applied` | official Z.ai icon applied as review-pending GLM developer overlay; dedicated GLM product logo not confirmed | `not_reviewed` |
| 5 | `D-46` | DeepSeek V3 | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 6 | `D-47` | DeepSeek R1 | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 7 | `D-50` | DALL-E | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 8 | `D-51` | Imagen | `overlay_audit` | `official_logo_applied` | review official Google DeepMind icon overlay before final promotion | `not_reviewed` |
| 9 | `D-52` | Sora | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 10 | `D-53` | Veo | `overlay_audit` | `official_logo_applied` | review official Google DeepMind icon overlay before final promotion | `not_reviewed` |
| 11 | `D-54` | Stable Diffusion | `overlay_audit` | `official_logo_applied` | official Stability AI header logo applied on approved-blue plate as review-pending organization overlay; dedicated Stable Diffusion product logo not confirmed | `not_reviewed` |
| 12 | `D-55` | Nano Banana | `overlay_audit` | `official_logo_applied` | official Gemini sparkle applied as review-pending Gemini-family overlay; dedicated Nano Banana product logo not confirmed | `not_reviewed` |
| 13 | `D-56` | Seedance | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 14 | `D-57` | Flow | `overlay_audit` | `official_logo_applied` | official Google Flow favicon applied on approved-blue plate as review-pending icon overlay; standalone Flow lockup not confirmed | `not_reviewed` |
| 15 | `D-58` | Whisk | `overlay_audit` | `official_logo_applied` | official Google Labs Whisk favicon applied as review-pending icon overlay; standalone Whisk lockup not confirmed | `not_reviewed` |
| 16 | `D-60` | AlphaGo | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 17 | `D-70` | Amical | `overlay_audit` | `official_logo_applied` | official Amical GitHub/website icon applied as review-pending overlay; entry text/source mismatch remains review note | `not_reviewed` |
| 18 | `D-71` | Whisper | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 19 | `E-1` | SWE-Bench | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 20 | `E-2` | SWE-Bench Verified | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_report.py ponchi-batch-006
python scripts\ponchi_prompt_lint.py <prompt-files>
python scripts\ponchi_color_audit.py --manifest-root assets\ponchi\final_candidates
```
