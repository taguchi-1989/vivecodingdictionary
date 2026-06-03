# ponchi-batch-004 progress summary

対象: `C-10` から `C-83` までの 20 件。

## 数字サマリー

| 段階 | 件数 | 対象 |
| --- | ---: | --- |
| prompt 作成済み | 20 / 20 | C-10 - C-83 全件 |
| prompt lint pass | 20 / 20 | C-10 - C-83 全件 |
| 2:1 base 作成済み | 20 / 20 | C-10 - C-14, C-50 - C-60, C-80 - C-83 |
| 2:1 base audit pass | 20 / 20 | C-10 - C-14, C-50 - C-60, C-80 - C-83 |
| 公式ロゴ/公式アイコン要確認 | 1 / 20 | C-12 |
| overlay_audit | 8 / 20 | C-10, C-11, C-13, C-14, C-80 - C-83 |
| logo avoid | 11 / 20 | C-50 - C-60 |
| overlay_wait | 1 / 20 | C-12 |
| color_audit | 11 / 20 | C-50 - C-60 |
| final candidate 化済み | 19 / 20 | C-10, C-11, C-13, C-14, C-50 - C-60, C-80 - C-83 |
| color audit pass | 19 / 20 | final candidate 化済み全件 |
| final 昇格済み | 0 / 20 | まだ `assets/ponchi/final/` へはコピーしない |

## Entry 一覧

| entry | title | prompt | 2:1 base | official logo source | current status |
| --- | --- | --- | --- | --- | --- |
| C-10 | Moonshot AI | done | pass | official applied | overlay_audit |
| C-11 | Z.ai | done | pass | official applied | overlay_audit |
| C-12 | TSMC | done | pass | waiting | overlay_wait |
| C-13 | Groq | done | pass | official applied | overlay_audit |
| C-14 | AMD | done | pass | official applied | overlay_audit |
| C-50 | Sam Altman | done | pass | logo avoid | color_audit |
| C-51 | Dario Amodei | done | pass | logo avoid | color_audit |
| C-52 | Demis Hassabis | done | pass | logo avoid | color_audit |
| C-53 | Andrej Karpathy | done | pass | logo avoid | color_audit |
| C-54 | Ilya Sutskever | done | pass | logo avoid | color_audit |
| C-55 | Mira Murati | done | pass | logo avoid | color_audit |
| C-56 | Yann LeCun | done | pass | logo avoid | color_audit |
| C-57 | Geoffrey Hinton | done | pass | logo avoid | color_audit |
| C-58 | Elon Musk | done | pass | logo avoid | color_audit |
| C-59 | Jensen Huang | done | pass | logo avoid | color_audit |
| C-60 | Ray Kurzweil | done | pass | logo avoid | color_audit |
| C-80 | AI大学 | done | pass | official YouTube avatar applied | overlay_audit |
| C-81 | にゃんた | done | pass | official YouTube avatar applied | overlay_audit |
| C-82 | まさお | done | pass | official YouTube avatar applied | overlay_audit |
| C-83 | AI の羅針盤 | done | pass | official YouTube avatar applied; source page name is `AI時代の羅針盤` | overlay_audit |

## Generated locations

- Prompt briefs: `assets/ponchi/pipeline_prompts/ponchi-batch-004/*.md`
- 2:1 base images: `assets/ponchi/experiments/batches/ponchi-batch-004/*_base_1254x627.png`
- Base audit: `docs/ponchi_batch_audits/ponchi-batch-004-base-image-audit.md`
- Overlay audit: `docs/ponchi_batch_audits/ponchi-batch-004-overlay-image-audit.md`
- Final candidates: `assets/ponchi/final_candidates/ponchi-batch-004/`
- Batch audit: `docs/ponchi_batch_audits/ponchi-batch-004.md`
- Batch report: `ledgers/ponchi_batches/ponchi-batch-004.md`

## Next action

Batch 004 base generation is complete. C-10 Moonshot AI, C-11 Z.ai, C-13 Groq,
C-14 AMD, C-80 AI大学, C-81 にゃんた, C-82 まさお, and C-83 AI の羅針盤 now have
deterministic official-logo or official-icon overlays staged as review-pending
final candidates. C-50 - C-60 are staged as non-brand base candidates and pass
the mechanical color gate. C-12 TSMC remains in `overlay_wait`. C-10 still reports
`review` in the overlay image audit because its clearspace ink is high, so it
needs visual review before any final promotion. Do not promote anything to
`assets/ponchi/final/` without explicit approval.
