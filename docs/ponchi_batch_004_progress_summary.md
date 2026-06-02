# ponchi-batch-004 progress summary

対象: `C-10` から `C-83` までの 20 件。

## 数字サマリー

| 段階 | 件数 | 対象 |
| --- | ---: | --- |
| prompt 作成済み | 20 / 20 | C-10 - C-83 全件 |
| prompt lint pass | 20 / 20 | C-10 - C-83 全件 |
| 2:1 base 作成済み | 20 / 20 | C-10 - C-14, C-50 - C-60, C-80 - C-83 |
| 2:1 base audit pass | 20 / 20 | C-10 - C-14, C-50 - C-60, C-80 - C-83 |
| 公式ロゴ/公式アイコン要確認 | 9 / 20 | C-10 - C-14, C-80 - C-83 |
| logo avoid | 11 / 20 | C-50 - C-60 |
| overlay_wait | 9 / 20 | C-10 - C-14, C-80 - C-83 |
| prompt_review | 11 / 20 | C-50 - C-60 |
| final candidate 化済み | 0 / 20 | 未生成 |
| final 昇格済み | 0 / 20 | まだ `assets/ponchi/final/` へはコピーしない |

## Entry 一覧

| entry | title | prompt | 2:1 base | official logo source | current status |
| --- | --- | --- | --- | --- | --- |
| C-10 | Moonshot AI | done | pass | waiting | overlay_wait |
| C-11 | Z.ai | done | pass | waiting | overlay_wait |
| C-12 | TSMC | done | pass | waiting | overlay_wait |
| C-13 | Groq | done | pass | waiting | overlay_wait |
| C-14 | AMD | done | pass | waiting | overlay_wait |
| C-50 | Sam Altman | done | pass | logo avoid | prompt_review |
| C-51 | Dario Amodei | done | pass | logo avoid | prompt_review |
| C-52 | Demis Hassabis | done | pass | logo avoid | prompt_review |
| C-53 | Andrej Karpathy | done | pass | logo avoid | prompt_review |
| C-54 | Ilya Sutskever | done | pass | logo avoid | prompt_review |
| C-55 | Mira Murati | done | pass | logo avoid | prompt_review |
| C-56 | Yann LeCun | done | pass | logo avoid | prompt_review |
| C-57 | Geoffrey Hinton | done | pass | logo avoid | prompt_review |
| C-58 | Elon Musk | done | pass | logo avoid | prompt_review |
| C-59 | Jensen Huang | done | pass | logo avoid | prompt_review |
| C-60 | Ray Kurzweil | done | pass | logo avoid | prompt_review |
| C-80 | AI大学 | done | pass | waiting | overlay_wait |
| C-81 | にゃんた | done | pass | waiting | overlay_wait |
| C-82 | まさお | done | pass | waiting | overlay_wait |
| C-83 | AI の羅針盤 | done | pass | waiting | overlay_wait |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-004/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-004/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-004-base-image-audit.md`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-004.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-004.md`

## Next action

Batch 004 base generation is complete. Continue with official source review for
the 9 `overlay_wait` entries before deterministic logo/icon compositing. Keep
all unresolved source items in `overlay_wait`; do not promote anything to
`assets/ponchi/final/` without explicit approval.
