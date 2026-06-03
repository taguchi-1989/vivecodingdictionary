# ponchi-batch-001 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- `color_audit` means a non-brand base candidate is staged and has passed the mechanical color gate; it still needs visual review before final promotion.
- Generate or update scene briefs only for rows that truly lack prompts or need a rerun.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `A-1` | まえがき | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 2 | `A-2` | この本の読み方 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 3 | `A-3` | 図鑑の歩き方 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 4 | `A-4` | 体験区分の凡例 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 5 | `A-5` | 読者レベルの凡例 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 6 | `A-6` | 評価日・時変情報の見方 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 7 | `A-7` | 図のタイプ | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 8 | `A-8` | 色・記号の凡例 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 9 | `A-9` | 索引 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 10 | `A-10` | 更新履歴と更新方針 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 11 | `A-11` | 略称表記 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 12 | `B-1` | Gemini | `overlay_audit` | `official_logo_applied` | review official Gemini sparkle overlay before final promotion | `not_reviewed` |
| 13 | `B-2` | Claude | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `not_reviewed` |
| 14 | `B-3` | ChatGPT | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 15 | `B-4` | Cursor | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `not_reviewed` |
| 16 | `B-5` | GitHub Copilot | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `not_reviewed` |
| 17 | `B-6` | Windsurf | `overlay_audit` | `official_logo_applied` | review official Windsurf wordmark overlay before final promotion; density warning requires visual review | `not_reviewed` |
| 18 | `B-7` | Claude Code | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `not_reviewed` |
| 19 | `B-8` | Codex | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 20 | `B-9` | v0 | `overlay_audit` | `official_logo_applied` | review existing official overlay before final promotion | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_report.py ponchi-batch-001
python scripts\ponchi_prompt_lint.py <prompt-files>
python scripts\ponchi_color_audit.py --manifest-root assets\ponchi\final_candidates
```
