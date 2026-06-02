# ponchi-batch-003 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- Generate or update scene briefs first, then lint prompts, then generate base images.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `B-30` | Amazon Bedrock | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 2 | `B-31` | Excalidraw | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 3 | `B-32` | Figma | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 4 | `B-33` | Canva | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 5 | `B-40` | Reddit | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 6 | `B-41` | arXiv | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 7 | `B-50` | Claude の料金プラン | `overlay_wait` | `official_logo_source_available_needs_import` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 8 | `B-51` | ChatGPT の料金プラン | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 9 | `B-52` | Gemini の料金プラン | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 10 | `B-60` | Suno | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 11 | `B-61` | ACE-Step 1.5 | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 12 | `C-1` | OpenAI | `overlay_audit` | `official_logo_available` | audit deterministic official logo overlay; stage as review-pending candidate only | `not_reviewed` |
| 13 | `C-2` | Anthropic | `overlay_audit` | `official_logo_available` | audit deterministic official logo overlay; stage as review-pending candidate only | `not_reviewed` |
| 14 | `C-3` | Google DeepMind | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 15 | `C-4` | Meta AI | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 16 | `C-5` | xAI | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 17 | `C-6` | Mistral AI | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 18 | `C-7` | Hugging Face | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 19 | `C-8` | Microsoft AI | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 20 | `C-9` | NVIDIA | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
python scripts\ponchi_batch_report.py ponchi-batch-003
python scripts\ponchi_prompt_lint.py <prompt-files>
```
