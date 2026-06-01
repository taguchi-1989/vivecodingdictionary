# Ponchi chapter logo overlay audit - 2026-06-01

This audit records the first official-logo overlay pass for the chapter trial
images generated on 2026-06-01.

## Inputs

Base folder:

`assets/ponchi/experiments/regeneration/chapter-trials-2026-06-01/`

Official OpenAI source:

- Brand page: `https://openai.com/brand/`
- Official package: `https://cdn.openai.com/brand/OpenAI-Partnership-Templates-2025.zip`
- Imported package: `assets/logos/openai/OpenAI-Partnership-Templates-2025.zip`
- Extracted source: `assets/logos/openai/OpenAI-Partnership-Templates-2025/02.03_Brand Partnerships_Templates/Brand Partnerships_Template_Horizontal.psb`
- Overlay asset: `assets/logos/openai/openai_wordmark_black_official_template_layer.png`

Comparison sheet:

`assets/ponchi/experiments/regeneration/chapter-trials-2026-06-01/openai_logo_overlay_size_comparison_sheet.png`

## Overlay Results

| Entry | Base | Overlay output | Logo | Params | Status |
| --- | --- | --- | --- | --- | --- |
| C-1 OpenAI | `C-1_openai_chapter_trial_v3_1254x627.png` | `C-1_openai_chapter_trial_v3_official_openai_logo_480w_1254x627.png` | OpenAI wordmark | `width=480`, `x=726`, `y=18` | candidate |
| H-53 ChatGPT 登場 | `H-53_chatgpt-launch_chapter_trial_v3_1254x627.png` | `H-53_chatgpt-launch_chapter_trial_v3_official_openai_logo_480w_1254x627.png` | OpenAI wordmark | `width=480`, `x=726`, `y=18` | candidate, brand choice needs review |

The first standard pass used `width=520`, `x=686`, `y=36`. The smaller
`480px` pass is preferred for these two images because the OpenAI wordmark is
tall enough that `520px` sits too low against nearby diagram or crowd elements.

## Density Gate

The overlay script was run with:

```powershell
python scripts\composite_official_logo.py `
  --audit-density `
  --min-bbox-coverage 0.50
```

Results:

| Entry | Base bbox coverage | Gate |
| --- | ---: | --- |
| C-1 | 0.656 | pass |
| H-53 | 0.549 | pass |

## Not Yet Overlaid

| Entry | Reason |
| --- | --- |
| B-1 Gemini | Official Gemini/Google asset selection is still not imported. Keep as source review / blocked for overlay. |
| D-12 Claude 4 系 | Official Claude/Anthropic asset selection is still not imported. Keep as source review / blocked for overlay. |

## Judgment

Do not promote these candidates to `assets/ponchi/final/` yet. They prove the
pipeline path works with a real official asset, but final use still requires:

- deciding whether `H-53 ChatGPT 登場` should use the OpenAI wordmark or a
  ChatGPT-specific official asset if one is imported;
- importing official Gemini and Claude/Anthropic assets before B-1 and D-12 can
  proceed;
- final visual review at the actual book preview size.
