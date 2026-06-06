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

- CSV: `ledgers/semantic_regen_022_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_022/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-022` | 8 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-33` |  | `semantic-regen-022` | 0.008930 | `pass` | `blue:3533;dark:3054;neutral:256;purple:110;orange:37` | `assets/ponchi/experiments/batches/semantic-regen-022/J-33_base_1254x627.png` |
| `J-31` |  | `semantic-regen-022` | 0.007000 | `pass` | `dark:2471;blue:2399;neutral:376;purple:133;orange:101` | `assets/ponchi/experiments/batches/semantic-regen-022/J-31_base_1254x627.png` |
| `J-43` |  | `semantic-regen-022` | 0.006770 | `pass` | `blue:3845;dark:1262;neutral:135;orange:28;purple:27` | `assets/ponchi/experiments/batches/semantic-regen-022/J-43_base_1254x627.png` |
| `J-32` |  | `semantic-regen-022` | 0.006746 | `pass` | `blue:3218;dark:1912;neutral:97;orange:61;yellow:13` | `assets/ponchi/experiments/batches/semantic-regen-022/J-32_base_1254x627.png` |
| `J-42` |  | `semantic-regen-022` | 0.005959 | `pass` | `blue:3106;dark:1079;neutral:239;purple:219;orange:22` | `assets/ponchi/experiments/batches/semantic-regen-022/J-42_base_1254x627.png` |
| `J-40` |  | `semantic-regen-022` | 0.005643 | `pass` | `blue:3266;dark:818;neutral:242;orange:62;purple:19` | `assets/ponchi/experiments/batches/semantic-regen-022/J-40_base_1254x627.png` |
| `J-100` |  | `semantic-regen-022` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-022/J-100_base_1254x627.png` |
| `J-41` |  | `semantic-regen-022` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-022/J-41_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
