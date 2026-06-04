# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 1 |
| `review` | 17 |
| `fail` | 2 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/lightweight_regen_004_color_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/lightweight-regen-004-color-contact-sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `lightweight-regen-004` | 1 | 17 | 2 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-13` |  | `lightweight-regen-004` | 0.021904 | `fail` | `blue:14169;purple:1720;neutral:970;dark:334;magenta:12` | `assets/ponchi/experiments/batches/lightweight-regen-004/J-13_base_1254x627.png` |
| `A-10` |  | `lightweight-regen-004` | 0.021094 | `fail` | `blue:12162;neutral:3577;dark:630;purple:211;magenta:3` | `assets/ponchi/experiments/batches/lightweight-regen-004/A-10_base_1254x627.png` |
| `J-33` |  | `lightweight-regen-004` | 0.019948 | `review` | `blue:13102;neutral:1253;dark:1029;purple:159;orange:93` | `assets/ponchi/experiments/batches/lightweight-regen-004/J-33_base_1254x627.png` |
| `I-81` |  | `lightweight-regen-004` | 0.019851 | `review` | `blue:13282;neutral:1271;dark:792;purple:163;orange:58` | `assets/ponchi/experiments/batches/lightweight-regen-004/I-81_base_1254x627.png` |
| `J-10` |  | `lightweight-regen-004` | 0.018414 | `review` | `blue:13345;dark:580;neutral:285;purple:170;orange:67` | `assets/ponchi/experiments/batches/lightweight-regen-004/J-10_base_1254x627.png` |
| `J-53` |  | `lightweight-regen-004` | 0.017934 | `review` | `blue:12540;neutral:859;dark:405;purple:224;orange:40` | `assets/ponchi/experiments/batches/lightweight-regen-004/J-53_base_1254x627.png` |
| `I-41` |  | `lightweight-regen-004` | 0.016650 | `review` | `blue:11290;dark:1052;neutral:425;purple:278;orange:24` | `assets/ponchi/experiments/batches/lightweight-regen-004/I-41_base_1254x627.png` |
| `I-11` |  | `lightweight-regen-004` | 0.016442 | `review` | `blue:11837;neutral:527;purple:262;dark:249;orange:24` | `assets/ponchi/experiments/batches/lightweight-regen-004/I-11_base_1254x627.png` |
| `I-23` |  | `lightweight-regen-004` | 0.016224 | `review` | `blue:10760;neutral:1294;dark:448;purple:202;orange:31` | `assets/ponchi/experiments/batches/lightweight-regen-004/I-23_base_1254x627.png` |
| `J-54` |  | `lightweight-regen-004` | 0.016103 | `review` | `blue:10754;dark:1233;neutral:455;purple:103;orange:82` | `assets/ponchi/experiments/batches/lightweight-regen-004/J-54_base_1254x627.png` |
| `H-50` |  | `lightweight-regen-004` | 0.016030 | `review` | `blue:11514;dark:513;neutral:442;purple:125;orange:5` | `assets/ponchi/experiments/batches/lightweight-regen-004/H-50_base_1254x627.png` |
| `I-13` |  | `lightweight-regen-004` | 0.015588 | `review` | `blue:10533;neutral:1062;dark:283;purple:207;orange:114` | `assets/ponchi/experiments/batches/lightweight-regen-004/I-13_base_1254x627.png` |
| `A-4` |  | `lightweight-regen-004` | 0.014522 | `review` | `blue:10303;dark:444;neutral:389;purple:223;orange:33` | `assets/ponchi/experiments/batches/lightweight-regen-004/A-4_base_1254x627.png` |
| `J-15` |  | `lightweight-regen-004` | 0.014391 | `review` | `blue:10450;neutral:352;dark:297;purple:208;orange:3` | `assets/ponchi/experiments/batches/lightweight-regen-004/J-15_base_1254x627.png` |
| `I-50` |  | `lightweight-regen-004` | 0.013316 | `review` | `blue:8967;neutral:654;dark:431;purple:300;orange:59` | `assets/ponchi/experiments/batches/lightweight-regen-004/I-50_base_1254x627.png` |
| `J-3` |  | `lightweight-regen-004` | 0.013114 | `review` | `blue:9308;neutral:383;dark:259;purple:199;cyan_teal:57` | `assets/ponchi/experiments/batches/lightweight-regen-004/J-3_base_1254x627.png` |
| `B-1` |  | `lightweight-regen-004` | 0.011789 | `review` | `blue:8207;dark:480;neutral:293;purple:182;orange:63` | `assets/ponchi/experiments/batches/lightweight-regen-004/B-1_base_1254x627.png` |
| `B-9` |  | `lightweight-regen-004` | 0.011690 | `review` | `blue:6349;neutral:2583;dark:138;purple:100;orange:8` | `assets/ponchi/experiments/batches/lightweight-regen-004/B-9_base_1254x627.png` |
| `A-2` |  | `lightweight-regen-004` | 0.011017 | `review` | `blue:8032;dark:320;neutral:201;purple:83;orange:18` | `assets/ponchi/experiments/batches/lightweight-regen-004/A-2_base_1254x627.png` |
| `H-63` |  | `lightweight-regen-004` | 0.006486 | `pass` | `blue:4753;neutral:209;dark:122;purple:14;cyan_teal:2` | `assets/ponchi/experiments/batches/lightweight-regen-004/H-63_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
