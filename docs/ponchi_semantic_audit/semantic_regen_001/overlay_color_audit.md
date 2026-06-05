# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 5 |
| `review` | 3 |
| `fail` | 1 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_001_overlay_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_001/overlay_color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-001` | 5 | 3 | 1 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `D-53` |  | `semantic-regen-001` | 0.032187 | `fail` | `blue:23621;dark:1013;neutral:518;orange:80;purple:44` | `assets/ponchi/experiments/batches/semantic-regen-001/D-53_overlay_1254x627.png` |
| `B-31` |  | `semantic-regen-001` | 0.014156 | `review` | `purple:9081;dark:1892;blue:120;neutral:35;orange:2` | `assets/ponchi/experiments/batches/semantic-regen-001/B-31_overlay_1254x627.png` |
| `D-70` |  | `semantic-regen-001` | 0.010442 | `review` | `blue:2701;purple:1488;dark:1164;green:911;yellow:872` | `assets/ponchi/experiments/batches/semantic-regen-001/D-70_overlay_1254x627.png` |
| `B-26` |  | `semantic-regen-001` | 0.010236 | `review` | `blue:5940;dark:1800;neutral:268;orange:27;yellow:8` | `assets/ponchi/experiments/batches/semantic-regen-001/B-26_overlay_1254x627.png` |
| `B-52` |  | `semantic-regen-001` | 0.009404 | `pass` | `blue:2733;green:1470;red:905;cyan_teal:619;orange:520` | `assets/ponchi/experiments/batches/semantic-regen-001/B-52_overlay_1254x627.png` |
| `D-58` |  | `semantic-regen-001` | 0.009133 | `pass` | `blue:5685;dark:914;neutral:497;purple:64;cyan_teal:10` | `assets/ponchi/experiments/batches/semantic-regen-001/D-58_overlay_1254x627.png` |
| `D-22` |  | `semantic-regen-001` | 0.006715 | `pass` | `blue:4143;dark:1054;purple:51;neutral:31;cyan_teal:1` | `assets/ponchi/experiments/batches/semantic-regen-001/D-22_overlay_1254x627.png` |
| `B-5` |  | `semantic-regen-001` | 0.005421 | `pass` | `blue:2768;dark:1294;neutral:162;orange:16;cyan_teal:11` | `assets/ponchi/experiments/batches/semantic-regen-001/B-5_overlay_1254x627.png` |
| `B-6` |  | `semantic-regen-001` | 0.005043 | `pass` | `blue:3110;dark:419;neutral:403;purple:17;cyan_teal:9` | `assets/ponchi/experiments/batches/semantic-regen-001/B-6_overlay_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
