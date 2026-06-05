# Ponchi Quality Score Summary

This is a mechanical outlier score for planning visual review and regeneration. It is not final approval.

## Artifacts

- CSV: `ledgers/ponchi_quality_scores.csv`
- Low score contact sheet: `docs/ponchi_batch_audits/ponchi-quality-low-contact-sheet.png`
- Mid review contact sheet: `docs/ponchi_batch_audits/ponchi-quality-mid-review-contact-sheet.png`
- Known padding contact sheet: `docs/ponchi_batch_audits/ponchi-quality-known-padding-contact-sheet.png`
- Sparse diagram contact sheet: `docs/ponchi_batch_audits/ponchi-quality-sparse-diagram-contact-sheet.png`

## Score Bands

| band | count |
| --- | ---: |
| `high` | 327 |
| `mid` | 20 |
| `low` | 3 |

## Recommended Actions

| action | count |
| --- | ---: |
| `color_or_full_regen` | 6 |
| `composition_regen_review` | 23 |
| `full_regen_review` | 1 |
| `light_review` | 294 |
| `official_overlay_color_review` | 9 |
| `sparse_diagram_review` | 1 |
| `visual_review` | 16 |

## Color Gate Counts

| color status | count |
| --- | ---: |
| `pass` | 242 |
| `review` | 93 |
| `fail` | 15 |

## Lowest Scores

| entry | title | score | action | reasons |
| --- | --- | ---: | --- | --- |
| `F-84` | Ghostty | 59 | `full_regen_review` | `色味;明るさ;濃淡;線密度;外れ値` |
| `J-73` | Blackwell | 67 | `color_or_full_regen` | `濃淡;線密度;外れ値;color_fail` |
| `J-72` | H100 | 69 | `color_or_full_regen` | `濃淡;線密度;外れ値;color_fail` |
| `J-78` | HDD | 70 | `visual_review` | `濃淡;線密度;color_review` |
| `C-59` | Jensen Huang | 76 | `visual_review` | `濃淡;線密度` |
| `D-58` | Whisk | 76 | `visual_review` | `濃淡;線密度` |
| `J-42` | Web3 | 76 | `visual_review` | `濃淡;線密度;余白` |
| `J-79` | SSD | 76 | `visual_review` | `濃淡;線密度;color_review` |
| `J-91` | CLI | 77 | `composition_regen_review` | `濃淡;known_padding_2to1;color_review` |
| `D-57` | Flow | 78 | `visual_review` | `濃淡;線密度` |
| `B-5` | GitHub Copilot | 79 | `visual_review` | `濃淡;color_review;official_asset_color_context` |
| `I-24` | Context7 MCP | 79 | `visual_review` | `濃淡;線密度;color_review` |
| `J-80` | SATA | 80 | `visual_review` | `線密度;color_review` |
| `A-6` | 評価日・時変情報の見方 | 81 | `color_or_full_regen` | `線密度;color_fail` |
| `B-6` | Windsurf | 81 | `visual_review` | `濃淡;color_review;official_asset_color_context` |
| `J-93` | Ubuntu | 81 | `composition_regen_review` | `濃淡;線密度;known_padding_2to1` |
| `B-41` | arXiv | 83 | `official_overlay_color_review` | `濃淡;線密度;color_fail;official_asset_color_context` |
| `G-18` | Chain of Thought | 83 | `visual_review` | `線密度` |
| `J-75` | Tensor コア | 83 | `visual_review` | `線密度;color_review` |
| `G-7` | 指示追従性 | 84 | `visual_review` | `線密度` |
| `G-19` | Prompt Caching | 84 | `visual_review` | `線密度` |
| `J-71` | RAM | 84 | `visual_review` | `線密度` |
| `J-74` | RTX シリーズ | 84 | `visual_review` | `線密度;color_review` |
| `C-51` | Dario Amodei | 85 | `light_review` | `濃淡;線密度` |
| `C-56` | Yann LeCun | 85 | `light_review` | `濃淡;color_review` |

## Mid Band With Structural Reasons

| entry | title | score | action | reasons |
| --- | --- | ---: | --- | --- |
| `J-91` | CLI | 77 | `composition_regen_review` | `濃淡;known_padding_2to1;color_review` |
| `A-6` | 評価日・時変情報の見方 | 81 | `color_or_full_regen` | `線密度;color_fail` |
| `J-93` | Ubuntu | 81 | `composition_regen_review` | `濃淡;線密度;known_padding_2to1` |
| `B-41` | arXiv | 83 | `official_overlay_color_review` | `濃淡;線密度;color_fail;official_asset_color_context` |

## Sparse High-Score Diagram Candidates

These score well mechanically but are likely too thin for branded/service illustrations.

| entry | title | score | file KB | ink | contrast | reasons |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `D-35` | Cursor Composer | 86 | 44.7 | 0.15245 | 10.081 | `線密度;sparse_logo_diagram` |

## Known Mechanical Padding Set

- known padding ids detected in final set: 23 / 23

| entry | title | score | action | central shape |
| --- | --- | ---: | --- | --- |
| `B-2` | Claude | 96 | `composition_regen_review` | `no` |
| `B-3` | ChatGPT | 92 | `composition_regen_review` | `no` |
| `B-4` | Cursor | 96 | `composition_regen_review` | `no` |
| `E-25` | AIME | 95 | `composition_regen_review` | `no` |
| `E-26` | Humanity's Last Exam | 91 | `composition_regen_review` | `no` |
| `E-27` | IQ Bench | 97 | `composition_regen_review` | `no` |
| `E-30` | TAU-Bench | 98 | `composition_regen_review` | `no` |
| `E-50` | Chatbot Arena | 93 | `composition_regen_review` | `no` |
| `H-1` | TDD | 93 | `composition_regen_review` | `no` |
| `H-5` | Scrum / Agile | 94 | `composition_regen_review` | `no` |
| `H-6` | Git Flow | 85 | `composition_regen_review` | `no` |
| `H-7` | CI/CD | 86 | `composition_regen_review` | `no` |
| `H-8` | DevOps | 92 | `composition_regen_review` | `no` |
| `I-2` | MCP Server | 97 | `composition_regen_review` | `no` |
| `I-3` | MCP Client | 93 | `composition_regen_review` | `no` |
| `I-4` | MCP Transport | 92 | `composition_regen_review` | `no` |
| `I-5` | MCP SDK | 95 | `composition_regen_review` | `no` |
| `J-81` | M.2 | 89 | `composition_regen_review` | `no` |
| `J-90` | GUI | 95 | `composition_regen_review` | `no` |
| `J-91` | CLI | 77 | `composition_regen_review` | `no` |
| `J-92` | Linux | 96 | `composition_regen_review` | `no` |
| `J-93` | Ubuntu | 81 | `composition_regen_review` | `no` |
| `J-100` | 識字（リテラシー） | 95 | `composition_regen_review` | `no` |

## Initial Rule Assessment

- Low scores are useful for finding visual outliers, but they should be treated as review priority rather than automatic rejection.
- Known mechanical padding must be an explicit rule because several padded images can still score mid or high on color and density.
- Sparse high-score diagrams must be an explicit rule because clean logo/box/arrow images can look statistically normal while feeling under-produced.
- Mid-band images with padding or color reasons are the important validation set: they test whether the score catches boring or weak 2:1 composition.
- High-band images still need light visual review for semantic mismatch, generated logos, or policy issues that pixel metrics cannot see.
