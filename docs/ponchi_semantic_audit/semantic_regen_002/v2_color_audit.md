# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 2 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_002_v2_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_002/v2_color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-002` | 2 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-72_v2` |  | `semantic-regen-002` | 0.007735 | `pass` | `blue:4023;neutral:786;dark:663;purple:342;orange:102` | `assets/ponchi/experiments/batches/semantic-regen-002/J-72_v2_base_1254x627.png` |
| `D-57_v2` |  | `semantic-regen-002` | 0.006448 | `pass` | `blue:2495;neutral:1438;purple:995;dark:94;magenta:15` | `assets/ponchi/experiments/batches/semantic-regen-002/D-57_v2_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
