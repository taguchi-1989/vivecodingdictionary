# I/J full ponchi regeneration plan

Date: 2026-06-06

Goal: rebuild every I/J ponchi image as a new raster candidate, not just repair
low-score rows. Existing `assets/ponchi/final/` files remain untouched until a
separate promotion decision.

## Scope

- I chapter: 19 final images.
- J chapter: 50 final images.
- Total rebuild target: 69 images.

## Why Full Rebuild

The current I/J images are semantically reviewed, but the image set still has
system-level weaknesses:

- Many rows are mechanically `color_review` or `color_fail`.
- Several J hardware/UI images have low score, low density, or too much empty
  2:1 space.
- Some images read like thin SVG diagrams instead of full ponchi pages.
- Several clusters rely on captions to separate close concepts.
- Character use is inconsistent: some entries would benefit from recurring
  Character A/B/C, while hardware/protocol diagrams should stay diagram-first.

## Audit Beyond Score

Each rebuild batch must pass these checks:

| gate | check |
| --- | --- |
| Prompt policy | `scene_brief` exists and `ponchi_prompt_lint.py` passes |
| Image policy | no generated logo, product UI, official seal, readable text, or prohibited colors |
| Image audit | `1254x627`, bbox coverage pass, no false logo-clearspace assumption |
| Color audit | generated body `pass` |
| Quality score | no low outlier; high preferred, mid requires visual reason |
| Intra-cluster comparison | close entries in the same cluster are visually distinct |
| Cross-chapter comparison | image does not collapse into a generic B/D/F/G service/tool picture |
| SVG/thinness review | not just sparse cards, stick figures, or isolated wire icons |
| Character review | Character A/B/C only when useful; no new mascot or unstable human design |

## Character Policy

- Use `diagram_only` for protocol, hardware form factor, model architecture, and
  legal boundary diagrams when characters would dilute the subject.
- Use Character A/B for human workflow entries: CLI use, setup/configuration,
  literacy, review, decision, or comparison tasks.
- Use Character C only as a small AI/helper signal. Do not make it the main
  mascot for every AI concept.
- Rotate roles: do not default to "male explains, female listens".

## Batch Plan

| batch | target entries | focus | character strategy |
| --- | --- | --- | --- |
| `semantic-regen-015` | `J-72;J-73;J-78;J-79;J-91` | worst J hardware/UI outliers | diagram-only except CLI with one human operator |
| `semantic-regen-016` | `J-70;J-71;J-74;J-75;J-76;J-77;J-80;J-81` | hardware accelerator, memory, storage interfaces | diagram-only |
| `semantic-regen-017` | `I-1;I-2;I-3;I-4;I-5;I-80;I-81` | MCP core roles and setup | mostly diagram-first, small Character C only for AI helper |
| `semantic-regen-018` | `I-10;I-11;I-12;I-13;I-23;I-24;I-30;I-41;I-50` | MCP tool domains | mixed tool-loop and domain-specific diagrams |
| `semantic-regen-019` | `I-20;I-21;I-22` | browser automation MCP exact distinction | diagram-first, no product UI |
| `semantic-regen-020` | `J-1;J-2;J-3;J-4;J-10;J-11;J-12;J-13;J-14;J-15` | AI/ML basics, model scale, architecture | diagrams with occasional Character C |
| `semantic-regen-021` | `J-16;J-17;J-18;J-19;J-20;J-21;J-22;J-23` | training/adaptation/data/model mechanics | diagrams |
| `semantic-regen-022` | `J-31;J-32;J-33;J-40;J-41;J-42;J-43;J-100` | history, buzzwords, literacy | mixed diagrams and human workflow |
| `semantic-regen-023` | `J-50;J-51;J-52;J-53;J-54;J-55;J-56;J-62` | law/ethics/safety retest as full rebuild set | reuse semantic-regen-014 direction, add privacy-law fixes |
| `semantic-regen-024` | `J-90;J-92;J-93` | UI/OS ecosystem | human workflow plus OS ecosystem diagrams |

## First Batch Acceptance

`semantic-regen-015` is accepted only if:

- All five prompts pass lint.
- All five generated bases pass image audit and color audit.
- Contact sheet shows clear visual separation:
  - H100: datacenter accelerator module with HBM/rack context.
  - Blackwell: newer generation multi-die/rack-scale accelerator flow.
  - HDD: mechanical platter/head storage.
  - SSD: solid-state chip/module storage.
  - CLI: command loop and terminal workflow, not generic app UI.
- No production final image is overwritten.
