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

- CSV: `ledgers/semantic_regen_004_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_004/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-004` | 5 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `A-6` |  | `semantic-regen-004` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-004/A-6_base_1254x627.png` |
| `D-35` |  | `semantic-regen-004` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-004/D-35_base_1254x627.png` |
| `I-10` |  | `semantic-regen-004` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-004/I-10_base_1254x627.png` |
| `J-55` |  | `semantic-regen-004` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-004/J-55_base_1254x627.png` |
| `J-76` |  | `semantic-regen-004` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-004/J-76_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
