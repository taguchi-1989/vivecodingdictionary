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
| overlay_audit | 20 / 20 | D-1 - D-4, D-10 - D-14, D-20 - D-26, D-30, D-35, D-40, D-41 |
| overlay_wait | 0 / 20 | none |
| final candidate 化済み | 20 / 20 | overlay_audit entries staged as review_pending |
| color audit pass | 20 / 20 staged candidates | all staged candidates |
| final 昇格済み | 0 / 20 | まだ `assets/ponchi/final/` へはコピーしない |

## Entry 一覧

| entry | title | prompt | 2:1 base | official logo source | current status |
| --- | --- | --- | --- | --- | --- |
| D-1 | Gemini 2 系 | done | pass | official Gemini asset applied | overlay_audit |
| D-2 | Gemini 2.5 系 | done | pass | official Gemini asset applied | overlay_audit |
| D-3 | Gemini 3 系 | done | pass | official Gemini asset applied | overlay_audit |
| D-4 | Gemini 3.1 系 | done | pass | official Gemini asset applied | overlay_audit |
| D-10 | Claude 3 系 | done | pass | local official asset applied | overlay_audit |
| D-11 | Claude 3.5 系 | done | pass | local official asset applied | overlay_audit |
| D-12 | Claude 4 系 | done | pass | local official asset applied | overlay_audit |
| D-13 | Claude 4.5 系 | done | pass | local official asset applied | overlay_audit |
| D-14 | Claude Mythos Preview | done | pass | local official asset applied | overlay_audit |
| D-20 | GPT-5 系 | done | pass | local OpenAI wordmark applied | overlay_audit |
| D-21 | GPT-4 系 | done | pass | local OpenAI wordmark applied | overlay_audit |
| D-22 | o1 系 | done | pass | local OpenAI wordmark applied | overlay_audit |
| D-23 | o3 系 | done | pass | local OpenAI wordmark applied | overlay_audit |
| D-24 | GPT-3 系 | done | pass | local OpenAI wordmark applied | overlay_audit |
| D-25 | GPT-1 / GPT-2 系 | done | pass | local OpenAI wordmark applied | overlay_audit |
| D-26 | gpt-oss | done | pass | local OpenAI wordmark applied | overlay_audit |
| D-30 | Grok 系 | done | pass | official xAI favicon applied | overlay_audit |
| D-35 | Cursor Composer | done | pass | local official asset applied | overlay_audit |
| D-40 | Llama 系 | done | pass | official Meta organization icon from llama.com applied | overlay_audit |
| D-41 | Mistral 系 | done | pass | official Mistral asset applied | overlay_audit |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-005/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-005/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-005-base-image-audit.md`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-005-base-contact-sheet.png`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-005.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-005.md`

## Next action

Batch 005 base generation is complete, and all 20 deterministic official
overlays are staged as review-pending candidates. D-40 uses the official Meta
organization icon from llama.com as a review-pending organization overlay, not
a Llama-specific product lockup. Do not promote anything to `assets/ponchi/final/`
without explicit approval.
