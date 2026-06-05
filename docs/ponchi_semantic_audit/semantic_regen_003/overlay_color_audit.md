# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 4 |
| `review` | 1 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_003_overlay_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_003/overlay_color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-003` | 4 | 1 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `B-1` |  | `semantic-regen-003` | 0.016437 | `review` | `blue:7383;green:1651;red:1024;cyan_teal:691;orange:587` | `assets/ponchi/experiments/batches/semantic-regen-003/B-1_overlay_1254x627.png` |
| `B-2` |  | `semantic-regen-003` | 0.009705 | `pass` | `red:4998;blue:2424;dark:109;neutral:82;orange:9` | `assets/ponchi/experiments/batches/semantic-regen-003/B-2_overlay_1254x627.png` |
| `B-10` |  | `semantic-regen-003` | 0.007927 | `pass` | `blue:5507;dark:589;neutral:111;purple:19;red:3` | `assets/ponchi/experiments/batches/semantic-regen-003/B-10_overlay_1254x627.png` |
| `B-3` |  | `semantic-regen-003` | 0.003052 | `pass` | `blue:2150;neutral:118;dark:59;purple:37;orange:24` | `assets/ponchi/experiments/batches/semantic-regen-003/B-3_overlay_1254x627.png` |
| `B-14` |  | `semantic-regen-003` | 0.002316 | `pass` | `blue:1725;dark:41;neutral:32;cyan_teal:13;purple:5` | `assets/ponchi/experiments/batches/semantic-regen-003/B-14_overlay_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
