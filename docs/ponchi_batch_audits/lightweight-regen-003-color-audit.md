# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 0 |
| `review` | 16 |
| `fail` | 4 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/lightweight_regen_003_color_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/lightweight-regen-003-color-contact-sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `lightweight-regen-003` | 0 | 16 | 4 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `A-6` |  | `lightweight-regen-003` | 0.035206 | `fail` | `blue:24793;neutral:1734;dark:840;purple:140;orange:132` | `assets/ponchi/experiments/batches/lightweight-regen-003/A-6_base_1254x627.png` |
| `J-76` |  | `lightweight-regen-003` | 0.026405 | `fail` | `blue:18238;purple:1004;neutral:953;dark:349;orange:156` | `assets/ponchi/experiments/batches/lightweight-regen-003/J-76_base_1254x627.png` |
| `J-55` |  | `lightweight-regen-003` | 0.025932 | `fail` | `blue:18973;neutral:604;dark:357;purple:337;orange:60` | `assets/ponchi/experiments/batches/lightweight-regen-003/J-55_base_1254x627.png` |
| `J-31` |  | `lightweight-regen-003` | 0.025466 | `fail` | `blue:17426;neutral:1971;purple:310;dark:278;orange:18` | `assets/ponchi/experiments/batches/lightweight-regen-003/J-31_base_1254x627.png` |
| `I-1` |  | `lightweight-regen-003` | 0.018170 | `review` | `blue:12854;dark:671;neutral:368;purple:169;orange:159` | `assets/ponchi/experiments/batches/lightweight-regen-003/I-1_base_1254x627.png` |
| `I-30` |  | `lightweight-regen-003` | 0.017915 | `review` | `blue:12724;neutral:965;dark:275;purple:59;orange:31` | `assets/ponchi/experiments/batches/lightweight-regen-003/I-30_base_1254x627.png` |
| `I-20` |  | `lightweight-regen-003` | 0.017255 | `review` | `blue:12488;neutral:544;dark:344;purple:113;orange:52` | `assets/ponchi/experiments/batches/lightweight-regen-003/I-20_base_1254x627.png` |
| `A-3` |  | `lightweight-regen-003` | 0.016198 | `review` | `blue:10609;dark:941;neutral:740;purple:331;orange:50` | `assets/ponchi/experiments/batches/lightweight-regen-003/A-3_base_1254x627.png` |
| `J-79` |  | `lightweight-regen-003` | 0.015893 | `review` | `blue:10349;dark:1140;neutral:486;purple:329;orange:114` | `assets/ponchi/experiments/batches/lightweight-regen-003/J-79_base_1254x627.png` |
| `I-12` |  | `lightweight-regen-003` | 0.015322 | `review` | `blue:10874;neutral:537;dark:289;purple:218;orange:74` | `assets/ponchi/experiments/batches/lightweight-regen-003/I-12_base_1254x627.png` |
| `J-75` |  | `lightweight-regen-003` | 0.014998 | `review` | `blue:10784;dark:628;neutral:316;purple:62;red:2` | `assets/ponchi/experiments/batches/lightweight-regen-003/J-75_base_1254x627.png` |
| `A-8` |  | `lightweight-regen-003` | 0.014555 | `review` | `blue:10061;dark:859;neutral:274;purple:226;orange:8` | `assets/ponchi/experiments/batches/lightweight-regen-003/A-8_base_1254x627.png` |
| `J-77` |  | `lightweight-regen-003` | 0.014502 | `review` | `blue:10517;neutral:413;dark:373;purple:88;orange:5` | `assets/ponchi/experiments/batches/lightweight-regen-003/J-77_base_1254x627.png` |
| `J-74` |  | `lightweight-regen-003` | 0.014013 | `review` | `blue:8367;dark:1554;orange:439;neutral:428;purple:128` | `assets/ponchi/experiments/batches/lightweight-regen-003/J-74_base_1254x627.png` |
| `J-51` |  | `lightweight-regen-003` | 0.013702 | `review` | `blue:9899;dark:401;neutral:318;purple:87;orange:47` | `assets/ponchi/experiments/batches/lightweight-regen-003/J-51_base_1254x627.png` |
| `H-62` |  | `lightweight-regen-003` | 0.013613 | `review` | `blue:9569;dark:582;neutral:318;purple:115;orange:67` | `assets/ponchi/experiments/batches/lightweight-regen-003/H-62_base_1254x627.png` |
| `J-18` |  | `lightweight-regen-003` | 0.012880 | `review` | `blue:9441;neutral:413;purple:129;dark:123;orange:9` | `assets/ponchi/experiments/batches/lightweight-regen-003/J-18_base_1254x627.png` |
| `A-5` |  | `lightweight-regen-003` | 0.012716 | `review` | `blue:9044;dark:364;neutral:346;purple:180;orange:33` | `assets/ponchi/experiments/batches/lightweight-regen-003/A-5_base_1254x627.png` |
| `J-71` |  | `lightweight-regen-003` | 0.012216 | `review` | `blue:7927;dark:1103;neutral:425;purple:102;orange:40` | `assets/ponchi/experiments/batches/lightweight-regen-003/J-71_base_1254x627.png` |
| `A-11` |  | `lightweight-regen-003` | 0.011135 | `review` | `blue:7860;dark:488;neutral:322;purple:70;orange:8` | `assets/ponchi/experiments/batches/lightweight-regen-003/A-11_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
