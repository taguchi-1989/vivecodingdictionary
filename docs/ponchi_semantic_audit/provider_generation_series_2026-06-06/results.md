# Provider generation series review

Date: 2026-06-06

Cluster: `D-provider-generation-series`
Pass mode: `cluster_family`

## Judgment

This cluster is not suitable for strict `exact_entry` image-only judgment. The images can honestly show provider family, generation ladder, tier/capability direction, and rough milestone, but exact distinctions such as Gemini 2 vs 2.5 or Claude 4 vs 4.5 need surrounding title/caption support.

## Findings

| entry | title | provider family | exact-entry visual status | action |
| --- | --- | --- | --- | --- |
| `D-1` | Gemini 2 series | visible | caption_required | keep |
| `D-2` | Gemini 2.5 series | visible | caption_required | keep |
| `D-3` | Gemini 3 series | visible | caption_required | keep |
| `D-4` | Gemini 3.1 series | visible | caption_required | keep |
| `D-10` | Claude 3 series | visible | caption_required | keep |
| `D-11` | Claude 3.5 series | visible | caption_required | keep |
| `D-12` | Claude 4 series | visible | caption_required | keep |
| `D-13` | Claude 4.5 series | visible | caption_required | keep |
| `D-20` | GPT-5 series | visible | caption_required | keep |
| `D-21` | GPT-4 series | visible | caption_required | keep |

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/provider_generation_series_2026-06-06/provider_generation_series_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/provider_generation_series_2026-06-06/provider_generation_series_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/provider_generation_series_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/provider_generation_series_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/provider_generation_series_2026-06-06/response_template.csv`

## Notes

- The brand/family marks are strong enough to keep the series recognizable.
- The exact generation number is a title/caption responsibility for all entries in this unit.
- No regeneration was performed because trying to invent fine-grained visual differences for minor generation deltas would overstate what the image can honestly encode.
