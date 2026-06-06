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

- CSV: `ledgers/semantic_regen_011_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_011/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-011` | 2 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `A-9` |  | `semantic-regen-011` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-011/A-9_base_1254x627.png` |
| `A-11` |  | `semantic-regen-011` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-011/A-11_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
