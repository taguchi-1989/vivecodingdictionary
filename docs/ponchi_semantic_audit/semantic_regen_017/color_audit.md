# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 7 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_017_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_017/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-017` | 7 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `I-81` |  | `semantic-regen-017` | 0.009056 | `pass` | `blue:5646;dark:1250;neutral:214;purple:9;cyan_teal:1` | `assets/ponchi/experiments/batches/semantic-regen-017/I-81_base_1254x627.png` |
| `I-4` |  | `semantic-regen-017` | 0.008959 | `pass` | `blue:4743;dark:1579;neutral:708;purple:12;orange:1` | `assets/ponchi/experiments/batches/semantic-regen-017/I-4_base_1254x627.png` |
| `I-3` |  | `semantic-regen-017` | 0.008425 | `pass` | `blue:4405;dark:1790;purple:217;neutral:211;cyan_teal:1` | `assets/ponchi/experiments/batches/semantic-regen-017/I-3_base_1254x627.png` |
| `I-2` |  | `semantic-regen-017` | 0.007782 | `pass` | `dark:3044;blue:2814;neutral:257;purple:2;cyan_teal:2` | `assets/ponchi/experiments/batches/semantic-regen-017/I-2_base_1254x627.png` |
| `I-80` |  | `semantic-regen-017` | 0.007119 | `pass` | `blue:3791;dark:1608;neutral:188;purple:7;cyan_teal:3` | `assets/ponchi/experiments/batches/semantic-regen-017/I-80_base_1254x627.png` |
| `I-1` |  | `semantic-regen-017` | 0.004369 | `pass` | `dark:1914;blue:1075;neutral:435;purple:6;cyan_teal:4` | `assets/ponchi/experiments/batches/semantic-regen-017/I-1_base_1254x627.png` |
| `I-5` |  | `semantic-regen-017` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-017/I-5_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
