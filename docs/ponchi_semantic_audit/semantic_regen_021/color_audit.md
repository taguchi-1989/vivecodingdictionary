# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 8 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_021_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_021/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-021` | 8 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-20` |  | `semantic-regen-021` | 0.008961 | `pass` | `blue:4876;dark:1429;neutral:426;orange:150;purple:105` | `assets/ponchi/experiments/batches/semantic-regen-021/J-20_base_1254x627.png` |
| `J-23` |  | `semantic-regen-021` | 0.008640 | `pass` | `blue:4766;dark:1278;neutral:576;purple:158;orange:10` | `assets/ponchi/experiments/batches/semantic-regen-021/J-23_base_1254x627.png` |
| `J-18` |  | `semantic-regen-021` | 0.006860 | `pass` | `blue:5057;dark:216;neutral:63;orange:28;purple:19` | `assets/ponchi/experiments/batches/semantic-regen-021/J-18_base_1254x627.png` |
| `J-16` |  | `semantic-regen-021` | 0.006823 | `pass` | `blue:4068;dark:677;neutral:312;orange:104;purple:65` | `assets/ponchi/experiments/batches/semantic-regen-021/J-16_base_1254x627.png` |
| `J-21` |  | `semantic-regen-021` | 0.004995 | `pass` | `blue:3043;dark:708;neutral:112;purple:26;orange:22` | `assets/ponchi/experiments/batches/semantic-regen-021/J-21_base_1254x627.png` |
| `J-17` |  | `semantic-regen-021` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-021/J-17_base_1254x627.png` |
| `J-19` |  | `semantic-regen-021` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-021/J-19_base_1254x627.png` |
| `J-22` |  | `semantic-regen-021` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-021/J-22_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
