# Ponchi chapter trial generation audit - 2026-06-01

This audit records the first chapter-by-chapter trial set generated from the current ponchi image rules.

## Scope

- Purpose: create one fresh 2:1 trial image for each major chapter group.
- Output folder: `assets/ponchi/experiments/regeneration/chapter-trials-2026-06-01/`
- Final replacement status: not applied to `assets/ponchi/final/`.
- Base output size from generator: 1774x887.
- Standardized review size: 1254x627.
- Contact sheet: `assets/ponchi/experiments/regeneration/chapter-trials-2026-06-01/chapter_trials_selected_contact_sheet.png`

## Results

| Entry | Topic | Standard image | Base judgement | Logo follow-up |
| --- | --- | --- | --- | --- |
| A-1 | まえがき | `A-1_preface_chapter_trial_1254x627.png` | Good chapter-level bridge metaphor. | Not needed. |
| B-1 | Gemini | `B-1_gemini_chapter_trial_v3_1254x627.png` | V3 improves subject scale and keeps a controlled upper-right logo area. | Needs official Gemini/Google logo placement if used as final. |
| C-1 | OpenAI | `C-1_openai_chapter_trial_v3_1254x627.png` | V3 fixes sparse composition with a larger main hub and clear upper-right area. | Needs official OpenAI logo placement if used as final. |
| D-12 | Claude 4 系 | `D-12_claude-4-series_chapter_trial_v3_1254x627.png` | V3 simplifies the timeline into fewer larger lanes. | Needs official Claude/Anthropic logo placement if used as final. |
| E-1 | SWE-Bench | `E-1_swe-bench_chapter_trial_1254x627.png` | Good evaluation workflow. Uses Character A, not Character B. | Logo usually not required; character choice should be reviewed. |
| F-1 | JavaScript | `F-1_javascript_chapter_trial_1254x627.png` | Good web-to-runtime flow. | Not needed. |
| G-1 | Context | `G-1_context_chapter_trial_1254x627.png` | Good context-container metaphor with supporting characters. | Not needed. |
| H-53 | ChatGPT 登場 | `H-53_chatgpt-launch_chapter_trial_v3_1254x627.png` | V3 makes the crowd denser while preserving a controlled upper-right logo area. | Needs official ChatGPT/OpenAI logo placement if used as final. |
| I-1 | MCP | `I-1_mcp_chapter_trial_1254x627.png` | Good connector/server concept. | No official product logo required unless a specific MCP mark is adopted. |
| J-14 | LLM | `J-14_llm_chapter_trial_1254x627.png` | Good internal model-routing metaphor. | Not needed. |

## Rule Check

- 2:1 ratio: passed for all generated originals and standardized copies.
- Full-canvas illustration: v3 reruns fix the earlier sparse B-1 and C-1 bases. A-1, G-1, I-1, and J-14 remain usable from v1.
- Logo-safe space: v3 uses controlled upper-right space rather than leaving a broad empty half-page. Final logo overlay still needs visual confirmation per brand.
- Base characters: mostly passed. Character A and the robot appear consistently; Character B appears in A-1, G-1, and I-1. E-1 may need a rerun if the teacher/evaluator role should be Character B.
- Temporary people rule: H-53 uses a wider crowd as an abstract audience, which is acceptable under the temporary people exception.

## Density Audit

Approximate non-white bounding-box coverage from the standardized `1254x627` images:

| Entry | BBox coverage | Decision |
| --- | ---: | --- |
| A-1 | 69% | Acceptable. |
| B-1 v1 | 42% | Superseded. Too much open space for a brand base. |
| B-1 v3 | 57% | Improved. Use as current base candidate. |
| C-1 v1 | 45% | Superseded. Main subject is too small. |
| C-1 v3 | 66% | Improved. Use as current base candidate. |
| D-12 v1 | 88% | Superseded. Width is used, but elements are too fine. |
| D-12 v3 | 52% | Improved. Fewer larger lanes. |
| E-1 | 56% | Acceptable with character review. |
| F-1 | 65% | Acceptable. |
| G-1 | 82% | Acceptable. |
| H-53 v1 | 64% | Superseded. Concept is good but crowd can be denser. |
| H-53 v3 | 55% | Improved. Crowd is more intentional, despite lower bbox coverage. |
| I-1 | 70% | Acceptable. |
| J-14 | 66% | Acceptable. |

V3 comparison sheet: `assets/ponchi/experiments/regeneration/chapter-trials-2026-06-01/chapter_trials_v1_v2_v3_comparison_sheet.png`

## Logo Overlay Pass

First official overlay audit:

`docs/ponchi_chapter_logo_overlay_audit_2026-06-01.md`

Current overlay candidates:

- `C-1_openai_chapter_trial_v3_official_openai_logo_480w_1254x627.png`
- `H-53_chatgpt-launch_chapter_trial_v3_official_openai_logo_480w_1254x627.png`

These use the OpenAI wordmark extracted from the official OpenAI partnership
template package. B-1 Gemini and D-12 Claude 4 系 remain blocked until official
Gemini/Google and Claude/Anthropic overlay assets are imported.

## Next Step Before Final Use

For brand/product entries, apply the logo-reference pipeline before promoting anything into `assets/ponchi/final/`:

- B-1 Gemini: add official Gemini/Google logo.
- C-1 OpenAI: add official OpenAI logo.
- D-12 Claude 4 系: add official Claude/Anthropic logo.
- H-53 ChatGPT 登場: add official ChatGPT/OpenAI logo.

The current files should be treated as clean base illustrations, not final branded images.

Before final promotion, apply official logo overlays to the v3 brand bases and run the overlay pipeline density check. If the official lockup collides with a card, arrow, or crowd mark, rerun with the same v3 density target and a slightly lower main diagram.
