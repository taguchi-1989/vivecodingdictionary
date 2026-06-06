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

- CSV: `ledgers/semantic_regen_016_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_016/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-016` | 8 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-70` |  | `semantic-regen-016` | 0.009195 | `pass` | `blue:5177;dark:1968;neutral:76;orange:5;cyan_teal:2` | `assets/ponchi/experiments/batches/semantic-regen-016/J-70_base_1254x627.png` |
| `J-77` |  | `semantic-regen-016` | 0.008956 | `pass` | `blue:6611;dark:339;neutral:74;purple:12;orange:3` | `assets/ponchi/experiments/batches/semantic-regen-016/J-77_base_1254x627.png` |
| `J-75` |  | `semantic-regen-016` | 0.008312 | `pass` | `blue:5607;dark:554;neutral:264;cyan_teal:87;purple:19` | `assets/ponchi/experiments/batches/semantic-regen-016/J-75_base_1254x627.png` |
| `J-74` |  | `semantic-regen-016` | 0.007509 | `pass` | `blue:3120;dark:2247;neutral:435;purple:102` | `assets/ponchi/experiments/batches/semantic-regen-016/J-74_base_1254x627.png` |
| `J-71` |  | `semantic-regen-016` | 0.006465 | `pass` | `blue:3649;dark:1300;neutral:86;purple:30;orange:12` | `assets/ponchi/experiments/batches/semantic-regen-016/J-71_base_1254x627.png` |
| `J-76` |  | `semantic-regen-016` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-016/J-76_base_1254x627.png` |
| `J-80` |  | `semantic-regen-016` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-016/J-80_base_1254x627.png` |
| `J-81` |  | `semantic-regen-016` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-016/J-81_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
