# Image and video generation review

Date: 2026-06-06

Cluster: `D-image-video-generation`
Pass mode: `type_distinction`

## Findings

| entry | title | output type | judgment |
| --- | --- | --- | --- |
| `D-51` | Imagen | still image generation | keep: image input/output panels and still-image batch are visible |
| `D-52` | Sora | video model | keep: video timeline and OpenAI context are visible; exact Sora vs Veo is caption-supported |
| `D-53` | Veo | video model | keep: video timeline and Google/DeepMind context are visible; exact Veo vs Sora is caption-supported |
| `D-55` | Nano Banana | image generation/editing | keep: image model/editing workflow and Gemini-family cue are visible |
| `D-57` | Flow | creator-facing video studio | keep: storyboard/timeline/tool surface is distinct from raw video model |
| `D-58` | Whisk | image remix/blending | keep: ingredient images flowing into remix output is distinct |

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/image_video_generation_2026-06-06/image_video_generation_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/image_video_generation_2026-06-06/image_video_generation_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/image_video_generation_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/image_video_generation_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/image_video_generation_2026-06-06/response_template.csv`

## Judgment

No new regeneration required in U007. The cluster passes at the intended `type_distinction` level: still image, video model, creator workflow, and remix workflow are separable.
