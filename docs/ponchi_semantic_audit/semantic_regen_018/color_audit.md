# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 9 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_018_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_018/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-018` | 9 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `I-41` |  | `semantic-regen-018` | 0.007959 | `pass` | `blue:4089;dark:1940;purple:146;neutral:81;orange:2` | `assets/ponchi/experiments/batches/semantic-regen-018/I-41_base_1254x627.png` |
| `I-10` |  | `semantic-regen-018` | 0.007902 | `pass` | `blue:4687;dark:1193;neutral:299;purple:23;yellow:8` | `assets/ponchi/experiments/batches/semantic-regen-018/I-10_base_1254x627.png` |
| `I-13` |  | `semantic-regen-018` | 0.007662 | `pass` | `blue:4139;dark:1329;neutral:435;purple:36;orange:36` | `assets/ponchi/experiments/batches/semantic-regen-018/I-13_base_1254x627.png` |
| `I-12` |  | `semantic-regen-018` | 0.007233 | `pass` | `blue:4831;dark:680;neutral:113;purple:58;cyan_teal:4` | `assets/ponchi/experiments/batches/semantic-regen-018/I-12_base_1254x627.png` |
| `I-23` |  | `semantic-regen-018` | 0.006196 | `pass` | `blue:4020;neutral:409;dark:390;purple:51;cyan_teal:2` | `assets/ponchi/experiments/batches/semantic-regen-018/I-23_base_1254x627.png` |
| `I-24` |  | `semantic-regen-018` | 0.005357 | `pass` | `blue:3429;dark:463;neutral:269;purple:40;orange:6` | `assets/ponchi/experiments/batches/semantic-regen-018/I-24_base_1254x627.png` |
| `I-30` |  | `semantic-regen-018` | 0.003789 | `pass` | `blue:2129;neutral:649;dark:159;purple:38;orange:3` | `assets/ponchi/experiments/batches/semantic-regen-018/I-30_base_1254x627.png` |
| `I-11` |  | `semantic-regen-018` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-018/I-11_base_1254x627.png` |
| `I-50` |  | `semantic-regen-018` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-018/I-50_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
