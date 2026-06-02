# ponchi-batch-008 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- Generate or update scene briefs first, then lint prompts, then generate base images.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `F-4` | HTML | `brief_needed` | `logo_avoid` | create language concept scene brief without logos | `not_reviewed` |
| 2 | `F-5` | CSS | `brief_needed` | `logo_avoid` | create language concept scene brief without logos | `not_reviewed` |
| 3 | `F-6` | Markdown | `brief_needed` | `logo_avoid` | create language concept scene brief without logos | `not_reviewed` |
| 4 | `F-7` | YAML | `brief_needed` | `logo_avoid` | create data format scene brief without logos | `not_reviewed` |
| 5 | `F-8` | JSON | `brief_needed` | `logo_avoid` | create data format scene brief without logos | `not_reviewed` |
| 6 | `F-9` | SVG | `brief_needed` | `logo_avoid` | create vector format scene brief without logos | `not_reviewed` |
| 7 | `F-10` | React | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 8 | `F-11` | Next.js | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 9 | `F-12` | Electron | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 10 | `F-13` | Tauri | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 11 | `F-14` | three.js | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 12 | `F-15` | shadcn/ui | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 13 | `F-16` | Tailwind CSS | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 14 | `F-17` | Astro | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 15 | `F-20` | ESLint | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 16 | `F-21` | Prettier | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 17 | `F-30` | VS Code | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 18 | `F-34` | VS Code 拡張機能 | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 19 | `F-35` | Markdown Preview Enhanced | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 20 | `F-36` | Git Graph | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
python scripts\ponchi_batch_report.py ponchi-batch-008
python scripts\ponchi_prompt_lint.py <prompt-files>
```
