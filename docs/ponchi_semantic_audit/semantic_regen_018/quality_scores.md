# Ponchi Quality Score Summary

This is a mechanical outlier score for planning visual review and regeneration. It is not final approval.

## Artifacts

- CSV: `ledgers/semantic_regen_018_quality_scores.csv`
- Low score contact sheet: `docs/ponchi_semantic_audit/semantic_regen_018/quality_low_contact_sheet.png`
- Mid review contact sheet: `docs/ponchi_semantic_audit/semantic_regen_018/quality_mid_contact_sheet.png`
- Known padding contact sheet: `docs/ponchi_semantic_audit/semantic_regen_018/quality_known_contact_sheet.png`
- Sparse diagram contact sheet: `docs/ponchi_semantic_audit/semantic_regen_018/quality_sparse_contact_sheet.png`

## Score Bands

| band | count |
| --- | ---: |
| `high` | 9 |
| `mid` | 0 |
| `low` | 0 |

## Recommended Actions

| action | count |
| --- | ---: |
| `light_review` | 9 |

## Color Gate Counts

| color status | count |
| --- | ---: |
| `pass` | 9 |
| `review` | 0 |
| `fail` | 0 |

## Lowest Scores

| entry | title | score | action | reasons |
| --- | --- | ---: | --- | --- |
| `I-10_base_1254x627` |  | 92 | `light_review` | `線密度` |
| `I-24_base_1254x627` |  | 92 | `light_review` | `` |
| `I-13_base_1254x627` |  | 93 | `light_review` | `` |
| `I-30_base_1254x627` |  | 93 | `light_review` | `` |
| `I-23_base_1254x627` |  | 94 | `light_review` | `` |
| `I-50_base_1254x627` |  | 97 | `light_review` | `` |
| `I-11_base_1254x627` |  | 99 | `light_review` | `` |
| `I-12_base_1254x627` |  | 99 | `light_review` | `` |
| `I-41_base_1254x627` |  | 99 | `light_review` | `` |

## Mid Band With Structural Reasons

| entry | title | score | action | reasons |
| --- | --- | ---: | --- | --- |

## Sparse High-Score Diagram Candidates

These score well mechanically but are likely too thin for branded/service illustrations.

| entry | title | score | file KB | ink | contrast | reasons |
| --- | --- | ---: | ---: | ---: | ---: | --- |

## Known Mechanical Padding Set

- known padding ids detected in final set: 0 / 23

| entry | title | score | action | central shape |
| --- | --- | ---: | --- | --- |

## Initial Rule Assessment

- Low scores are useful for finding visual outliers, but they should be treated as review priority rather than automatic rejection.
- Known mechanical padding must be an explicit rule because several padded images can still score mid or high on color and density.
- Sparse high-score diagrams must be an explicit rule because clean logo/box/arrow images can look statistically normal while feeling under-produced.
- Mid-band images with padding or color reasons are the important validation set: they test whether the score catches boring or weak 2:1 composition.
- High-band images still need light visual review for semantic mismatch, generated logos, or policy issues that pixel metrics cannot see.
