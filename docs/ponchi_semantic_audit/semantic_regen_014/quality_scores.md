# Ponchi Quality Score Summary

This is a mechanical outlier score for planning visual review and regeneration. It is not final approval.

## Artifacts

- CSV: `ledgers/semantic_regen_014_quality_scores.csv`
- Contact sheets are not retained for this focused four-image check; the base
  and color contact sheets are in `docs/ponchi_semantic_audit/semantic_regen_014/`.

## Score Bands

| band | count |
| --- | ---: |
| `high` | 4 |
| `mid` | 0 |
| `low` | 0 |

## Recommended Actions

| action | count |
| --- | ---: |
| `light_review` | 4 |

## Color Gate Counts

| color status | count |
| --- | ---: |
| `pass` | 4 |
| `review` | 0 |
| `fail` | 0 |

## Lowest Scores

| entry | title | score | action | reasons |
| --- | --- | ---: | --- | --- |
| `J-52_candidate` |  | 93 | `light_review` | `` |
| `J-50_candidate` |  | 94 | `light_review` | `` |
| `J-53_candidate` |  | 94 | `light_review` | `` |
| `J-54_candidate` |  | 94 | `light_review` | `` |

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
