# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 5 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_003_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_003/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-003` | 5 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `B-10` |  | `semantic-regen-003` | 0.008001 | `pass` | `blue:5558;dark:593;neutral:112;purple:19;orange:4` | `assets/ponchi/experiments/batches/semantic-regen-003/B-10_base_1254x627.png` |
| `B-1` |  | `semantic-regen-003` | 0.005884 | `pass` | `blue:4308;dark:278;neutral:28;purple:7;orange:2` | `assets/ponchi/experiments/batches/semantic-regen-003/B-1_base_1254x627.png` |
| `B-2` |  | `semantic-regen-003` | 0.003299 | `pass` | `blue:2424;dark:109;neutral:43;orange:9;purple:7` | `assets/ponchi/experiments/batches/semantic-regen-003/B-2_base_1254x627.png` |
| `B-3` |  | `semantic-regen-003` | 0.003051 | `pass` | `blue:2150;neutral:118;dark:58;purple:37;orange:24` | `assets/ponchi/experiments/batches/semantic-regen-003/B-3_base_1254x627.png` |
| `B-14` |  | `semantic-regen-003` | 0.002316 | `pass` | `blue:1725;dark:41;neutral:32;cyan_teal:13;purple:5` | `assets/ponchi/experiments/batches/semantic-regen-003/B-14_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
