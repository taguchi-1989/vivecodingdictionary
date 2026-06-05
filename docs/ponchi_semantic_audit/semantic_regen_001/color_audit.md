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

- CSV: `ledgers/semantic_regen_001_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_001/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-001` | 9 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `D-53` |  | `semantic-regen-001` | 0.009100 | `pass` | `blue:5469;dark:1013;neutral:518;orange:80;purple:44` | `assets/ponchi/experiments/batches/semantic-regen-001/D-53_base_1254x627.png` |
| `D-58` |  | `semantic-regen-001` | 0.009053 | `pass` | `blue:5685;dark:885;neutral:478;purple:64;cyan_teal:2` | `assets/ponchi/experiments/batches/semantic-regen-001/D-58_base_1254x627.png` |
| `D-22` |  | `semantic-regen-001` | 0.006715 | `pass` | `blue:4143;dark:1054;purple:51;neutral:31;cyan_teal:1` | `assets/ponchi/experiments/batches/semantic-regen-001/D-22_base_1254x627.png` |
| `B-26` |  | `semantic-regen-001` | 0.005971 | `pass` | `blue:2587;dark:1800;neutral:268;orange:27;yellow:8` | `assets/ponchi/experiments/batches/semantic-regen-001/B-26_base_1254x627.png` |
| `B-5` |  | `semantic-regen-001` | 0.005421 | `pass` | `blue:2768;dark:1294;neutral:162;orange:16;cyan_teal:11` | `assets/ponchi/experiments/batches/semantic-regen-001/B-5_base_1254x627.png` |
| `B-6` |  | `semantic-regen-001` | 0.005043 | `pass` | `blue:3110;dark:419;neutral:403;purple:17;cyan_teal:9` | `assets/ponchi/experiments/batches/semantic-regen-001/B-6_base_1254x627.png` |
| `D-70` |  | `semantic-regen-001` | 0.004752 | `pass` | `blue:2634;dark:1013;neutral:88;purple:1` | `assets/ponchi/experiments/batches/semantic-regen-001/D-70_base_1254x627.png` |
| `B-31` |  | `semantic-regen-001` | 0.002610 | `pass` | `dark:1892;blue:120;neutral:35;purple:3;orange:2` | `assets/ponchi/experiments/batches/semantic-regen-001/B-31_base_1254x627.png` |
| `B-52` |  | `semantic-regen-001` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-001/B-52_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
