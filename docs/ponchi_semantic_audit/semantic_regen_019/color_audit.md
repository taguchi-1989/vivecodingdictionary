# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 3 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/semantic_regen_019_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_019/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-019` | 3 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `I-22` |  | `semantic-regen-019` | 0.009794 | `pass` | `blue:6115;dark:1108;neutral:431;purple:38;orange:8` | `assets/ponchi/experiments/batches/semantic-regen-019/I-22_base_1254x627.png` |
| `I-21` |  | `semantic-regen-019` | 0.007590 | `pass` | `blue:5092;dark:658;neutral:160;orange:35;purple:13` | `assets/ponchi/experiments/batches/semantic-regen-019/I-21_base_1254x627.png` |
| `I-20` |  | `semantic-regen-019` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-019/I-20_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
