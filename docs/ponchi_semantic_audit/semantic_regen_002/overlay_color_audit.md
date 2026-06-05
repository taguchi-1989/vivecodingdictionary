# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 2 |
| `review` | 1 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_002_overlay_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_002/overlay_color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-002` | 2 | 1 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `D-51` |  | `semantic-regen-002` | 0.016127 | `review` | `blue:11305;dark:553;neutral:545;purple:215;cyan_teal:47` | `assets/ponchi/experiments/batches/semantic-regen-002/D-51_overlay_1254x627.png` |
| `D-57` |  | `semantic-regen-002` | 0.008280 | `pass` | `blue:3830;neutral:1672;purple:552;dark:443;cyan_teal:12` | `assets/ponchi/experiments/batches/semantic-regen-002/D-57_overlay_1254x627.png` |
| `F-84` |  | `semantic-regen-002` | 0.001148 | `pass` | `blue:799;dark:71;neutral:28;purple:3;cyan_teal:1` | `assets/ponchi/experiments/batches/semantic-regen-002/F-84_overlay_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
