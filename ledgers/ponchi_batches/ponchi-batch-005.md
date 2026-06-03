# ponchi-batch-005 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- `color_audit` means a non-brand base candidate is staged and has passed the mechanical color gate; it still needs visual review before final promotion.
- Generate or update scene briefs only for rows that truly lack prompts or need a rerun.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `D-1` | Gemini 2 系 | `overlay_audit` | `official_logo_applied` | review official Gemini sparkle overlay before final promotion | `not_reviewed` |
| 2 | `D-2` | Gemini 2.5 系 | `overlay_audit` | `official_logo_applied` | review official Gemini sparkle overlay before final promotion | `not_reviewed` |
| 3 | `D-3` | Gemini 3 系 | `overlay_audit` | `official_logo_applied` | review official Gemini sparkle overlay before final promotion | `not_reviewed` |
| 4 | `D-4` | Gemini 3.1 系 | `overlay_audit` | `official_logo_applied` | review official Gemini sparkle overlay before final promotion | `not_reviewed` |
| 5 | `D-10` | Claude 3 系 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 6 | `D-11` | Claude 3.5 系 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 7 | `D-12` | Claude 4 系 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 8 | `D-13` | Claude 4.5 系 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 9 | `D-14` | Claude Mythos Preview | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 10 | `D-20` | GPT-5 系 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 11 | `D-21` | GPT-4 系 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 12 | `D-22` | o1 系 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 13 | `D-23` | o3 系 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 14 | `D-24` | GPT-3 系 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 15 | `D-25` | GPT-1 / GPT-2 系 | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 16 | `D-26` | gpt-oss | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 17 | `D-30` | Grok 系 | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 18 | `D-35` | Cursor Composer | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 19 | `D-40` | Llama 系 | `overlay_audit` | `official_logo_applied` | official Meta organization icon from llama.com applied as review-pending overlay; not a Llama-specific product lockup | `not_reviewed` |
| 20 | `D-41` | Mistral 系 | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_report.py ponchi-batch-005
python scripts\ponchi_prompt_lint.py <prompt-files>
python scripts\ponchi_color_audit.py --manifest-root assets\ponchi\final_candidates
```
