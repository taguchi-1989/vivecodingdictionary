# semantic-regen-001 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- `color_audit` means a non-brand base candidate is staged and has passed the mechanical color gate; it still needs visual review before final promotion.
- Generate or update scene briefs only for rows that truly lack prompts or need a rerun.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `B-26` | Azure OpenAI | `overlay_audit` | `official_logo_applied` | semantic-regeneration base generated; overlay and blind retest required before final promotion | `generated_base_pass` |
| 2 | `B-31` | Excalidraw | `overlay_audit` | `official_logo_applied` | semantic-regeneration base generated; overlay and blind retest required before final promotion | `generated_base_pass` |
| 3 | `B-5` | GitHub Copilot | `overlay_audit` | `official_logo_applied` | semantic-regeneration base generated; overlay and blind retest required before final promotion | `generated_base_pass` |
| 4 | `B-52` | Gemini の料金プラン | `overlay_audit` | `official_logo_applied` | semantic-regeneration base generated; overlay and blind retest required before final promotion | `generated_base_pass` |
| 5 | `B-6` | Windsurf | `overlay_audit` | `official_logo_applied` | semantic-regeneration base generated; overlay and blind retest required before final promotion | `generated_base_pass` |
| 6 | `D-22` | o1 系 | `overlay_audit` | `official_logo_applied` | semantic-regeneration base generated; overlay and blind retest required before final promotion | `generated_base_pass` |
| 7 | `D-53` | Veo | `overlay_audit` | `official_logo_applied` | semantic-regeneration base generated; overlay and blind retest required before final promotion | `generated_base_pass` |
| 8 | `D-58` | Whisk | `overlay_audit` | `official_logo_applied` | semantic-regeneration base generated; overlay and blind retest required before final promotion | `generated_base_pass` |
| 9 | `D-70` | Amical | `overlay_audit` | `official_logo_applied` | semantic-regeneration base generated for brand-audit scope; entry text reconciliation and blind retest required before final promotion | `generated_base_pass` |

## Batch Commands

```powershell
python scripts\ponchi_batch_report.py semantic-regen-001
python scripts\ponchi_prompt_lint.py <prompt-files>
python scripts\ponchi_color_audit.py --manifest-root assets\ponchi\final_candidates
```
