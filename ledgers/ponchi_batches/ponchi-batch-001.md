# ponchi-batch-001 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- Generate or update scene briefs first, then lint prompts, then generate base images.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `A-1` | まえがき | `brief_needed` | `unclassified` | create subject_stack scene brief and prompt | `not_reviewed` |
| 2 | `A-2` | この本の読み方 | `brief_needed` | `unclassified` | create subject_stack scene brief and prompt | `not_reviewed` |
| 3 | `A-3` | 図鑑の歩き方 | `brief_needed` | `unclassified` | create subject_stack scene brief and prompt | `not_reviewed` |
| 4 | `A-4` | 体験区分の凡例 | `brief_needed` | `unclassified` | create subject_stack scene brief and prompt | `not_reviewed` |
| 5 | `A-5` | 読者レベルの凡例 | `brief_needed` | `unclassified` | create subject_stack scene brief and prompt | `not_reviewed` |
| 6 | `A-6` | 評価日・時変情報の見方 | `brief_needed` | `unclassified` | create subject_stack scene brief and prompt | `not_reviewed` |
| 7 | `A-7` | 図のタイプ | `brief_needed` | `unclassified` | create subject_stack scene brief and prompt | `not_reviewed` |
| 8 | `A-8` | 色・記号の凡例 | `brief_needed` | `unclassified` | create subject_stack scene brief and prompt | `not_reviewed` |
| 9 | `A-9` | 索引 | `brief_needed` | `unclassified` | create subject_stack scene brief and prompt | `not_reviewed` |
| 10 | `A-10` | 更新履歴と更新方針 | `brief_needed` | `unclassified` | create subject_stack scene brief and prompt | `not_reviewed` |
| 11 | `A-11` | 略称表記 | `brief_needed` | `unclassified` | create subject_stack scene brief and prompt | `not_reviewed` |
| 12 | `B-1` | Gemini | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 13 | `B-2` | Claude | `overlay_audit` | `official_logo_applied` | review official Claude overlay candidate before final promotion | `not_reviewed` |
| 14 | `B-3` | ChatGPT | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 15 | `B-4` | Cursor | `overlay_audit` | `official_logo_applied` | review official Cursor overlay candidate before final promotion | `not_reviewed` |
| 16 | `B-5` | GitHub Copilot | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `not_reviewed` |
| 17 | `B-6` | Windsurf | `blocked_brand_asset` | `blocked_brand_asset` | stop until official Windsurf asset and usage conditions are confirmed | `not_reviewed` |
| 18 | `B-7` | Claude Code | `overlay_audit` | `official_logo_applied` | review official Claude Code overlay candidate before final promotion | `not_reviewed` |
| 19 | `B-8` | Codex | `overlay_wait` | `official_logo_source_review_required` | do not final; import/confirm official logo asset first | `not_reviewed` |
| 20 | `B-9` | v0 | `overlay_audit` | `official_logo_applied` | review adjusted official v0 overlay candidate before final promotion | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
python scripts\ponchi_batch_report.py ponchi-batch-001
python scripts\ponchi_prompt_lint.py <prompt-files>
```
