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

- CSV: `ledgers/semantic_regen_015_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_015/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-015` | 5 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-72` |  | `semantic-regen-015` | 0.009260 | `pass` | `blue:4076;neutral:1774;dark:864;purple:464;orange:41` | `assets/ponchi/experiments/batches/semantic-regen-015/J-72_base_1254x627.png` |
| `J-73` |  | `semantic-regen-015` | 0.008504 | `pass` | `blue:4672;neutral:912;purple:371;dark:293;orange:292` | `assets/ponchi/experiments/batches/semantic-regen-015/J-73_base_1254x627.png` |
| `J-91` |  | `semantic-regen-015` | 0.007330 | `pass` | `blue:4095;dark:1657;purple:11` | `assets/ponchi/experiments/batches/semantic-regen-015/J-91_base_1254x627.png` |
| `J-78` |  | `semantic-regen-015` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-015/J-78_base_1254x627.png` |
| `J-79` |  | `semantic-regen-015` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-015/J-79_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
