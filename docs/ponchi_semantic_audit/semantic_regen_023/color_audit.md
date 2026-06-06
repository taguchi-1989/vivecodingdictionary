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

- CSV: `ledgers/semantic_regen_023_color_audit.csv`
- Contact sheet: `docs/ponchi_semantic_audit/semantic_regen_023/color_contact_sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `semantic-regen-023` | 8 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `J-62` |  | `semantic-regen-023` | 0.008474 | `pass` | `blue:4803;dark:1590;neutral:125;orange:97;purple:27` | `assets/ponchi/experiments/batches/semantic-regen-023/J-62_base_1254x627.png` |
| `J-51` |  | `semantic-regen-023` | 0.008234 | `pass` | `blue:6151;dark:186;neutral:80;purple:26;orange:23` | `assets/ponchi/experiments/batches/semantic-regen-023/J-51_base_1254x627.png` |
| `J-55` |  | `semantic-regen-023` | 0.006975 | `pass` | `blue:4946;neutral:293;purple:157;dark:33;orange:33` | `assets/ponchi/experiments/batches/semantic-regen-023/J-55_base_1254x627.png` |
| `J-53` |  | `semantic-regen-023` | 0.006553 | `pass` | `blue:4105;neutral:662;purple:202;dark:146;orange:18` | `assets/ponchi/experiments/batches/semantic-regen-023/J-53_base_1254x627.png` |
| `J-54` |  | `semantic-regen-023` | 0.004120 | `pass` | `blue:2773;neutral:246;dark:112;purple:44;orange:36` | `assets/ponchi/experiments/batches/semantic-regen-023/J-54_base_1254x627.png` |
| `J-50` |  | `semantic-regen-023` | 0.003255 | `pass` | `blue:1565;neutral:640;dark:195;purple:144;orange:11` | `assets/ponchi/experiments/batches/semantic-regen-023/J-50_base_1254x627.png` |
| `J-52` |  | `semantic-regen-023` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-023/J-52_base_1254x627.png` |
| `J-56` |  | `semantic-regen-023` | 0.000000 | `pass` | `` | `assets/ponchi/experiments/batches/semantic-regen-023/J-56_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
