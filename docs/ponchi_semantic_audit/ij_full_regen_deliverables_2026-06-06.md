# I/J full ponchi regeneration deliverables

Date: 2026-06-06; final promotion updated 2026-06-07

Purpose: review index and final promotion record for the full I/J ponchi image
rebuild. The accepted candidates are now promoted to production files under
`assets/ponchi/final/`.

## Overall Status

| item | result |
| --- | --- |
| scope | I chapter 19 images, J chapter 50 images |
| total candidates staged | 69 |
| batch status | `semantic-regen-015` through `semantic-regen-024` are `final_promoted` |
| prompt lint | all target prompts passed |
| image audit | all staged candidates passed |
| color audit | all staged candidates passed after documented palette normalization where needed |
| quality score | high=61, mid=8, low=0 |
| comparison audit | recorded for every batch |
| final promotion audit | image pass=69, color pass=69, quality high=59 mid=7 low=3; visual accepted |
| production update | promoted to `assets/ponchi/final/` on 2026-06-07 |

## Batch Deliverables

| batch | entries | focus | quality | candidate sheet | results | candidate update |
| --- | --- | --- | --- | --- | --- | --- |
| `semantic-regen-015` | `J-72;J-73;J-78;J-79;J-91` | worst hardware/UI outliers | high=3 mid=2 low=0 | `assets/ponchi/final_candidates/semantic-regen-015/final_candidates_contact_sheet.png` | `docs/ponchi_semantic_audit/semantic_regen_015/results.md` | `ledgers/semantic_regen_015_candidate_update.csv` |
| `semantic-regen-016` | `J-70;J-71;J-74;J-75;J-76;J-77;J-80;J-81` | hardware accelerator memory and storage interfaces | high=4 mid=4 low=0 | `assets/ponchi/final_candidates/semantic-regen-016/final_candidates_contact_sheet.png` | `docs/ponchi_semantic_audit/semantic_regen_016/results.md` | `ledgers/semantic_regen_016_candidate_update.csv` |
| `semantic-regen-017` | `I-1;I-2;I-3;I-4;I-5;I-80;I-81` | MCP core roles and setup | high=7 mid=0 low=0 | `assets/ponchi/final_candidates/semantic-regen-017/final_candidates_contact_sheet.png` | `docs/ponchi_semantic_audit/semantic_regen_017/results.md` | `ledgers/semantic_regen_017_candidate_update.csv` |
| `semantic-regen-018` | `I-10;I-11;I-12;I-13;I-23;I-24;I-30;I-41;I-50` | MCP tool domains | high=9 mid=0 low=0 | `assets/ponchi/final_candidates/semantic-regen-018/final_candidates_contact_sheet.png` | `docs/ponchi_semantic_audit/semantic_regen_018/results.md` | `ledgers/semantic_regen_018_candidate_update.csv` |
| `semantic-regen-019` | `I-20;I-21;I-22` | browser automation MCP exact distinction | high=3 mid=0 low=0 | `assets/ponchi/final_candidates/semantic-regen-019/final_candidates_contact_sheet.png` | `docs/ponchi_semantic_audit/semantic_regen_019/results.md` | `ledgers/semantic_regen_019_candidate_update.csv` |
| `semantic-regen-020` | `J-1;J-2;J-3;J-4;J-10;J-11;J-12;J-13;J-14;J-15` | AI ML concepts first half | high=9 mid=1 low=0 | `assets/ponchi/final_candidates/semantic-regen-020/final_candidates_contact_sheet.png` | `docs/ponchi_semantic_audit/semantic_regen_020/results.md` | `ledgers/semantic_regen_020_candidate_update.csv` |
| `semantic-regen-021` | `J-16;J-17;J-18;J-19;J-20;J-21;J-22;J-23` | training adaptation and data/model mechanics | high=7 mid=1 low=0 | `assets/ponchi/final_candidates/semantic-regen-021/final_candidates_contact_sheet.png` | `docs/ponchi_semantic_audit/semantic_regen_021/results.md` | `ledgers/semantic_regen_021_candidate_update.csv` |
| `semantic-regen-022` | `J-31;J-32;J-33;J-40;J-41;J-42;J-43;J-100` | history buzzwords and literacy | high=8 mid=0 low=0 | `assets/ponchi/final_candidates/semantic-regen-022/final_candidates_contact_sheet.png` | `docs/ponchi_semantic_audit/semantic_regen_022/results.md` | `ledgers/semantic_regen_022_candidate_update.csv` |
| `semantic-regen-023` | `J-50;J-51;J-52;J-53;J-54;J-55;J-56;J-62` | law ethics safety | high=8 mid=0 low=0 | `assets/ponchi/final_candidates/semantic-regen-023/final_candidates_contact_sheet.png` | `docs/ponchi_semantic_audit/semantic_regen_023/results.md` | `ledgers/semantic_regen_023_candidate_update.csv` |
| `semantic-regen-024` | `J-90;J-92;J-93` | UI OS ecosystem | high=3 mid=0 low=0 | `assets/ponchi/final_candidates/semantic-regen-024/final_candidates_contact_sheet.png` | `docs/ponchi_semantic_audit/semantic_regen_024/results.md` | `ledgers/semantic_regen_024_candidate_update.csv` |

## Final Promotion Artifacts

- Promotion ledger: `ledgers/ij_full_regen_final_promotion_2026-06-07.csv`
- Promotion results: `docs/ponchi_semantic_audit/ij_full_regen_final_promotion_2026-06-07/results.md`
- Final color audit: `ledgers/ij_full_regen_final_promotion_color_audit_2026-06-07.csv`
- Final quality score: `ledgers/ij_full_regen_final_promotion_quality_scores_2026-06-07.csv`

## Review Order

1. Open each `final_candidates_contact_sheet.png` and check visual distinction
   inside the batch.
2. For any questionable row, read the batch `results.md` and
   `comparison_audit.csv`.
3. Use the corresponding `candidate_update.csv` to compare candidate file size
   and promotion status against the current final image.
4. Final promotion has been completed; use the final promotion artifacts above
   for post-promotion audit checks.

## Source Ledgers

- Batch status ledger: `ledgers/ij_full_regen_batches.csv`
- Generation ledger: `ledgers/ponchi_generation_batches.csv`
- Full rebuild plan: `docs/ponchi_semantic_audit/ij_full_regen_plan_2026-06-06.md`
