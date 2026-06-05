# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 5 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_002_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_002/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-002` | 5 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-72` |  | `semantic-regen-002` | 0.007735 | `pass` | `blue:4023;neutral:786;dark:663;purple:342;orange:102` | `assets/ponchi/experiments/batches/semantic-regen-002/J-72_base_1254x627.png` |
| `D-57` |  | `semantic-regen-002` | 0.006448 | `pass` | `blue:2495;neutral:1438;purple:995;dark:94;magenta:15` | `assets/ponchi/experiments/batches/semantic-regen-002/D-57_base_1254x627.png` |
| `D-51` |  | `semantic-regen-002` | 0.005833 | `pass` | `blue:3211;dark:553;neutral:545;purple:215;cyan_teal:47` | `assets/ponchi/experiments/batches/semantic-regen-002/D-51_base_1254x627.png` |
| `F-84` |  | `semantic-regen-002` | 0.000869 | `pass` | `blue:614;dark:36;neutral:28;purple:3;cyan_teal:1` | `assets/ponchi/experiments/batches/semantic-regen-002/F-84_base_1254x627.png` |
| `J-73` |  | `semantic-regen-002` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-002/J-73_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
