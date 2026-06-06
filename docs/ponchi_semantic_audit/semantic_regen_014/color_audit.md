# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 4 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_014_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_014/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-014` | 4 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-52` |  | `semantic-regen-014` | 0.006994 | `pass` | `blue:5041;dark:353;neutral:91;purple:14` | `assets/ponchi/experiments/batches/semantic-regen-014/J-52_base_1254x627.png` |
| `J-53` |  | `semantic-regen-014` | 0.002425 | `pass` | `blue:1782;dark:108;purple:11;neutral:6` | `assets/ponchi/experiments/batches/semantic-regen-014/J-53_base_1254x627.png` |
| `J-50` |  | `semantic-regen-014` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-014/J-50_base_1254x627.png` |
| `J-54` |  | `semantic-regen-014` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-014/J-54_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
