# ponchi-batch-005 progress summary

対象: `D-1` から `D-41` までの 20 件。

## 数字サマリー

| 段階 | 件数 | 対象 |
| --- | ---: | --- |
| prompt 作成済み | 20 / 20 | D-1 - D-41 全件 |
| prompt lint pass | 20 / 20 | D-1 - D-41 全件 |
| 2:1 base 作成済み | 20 / 20 | D-1 - D-41 全件 |
| 2:1 base audit pass | 20 / 20 | D-1 - D-41 全件 |
| 公式ロゴ/公式アイコン要確認 | 20 / 20 | D-1 - D-41 全件 |
| overlay_ready | 7 / 20 | D-20 - D-26 |
| overlay_wait | 13 / 20 | D-1 - D-14, D-30, D-35, D-40 - D-41 |
| final candidate 化済み | 0 / 20 | 未生成 |
| final 昇格済み | 0 / 20 | まだ `assets/ponchi/final/` へはコピーしない |

## Entry 一覧

| entry | title | prompt | 2:1 base | official logo source | current status |
| --- | --- | --- | --- | --- | --- |
| D-1 | Gemini 2 系 | done | pass | waiting | overlay_wait |
| D-2 | Gemini 2.5 系 | done | pass | waiting | overlay_wait |
| D-3 | Gemini 3 系 | done | pass | waiting | overlay_wait |
| D-4 | Gemini 3.1 系 | done | pass | waiting | overlay_wait |
| D-10 | Claude 3 系 | done | pass | local asset, usage review | overlay_wait |
| D-11 | Claude 3.5 系 | done | pass | local asset, usage review | overlay_wait |
| D-12 | Claude 4 系 | done | pass | local asset, usage review | overlay_wait |
| D-13 | Claude 4.5 系 | done | pass | local asset, usage review | overlay_wait |
| D-14 | Claude Mythos Preview | done | pass | local asset, usage review | overlay_wait |
| D-20 | GPT-5 系 | done | pass | local OpenAI wordmark | overlay_ready |
| D-21 | GPT-4 系 | done | pass | local OpenAI wordmark | overlay_ready |
| D-22 | o1 系 | done | pass | local OpenAI wordmark | overlay_ready |
| D-23 | o3 系 | done | pass | local OpenAI wordmark | overlay_ready |
| D-24 | GPT-3 系 | done | pass | local OpenAI wordmark | overlay_ready |
| D-25 | GPT-1 / GPT-2 系 | done | pass | local OpenAI wordmark | overlay_ready |
| D-26 | gpt-oss | done | pass | local OpenAI wordmark | overlay_ready |
| D-30 | Grok 系 | done | pass | waiting | overlay_wait |
| D-35 | Cursor Composer | done | pass | local asset, usage review | overlay_wait |
| D-40 | Llama 系 | done | pass | waiting | overlay_wait |
| D-41 | Mistral 系 | done | pass | waiting | overlay_wait |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-005/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-005/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-005-base-image-audit.md`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-005-base-contact-sheet.png`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-005.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-005.md`

## Next action

Batch 005 base generation is complete. Continue with official source and usage
review for the 13 `overlay_wait` entries before deterministic logo/icon
compositing. The 7 `overlay_ready` entries can move to deterministic OpenAI
wordmark overlay after placement review. Do not promote anything to
`assets/ponchi/final/` without explicit approval.
