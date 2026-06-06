# semantic-regen-015 results

Date: 2026-06-06

Purpose: first execution batch for the full I/J ponchi rebuild. This batch
targets the weakest J hardware/UI outliers before moving to the remaining I/J
entries.

## Scope

| entry | result |
| --- | --- |
| `J-72 H100` | staged as datacenter accelerator module with HBM/rack context |
| `J-73 Blackwell` | staged as newer paired-module rack-scale accelerator generation |
| `J-78 HDD` | staged as mechanical platter/actuator storage |
| `J-79 SSD` | staged as solid-state chip storage |
| `J-91 CLI` | staged as bright command-line loop with Character A operator |

## Gates

| gate | result |
| --- | --- |
| prompt lint | `ok: 5 file(s)` |
| image audit | `pass=5`, `review=0`, `fail=0` |
| color audit | `pass=5`, `review=0`, `fail=0` |
| quality score | `high=3`, `mid=2`, `low=0` |
| comparison audit | `candidate_ok=3`, `candidate_ok_mid_review=2` |

## Comparison Notes

- `J-72` and `J-73` are now separated by single-module HBM/rack context versus
  paired-module rack-scale interconnect.
- `J-78` and `J-79` are separated by mechanical platter/actuator versus
  solid-state chip board.
- `J-91` no longer depends on a dark terminal block. It uses Character A as a
  stable secondary operator and keeps CLI distinct from GUI/Linux/Ubuntu.
- No generated logos, official seals, product UI, readable words, or brand
  colors are accepted in the staged candidates.

## Artifacts

- Full rebuild plan: `docs/ponchi_semantic_audit/ij_full_regen_plan_2026-06-06.md`
- Batch queue: `ledgers/ij_full_regen_batches.csv`
- Prompts: `assets/ponchi/pipeline_prompts/semantic-regen-015/`
- Generated bases: `assets/ponchi/experiments/batches/semantic-regen-015/`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-015/`
- Candidate audit: `docs/ponchi_batch_audits/semantic-regen-015-final-candidates.md`
- Image audit: `docs/ponchi_semantic_audit/semantic_regen_015/base_image_audit.md`
- Color audit: `docs/ponchi_semantic_audit/semantic_regen_015/color_audit.md`
- Quality scores: `docs/ponchi_semantic_audit/semantic_regen_015/quality_scores.md`
- Comparison audit: `docs/ponchi_semantic_audit/semantic_regen_015/comparison_audit.csv`
- Candidate update ledger: `ledgers/semantic_regen_015_candidate_update.csv`

## Judgment

`semantic-regen-015` passes as a staged candidate batch for the full I/J
rebuild. No production final image was overwritten. `J-72` and `J-91` remain
mid-score visual-review rows, but both pass image/color gates and comparison
audit.
