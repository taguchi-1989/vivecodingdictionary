# ponchi-batch-002 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- Generate or update scene briefs first, then lint prompts, then generate base images.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `B-10` | Devin | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 2 | `B-11` | Bolt.new | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `accept_overlay` |
| 3 | `B-12` | Perplexity | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `accept_overlay` |
| 4 | `B-13` | ElevenLabs | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `accept_overlay` |
| 5 | `B-14` | Genspark | `overlay_wait` | `official_logo_source_available_needs_import` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 6 | `B-15` | Microsoft Copilot | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 7 | `B-16` | Microsoft 365 Copilot | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 8 | `B-17` | Edge Copilot | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 9 | `B-18` | Aqua Voice | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 10 | `B-19` | Claude Cowork | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 11 | `B-20` | Vercel | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `accept_overlay` |
| 12 | `B-21` | Netlify | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `accept_overlay` |
| 13 | `B-22` | Cloudflare | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `accept_overlay` |
| 14 | `B-23` | AWS | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 15 | `B-24` | Google Cloud | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 16 | `B-25` | Azure | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 17 | `B-26` | Azure OpenAI | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 18 | `B-27` | Vertex AI | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 19 | `B-28` | Render | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `accept_overlay` |
| 20 | `B-29` | Supabase | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `accept_overlay` |

## Batch Commands

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
python scripts\ponchi_batch_report.py ponchi-batch-002
python scripts\ponchi_prompt_lint.py <prompt-files>
```
