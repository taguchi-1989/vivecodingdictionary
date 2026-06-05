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

- CSV: `ledgers/semantic_regen_007_overlay_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_007/overlay_color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-007` | 2 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `B-15` |  | `semantic-regen-007` | 0.005853 | `pass` | `blue:952;red:860;magenta:840;green:588;yellow:403` | `assets/ponchi/experiments/batches/semantic-regen-007/B-15_overlay_1254x627.png` |
| `B-16` |  | `semantic-regen-007` | 0.005853 | `pass` | `blue:952;red:860;magenta:840;green:588;yellow:403` | `assets/ponchi/experiments/batches/semantic-regen-007/B-16_overlay_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
