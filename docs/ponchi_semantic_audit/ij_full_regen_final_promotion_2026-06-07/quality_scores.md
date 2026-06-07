# Ponchi Quality Score Summary

This is a mechanical outlier score for planning visual review and regeneration. It is not final approval.

## Artifacts

- CSV: `ledgers/ij_full_regen_final_promotion_quality_scores_2026-06-07.csv`
- Low score contact sheet: `docs/ponchi_semantic_audit/ij_full_regen_final_promotion_2026-06-07/quality_low_contact_sheet.png`
- Mid review contact sheet: `docs/ponchi_semantic_audit/ij_full_regen_final_promotion_2026-06-07/quality_mid_contact_sheet.png`
- Known padding contact sheet: `docs/ponchi_semantic_audit/ij_full_regen_final_promotion_2026-06-07/quality_known_contact_sheet.png`
- Sparse diagram contact sheet: `docs/ponchi_semantic_audit/ij_full_regen_final_promotion_2026-06-07/quality_sparse_contact_sheet.png`

## Score Bands

| band | count |
| --- | ---: |
| `high` | 59 |
| `mid` | 7 |
| `low` | 3 |

## Recommended Actions

| action | count |
| --- | ---: |
| `composition_regen_review` | 10 |
| `full_regen_review` | 2 |
| `light_review` | 50 |
| `visual_review` | 7 |

## Color Gate Counts

| color status | count |
| --- | ---: |
| `pass` | 69 |
| `review` | 0 |
| `fail` | 0 |

## Lowest Scores

| entry | title | score | action | reasons |
| --- | --- | ---: | --- | --- |
| `J-72` | H100 | 57 | `full_regen_review` | `色味;明るさ;濃淡;線密度;外れ値` |
| `J-81` | M.2 | 58 | `composition_regen_review` | `濃淡;線密度;外れ値;known_padding_2to1` |
| `J-80` | SATA | 66 | `full_regen_review` | `濃淡;線密度;外れ値` |
| `J-78` | HDD | 72 | `visual_review` | `濃淡;線密度` |
| `J-73` | Blackwell | 75 | `visual_review` | `濃淡;線密度` |
| `J-74` | RTX シリーズ | 78 | `visual_review` | `濃淡;線密度` |
| `J-70` | VRAM | 80 | `visual_review` | `濃淡;線密度` |
| `J-18` | MoE | 81 | `visual_review` | `濃淡;線密度` |
| `J-71` | RAM | 83 | `visual_review` | `線密度` |
| `J-3` | Singularity | 84 | `visual_review` | `濃淡` |
| `J-51` | Hallucination | 85 | `light_review` | `線密度` |
| `J-17` | Attention | 86 | `light_review` | `線密度` |
| `I-30` | Notion MCP | 87 | `light_review` | `線密度` |
| `J-1` | AGI | 87 | `light_review` | `線密度` |
| `J-31` | 第 5 世代コンピュータ | 87 | `light_review` | `` |
| `J-52` | Sycophancy | 87 | `light_review` | `線密度` |
| `J-12` | Neural Network | 88 | `light_review` | `線密度` |
| `J-19` | 量子化 | 88 | `light_review` | `線密度` |
| `J-76` | CPU | 88 | `light_review` | `線密度` |
| `J-92` | Linux | 88 | `composition_regen_review` | `余白;known_padding_2to1` |
| `I-5` | MCP SDK | 89 | `composition_regen_review` | `線密度;known_padding_2to1` |
| `I-23` | Serena MCP | 89 | `light_review` | `線密度` |
| `J-79` | SSD | 89 | `light_review` | `` |
| `J-11` | Deep Learning | 90 | `light_review` | `線密度` |
| `J-50` | AI 倫理 | 90 | `light_review` | `` |

## Mid Band With Structural Reasons

| entry | title | score | action | reasons |
| --- | --- | ---: | --- | --- |

## Sparse High-Score Diagram Candidates

These score well mechanically but are likely too thin for branded/service illustrations.

| entry | title | score | file KB | ink | contrast | reasons |
| --- | --- | ---: | ---: | ---: | ---: | --- |

## Known Mechanical Padding Set

- known padding ids detected in final set: 10 / 23

| entry | title | score | action | central shape |
| --- | --- | ---: | --- | --- |
| `I-2` | MCP Server | 94 | `composition_regen_review` | `no` |
| `I-3` | MCP Client | 96 | `composition_regen_review` | `no` |
| `I-4` | MCP Transport | 95 | `composition_regen_review` | `no` |
| `I-5` | MCP SDK | 89 | `composition_regen_review` | `no` |
| `J-81` | M.2 | 58 | `composition_regen_review` | `no` |
| `J-90` | GUI | 93 | `composition_regen_review` | `no` |
| `J-91` | CLI | 94 | `composition_regen_review` | `no` |
| `J-92` | Linux | 88 | `composition_regen_review` | `no` |
| `J-93` | Ubuntu | 94 | `composition_regen_review` | `no` |
| `J-100` | 識字（リテラシー） | 97 | `composition_regen_review` | `no` |

## Initial Rule Assessment

- Low scores are useful for finding visual outliers, but they should be treated as review priority rather than automatic rejection.
- Known mechanical padding must be an explicit rule because several padded images can still score mid or high on color and density.
- Sparse high-score diagrams must be an explicit rule because clean logo/box/arrow images can look statistically normal while feeling under-produced.
- Mid-band images with padding or color reasons are the important validation set: they test whether the score catches boring or weak 2:1 composition.
- High-band images still need light visual review for semantic mismatch, generated logos, or policy issues that pixel metrics cannot see.
