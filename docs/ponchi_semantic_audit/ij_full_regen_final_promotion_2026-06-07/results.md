# I/J Final Promotion Results

Date: 2026-06-07

Scope: 69 accepted I/J ponchi candidates from `semantic-regen-015` through
`semantic-regen-024` were promoted to `assets/ponchi/final/`.

## Promotion Summary

| item | result |
| --- | --- |
| promoted entries | 69 |
| source candidates | `assets/ponchi/final_candidates/semantic-regen-015` through `semantic-regen-024` |
| final destination | `assets/ponchi/final/` |
| final WebP encoding | lossless WebP generated from promoted PNGs |
| promotion ledger | `ledgers/ij_full_regen_final_promotion_2026-06-07.csv` |
| batch ledger status | `final_promoted` |
| candidate update status | `accepted` / `promoted` |

## Final Audit

| gate | result |
| --- | --- |
| image audit | pass=69 |
| color audit | pass=69 |
| quality score | high=59, mid=7, low=3 |
| visual acceptance | accepted |

The quality score is a mechanical outlier score for review planning, not final
approval. The three low rows are `J-72` H100, `J-80` SATA, and `J-81` M.2. They
remain visually accepted after final contact-sheet review because the flags are
caused by dense hardware/exploded-diagram contrast and line-density differences,
not by size, palette, semantic mismatch, or SVG/stick-figure regression.

## Audit Artifacts

- Image audits: `docs/ponchi_semantic_audit/ij_full_regen_final_promotion_2026-06-07/semantic_regen_*_final_image_audit.csv`
- Color audit: `ledgers/ij_full_regen_final_promotion_color_audit_2026-06-07.csv`
- Quality score: `ledgers/ij_full_regen_final_promotion_quality_scores_2026-06-07.csv`
- Color contact sheet: `docs/ponchi_semantic_audit/ij_full_regen_final_promotion_2026-06-07/color_contact_sheet.png`
- Quality low contact sheet: `docs/ponchi_semantic_audit/ij_full_regen_final_promotion_2026-06-07/quality_low_contact_sheet.png`
