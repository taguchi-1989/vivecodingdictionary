# Ponchi Quality Score Summary

This is a mechanical outlier score for planning visual review and regeneration. It is not final approval.

## Artifacts

- CSV: `ledgers/semantic_regen_016_quality_scores.csv`
- Base image contact sheet: `docs/ponchi_semantic_audit/semantic_regen_016/base_contact_sheet.png`
- Color-audited contact sheet: `docs/ponchi_semantic_audit/semantic_regen_016/color_contact_sheet.png`
- Final candidate contact sheet: `assets/ponchi/final_candidates/semantic-regen-016/final_candidates_contact_sheet.png`

## Score Bands

| band | count |
| --- | ---: |
| `high` | 4 |
| `mid` | 4 |
| `low` | 0 |

## Recommended Actions

| action | count |
| --- | ---: |
| `light_review` | 4 |
| `visual_review` | 4 |

## Color Gate Counts

| color status | count |
| --- | ---: |
| `pass` | 8 |
| `review` | 0 |
| `fail` | 0 |

## Lowest Scores

| entry | title | score | action | reasons |
| --- | --- | ---: | --- | --- |
| `J-81_base_1254x627` |  | 72 | `visual_review` | `濃淡;線密度` |
| `J-77_base_1254x627` |  | 80 | `visual_review` | `濃淡;線密度` |
| `J-75_base_1254x627` |  | 82 | `visual_review` | `線密度` |
| `J-80_base_1254x627` |  | 83 | `visual_review` | `濃淡;線密度` |
| `J-74_base_1254x627` |  | 92 | `light_review` | `` |
| `J-76_base_1254x627` |  | 94 | `light_review` | `` |
| `J-70_base_1254x627` |  | 97 | `light_review` | `` |
| `J-71_base_1254x627` |  | 97 | `light_review` | `` |

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
