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
| `high` | 325 |
| `mid` | 24 |
| `low` | 1 |

## Recommended Actions

| action | count |
| --- | ---: |
| `composition_regen_review` | 23 |
| `full_regen_review` | 1 |
| `light_review` | 290 |
| `official_overlay_color_review` | 10 |
| `sparse_diagram_review` | 4 |
| `visual_review` | 22 |

## Color Gate Counts

| color status | count |
| --- | ---: |
| `pass` | 304 |
| `review` | 36 |
| `fail` | 10 |

## Lowest Scores

| entry | title | score | action | reasons |
| --- | --- | ---: | --- | --- |
| `F-84` | Ghostty | 56 | `full_regen_review` | `色味;明るさ;濃淡;線密度;外れ値` |
| `D-58` | Whisk | 71 | `visual_review` | `濃淡;線密度` |
| `C-59` | Jensen Huang | 72 | `visual_review` | `濃淡;線密度` |
| `D-57` | Flow | 73 | `visual_review` | `濃淡;線密度` |
| `A-3` | 図鑑の歩き方 | 79 | `visual_review` | `濃淡;線密度;余白` |
| `C-51` | Dario Amodei | 80 | `visual_review` | `濃淡;線密度` |
| `C-56` | Yann LeCun | 80 | `visual_review` | `濃淡;線密度;color_review` |
| `D-54` | Stable Diffusion | 80 | `visual_review` | `濃淡;線密度` |
| `B-9` | v0 | 81 | `visual_review` | `濃淡;線密度;color_review;official_asset_color_context` |
| `B-41` | arXiv | 81 | `official_overlay_color_review` | `濃淡;線密度;color_fail;official_asset_color_context` |
| `C-52` | Demis Hassabis | 81 | `visual_review` | `濃淡;color_review` |
| `C-58` | Elon Musk | 81 | `visual_review` | `濃淡;線密度` |
| `C-82` | まさお | 81 | `official_overlay_color_review` | `濃淡;線密度;color_fail;official_asset_color_context` |
| `E-3` | Terminal-Bench | 81 | `visual_review` | `濃淡` |
| `J-42` | Web3 | 81 | `visual_review` | `濃淡;線密度` |
| `A-8` | 色・記号の凡例 | 82 | `visual_review` | `濃淡` |
| `C-10` | Moonshot AI | 82 | `visual_review` | `濃淡` |
| `D-10` | Claude 3 系 | 82 | `visual_review` | `濃淡;線密度` |
| `D-24` | GPT-3 系 | 82 | `visual_review` | `濃淡;線密度` |
| `A-6` | 評価日・時変情報の見方 | 83 | `visual_review` | `濃淡` |
| `C-14` | AMD | 84 | `visual_review` | `濃淡;線密度;color_review;official_asset_color_context` |
| `C-81` | にゃんた | 84 | `visual_review` | `濃淡;線密度` |
| `D-50` | DALL-E | 84 | `visual_review` | `濃淡;線密度` |
| `F-82` | WSL | 84 | `visual_review` | `濃淡` |
| `J-50` | AI 倫理 | 84 | `visual_review` | `濃淡` |

## Mid Band With Structural Reasons

| entry | title | score | action | reasons |
| --- | --- | ---: | --- | --- |
| `B-41` | arXiv | 81 | `official_overlay_color_review` | `濃淡;線密度;color_fail;official_asset_color_context` |
| `C-82` | まさお | 81 | `official_overlay_color_review` | `濃淡;線密度;color_fail;official_asset_color_context` |

## Sparse High-Score Diagram Candidates

These score well mechanically but are likely too thin for branded/service illustrations.

| entry | title | score | file KB | ink | contrast | reasons |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `B-6` | Windsurf | 93 | 24.1 | 0.11176 | 10.250 | `sparse_logo_diagram` |
| `B-4` | Cursor | 95 | 30.5 | 0.12977 | 11.794 | `known_padding_2to1;sparse_logo_diagram` |
| `B-1` | Gemini | 97 | 30.8 | 0.15343 | 11.471 | `color_fail;official_asset_color_context;sparse_logo_diagram` |
| `B-7` | Claude Code | 95 | 31.6 | 0.14572 | 11.378 | `color_review;official_asset_color_context;sparse_logo_diagram` |
| `B-5` | GitHub Copilot | 96 | 32.5 | 0.15104 | 12.070 | `color_review;official_asset_color_context;sparse_logo_diagram` |
| `B-2` | Claude | 95 | 34.5 | 0.15951 | 12.050 | `known_padding_2to1;color_review;official_asset_color_context;sparse_logo_diagram` |
| `D-35` | Cursor Composer | 91 | 44.7 | 0.15245 | 10.081 | `sparse_logo_diagram` |

## Known Mechanical Padding Set

- known padding ids detected in final set: 23 / 23

| entry | title | score | action | central shape |
| --- | --- | ---: | --- | --- |
| `B-2` | Claude | 95 | `composition_regen_review` | `no` |
| `B-3` | ChatGPT | 87 | `composition_regen_review` | `no` |
| `B-4` | Cursor | 95 | `composition_regen_review` | `no` |
| `E-25` | AIME | 96 | `composition_regen_review` | `no` |
| `E-26` | Humanity's Last Exam | 86 | `composition_regen_review` | `no` |
| `E-27` | IQ Bench | 96 | `composition_regen_review` | `no` |
| `E-30` | TAU-Bench | 95 | `composition_regen_review` | `no` |
| `E-50` | Chatbot Arena | 94 | `composition_regen_review` | `no` |
| `H-1` | TDD | 95 | `composition_regen_review` | `no` |
| `H-5` | Scrum / Agile | 90 | `composition_regen_review` | `no` |
| `H-6` | Git Flow | 89 | `composition_regen_review` | `no` |
| `H-7` | CI/CD | 91 | `composition_regen_review` | `no` |
| `H-8` | DevOps | 97 | `composition_regen_review` | `no` |
| `I-2` | MCP Server | 92 | `composition_regen_review` | `no` |
| `I-3` | MCP Client | 97 | `composition_regen_review` | `no` |
| `I-4` | MCP Transport | 90 | `composition_regen_review` | `no` |
| `I-5` | MCP SDK | 94 | `composition_regen_review` | `no` |
| `J-81` | M.2 | 91 | `composition_regen_review` | `no` |
| `J-90` | GUI | 94 | `composition_regen_review` | `no` |
| `J-91` | CLI | 95 | `composition_regen_review` | `no` |
| `J-92` | Linux | 95 | `composition_regen_review` | `no` |
| `J-93` | Ubuntu | 87 | `composition_regen_review` | `no` |
| `J-100` | 識字（リテラシー） | 89 | `composition_regen_review` | `no` |

## Initial Rule Assessment

- Low scores are useful for finding visual outliers, but they should be treated as review priority rather than automatic rejection.
- Known mechanical padding must be an explicit rule because several padded images can still score mid or high on color and density.
- Sparse high-score diagrams must be an explicit rule because clean logo/box/arrow images can look statistically normal while feeling under-produced.
- Mid-band images with padding or color reasons are the important validation set: they test whether the score catches boring or weak 2:1 composition.
- High-band images still need light visual review for semantic mismatch, generated logos, or policy issues that pixel metrics cannot see.
