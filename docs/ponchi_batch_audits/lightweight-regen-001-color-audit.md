# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 7 |
| `review` | 12 |
| `fail` | 1 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/lightweight_regen_001_color_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/lightweight-regen-001-color-contact-sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `lightweight-regen-001` | 7 | 12 | 1 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-80` |  | `lightweight-regen-001` | 0.020004 | `fail` | `blue:13604;dark:1425;neutral:619;purple:40;orange:21` | `assets/ponchi/experiments/batches/lightweight-regen-001/J-80_base_1254x627.png` |
| `I-21` |  | `lightweight-regen-001` | 0.016834 | `review` | `blue:12011;dark:942;neutral:136;orange:93;purple:28` | `assets/ponchi/experiments/batches/lightweight-regen-001/I-21_base_1254x627.png` |
| `B-2` |  | `lightweight-regen-001` | 0.016525 | `review` | `blue:11621;dark:865;neutral:258;purple:195;orange:44` | `assets/ponchi/experiments/batches/lightweight-regen-001/B-2_base_1254x627.png` |
| `B-3` |  | `lightweight-regen-001` | 0.015580 | `review` | `blue:10816;dark:680;neutral:656;orange:54;purple:19` | `assets/ponchi/experiments/batches/lightweight-regen-001/B-3_base_1254x627.png` |
| `J-90` |  | `lightweight-regen-001` | 0.015569 | `review` | `blue:10827;dark:1139;neutral:176;purple:58;orange:29` | `assets/ponchi/experiments/batches/lightweight-regen-001/J-90_base_1254x627.png` |
| `J-91` |  | `lightweight-regen-001` | 0.013969 | `review` | `blue:9689;dark:983;neutral:182;orange:51;purple:37` | `assets/ponchi/experiments/batches/lightweight-regen-001/J-91_base_1254x627.png` |
| `B-5` |  | `lightweight-regen-001` | 0.012855 | `review` | `blue:8709;dark:996;neutral:248;purple:72;orange:50` | `assets/ponchi/experiments/batches/lightweight-regen-001/B-5_base_1254x627.png` |
| `B-4` |  | `lightweight-regen-001` | 0.012598 | `review` | `blue:7433;neutral:1263;dark:1095;purple:76;orange:27` | `assets/ponchi/experiments/batches/lightweight-regen-001/B-4_base_1254x627.png` |
| `I-2` |  | `lightweight-regen-001` | 0.012057 | `review` | `blue:8116;dark:757;neutral:407;purple:93;orange:80` | `assets/ponchi/experiments/batches/lightweight-regen-001/I-2_base_1254x627.png` |
| `J-4` |  | `lightweight-regen-001` | 0.011994 | `review` | `blue:8582;dark:355;neutral:312;purple:91;orange:57` | `assets/ponchi/experiments/batches/lightweight-regen-001/J-4_base_1254x627.png` |
| `I-5` |  | `lightweight-regen-001` | 0.011545 | `review` | `blue:7608;dark:1095;neutral:247;purple:72;orange:43` | `assets/ponchi/experiments/batches/lightweight-regen-001/I-5_base_1254x627.png` |
| `B-6` |  | `lightweight-regen-001` | 0.011055 | `review` | `blue:6849;dark:1409;neutral:365;purple:50;orange:15` | `assets/ponchi/experiments/batches/lightweight-regen-001/B-6_base_1254x627.png` |
| `I-3` |  | `lightweight-regen-001` | 0.010163 | `review` | `blue:6659;dark:1008;neutral:179;purple:76;orange:35` | `assets/ponchi/experiments/batches/lightweight-regen-001/I-3_base_1254x627.png` |
| `J-19` |  | `lightweight-regen-001` | 0.009711 | `pass` | `blue:6041;dark:805;neutral:652;purple:74;orange:38` | `assets/ponchi/experiments/batches/lightweight-regen-001/J-19_base_1254x627.png` |
| `J-100` |  | `lightweight-regen-001` | 0.007821 | `pass` | `blue:4765;dark:1138;neutral:147;orange:31;cyan_teal:30` | `assets/ponchi/experiments/batches/lightweight-regen-001/J-100_base_1254x627.png` |
| `J-81` |  | `lightweight-regen-001` | 0.007788 | `pass` | `blue:3318;dark:2731;neutral:72;purple:1;orange:1` | `assets/ponchi/experiments/batches/lightweight-regen-001/J-81_base_1254x627.png` |
| `J-92` |  | `lightweight-regen-001` | 0.007027 | `pass` | `blue:4523;dark:836;neutral:115;orange:25;purple:13` | `assets/ponchi/experiments/batches/lightweight-regen-001/J-92_base_1254x627.png` |
| `I-4` |  | `lightweight-regen-001` | 0.006929 | `pass` | `blue:4903;dark:283;neutral:183;purple:40;orange:32` | `assets/ponchi/experiments/batches/lightweight-regen-001/I-4_base_1254x627.png` |
| `J-93` |  | `lightweight-regen-001` | 0.006125 | `pass` | `blue:2620;dark:1843;neutral:238;purple:53;orange:52` | `assets/ponchi/experiments/batches/lightweight-regen-001/J-93_base_1254x627.png` |
| `B-7` |  | `lightweight-regen-001` | 0.005854 | `pass` | `dark:1811;blue:1435;neutral:1235;cyan_teal:94;orange:14` | `assets/ponchi/experiments/batches/lightweight-regen-001/B-7_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
