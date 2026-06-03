# ponchi-batch-004 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- `color_audit` means a non-brand base candidate is staged and has passed the mechanical color gate; it still needs visual review before final promotion.
- Generate or update scene briefs only for rows that truly lack prompts or need a rerun.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `C-10` | Moonshot AI | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 2 | `C-11` | Z.ai | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 3 | `C-12` | TSMC | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 4 | `C-13` | Groq | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 5 | `C-14` | AMD | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 6 | `C-50` | Sam Altman | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 7 | `C-51` | Dario Amodei | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 8 | `C-52` | Demis Hassabis | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 9 | `C-53` | Andrej Karpathy | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 10 | `C-54` | Ilya Sutskever | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 11 | `C-55` | Mira Murati | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 12 | `C-56` | Yann LeCun | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 13 | `C-57` | Geoffrey Hinton | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 14 | `C-58` | Elon Musk | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 15 | `C-59` | Jensen Huang | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 16 | `C-60` | Ray Kurzweil | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 17 | `C-80` | AI大学 | `overlay_audit` | `official_logo_applied` | official YouTube channel avatar applied as review-pending icon overlay; body colors normalized; keep C-80 final pending visual review | `not_reviewed` |
| 18 | `C-81` | にゃんた | `overlay_audit` | `official_logo_applied` | official YouTube channel avatar applied as review-pending icon overlay; body colors normalized; keep C-81 final pending visual review | `not_reviewed` |
| 19 | `C-82` | まさお | `overlay_audit` | `official_logo_applied` | official YouTube channel avatar applied as review-pending icon overlay; body colors normalized; keep C-82 final pending visual review | `not_reviewed` |
| 20 | `C-83` | AI の羅針盤 | `overlay_audit` | `official_logo_applied` | official YouTube channel avatar for AI時代の羅針盤 applied as review-pending icon overlay; title/source naming mismatch remains review note | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_report.py ponchi-batch-004
python scripts\ponchi_prompt_lint.py <prompt-files>
python scripts\ponchi_color_audit.py --manifest-root assets\ponchi\final_candidates
```
