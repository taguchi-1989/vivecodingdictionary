# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 9 |
| `review` | 13 |
| `fail` | 3 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/ui_os_storage_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/ui_os_storage_2026-06-06/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `final` | 9 | 13 | 3 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-73` |  | `final` | 0.027321 | `fail` | `blue:16323;neutral:3626;dark:1302;purple:208;cyan_teal:22` | `assets/ponchi/final/J-73.webp` |
| `J-76` |  | `final` | 0.024311 | `fail` | `blue:16813;neutral:1552;purple:471;dark:247;cyan_teal:28` | `assets/ponchi/final/J-76.webp` |
| `J-72` |  | `final` | 0.020608 | `fail` | `blue:11960;neutral:2913;dark:1046;purple:227;cyan_teal:42` | `assets/ponchi/final/J-72.webp` |
| `J-33` |  | `final` | 0.018460 | `review` | `blue:11796;neutral:2151;dark:459;purple:79;cyan_teal:28` | `assets/ponchi/final/J-33.webp` |
| `J-80` |  | `final` | 0.018008 | `review` | `blue:11418;dark:1751;neutral:944;cyan_teal:24;purple:22` | `assets/ponchi/final/J-80.webp` |
| `J-32` |  | `final` | 0.017601 | `review` | `blue:12408;neutral:888;dark:373;purple:147;cyan_teal:23` | `assets/ponchi/final/J-32.webp` |
| `J-31` |  | `final` | 0.016899 | `review` | `blue:10991;neutral:1835;dark:280;purple:140;cyan_teal:40` | `assets/ponchi/final/J-31.webp` |
| `J-78` |  | `final` | 0.016832 | `review` | `blue:7248;dark:3360;neutral:2406;purple:74;cyan_teal:61` | `assets/ponchi/final/J-78.webp` |
| `J-90` |  | `final` | 0.014544 | `review` | `blue:10080;dark:893;neutral:423;cyan_teal:28;purple:11` | `assets/ponchi/final/J-90.webp` |
| `J-41` |  | `final` | 0.013967 | `review` | `blue:9916;neutral:709;dark:309;purple:28;cyan_teal:20` | `assets/ponchi/final/J-41.webp` |
| `J-74` |  | `final` | 0.013246 | `review` | `blue:6426;dark:2245;neutral:1082;orange:376;cyan_teal:124` | `assets/ponchi/final/J-74.webp` |
| `J-79` |  | `final` | 0.012575 | `review` | `blue:7216;dark:1613;neutral:795;orange:87;cyan_teal:73` | `assets/ponchi/final/J-79.webp` |
| `J-70` |  | `final` | 0.012339 | `review` | `blue:8305;neutral:811;dark:465;cyan_teal:95;purple:25` | `assets/ponchi/final/J-70.webp` |
| `J-91` |  | `final` | 0.011570 | `review` | `blue:7884;dark:1019;neutral:154;cyan_teal:35;purple:5` | `assets/ponchi/final/J-91.webp` |
| `J-75` |  | `final` | 0.011556 | `review` | `blue:8052;neutral:503;dark:458;purple:44;cyan_teal:29` | `assets/ponchi/final/J-75.webp` |
| `J-77` |  | `final` | 0.011323 | `review` | `blue:8032;neutral:579;dark:230;cyan_teal:35;purple:25` | `assets/ponchi/final/J-77.webp` |
| `J-71` |  | `final` | 0.009371 | `pass` | `blue:5798;neutral:1235;dark:300;cyan_teal:21;purple:13` | `assets/ponchi/final/J-71.webp` |
| `J-93` |  | `final` | 0.009148 | `pass` | `dark:3411;blue:2973;neutral:766;cyan_teal:23;purple:19` | `assets/ponchi/final/J-93.webp` |
| `J-43` |  | `final` | 0.009147 | `pass` | `blue:5287;dark:1062;neutral:762;purple:65;cyan_teal:16` | `assets/ponchi/final/J-43.webp` |
| `J-40` |  | `final` | 0.007779 | `pass` | `blue:5112;neutral:472;dark:435;cyan_teal:70;purple:25` | `assets/ponchi/final/J-40.webp` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
