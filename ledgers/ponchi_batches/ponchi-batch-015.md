# ponchi-batch-015 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- `color_audit` means a non-brand base candidate is staged and has passed the mechanical color gate; it still needs visual review before final promotion.
- Generate or update scene briefs only for rows that truly lack prompts or need a rerun.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `H-63` | Vibe Coding 命名 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 2 | `I-1` | MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 3 | `I-2` | MCP Server | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 4 | `I-3` | MCP Client | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 5 | `I-4` | MCP Transport | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 6 | `I-5` | MCP SDK | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 7 | `I-10` | Filesystem MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 8 | `I-11` | GitHub MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 9 | `I-12` | Git MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 10 | `I-13` | Slack MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 11 | `I-20` | Playwright MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 12 | `I-21` | Puppeteer MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 13 | `I-22` | Chrome DevTools MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 14 | `I-23` | Serena MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 15 | `I-24` | Context7 MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 16 | `I-30` | Notion MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 17 | `I-41` | SQLite MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 18 | `I-50` | AWS MCP | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 19 | `I-80` | 自作 MCP のテンプレ | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 20 | `I-81` | MCP の登録・設定 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_report.py ponchi-batch-015
python scripts\ponchi_prompt_lint.py <prompt-files>
python scripts\ponchi_color_audit.py --manifest-root assets\ponchi\final_candidates
```
