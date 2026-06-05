# D OpenAI Model Series Cluster Review

作成日: 2026-06-06

Cluster: `D-openai-model-series`

Master rules:

- `docs/ponchi_semantic_audit/semantic_cluster_registry.md`
- `docs/ponchi_semantic_audit/model_distinction_rules.md`

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/D_openai_model_series_2026-06-06/D_openai_model_series_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/D_openai_model_series_2026-06-06/D_openai_model_series_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/D_openai_model_series_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/D_openai_model_series_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/D_openai_model_series_2026-06-06/response_template.csv`

## Judgment

| entry | pass mode | decision | rationale | action |
| --- | --- | --- | --- | --- |
| `D-20` GPT-5 系 | `honest_ambiguous` | `caption_required` | Broad frontier/general capability hub is visible, but exact GPT-5 identity cannot be honestly enforced from image alone. | keep with caption support |
| `D-21` GPT-4 系 | `capability_milestone` | `caption_required` | Multimodal/general capability cues are visible, but GPT-4 vs GPT-5 remains visually close. | keep with caption support |
| `D-22` o1 系 | `type_distinction` | `clear_milestone` | semantic-regen-001 candidate communicates slow/deep reasoning ladder and avoids audio/Whisper cues. | keep candidate |
| `D-23` o3 系 | `type_distinction` | `family_only` | Branching reasoning/checklist structure suggests reasoning successor, but exact o3 identity remains caption-dependent. | keep; pair with o1 in future focus retest |
| `D-24` GPT-3 系 | `capability_milestone` | `clear_milestone` | Scale-up, text/model progression, and earlier generation feel are visible enough. | keep |
| `D-25` GPT-1 / GPT-2 系 | `capability_milestone` | `recomposed` | Previous image implied modern multimodal/general AI. New semantic-regen-006 candidate shows early text-only research-era scaling. | staged in semantic-regen-006 |
| `D-26` gpt-oss | `deployment_context` | `clear_milestone` | Open-weight/package/deployment context is visible and distinct from ChatGPT service. | keep |

## Fixes

`D-25` was regenerated because the old candidate carried `invented_feature_risk`: robot and broad modern AI dashboard cues were too strong for GPT-1/GPT-2.

New candidate:

- `assets/ponchi/final_candidates/semantic-regen-006/D-25_candidate.png`
- `assets/ponchi/final_candidates/semantic-regen-006/D-25_candidate.webp`

Audit:

- base image audit: pass
- base color audit: pass
- overlay image audit: pass
- overlay color audit: pass

## Cluster-Level Conclusion

This cluster should not be judged by exact entry recognition for every row.

Strict enough:

- `D-22` o1: reasoning type distinction.
- `D-26` gpt-oss: deployment/open-weight distinction.
- `D-25` GPT-1/GPT-2 after semantic-regen-006: early text-only milestone.

Caption-required:

- `D-20` GPT-5 and `D-21` GPT-4: both represent broad frontier GPT capability and should rely on title/caption for exact generation.
- `D-23` o3: reasoning family is visible, exact o3 identity should be caption-supported.

Do not invent visual differences such as unsupported MoE internals, spatial reasoning architecture, or hidden attention mechanisms unless the entry text explicitly establishes them.
