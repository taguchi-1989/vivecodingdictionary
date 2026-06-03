# ponchi-batch-016 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- `color_audit` means a non-brand base candidate is staged and has passed the mechanical color gate; it still needs visual review before final promotion.
- Generate or update scene briefs only for rows that truly lack prompts or need a rerun.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `J-1` | AGI | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 2 | `J-2` | 強い AI／弱い AI | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 3 | `J-3` | Singularity | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 4 | `J-4` | ASI | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 5 | `J-10` | Machine Learning | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 6 | `J-11` | Deep Learning | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 7 | `J-12` | Neural Network | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 8 | `J-13` | Transformer | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 9 | `J-14` | LLM | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 10 | `J-15` | VLM | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 11 | `J-16` | Fine-tuning | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 12 | `J-17` | Attention | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 13 | `J-18` | MoE | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 14 | `J-19` | 量子化 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 15 | `J-20` | Big Data | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 16 | `J-21` | LoRA | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 17 | `J-22` | パラメータ数の単位 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 18 | `J-23` | 拡散モデル | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 19 | `J-31` | 第 5 世代コンピュータ | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |
| 20 | `J-32` | ノイマン型 | `color_audit` | `logo_avoid` | review color-pass non-brand base candidate before final promotion | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_report.py ponchi-batch-016
python scripts\ponchi_prompt_lint.py <prompt-files>
python scripts\ponchi_color_audit.py --manifest-root assets\ponchi\final_candidates
```
