# Ponchi Color Audit Summary

This audit checks generated-body color drift against the ponchi palette.
For overlay candidates, the matching base image is audited when present so official asset colors do not count against the body palette.

## Counts

| status | count |
| --- | ---: |
| `pass` | 350 |
| `review` | 0 |
| `fail` | 0 |
| `missing` | 0 |

## Artifacts

- CSV: `ledgers/ponchi_color_audit.csv`
- Contact sheet: `docs/ponchi_batch_audits/ponchi-color-audit-contact-sheet.png`

## By Batch

| batch | pass | review | fail | missing |
| --- | ---: | ---: | ---: | ---: |
| `ponchi-batch-001` | 20 | 0 | 0 | 0 |
| `ponchi-batch-002` | 20 | 0 | 0 | 0 |
| `ponchi-batch-003` | 20 | 0 | 0 | 0 |
| `ponchi-batch-004` | 20 | 0 | 0 | 0 |
| `ponchi-batch-005` | 20 | 0 | 0 | 0 |
| `ponchi-batch-006` | 20 | 0 | 0 | 0 |
| `ponchi-batch-007` | 20 | 0 | 0 | 0 |
| `ponchi-batch-008` | 20 | 0 | 0 | 0 |
| `ponchi-batch-009` | 20 | 0 | 0 | 0 |
| `ponchi-batch-010` | 20 | 0 | 0 | 0 |
| `ponchi-batch-011` | 20 | 0 | 0 | 0 |
| `ponchi-batch-012` | 20 | 0 | 0 | 0 |
| `ponchi-batch-013` | 20 | 0 | 0 | 0 |
| `ponchi-batch-014` | 20 | 0 | 0 | 0 |
| `ponchi-batch-015` | 20 | 0 | 0 | 0 |
| `ponchi-batch-016` | 20 | 0 | 0 | 0 |
| `ponchi-batch-017` | 20 | 0 | 0 | 0 |
| `ponchi-batch-018` | 10 | 0 | 0 | 0 |

## Highest Off-Palette Ratios

| entry | title | batch | ratio | status | dominant off-palette | audited file |
| --- | --- | --- | ---: | --- | --- | --- |
| `C-56` | Yann LeCun | `ponchi-batch-004` | 0.009783 | `pass` | `blue:5728;dark:713;neutral:651;purple:475;orange:89` | `assets/ponchi/experiments/batches/ponchi-batch-004/C-56_base_1254x627.png` |
| `H-61` | Preview 版という文化 | `ponchi-batch-014` | 0.009772 | `pass` | `blue:6922;dark:698;neutral:55;purple:7;orange:1` | `assets/ponchi/experiments/batches/ponchi-batch-014/H-61_base_1254x627.png` |
| `H-52` | Copilot から Claude Code までの流れ | `ponchi-batch-014` | 0.009688 | `pass` | `blue:6885;dark:622;neutral:64;purple:22;orange:16` | `assets/ponchi/experiments/batches/ponchi-batch-014/H-52_base_1254x627.png` |
| `D-43` | Qwen 系 | `ponchi-batch-006` | 0.009571 | `pass` | `blue:6380;dark:531;neutral:327;orange:170;purple:61` | `assets/ponchi/experiments/batches/ponchi-batch-006/D-43_base_1254x627.png` |
| `B-11` | Bolt.new | `ponchi-batch-002` | 0.009301 | `pass` | `blue:6501;dark:797;neutral:13;orange:2` | `assets/ponchi/experiments/batches/ponchi-batch-002/B-11_base_1254x627.png` |
| `D-2` | Gemini 2.5 系 | `ponchi-batch-005` | 0.009300 | `pass` | `blue:6621;dark:271;neutral:229;orange:123;purple:36` | `assets/ponchi/experiments/batches/ponchi-batch-005/D-2_base_1254x627.png` |
| `H-59` | AI エージェント元年 | `ponchi-batch-014` | 0.009288 | `pass` | `blue:6914;dark:205;neutral:110;purple:61;orange:7` | `assets/ponchi/experiments/batches/ponchi-batch-014/H-59_base_1254x627.png` |
| `B-8` | Codex | `ponchi-batch-001` | 0.009211 | `pass` | `blue:4377;purple:1620;dark:1051;neutral:193;orange:1` | `assets/ponchi/experiments/batches/ponchi-batch-001/B-8_base_1254x627.png` |
| `C-14` | AMD | `ponchi-batch-004` | 0.009176 | `pass` | `blue:4627;dark:1699;neutral:745;purple:132;orange:7` | `assets/ponchi/experiments/batches/ponchi-batch-004/C-14_base_1254x627.png` |
| `H-50` | Bard → Gemini | `ponchi-batch-014` | 0.009120 | `pass` | `blue:5734;dark:1431;neutral:4;purple:1;cyan_teal:1` | `assets/ponchi/experiments/batches/ponchi-batch-014/H-50_base_1254x627.png` |
| `G-40` | バイブコーディング | `ponchi-batch-013` | 0.009016 | `pass` | `blue:6037;dark:1006;neutral:40;cyan_teal:5;orange:1` | `assets/ponchi/experiments/batches/ponchi-batch-013/G-40_base_1254x627.png` |
| `D-22` | o1 系 | `ponchi-batch-005` | 0.008790 | `pass` | `blue:6389;neutral:256;dark:130;orange:71;purple:35` | `assets/ponchi/experiments/batches/ponchi-batch-005/D-22_base_1254x627.png` |
| `B-20` | Vercel | `ponchi-batch-002` | 0.008772 | `pass` | `blue:6240;dark:642;purple:12;neutral:2;orange:1` | `assets/ponchi/experiments/batches/ponchi-batch-002/B-20_base_1254x627.png` |
| `D-44` | Kimi | `ponchi-batch-006` | 0.008769 | `pass` | `blue:5942;neutral:613;purple:122;orange:82;dark:68` | `assets/ponchi/experiments/batches/ponchi-batch-006/D-44_base_1254x627.png` |
| `H-53` | ChatGPT 登場 | `ponchi-batch-014` | 0.008609 | `pass` | `blue:5798;dark:922;neutral:40;purple:4;orange:2` | `assets/ponchi/experiments/batches/ponchi-batch-014/H-53_base_1254x627.png` |
| `B-25` | Azure | `ponchi-batch-002` | 0.008563 | `pass` | `blue:5452;dark:1189;neutral:40;purple:33;orange:12` | `assets/ponchi/experiments/batches/ponchi-batch-002/B-25_base_1254x627.png` |
| `H-55` | LLaMA のオープン化 | `ponchi-batch-014` | 0.008495 | `pass` | `blue:5678;dark:918;neutral:54;orange:12;cyan_teal:5` | `assets/ponchi/experiments/batches/ponchi-batch-014/H-55_base_1254x627.png` |
| `B-27` | Vertex AI | `ponchi-batch-002` | 0.008492 | `pass` | `blue:5668;dark:962;neutral:29;orange:11;yellow:5` | `assets/ponchi/experiments/batches/ponchi-batch-002/B-27_base_1254x627.png` |
| `B-21` | Netlify | `ponchi-batch-002` | 0.008484 | `pass` | `blue:5697;dark:952;neutral:21;yellow:1` | `assets/ponchi/experiments/batches/ponchi-batch-002/B-21_base_1254x627.png` |
| `B-5` | GitHub Copilot | `ponchi-batch-001` | 0.008451 | `pass` | `blue:4907;purple:1092;dark:445;neutral:199;orange:1` | `assets/ponchi/experiments/batches/ponchi-batch-001/B-5_base_1254x627.png` |

## Interpretation

- `pass` means the mechanical color gate did not find material off-palette body pixels.
- `review` means small off-palette traces exist and the image needs visual confirmation or minor cleanup.
- `fail` means off-palette color is materially present and the base should be rerendered, rebuilt, or deterministically recolored before final promotion.
- This is a first-pass gate; semantic issues such as generated product UI, logo-like icons, composition quality, or unclear meaning still require visual review.
