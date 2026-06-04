# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 2 |
| `review` | 12 |
| `fail` | 6 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/lightweight_regen_002_color_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/lightweight-regen-002-color-contact-sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `lightweight-regen-002` | 2 | 12 | 6 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `I-10` |  | `lightweight-regen-002` | 0.030159 | `fail` | `blue:18747;neutral:3487;dark:1196;purple:208;orange:46` | `assets/ponchi/experiments/batches/lightweight-regen-002/I-10_base_1254x627.png` |
| `J-73` |  | `lightweight-regen-002` | 0.029011 | `fail` | `blue:19219;neutral:2208;dark:1100;purple:254;red:11` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-73_base_1254x627.png` |
| `J-72` |  | `lightweight-regen-002` | 0.022350 | `fail` | `blue:14515;neutral:1997;dark:754;purple:269;orange:13` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-72_base_1254x627.png` |
| `J-32` |  | `lightweight-regen-002` | 0.022064 | `fail` | `blue:16044;dark:654;neutral:500;purple:136;orange:10` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-32_base_1254x627.png` |
| `I-22` |  | `lightweight-regen-002` | 0.020562 | `fail` | `blue:11869;neutral:3713;dark:236;purple:191;orange:104` | `assets/ponchi/experiments/batches/lightweight-regen-002/I-22_base_1254x627.png` |
| `J-52` |  | `lightweight-regen-002` | 0.020542 | `fail` | `blue:14817;dark:968;neutral:172;purple:117;orange:56` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-52_base_1254x627.png` |
| `A-1` |  | `lightweight-regen-002` | 0.018429 | `review` | `blue:12876;neutral:1011;purple:298;dark:280;magenta:10` | `assets/ponchi/experiments/batches/lightweight-regen-002/A-1_base_1254x627.png` |
| `I-24` |  | `lightweight-regen-002` | 0.017882 | `review` | `blue:11824;dark:1101;neutral:811;purple:248;orange:43` | `assets/ponchi/experiments/batches/lightweight-regen-002/I-24_base_1254x627.png` |
| `I-80` |  | `lightweight-regen-002` | 0.016552 | `review` | `blue:10122;neutral:2460;purple:244;dark:142;orange:25` | `assets/ponchi/experiments/batches/lightweight-regen-002/I-80_base_1254x627.png` |
| `J-41` |  | `lightweight-regen-002` | 0.016309 | `review` | `blue:12090;neutral:359;dark:238;purple:82;orange:33` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-41_base_1254x627.png` |
| `J-56` |  | `lightweight-regen-002` | 0.015950 | `review` | `blue:11288;neutral:882;dark:290;purple:70;orange:6` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-56_base_1254x627.png` |
| `J-70` |  | `lightweight-regen-002` | 0.015946 | `review` | `blue:11239;dark:695;neutral:511;purple:70;orange:10` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-70_base_1254x627.png` |
| `J-2` |  | `lightweight-regen-002` | 0.015809 | `review` | `blue:11319;dark:499;neutral:436;purple:119;orange:32` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-2_base_1254x627.png` |
| `J-1` |  | `lightweight-regen-002` | 0.013203 | `review` | `blue:8774;dark:724;neutral:600;purple:200;orange:58` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-1_base_1254x627.png` |
| `J-16` |  | `lightweight-regen-002` | 0.012732 | `review` | `blue:8626;purple:712;neutral:425;dark:225;orange:9` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-16_base_1254x627.png` |
| `J-50` |  | `lightweight-regen-002` | 0.011269 | `review` | `blue:7695;dark:776;neutral:280;purple:84;orange:12` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-50_base_1254x627.png` |
| `J-21` |  | `lightweight-regen-002` | 0.010901 | `review` | `blue:7398;dark:867;neutral:197;purple:70;orange:24` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-21_base_1254x627.png` |
| `A-7` |  | `lightweight-regen-002` | 0.010624 | `review` | `blue:5944;dark:1785;neutral:493;purple:79;orange:39` | `assets/ponchi/experiments/batches/lightweight-regen-002/A-7_base_1254x627.png` |
| `J-22` |  | `lightweight-regen-002` | 0.009689 | `pass` | `blue:6634;neutral:498;dark:325;purple:105;orange:40` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-22_base_1254x627.png` |
| `J-62` |  | `lightweight-regen-002` | 0.009159 | `pass` | `blue:5724;dark:1191;neutral:143;purple:133;orange:4` | `assets/ponchi/experiments/batches/lightweight-regen-002/J-62_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
