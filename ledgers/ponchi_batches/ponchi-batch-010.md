# ponchi-batch-010 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- Generate or update scene briefs first, then lint prompts, then generate base images.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `F-80` | Node.js | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 2 | `F-81` | bash | `brief_needed` | `logo_avoid` | create shell concept scene brief without logos | `not_reviewed` |
| 3 | `F-82` | WSL | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 4 | `F-83` | PowerShell | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 5 | `F-84` | Ghostty | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 6 | `F-85` | SuperClaude Framework | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 7 | `F-86` | ollama | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 8 | `F-87` | sudo | `brief_needed` | `logo_avoid` | create permission concept scene brief without logos | `not_reviewed` |
| 9 | `F-90` | Docker | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 10 | `F-91` | .env | `brief_needed` | `logo_avoid` | create env file concept scene brief without logos | `not_reviewed` |
| 11 | `F-100` | 拡張子早見表 | `brief_needed` | `logo_avoid` | create file extension guide scene brief without logos | `not_reviewed` |
| 12 | `F-101` | .ico | `brief_needed` | `logo_avoid` | create icon file format scene brief without logos | `not_reviewed` |
| 13 | `F-102` | .mp4 | `brief_needed` | `logo_avoid` | create video file format scene brief without logos | `not_reviewed` |
| 14 | `F-103` | .mp3 | `brief_needed` | `logo_avoid` | create audio file format scene brief without logos | `not_reviewed` |
| 15 | `F-104` | .webp | `brief_needed` | `logo_avoid` | create image file format scene brief without logos | `not_reviewed` |
| 16 | `F-110` | Lighthouse | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 17 | `F-111` | a11y | `brief_needed` | `logo_avoid` | create accessibility concept scene brief without logos | `not_reviewed` |
| 18 | `F-120` | PostgreSQL | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 19 | `F-121` | SQLite | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 20 | `F-122` | Prisma | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
python scripts\ponchi_batch_report.py ponchi-batch-010
python scripts\ponchi_prompt_lint.py <prompt-files>
```
