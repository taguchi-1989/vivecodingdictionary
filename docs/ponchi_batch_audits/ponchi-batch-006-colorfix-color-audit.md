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

- CSV: `ledgers/ponchi_batch_006_colorfix_color_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-006-colorfix-color-contact-sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `ponchi-batch-006` | 2 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `D-51` |  | `ponchi-batch-006` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-006/D-51_base_1254x627.png` |
| `D-60` |  | `ponchi-batch-006` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/ponchi-batch-006/D-60_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
