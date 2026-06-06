# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 10 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_020_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_020/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-020` | 10 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-4` |  | `semantic-regen-020` | 0.007559 | `pass` | `blue:3405;dark:2417;neutral:108;orange:7;yellow:4` | `assets/ponchi/experiments/batches/semantic-regen-020/J-4_base_1254x627.png` |
| `J-1` |  | `semantic-regen-020` | 0.007246 | `pass` | `dark:2899;blue:2633;neutral:158;purple:6;yellow:1` | `assets/ponchi/experiments/batches/semantic-regen-020/J-1_base_1254x627.png` |
| `J-14` |  | `semantic-regen-020` | 0.006979 | `pass` | `dark:2753;blue:2541;neutral:92;orange:73;purple:16` | `assets/ponchi/experiments/batches/semantic-regen-020/J-14_base_1254x627.png` |
| `J-2` |  | `semantic-regen-020` | 0.006827 | `pass` | `blue:2813;dark:2270;purple:150;neutral:131;orange:3` | `assets/ponchi/experiments/batches/semantic-regen-020/J-2_base_1254x627.png` |
| `J-10` |  | `semantic-regen-020` | 0.006717 | `pass` | `blue:3186;dark:1971;neutral:88;purple:25;green:5` | `assets/ponchi/experiments/batches/semantic-regen-020/J-10_base_1254x627.png` |
| `J-13` |  | `semantic-regen-020` | 0.006533 | `pass` | `blue:3377;dark:1594;neutral:110;purple:37;orange:9` | `assets/ponchi/experiments/batches/semantic-regen-020/J-13_base_1254x627.png` |
| `J-3` |  | `semantic-regen-020` | 0.004147 | `pass` | `blue:1619;dark:1568;neutral:57;orange:12;cyan_teal:2` | `assets/ponchi/experiments/batches/semantic-regen-020/J-3_base_1254x627.png` |
| `J-15` |  | `semantic-regen-020` | 0.002338 | `pass` | `dark:1416;blue:286;neutral:117;orange:10;cyan_teal:8` | `assets/ponchi/experiments/batches/semantic-regen-020/J-15_base_1254x627.png` |
| `J-11` |  | `semantic-regen-020` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-020/J-11_base_1254x627.png` |
| `J-12` |  | `semantic-regen-020` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-020/J-12_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
