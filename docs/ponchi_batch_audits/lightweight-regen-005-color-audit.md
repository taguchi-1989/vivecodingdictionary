# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 3 |
| `review` | 7 |
| `fail` | 2 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/lightweight_regen_005_color_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/lightweight-regen-005-color-contact-sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `lightweight-regen-005` | 3 | 7 | 2 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-14` |  | `lightweight-regen-005` | 0.023093 | `fail` | `blue:15813;neutral:1548;dark:434;purple:264;orange:59` | `assets/ponchi/experiments/batches/lightweight-regen-005/J-14_base_1254x627.png` |
| `J-17` |  | `lightweight-regen-005` | 0.020842 | `fail` | `blue:12224;neutral:3344;dark:536;purple:260;orange:10` | `assets/ponchi/experiments/batches/lightweight-regen-005/J-17_base_1254x627.png` |
| `B-28` |  | `lightweight-regen-005` | 0.019530 | `review` | `blue:14028;neutral:621;purple:260;dark:175;orange:173` | `assets/ponchi/experiments/batches/lightweight-regen-005/B-28_base_1254x627.png` |
| `J-11` |  | `lightweight-regen-005` | 0.016160 | `review` | `blue:10846;neutral:1283;dark:410;purple:148;orange:15` | `assets/ponchi/experiments/batches/lightweight-regen-005/J-11_base_1254x627.png` |
| `J-78` |  | `lightweight-regen-005` | 0.014335 | `review` | `blue:6514;dark:2741;neutral:1718;orange:140;purple:117` | `assets/ponchi/experiments/batches/lightweight-regen-005/J-78_base_1254x627.png` |
| `D-60` |  | `lightweight-regen-005` | 0.011977 | `review` | `blue:7711;dark:1274;neutral:312;purple:76;orange:27` | `assets/ponchi/experiments/batches/lightweight-regen-005/D-60_base_1254x627.png` |
| `A-9` |  | `lightweight-regen-005` | 0.011159 | `review` | `blue:6816;neutral:1731;purple:126;dark:84;cyan_teal:6` | `assets/ponchi/experiments/batches/lightweight-regen-005/A-9_base_1254x627.png` |
| `D-51` |  | `lightweight-regen-005` | 0.010481 | `review` | `blue:7512;dark:310;neutral:287;purple:97;orange:21` | `assets/ponchi/experiments/batches/lightweight-regen-005/D-51_base_1254x627.png` |
| `B-8` |  | `lightweight-regen-005` | 0.010195 | `review` | `blue:6537;neutral:752;dark:444;purple:215;orange:32` | `assets/ponchi/experiments/batches/lightweight-regen-005/B-8_base_1254x627.png` |
| `J-40` |  | `lightweight-regen-005` | 0.009877 | `pass` | `blue:6696;dark:518;neutral:358;purple:96;orange:61` | `assets/ponchi/experiments/batches/lightweight-regen-005/J-40_base_1254x627.png` |
| `J-43` |  | `lightweight-regen-005` | 0.009801 | `pass` | `blue:6457;dark:556;neutral:512;purple:152;orange:15` | `assets/ponchi/experiments/batches/lightweight-regen-005/J-43_base_1254x627.png` |
| `J-20` |  | `lightweight-regen-005` | 0.009405 | `pass` | `blue:6120;neutral:759;dark:342;orange:69;purple:68` | `assets/ponchi/experiments/batches/lightweight-regen-005/J-20_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
