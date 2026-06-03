# ponchi-batch-003 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- `color_audit` means a non-brand base candidate is staged and has passed the mechanical color gate; it still needs visual review before final promotion.
- Generate or update scene briefs only for rows that truly lack prompts or need a rerun.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `B-30` | Amazon Bedrock | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 2 | `B-31` | Excalidraw | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 3 | `B-32` | Figma | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 4 | `B-33` | Canva | `overlay_audit` | `official_logo_applied` | official Canva type logo from Canva dev brand guidelines package applied as review-pending overlay; do not final without color/visual approval | `not_reviewed` |
| 5 | `B-40` | Reddit | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 6 | `B-41` | arXiv | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 7 | `B-50` | Claude の料金プラン | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 8 | `B-51` | ChatGPT の料金プラン | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 9 | `B-52` | Gemini の料金プラン | `overlay_audit` | `official_logo_applied` | review official Gemini sparkle overlay before final promotion | `not_reviewed` |
| 10 | `B-60` | Suno | `overlay_audit` | `official_logo_applied` | review official Suno overlay before final promotion; light wordmark uses dark composition plate for visibility | `not_reviewed` |
| 11 | `B-61` | ACE-Step 1.5 | `overlay_audit` | `official_logo_applied` | official ACE-Step logo from official GitHub repo applied as review-pending overlay; keep black-square source artwork unchanged | `not_reviewed` |
| 12 | `C-1` | OpenAI | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 13 | `C-2` | Anthropic | `overlay_audit` | `official_logo_applied` | review deterministic official overlay before final promotion | `not_reviewed` |
| 14 | `C-3` | Google DeepMind | `overlay_audit` | `official_logo_applied` | review official Google DeepMind icon overlay before final promotion | `not_reviewed` |
| 15 | `C-4` | Meta AI | `overlay_audit` | `official_logo_applied` | official Meta AI orbit logo rendered from official SVG via local Chrome and applied as review-pending overlay; do not final without color/visual approval | `not_reviewed` |
| 16 | `C-5` | xAI | `overlay_audit` | `official_logo_applied` | review official xAI favicon overlay before final promotion; source site blocks full page fetch | `not_reviewed` |
| 17 | `C-6` | Mistral AI | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 18 | `C-7` | Hugging Face | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |
| 19 | `C-8` | Microsoft AI | `color_audit` | `logo_avoid` | review confirmed logo-less Microsoft AI organization base candidate before final promotion; do not use Microsoft square mark or generated Microsoft AI wordmark | `not_reviewed` |
| 20 | `C-9` | NVIDIA | `overlay_audit` | `official_logo_applied` | review official-logo overlay candidate | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_report.py ponchi-batch-003
python scripts\ponchi_prompt_lint.py <prompt-files>
python scripts\ponchi_color_audit.py --manifest-root assets\ponchi\final_candidates
```
