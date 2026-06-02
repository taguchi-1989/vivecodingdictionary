# ponchi-batch-004 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- Generate or update scene briefs first, then lint prompts, then generate base images.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `C-10` | Moonshot AI | `overlay_wait` | `official_logo_source_review_required` | generate base with logo clearspace; confirm official logo/icon source before overlay | `not_reviewed` |
| 2 | `C-11` | Z.ai | `overlay_wait` | `official_logo_source_review_required` | generate base with logo clearspace; confirm official logo/icon source before overlay | `not_reviewed` |
| 3 | `C-12` | TSMC | `overlay_wait` | `official_logo_source_review_required` | generate base with logo clearspace; confirm official logo/icon source before overlay | `not_reviewed` |
| 4 | `C-13` | Groq | `overlay_wait` | `official_logo_source_review_required` | generate base with logo clearspace; confirm official logo/icon source before overlay | `not_reviewed` |
| 5 | `C-14` | AMD | `overlay_wait` | `official_logo_source_review_required` | generate base with logo clearspace; confirm official logo/icon source before overlay | `not_reviewed` |
| 6 | `C-50` | Sam Altman | `prompt_review` | `logo_avoid` | generate no-logo person concept base; avoid real-person likeness and readable text | `not_reviewed` |
| 7 | `C-51` | Dario Amodei | `prompt_review` | `logo_avoid` | generate no-logo person concept base; avoid real-person likeness and readable text | `not_reviewed` |
| 8 | `C-52` | Demis Hassabis | `prompt_review` | `logo_avoid` | generate no-logo person concept base; avoid real-person likeness and readable text | `not_reviewed` |
| 9 | `C-53` | Andrej Karpathy | `prompt_review` | `logo_avoid` | generate no-logo person concept base; avoid real-person likeness and readable text | `not_reviewed` |
| 10 | `C-54` | Ilya Sutskever | `prompt_review` | `logo_avoid` | generate no-logo person concept base; avoid real-person likeness and readable text | `not_reviewed` |
| 11 | `C-55` | Mira Murati | `prompt_review` | `logo_avoid` | generate no-logo person concept base; avoid real-person likeness and readable text | `not_reviewed` |
| 12 | `C-56` | Yann LeCun | `prompt_review` | `logo_avoid` | generate no-logo person concept base; avoid real-person likeness and readable text | `not_reviewed` |
| 13 | `C-57` | Geoffrey Hinton | `prompt_review` | `logo_avoid` | generate no-logo person concept base; avoid real-person likeness and readable text | `not_reviewed` |
| 14 | `C-58` | Elon Musk | `prompt_review` | `logo_avoid` | generate no-logo person concept base; avoid real-person likeness and readable text | `not_reviewed` |
| 15 | `C-59` | Jensen Huang | `prompt_review` | `logo_avoid` | generate no-logo person concept base; avoid real-person likeness and readable text | `not_reviewed` |
| 16 | `C-60` | Ray Kurzweil | `prompt_review` | `logo_avoid` | generate no-logo person concept base; avoid real-person likeness and readable text | `not_reviewed` |
| 17 | `C-80` | AI大学 | `overlay_wait` | `official_logo_source_review_required` | generate base with logo clearspace; confirm official logo/icon source before overlay | `not_reviewed` |
| 18 | `C-81` | にゃんた | `overlay_wait` | `official_logo_source_review_required` | generate base with logo clearspace; confirm official logo/icon source before overlay | `not_reviewed` |
| 19 | `C-82` | まさお | `overlay_wait` | `official_logo_source_review_required` | generate base with logo clearspace; confirm official logo/icon source before overlay | `not_reviewed` |
| 20 | `C-83` | AI の羅針盤 | `overlay_wait` | `official_logo_source_review_required` | generate base with logo clearspace; confirm official logo/icon source before overlay | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
python scripts\ponchi_batch_report.py ponchi-batch-004
python scripts\ponchi_prompt_lint.py <prompt-files>
```
