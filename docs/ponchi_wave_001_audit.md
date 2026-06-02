# Ponchi Wave 001 audit

Wave 001 covers the first 60 active entries:

- `ponchi-batch-001`: A-1 - B-9
- `ponchi-batch-002`: B-10 - B-29
- `ponchi-batch-003`: B-30 - C-9

## Current summary

| metric | count |
| --- | ---: |
| entries in wave | 60 |
| entries with generated 2:1 batch-002 base | 20 |
| batch-003 prompt briefs | 20 |
| batch-003 generated 2:1 bases | 20 |
| accepted final candidates in batch-002 | 8 |
| known overlay audit items in wave ledger | 15 |
| known overlay wait items in wave ledger | 33 |
| known overlay ready items in wave ledger | 0 |
| known blocked brand asset items in wave ledger | 1 |

## Batch 001 status

Batch 001 is mixed frontmatter and early B chapter material. Several B entries
already have logo pipeline state in the ledger, but A-series content is still
`brief_needed`.

Immediate audit tasks:

- Decide whether A-series frontmatter requires new ponchi images or should be
  marked as `no_brand_asset` / lower priority.
- For B-1, B-3, and B-8, continue official logo source review.
- Keep B-6 blocked until a Windsurf official source is confirmed.
- Review existing overlay candidates for B-2, B-4, B-5, B-7, and B-9 before
  final promotion.

## Batch 002 status

Current detailed progress is tracked in
`docs/ponchi_batch_002_progress_summary.md`.

| metric | count |
| --- | ---: |
| 2:1 base images | 20 / 20 |
| official logo source confirmed | 9 / 20 |
| logo overlays | 8 / 20 |
| accepted final candidates | 8 / 20 |
| overlay_wait remaining | 12 / 20 |

Accepted candidates:

- B-11 Bolt.new
- B-12 Perplexity
- B-13 ElevenLabs
- B-20 Vercel
- B-21 Netlify
- B-22 Cloudflare
- B-28 Render
- B-29 Supabase

## Batch 003 status

Batch 003 is the next bridge from late B into C:

- B-30 Amazon Bedrock
- B-31 Excalidraw
- B-32 Figma
- B-33 Canva
- B-40 Reddit
- B-41 arXiv
- B-50 Claude の料金プラン
- B-51 ChatGPT の料金プラン
- B-52 Gemini の料金プラン
- B-60 Suno
- B-61 ACE-Step 1.5
- C-1 OpenAI
- C-2 Anthropic
- C-3 Google DeepMind
- C-4 Meta AI
- C-5 xAI
- C-6 Mistral AI
- C-7 Hugging Face
- C-8 Microsoft AI
- C-9 NVIDIA

Current prompt status:

- 20 / 20 prompt briefs exist under
  `assets/ponchi/pipeline_prompts/ponchi-batch-003/`.
- Prompt lint passes: `python scripts\ponchi_prompt_lint.py assets\ponchi\pipeline_prompts\ponchi-batch-003\*.md`.
- 20 / 20 generated 2:1 bases exist under
  `assets/ponchi/experiments/batches/ponchi-batch-003/`.
- 20 / 20 generated bases passed base audit:
  `docs/ponchi_batch_audits/ponchi-batch-003-base-image-audit.md`.
- Base contact sheet:
  `docs/ponchi_batch_audits/ponchi-batch-003-base-contact-sheet.png`.
- All 20 prompts use official-overlay clearspace and avoid fake logos, official
  icons, brand colors, real product UI, readable in-image text, mascots, and
  brand-like substitutes.
- C-1 OpenAI and C-2 Anthropic have deterministic official-logo overlays and
  are staged as review-pending candidates under
  `assets/ponchi/final_candidates/ponchi-batch-003/`.
- The other 18 items remain `overlay_wait` until official source review/import
  is complete.

Immediate generation tasks:

- Continue official logo source review/import for the 18 `overlay_wait`
  entries.
- Visually review C-1 OpenAI and C-2 Anthropic overlay candidates.
- Continue official source review/import for the remaining 18 Batch 003
  `overlay_wait` entries.
- Keep Batch 003 staged outside `assets/ponchi/final/` until overlay/candidate
  audit and explicit promotion approval.
- Do not promote or write any Batch 003 output to `assets/ponchi/final/`.

## Wave 001 completion target

Wave 001 is complete only when:

- Batches 001-003 have current batch audit files.
- Batch 002 accepted candidates remain staged outside `assets/ponchi/final/`.
- Batch 003 has 20 2:1 base images and base audit results.
- Every Wave 001 brand/logo item is either `official_logo_applied`,
  `overlay_wait` with reason, or `blocked_brand_asset` with reason.
- `docs/ponchi_wave_001_handoff.md` is updated with exact next actions.
