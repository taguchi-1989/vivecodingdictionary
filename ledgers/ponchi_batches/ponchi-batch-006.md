# ponchi-batch-006 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- Generate or update scene briefs first, then lint prompts, then generate base images.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `D-42` | Gemma 系 | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 2 | `D-43` | Qwen 系 | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 3 | `D-44` | Kimi | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 4 | `D-45` | GLM | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 5 | `D-46` | DeepSeek V3 | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 6 | `D-47` | DeepSeek R1 | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 7 | `D-50` | DALL-E | `overlay_ready` | `official_logo_available` | generate base if needed, then deterministic logo overlay | `not_reviewed` |
| 8 | `D-51` | Imagen | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 9 | `D-52` | Sora | `overlay_ready` | `official_logo_available` | generate base if needed, then deterministic logo overlay | `not_reviewed` |
| 10 | `D-53` | Veo | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 11 | `D-54` | Stable Diffusion | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 12 | `D-55` | Nano Banana | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 13 | `D-56` | Seedance | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 14 | `D-57` | Flow | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 15 | `D-58` | Whisk | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 16 | `D-60` | AlphaGo | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 17 | `D-70` | Amical | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 18 | `D-71` | Whisper | `overlay_ready` | `official_logo_available` | generate base if needed, then deterministic logo overlay | `not_reviewed` |
| 19 | `E-1` | SWE-Bench | `brief_needed` | `logo_avoid` | create subject_stack scene brief and prompt | `not_reviewed` |
| 20 | `E-2` | SWE-Bench Verified | `brief_needed` | `logo_avoid` | create subject_stack scene brief and prompt | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
python scripts\ponchi_batch_report.py ponchi-batch-006
python scripts\ponchi_prompt_lint.py <prompt-files>
```
