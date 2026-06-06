# Ponchi Quality Score Summary

This is a mechanical outlier score for planning visual review and regeneration. It is not final approval.

## Artifacts

- CSV: `ledgers/semantic_regen_021_quality_scores.csv`
- Low score contact sheet: `docs/ponchi_semantic_audit/semantic_regen_021/quality_low_contact_sheet.png`
- Mid review contact sheet: `docs/ponchi_semantic_audit/semantic_regen_021/quality_mid_contact_sheet.png`
- Known padding contact sheet: `docs/ponchi_semantic_audit/semantic_regen_021/quality_known_contact_sheet.png`
- Sparse diagram contact sheet: `docs/ponchi_semantic_audit/semantic_regen_021/quality_sparse_contact_sheet.png`

## Score Bands

| band | count |
| --- | ---: |
| `high` | 7 |
| `mid` | 1 |
| `low` | 0 |

## Recommended Actions

| action | count |
| --- | ---: |
| `light_review` | 7 |
| `visual_review` | 1 |

## Color Gate Counts

| color status | count |
| --- | ---: |
| `pass` | 8 |
| `review` | 0 |
| `fail` | 0 |

## Lowest Scores

| entry | title | score | action | reasons |
| --- | --- | ---: | --- | --- |
| `J-18_base_1254x627` |  | 81 | `visual_review` | `濃淡;線密度` |
| `J-17_base_1254x627` |  | 86 | `light_review` | `線密度` |
| `J-19_base_1254x627` |  | 88 | `light_review` | `線密度` |
| `J-21_base_1254x627` |  | 91 | `light_review` | `` |
| `J-20_base_1254x627` |  | 92 | `light_review` | `` |
| `J-22_base_1254x627` |  | 94 | `light_review` | `` |
| `J-23_base_1254x627` |  | 97 | `light_review` | `` |
| `J-16_base_1254x627` |  | 98 | `light_review` | `` |

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
