# Agent handoff: B continuation

Assigned scope:

- Finish B chapter logo/source/overlay work without touching C/D generation.
- Start with Batch 002 remaining overlay waits, then move to remaining B items
  in Batch 003.

## Current Batch 002 state

Accepted overlay candidates:

- B-13 ElevenLabs
- B-20 Vercel
- B-21 Netlify
- B-22 Cloudflare
- B-28 Render
- B-29 Supabase

Remaining overlay waits:

- B-10 Devin
- B-11 Bolt.new
- B-12 Perplexity
- B-14 Genspark
- B-15 Microsoft Copilot
- B-16 Microsoft 365 Copilot
- B-17 Edge Copilot
- B-18 Aqua Voice
- B-19 Claude Cowork
- B-23 AWS
- B-24 Google Cloud
- B-25 Azure
- B-26 Azure OpenAI
- B-27 Vertex AI

## Required workflow

1. Use official sources only.
2. Save official assets under `assets/logos/<brand>/`.
3. Record source URL, local path, and working rule in
   `docs/brand_usage_audit.md`.
4. Composite with `scripts/composite_official_logo.py`.
5. Do not touch `assets/ponchi/final/`.
6. Re-run:
   - `python scripts/ponchi_batch_audit.py ponchi-batch-002`
   - `python scripts/ponchi_batch_report.py ponchi-batch-002`
   - `python scripts/ponchi_pipeline_dashboard.py`
   - bundled Python for `scripts/ponchi_stage_final_candidates.py`

## Current blockers to preserve

- Microsoft/Copilot/Azure entries need policy-correct mark selection and usage
  confirmation before overlay.
- Google Cloud/Vertex AI need policy-correct choice between brand lockup,
  product icon, or no-logo treatment.
- AWS Architecture Icons are not the same as the primary AWS brand lockup.
- Claude Cowork has not been confirmed as a distinct official product logo;
  official sources currently use Claude Team / Team plan language.
- Genspark official source exists, but local shell download hit a Cloudflare
  challenge; import still needs a viable official-file path.

