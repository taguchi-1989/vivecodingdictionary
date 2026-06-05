# Model Distinction Rules

作成日: 2026-06-06

## Problem

モデル世代は、サービスや物理ハードウェアと違って、画像だけで厳密に判別しにくい。

例:

- `GPT-4` と `GPT-5`
- `Claude 4` と `Claude 4.5`
- `Gemini 2.5 Pro` と別の frontier model
- coding が強いモデル同士

これらを無理に「一目で分かる絵」にすると、実際には根拠の弱い能力差や架空の特徴を描くリスクがある。

## Principle

モデル系は、まず「何を区別したいのか」を分ける。

| distinction axis | what can be shown | example |
| --- | --- | --- |
| `family` | provider / model family | GPT系, Claude系, Gemini系, Grok系 |
| `era` | old/new generation ladder | GPT-1/2 → GPT-3 → GPT-4 → GPT-5 |
| `capability_milestone` | visible added capability | text-only, vision, tool use, coding, long context, realtime/audio |
| `model_type` | reasoning / general / open-weight / image / video | o1/o3 vs GPT, gpt-oss, Imagen/Veo |
| `product_context` | where users meet the model | ChatGPT, Claude, Gemini app, API, Vertex/Azure |
| `deployment_context` | open/closed, cloud/API/local | gpt-oss vs closed frontier model |
| `tier_role` | speed/depth/cost tradeoff | Pro / Flash / Lite, Opus / Sonnet / Haiku |

If an entry has no stable visible milestone, use `honest_ambiguous` and rely on text labels/captions in the book.

## Visual Rules by Group

### OpenAI Model Series

| entry | visual target | pass mode |
| --- | --- | --- |
| `D-25` GPT-1 / GPT-2 | early text-only model stack, small research-era blocks | `capability_milestone` |
| `D-24` GPT-3 | large text completion model, prompt-to-completion scale jump | `capability_milestone` |
| `D-21` GPT-4 | stronger general model with vision/multimodal doorway if supported by entry text | `capability_milestone` |
| `D-20` GPT-5 | latest frontier/general model, broader capability hub; do not invent unsupported internal architecture | `honest_ambiguous` unless entry text gives a stable feature |
| `D-22` o1 | slow/deep reasoning ladder, math/code optimization cards | `type_distinction` |
| `D-23` o3 | reasoning successor; must be paired with o1 as a later/deeper reasoning branch, not a generic GPT | `type_distinction` |
| `D-26` gpt-oss | open-weight/package/deployment diagram, not ChatGPT service | `deployment_context` |

Notes:

- `GPT-4` vs `GPT-5` should not be judged as a strict visual identity test unless the entry text defines a concrete capability milestone.
- For GPT frontier models, a better target is “which generation ladder / capability milestone does this represent?” rather than “can a stranger name GPT-5 from the picture alone?”
- Do not draw internal architecture such as MoE unless the project source explicitly requires it.

### Claude Model Series

| entry | visual target | pass mode |
| --- | --- | --- |
| `D-10` Claude 3 系 | Opus/Sonnet/Haiku tier triangle | `tier_role` |
| `D-11` Claude 3.5 系 | coding/agentic improvement milestone if supported by entry text | `capability_milestone` |
| `D-12` Claude 4 系 | next generation ladder with larger/deeper work capacity | `honest_ambiguous` unless entry text defines a stable feature |
| `D-13` Claude 4.5 系 | minor/advanced update; likely caption-dependent | `honest_ambiguous` |
| `D-14` Claude Mythos Preview | specialized/limited preview model; show scope restriction, not generic Claude | `type_distinction` |

### Gemini Model Series

| entry | visual target | pass mode |
| --- | --- | --- |
| `D-1` Gemini 2 系 | Gemini family generation base | `cluster_family` |
| `D-2` Gemini 2.5 系 | Pro / Flash / Flash-Lite tier roles | `tier_role` |
| `D-3` Gemini 3 系 | future/next generation; caption-dependent unless entry text gives stable feature | `honest_ambiguous` |
| `D-4` Gemini 3.1 系 | minor update; caption-dependent | `honest_ambiguous` |

### Image / Video Models

This group can be stricter because output type is visible.

| entry | visual target | pass mode |
| --- | --- | --- |
| `D-51` Imagen | still image generation, prompt-to-image variants | `type_distinction` |
| `D-53` Veo | video generation engine, frames/time/camera motion | `type_distinction` |
| `D-57` Flow | creator-facing video studio/workflow | `type_distinction` |
| `D-58` Whisk | image remix from subject/scene/style references | `type_distinction` |

## Review Decisions

Use these decisions for model clusters:

| decision | meaning | next action |
| --- | --- | --- |
| `clear_milestone` | image shows a real capability/tier/type milestone | keep or candidate promote |
| `family_only` | family is clear but exact generation is not | acceptable for `cluster_family`; review for exact entries |
| `caption_required` | image can work only with title/caption | acceptable for `honest_ambiguous` |
| `misleading_type` | image suggests the wrong model type, e.g. audio for reasoning | recompose |
| `invented_feature_risk` | image implies unsupported architecture/capability | reject/recompose |

## Goal Template for Model Clusters

```text
Goal: cluster_id=<model cluster> のモデル画像を、family / era / capability_milestone / model_type / deployment_context の軸で監査する。exact entry 名を当てることを必須にせず、根拠のある視覚差分だけを pass とする。根拠が弱い世代差は honest_ambiguous として本文・キャプション補助に回し、架空のアーキテクチャや未確認能力を描かない。
```
