# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 3 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_024_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_024/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-024` | 3 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-90` |  | `semantic-regen-024` | 0.009136 | `pass` | `blue:5426;dark:1080;purple:351;neutral:311;cyan_teal:6` | `assets/ponchi/experiments/batches/semantic-regen-024/J-90_base_1254x627.png` |
| `J-93` |  | `semantic-regen-024` | 0.006349 | `pass` | `blue:4054;dark:614;neutral:239;purple:37;orange:32` | `assets/ponchi/experiments/batches/semantic-regen-024/J-93_base_1254x627.png` |
| `J-92` |  | `semantic-regen-024` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-024/J-92_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
