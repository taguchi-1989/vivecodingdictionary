# Residual coverage review

Date: 2026-06-06

Unit: `U026 residual-coverage`
Pass mode: `mixed`

## Purpose

This cleanup unit covers final ponchi images that were not referenced by the
semantic migration units after `U025` corrected stale `J-30` to active `J-23`.
The goal is registry coverage, not final-asset promotion. No production image is
overwritten.

## Scope

`B-9;B-11;B-12;B-13;B-18;B-20;B-21;B-22;B-23;B-24;B-25;B-26;B-27;B-28;B-29;B-30;B-31;B-32;B-33;B-40;B-41;B-50;B-51;B-52;B-60;B-61;D-14;D-30;D-40;D-41;D-42;D-43;D-44;D-45;D-46;D-47;D-50;D-54;D-56;D-60;D-70;D-71;F-37;F-38;H-58;H-59;H-60;H-61;H-62`

## Findings

| group | entries | visual status | action |
| --- | --- | --- | --- |
| AI assistants and services | `B-9`, `B-11` - `B-13`, `B-18` | Agent/service surfaces are logo-backed or context-backed and are visually distinct enough at category level. | keep |
| Hosting, cloud, and managed platforms | `B-20` - `B-33` | Official logo overlays and platform motifs separate Vercel, Netlify, Cloudflare, AWS, Google Cloud, Azure, Azure OpenAI, Vertex AI, Render, Supabase, Bedrock, Databricks, Figma, Canva, Reddit, and arXiv. | keep |
| Pricing and coding-agent variants | `B-40`, `B-41`, `B-50` - `B-52`, `B-60`, `B-61` | Pricing entries are validated by prior blind retests; coding-agent variants are title/caption-assisted but visually aligned to their workflow. | keep |
| Model families and generation tools | `D-14`, `D-30`, `D-40` - `D-47`, `D-50`, `D-54`, `D-56`, `D-60`, `D-70`, `D-71` | Provider/model families and media tools are mostly logo-backed. Exact model generation remains caption-supported where family visuals are intentionally similar. | keep |
| Editor/history residuals | `F-37`, `F-38`, `H-58` - `H-62` | Cursor/background-agent and historical/event visuals have enough category cues for residual coverage. Exact date/event names remain caption-supported. | keep |

## Registry Reconciliation

- `B-pricing` can be marked `reviewed`. `semantic-regen-001` and follow-up
  blind retests show B-50/B-51/B-52 pricing layouts are distinguishable.
- `D-reasoning-models` can be marked `reviewed`. `D-openai-model-series`,
  `model_distinction_rules.md`, and `semantic-regen-001` retests define the
  rule: o-series exact identity is caption-supported, while reasoning type
  distinction is visible.

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/residual_coverage_2026-06-06/residual_coverage_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/residual_coverage_2026-06-06/residual_coverage_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/residual_coverage_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/residual_coverage_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/residual_coverage_2026-06-06/response_template.csv`

## Judgment

Residual coverage passes. No new regeneration is required for this cleanup unit.
