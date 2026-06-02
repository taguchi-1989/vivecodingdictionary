# ponchi-batch-009 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- Generate or update scene briefs first, then lint prompts, then generate base images.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `F-37` | Japanese Language Pack for VS Code | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 2 | `F-38` | Markdown All in One | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 3 | `F-40` | npm | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 4 | `F-41` | Vite | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 5 | `F-42` | ビルド | `brief_needed` | `logo_avoid` | create build concept scene brief without logos | `not_reviewed` |
| 6 | `F-44` | pnpm | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 7 | `F-50` | git | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 8 | `F-51` | git push | `brief_needed` | `logo_avoid` | create git operation scene brief without logos | `not_reviewed` |
| 9 | `F-52` | git pull | `brief_needed` | `logo_avoid` | create git operation scene brief without logos | `not_reviewed` |
| 10 | `F-53` | branch | `brief_needed` | `logo_avoid` | create git concept scene brief without logos | `not_reviewed` |
| 11 | `F-54` | commit | `brief_needed` | `logo_avoid` | create git concept scene brief without logos | `not_reviewed` |
| 12 | `F-55` | merge | `brief_needed` | `logo_avoid` | create git concept scene brief without logos | `not_reviewed` |
| 13 | `F-56` | .gitignore | `brief_needed` | `logo_avoid` | create git file-filter scene brief without logos | `not_reviewed` |
| 14 | `F-57` | リポジトリ | `brief_needed` | `logo_avoid` | create repository concept scene brief without logos | `not_reviewed` |
| 15 | `F-58` | git stash | `brief_needed` | `logo_avoid` | create git stash scene brief without logos | `not_reviewed` |
| 16 | `F-59` | README.md | `brief_needed` | `logo_avoid` | create README document scene brief without logos | `not_reviewed` |
| 17 | `F-60` | GitHub | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `not_reviewed` |
| 18 | `F-61` | Pull Request | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 19 | `F-62` | GitHub Actions | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 20 | `F-71` | ripgrep (rg) | `brief_needed` | `logo_avoid` | create search tool concept scene brief without logos | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
python scripts\ponchi_batch_report.py ponchi-batch-009
python scripts\ponchi_prompt_lint.py <prompt-files>
```
