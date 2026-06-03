# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 8 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/ponchi_batch_001_color_recheck.csv`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-batch-001-color-recheck-contact-sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `ponchi-batch-001` | 8 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `B-8` |  | `ponchi-batch-001` | 0.009211 | `pass` | `blue:4377;purple:1620;dark:1051;neutral:193;orange:1` | `assets/ponchi/experiments/batches/ponchi-batch-001/B-8_base_1254x627.png` |
| `B-5` |  | `ponchi-batch-001` | 0.008451 | `pass` | `blue:4907;purple:1092;dark:445;neutral:199;orange:1` | `assets/ponchi/experiments/batches/ponchi-batch-001/B-5_base_1254x627.png` |
| `B-1` |  | `ponchi-batch-001` | 0.008128 | `pass` | `blue:4661;purple:1087;dark:445;neutral:196;orange:1` | `assets/ponchi/experiments/batches/ponchi-batch-001/B-1_base_1254x627.png` |
| `B-9` |  | `ponchi-batch-001` | 0.008128 | `pass` | `blue:4661;purple:1087;dark:445;neutral:196;orange:1` | `assets/ponchi/experiments/batches/ponchi-batch-001/B-9_base_1254x627.png` |
| `B-2` |  | `ponchi-batch-001` | 0.007337 | `pass` | `blue:4177;purple:1041;dark:398;neutral:153` | `assets/ponchi/experiments/batches/ponchi-batch-001/B-2_base_1254x627.png` |
| `B-4` |  | `ponchi-batch-001` | 0.006185 | `pass` | `blue:2865;purple:1328;dark:458;neutral:212` | `assets/ponchi/experiments/batches/ponchi-batch-001/B-4_base_1254x627.png` |
| `B-3` |  | `ponchi-batch-001` | 0.004011 | `pass` | `blue:2892;neutral:96;purple:95;dark:43;orange:26` | `assets/ponchi/experiments/batches/ponchi-batch-001/B-3_base_1254x627.png` |
| `B-7` |  | `ponchi-batch-001` | 0.003929 | `pass` | `blue:2999;neutral:33;purple:30;dark:25;orange:1` | `assets/ponchi/experiments/batches/ponchi-batch-001/B-7_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
