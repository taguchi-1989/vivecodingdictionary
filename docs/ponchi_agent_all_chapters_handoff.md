# Agent handoff: all-chapters forward generation

Assigned scope:

- Move every remaining chapter forward, not only C/D.
- Start with Batch 003 and then continue through batches 004-018 in ledger
  order.
- Apply Batch 002 best practices to new 2:1 base generation.

## Current target

Batch 004:

- C-10 Moonshot AI
- C-11 Z.ai
- C-12 TSMC
- C-13 Groq
- C-14 AMD
- C-50 Sam Altman
- C-51 Dario Amodei
- C-52 Demis Hassabis
- C-53 Andrej Karpathy
- C-54 Ilya Sutskever
- C-55 Mira Murati
- C-56 Yann LeCun
- C-57 Geoffrey Hinton
- C-58 Elon Musk
- C-59 Jensen Huang
- C-60 Ray Kurzweil
- C-80 AI大学
- C-81 にゃんた
- C-82 まさお
- C-83 AI の羅針盤

Current status:

- Batch 003 has 20/20 generated base images and 20/20 base audit pass.
- Batch 003 has 2 review-pending overlay candidates: C-1 OpenAI and C-2
  Anthropic.
- Batch 004 has 20/20 prompt briefs under
  `assets/ponchi/pipeline_prompts/ponchi-batch-004/`.
- Batch 004 prompt lint passes.
- Batch 004 has 0/20 base images.
- Batch 004 ledger state: 9 `overlay_wait`, 11 `prompt_review`.
- Next concrete step: generate the 20 Batch 004 `1254x627` base images.

## Generation rules inherited from Batch 002

- Output base image size: `1254x627`.
- Use meaningful 2:1 book illustrations, not mechanical crops or padding.
- Use clean editorial diagram style.
- Keep logo/official icon clearspace if the entry is a brand, product, service,
  model family, company, or official platform.
- Do not generate any fake logo, fake product icon, fake official UI, fake
  mascot, readable in-image text, or brand-color substitute.
- If a logo will be needed, the base image should still read as finished but
  leave clean white upper-right clearspace.
- Do not write to `assets/ponchi/final/`.

## Deliverables

- Prompt briefs:
  `assets/ponchi/pipeline_prompts/ponchi-batch-004/*.md`
- Base images:
  `assets/ponchi/experiments/batches/ponchi-batch-004/*_base_1254x627.png`
- Raw generations where useful:
  `assets/ponchi/experiments/batches/ponchi-batch-004/*_base_raw.png`
- Batch audit:
  `docs/ponchi_batch_audits/ponchi-batch-004.md`
- Update ledger:
  `ledgers/ponchi_generation_batches.csv`

## Audit commands

Use existing project scripts when possible:

```powershell
python scripts\ponchi_prompt_lint.py assets\ponchi\pipeline_prompts\ponchi-batch-004\*.md
python scripts\ponchi_batch_audit.py ponchi-batch-004
python scripts\ponchi_batch_report.py ponchi-batch-004
python scripts\ponchi_pipeline_dashboard.py
```

## After Batch 004

Continue in ledger order:

- `ponchi-batch-005` through `ponchi-batch-018`
- Do not skip E/F/G/H/I/J.
- For each 20-entry batch, produce prompts, 2:1 base images, audits, and
  candidate staging where possible.
- At every 60-entry wave boundary, stop and update:
  - `docs/ponchi_progress_overview.md`
  - `docs/ponchi_wave_<nnn>_audit.md`
  - `docs/ponchi_wave_<nnn>_handoff.md`
