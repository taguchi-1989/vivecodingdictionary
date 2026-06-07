# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 69 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/ij_full_regen_final_promotion_color_audit_2026-06-07.csv`
- Contact sheet: `docs/ponchi_semantic_audit/ij_full_regen_final_promotion_2026-06-07/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `final` | 69 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `I-22` |  | `final` | 0.009794 | `pass` | `blue:6115;dark:1108;neutral:431;purple:38;orange:8` | `assets/ponchi/final/I-22.webp` |
| `J-72` |  | `final` | 0.009260 | `pass` | `blue:4076;neutral:1774;dark:864;purple:464;orange:41` | `assets/ponchi/final/J-72.webp` |
| `J-70` |  | `final` | 0.009195 | `pass` | `blue:5177;dark:1968;neutral:76;orange:5;cyan_teal:2` | `assets/ponchi/final/J-70.webp` |
| `J-90` |  | `final` | 0.009136 | `pass` | `blue:5426;dark:1080;purple:351;neutral:311;cyan_teal:6` | `assets/ponchi/final/J-90.webp` |
| `I-81` |  | `final` | 0.009056 | `pass` | `blue:5646;dark:1250;neutral:214;purple:9;cyan_teal:1` | `assets/ponchi/final/I-81.webp` |
| `J-20` |  | `final` | 0.008961 | `pass` | `blue:4876;dark:1429;neutral:426;orange:150;purple:105` | `assets/ponchi/final/J-20.webp` |
| `I-4` |  | `final` | 0.008959 | `pass` | `blue:4743;dark:1579;neutral:708;purple:12;orange:1` | `assets/ponchi/final/I-4.webp` |
| `J-77` |  | `final` | 0.008956 | `pass` | `blue:6611;dark:339;neutral:74;purple:12;orange:3` | `assets/ponchi/final/J-77.webp` |
| `J-33` |  | `final` | 0.008930 | `pass` | `blue:3533;dark:3054;neutral:256;purple:110;orange:37` | `assets/ponchi/final/J-33.webp` |
| `J-23` |  | `final` | 0.008640 | `pass` | `blue:4766;dark:1278;neutral:576;purple:158;orange:10` | `assets/ponchi/final/J-23.webp` |
| `J-73` |  | `final` | 0.008504 | `pass` | `blue:4672;neutral:912;purple:371;dark:293;orange:292` | `assets/ponchi/final/J-73.webp` |
| `J-62` |  | `final` | 0.008474 | `pass` | `blue:4803;dark:1590;neutral:125;orange:97;purple:27` | `assets/ponchi/final/J-62.webp` |
| `I-3` |  | `final` | 0.008425 | `pass` | `blue:4405;dark:1790;purple:217;neutral:211;cyan_teal:1` | `assets/ponchi/final/I-3.webp` |
| `J-75` |  | `final` | 0.008312 | `pass` | `blue:5607;dark:554;neutral:264;cyan_teal:87;purple:19` | `assets/ponchi/final/J-75.webp` |
| `J-51` |  | `final` | 0.008234 | `pass` | `blue:6151;dark:186;neutral:80;purple:26;orange:23` | `assets/ponchi/final/J-51.webp` |
| `I-41` |  | `final` | 0.007959 | `pass` | `blue:4089;dark:1940;purple:146;neutral:81;orange:2` | `assets/ponchi/final/I-41.webp` |
| `I-10` |  | `final` | 0.007902 | `pass` | `blue:4687;dark:1193;neutral:299;purple:23;yellow:8` | `assets/ponchi/final/I-10.webp` |
| `I-2` |  | `final` | 0.007782 | `pass` | `dark:3044;blue:2814;neutral:257;purple:2;cyan_teal:2` | `assets/ponchi/final/I-2.webp` |
| `I-13` |  | `final` | 0.007662 | `pass` | `blue:4139;dark:1329;neutral:435;purple:36;orange:36` | `assets/ponchi/final/I-13.webp` |
| `I-21` |  | `final` | 0.007590 | `pass` | `blue:5092;dark:658;neutral:160;orange:35;purple:13` | `assets/ponchi/final/I-21.webp` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
