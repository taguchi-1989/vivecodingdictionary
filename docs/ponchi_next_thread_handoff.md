# Ponchi next thread handoff

This is the quick restart note for the next Codex thread.

## State at handoff

- Working branch: `main`.
- Previous checkpoint commit before this continuation: `c9d605c`.
- Current tracked 2:1 base progress: 350 / 350.
- Current official overlay status: 133 entries in `overlay_audit` and 3 entries
  still in `overlay_wait`. No rows remain in `blocked_brand_asset`.
- Current non-brand status: 214 `logo_avoid` / confirmed-logo-less entries are in `color_audit` with
  staged review-pending base candidates.
- Current staged final-candidate status: 347 / 350 entries are staged as
  review-pending or accepted final candidates without changing
  `assets/ponchi/final/`.
- Current color-policy status: 347 mechanical color passes, 0 color reviews,
  and 0 color failures. Treat the 347 staged files as review candidates only,
  not final-ready images.
- Wave 004 is complete: 60 / 60 generated bases, 60 / 60 base audit pass.
- Wave 005 is complete: 60 / 60 generated bases, 60 / 60 base audit pass.
- Wave 006 is complete: 50 / 50 generated bases, 50 / 50 base audit pass.
- Latest verified base batch: `ponchi-batch-002` already had 20 / 20 base audit pass.
- Next target: official logo overlay cleanup and final-candidate review for the
  remaining `overlay_wait` rows: B-23 AWS, C-8 Microsoft AI, and C-12 TSMC.

## Files to read first

- `docs/ponchi_progress_overview.md`
- `docs/ponchi_wave_004_handoff.md`
- `docs/ponchi_wave_004_audit.md`
- `docs/ponchi_batch_013_progress_summary.md`
- `docs/ponchi_batch_014_progress_summary.md`
- `docs/ponchi_batch_015_progress_summary.md`
- `docs/ponchi_batch_016_progress_summary.md`
- `docs/ponchi_batch_017_progress_summary.md`
- `docs/ponchi_batch_018_progress_summary.md`
- `docs/ponchi_wave_005_handoff.md`
- `docs/ponchi_wave_005_audit.md`
- `docs/ponchi_wave_006_handoff.md`
- `docs/ponchi_wave_006_audit.md`
- `docs/ponchi_batch_001_progress_summary.md`
- `docs/brand_usage_audit.md`
- `docs/ponchi_color_acceptance_gate.md`
- `docs/ponchi_color_audit_summary.md`
- `ledgers/ponchi_color_audit.csv`
- `ledgers/ponchi_generation_batches.csv`

## Current stage counts

| stage | count |
| --- | ---: |
| `color_audit` | 214 |
| `overlay_wait` | 3 |
| `overlay_audit` | 133 |

## Restart plan

1. Continue official logo overlay cleanup and final-candidate review.
   The current color-policy gate is clean: 347 pass, 0 review, 0 fail.
2. Keep Batch 012-014 best practices:
   - use abstract non-brand metaphors for `logo_avoid`;
   - keep white clearspace only where an official overlay is required;
   - never ask image generation to invent logos, product UI, icons, or brand marks.
3. Keep the color gate active. All currently staged review-pending candidates
   pass `scripts/ponchi_color_audit.py`, but new overlays or regenerated bases
   must rerun the audit before final promotion.
4. Start from remaining `overlay_wait` rows, confirm/import official assets,
   overlay only deterministic official logos, then audit candidates.
5. Run image audit, color audit, batch audit, batch report, and dashboard refresh.
6. Stop for a commit/handoff checkpoint whenever the visible成果物 count grows past the next heavy threshold.

## Current continuation contents

The current continuation has completed Batch 013, Batch 014, Batch 015, Batch 016, Batch 017, Batch 018, and Batch 001 base generation and should
include:

- Batch 013 prompt briefs under `assets/ponchi/pipeline_prompts/ponchi-batch-013/`;
- Batch 013 raw generated images and normalized `1254x627` bases under
  `assets/ponchi/experiments/batches/ponchi-batch-013/`;
- Batch 013 base audit CSV, Markdown audit, contact sheet, batch audit, and
  batch report;
- Batch 014 prompt briefs under `assets/ponchi/pipeline_prompts/ponchi-batch-014/`;
- Batch 014 raw generated images and normalized `1254x627` bases under
  `assets/ponchi/experiments/batches/ponchi-batch-014/`;
- Batch 014 base audit CSV, Markdown audit, contact sheet, batch audit, and
  batch report;
- Batch 015 prompt briefs under `assets/ponchi/pipeline_prompts/ponchi-batch-015/`;
- Batch 015 raw generated images and normalized `1254x627` bases under
  `assets/ponchi/experiments/batches/ponchi-batch-015/`;
- Batch 015 base audit CSV, Markdown audit, contact sheet, batch audit, and
  batch report;
- Wave 005 audit and handoff docs;
- Batch 016 prompt briefs under `assets/ponchi/pipeline_prompts/ponchi-batch-016/`;
- Batch 016 raw generated images and normalized `1254x627` bases under
  `assets/ponchi/experiments/batches/ponchi-batch-016/`;
- Batch 016 base audit CSV, Markdown audit, contact sheet, batch audit, and
  batch report;
- Batch 017 prompt briefs under `assets/ponchi/pipeline_prompts/ponchi-batch-017/`;
- Batch 017 raw generated images and normalized `1254x627` bases under
  `assets/ponchi/experiments/batches/ponchi-batch-017/`;
- Batch 017 base audit CSV, Markdown audit, contact sheet, batch audit, and
  batch report;
- Batch 018 prompt briefs under `assets/ponchi/pipeline_prompts/ponchi-batch-018/`;
- Batch 018 raw generated images and normalized `1254x627` bases under
  `assets/ponchi/experiments/batches/ponchi-batch-018/`;
- Batch 018 base audit CSV, Markdown audit, contact sheet, batch audit, and
  batch report;
- Wave 006 audit and handoff docs;
- Batch 001 prompt briefs under `assets/ponchi/pipeline_prompts/ponchi-batch-001/`;
- Batch 001 raw generated images and normalized `1254x627` bases under
  `assets/ponchi/experiments/batches/ponchi-batch-001/`;
- Batch 001 base audit CSV, Markdown audit, contact sheet, batch audit, and
  batch report;
- progress overview, dashboard, and this restart note updated to 350 / 350 for
  generated 2:1 bases.

Batch 002 already had 20 / 20 generated 2:1 bases and 20 / 20 base audit pass.
It now has 2 `overlay_wait` entries and 18 `overlay_audit` entries.

The current continuation also applied and staged deterministic official overlays:

- Batch 001: B-1, B-3, B-6, B-8.
- Batch 002: B-10, B-14, B-15, B-16, B-17, B-18, B-24, B-25, B-26, B-27.
- Batch 003: B-30, B-31, B-32, B-33, B-40, B-41, B-50, B-51, B-52, B-60, B-61, C-1, C-2, C-3, C-4, C-5, C-6, C-7, C-9.
- Batch 004: C-10, C-11, C-13, C-14, C-80, C-81, C-82, C-83.
- Batch 005: D-1 - D-4, D-10 - D-14, D-20 - D-26, D-30, D-35, D-40, D-41.
- Batch 006: D-42, D-43, D-44, D-45, D-46, D-47, D-50, D-51, D-52, D-53, D-54, D-55, D-57, D-58, D-60, D-70, D-71.
- Batch 008: F-10, F-11, F-12, F-13, F-14, F-15, F-16, F-17, F-20, F-21, F-30, F-34, F-35, F-36.
- Batch 009: F-37, F-38, F-40, F-41, F-44, F-50, F-60, F-61, F-62.
- Batch 010: F-80, F-82, F-83, F-84, F-86, F-90, F-110, F-120, F-121, F-122.
- Batch 011: F-140, F-141, F-153, F-170, F-171, F-172, F-180, F-181, F-200.

These are review-pending final candidates only. `assets/ponchi/final/` was not
changed.

Latest Meta AI note: C-4 uses
`assets/logos/meta-ai/meta-ai-orbit-logo-gradient-3d_light.goto.png`, rendered
from the official Meta AI SVG
`https://www.meta.ai/images/meta-ai-orbit-logo-gradient-3d_light.svg`. Local
ImageMagick rendered that SVG blank/white, so the unchanged SVG was opened
directly in local Chrome and captured as a transparent PNG before deterministic
overlay.

Latest Canva note: B-33 uses
`assets/logos/canva/Canva-logos/Canva logos/png/512x512/Canva type logo_512x180.png`,
from Canva's official developer brand guidelines package
(`https://www.canva.dev/docs/connect/guidelines/brand/`, ZIP
`https://www.canva.dev/assets/connect/Canva-logos.zip`). ZIP metadata files
were removed from the extracted folder.

Latest Stability AI note: D-54 Stable Diffusion uses
`assets/logos/stability-ai/stability-ai-white-dot-on-approved-blue-plate.png`,
which places the unchanged official white Stability AI header logo
`assets/logos/stability-ai/stability-ai-white-dot-desktop.png` on an approved
`#123E82` plate for visibility. The source was the official Stability AI
homepage (`https://stability.ai/`, Squarespace logo asset). A dedicated Stable
Diffusion product logo was not confirmed, so this is review-pending as an
organization overlay.

Latest Google Flow note: D-57 uses
`assets/logos/google-flow/flow_favicon_w_on-approved-blue-plate.png`, which
places the unchanged official white Flow favicon
`assets/logos/google-flow/flow_favicon_w.png` on an approved `#123E82` plate.
The source was the official Google Labs Flow page
(`https://labs.google/fx/tools/flow`, canonical `https://flow.google/`). A
standalone Flow lockup was not confirmed, so this is review-pending as an
official icon overlay.

Latest Google Whisk note: D-58 uses
`assets/logos/google-whisk/whisk_favicon_b.svg`, the official black Whisk
favicon linked from the Google Labs Whisk page
(`https://labs.google/fx/tools/whisk`, asset
`https://labs.google/fx/icons/favicon/whisk_favicon_b.svg`). A standalone
Whisk lockup was not confirmed, so this is review-pending as an official icon
overlay.

Latest Seedance note: D-56 source review checked the official Seedance page
`https://seed.bytedance.com/en/seedance` and saved the current fetched page as
`assets/logos/seedance/seedance-official-page-2026-06-03.html` alongside the
earlier saved page. The fetched page confirms the Seedance page/title and a
shared site favicon / ByteDance Seed page mark, but not a distinct Seedance
product logo or lockup. D-56 is now a confirmed logo-less `color_audit`
candidate using the palette-normalized base image. Do not substitute
ByteDance, Doubao, Jimeng, fal.ai, or Replicate branding for Seedance.

Latest SuperClaude Framework note: F-85 source review checked the original
`https://github.com/NomenAK/SuperClaude` repository and the current
`https://github.com/SuperClaude-Org/SuperClaude_Framework` repository. The
README was saved at
`assets/logos/superclaude/SuperClaude_Framework_README.md`. No
SuperClaude-specific official logo, icon, or lockup asset was found; README
images are badges or external service marks only. F-85 is now a confirmed
logo-less `color_audit` candidate, using the normalized base image rather than
any synthetic logo. Do not use Claude/Anthropic marks, GitHub/SuperClaude
organization badges, or a synthesized "SuperClaude" wordmark.

Latest YouTube creator channel icon note: C-80 AI大学, C-81 にゃんた, C-82
まさお, and C-83 AI の羅針盤 now use official YouTube channel avatars as
review-pending official icon overlays. Source pages and unchanged 900x900
avatars are saved under:
`assets/logos/ai-daigaku/`, `assets/logos/nyanta/`,
`assets/logos/masao/`, and `assets/logos/ai-compass/`. C-83's source page is
`https://www.youtube.com/@compassinai` and displays `AI時代の羅針盤`, while the
ledger title remains `AI の羅針盤`; keep that naming mismatch as a final-review
note. The avatar rectangle is the only off-palette exception; do not allow
channel colors, YouTube UI, thumbnails, mascot substitutes, or portrait
likenesses in the generated illustration body.

Latest Amical note: D-70 uses `assets/logos/amical/amical-icon.png`, the
official app icon from the official Amical GitHub/website sources
(`https://github.com/amicalhq/amical`, `https://amical.ai/`). Source files are
saved under `assets/logos/amical/`, including the repo README, GitHub tree,
homepage HTML, SVG/PNG icon, and README header. This source identifies Amical
as a local-first AI dictation/note-taking app, while the current D-70 entry
prose still describes a Korean/NHN medical AI solution; keep D-70
review-pending until that content mismatch is reconciled. Do not use README
badges, store buttons, integration icons, product UI screenshots, or generated
Amical wordmarks as substitutes.

Latest Microsoft Copilot note: B-15, B-16, and B-17 use
`assets/logos/microsoft-copilot/copilot-official-inline-icon.svg`, extracted
from the official Copilot homepage `https://copilot.microsoft.com/` sidebar
brand button. The source page was saved as
`assets/logos/microsoft-copilot/copilot-homepage.html`; the official wordmark
and favicon were also saved under `assets/logos/microsoft-copilot/`.
Microsoft.com marketing pages for Microsoft Copilot, Microsoft 365 Copilot,
Edge Copilot, and Microsoft AI were reviewed locally in separate passes. The
current Microsoft AI page was saved as
`assets/logos/microsoft-ai/microsoft-ai-page.html` and confirms the official
page title plus UHF text brand link `Microsoft AI`, but does not provide a
dedicated Microsoft AI logo image or lockup. B-16 and B-17 remain
review-pending as Copilot-family icon overlays rather than confirmed dedicated
product lockups. C-8 Microsoft AI remains in `overlay_wait`; the Microsoft AI
page text and favicon are not sufficient as an organization logo overlay.

Latest Windsurf note: B-6 uses
`assets/logos/windsurf/windsurf-black-wordmark.svg`, the official black
Windsurf wordmark from the official brand page `https://windsurf.com/brand`.
The brand page was saved as `assets/logos/windsurf/windsurf-brand.html`, and
the official black wordmark/symbol SVG and PNG assets are saved under
`assets/logos/windsurf/`. The overlay output is
`assets/ponchi/experiments/batches/ponchi-batch-001/B-6_overlay_1254x627.png`
with metadata
`assets/ponchi/experiments/batches/ponchi-batch-001/B-6_overlay_1254x627.meta.json`.
The generated body was palette-normalized before re-compositing. Keep B-6
review-pending before final promotion because density was accepted with a
warning for the spacious logo composition; do not recolor, outline, rotate,
stretch, shadow, or otherwise modify the official wordmark.

Latest Gemini note: B-1, B-52, and D-1 - D-4 use the official Gemini sparkle
asset from `https://gemini.google.com/` /
`https://www.gstatic.com/lamda/images/gemini_sparkle_4g_512_lt_f94943af3be039176192d.png`,
saved as `assets/logos/gemini/gemini_sparkle_4g_512_lt.png`.
D-55 Nano Banana uses the same official Gemini sparkle as a Gemini-family
overlay because the entry identifies Nano Banana as Gemini 2.5 Flash Image; a
dedicated Nano Banana product logo was not confirmed.

Latest Devin note: B-10 uses
`assets/logos/devin/devin-official-header-mark.svg`, extracted from the
official Devin homepage header (`https://devin.ai/`, inline
`site-header__logo` SVG), as a review-pending official mark overlay.

Latest Aqua Voice note: B-18 uses
`assets/logos/aqua-voice/aquavoice-favicon.png`, the official favicon linked
from the official Aqua Voice homepage (`https://aquavoice.com/`, asset
`https://framerusercontent.com/images/KO3UUG0mbyyUBnMxZ3jjJyQu8I.png`), as a
review-pending official icon overlay. A standalone Aqua Voice lockup was not
confirmed, so do not synthesize a wordmark.

Latest ACE-Step note: B-61 uses
`assets/logos/ace-step/acestep_logo.png`, the ACE-Step-specific logo from the
official ACE-Step 1.5 GitHub repo
(`https://github.com/ace-step/ACE-Step-1.5`, raw asset
`https://raw.githubusercontent.com/ace-step/ACE-Step-1.5/main/assets/acestep_logo.png`).
The black square source artwork is preserved unchanged; do not crop it into a
transparent wordmark or substitute ACE Music / ACE Studio / StepFun logos.

Latest Google Cloud note: B-24 uses the official Google Cloud lockup referenced
from `https://cloud.google.com/` /
`https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg`, saved as
`assets/logos/google-cloud/google-cloud-logo-fullcolor.svg`. B-27 Vertex AI uses
`assets/logos/google-cloud/product-icons/core-products-icons/Unique Icons/Vertex AI/SVG/VertexAI-512-color.svg`,
imported from the official Google Cloud Core Products Icons ZIP linked by
`https://cloud.google.com/icons/`
(`https://services.google.com/fh/files/misc/core-products-icons.zip`), as a
review-pending product-icon overlay.

Latest Azure note: B-25 uses
`assets/logos/azure/Azure_Public_Service_Icons_V23/Azure_Public_Service_Icons/Icons/other/10018-icon-service-Azure-A.svg`,
and B-26 uses
`assets/logos/azure/Azure_Public_Service_Icons_V23/Azure_Public_Service_Icons/Icons/ai + machine learning/03438-icon-service-Azure-OpenAI.svg`.
Both came from the official Microsoft Azure Architecture Icons package
(`https://learn.microsoft.com/en-gb/azure/architecture/icons/`, ZIP
`https://arch-center.azureedge.net/icons/Azure_Public_Service_Icons_V23.zip`).

Latest Genspark note: B-14 uses the official favicon from
`https://www.genspark.ai/favicon.ico`, saved as
`assets/logos/genspark/genspark-favicon.ico`. The full brand lockup page still
returned 403 from local shell access, so this remains review-pending.

Latest Groq note: C-13 uses `assets/logos/groq/groq-wordmark-official-inline.svg`,
extracted from the official Groq homepage header branding SVG at
`https://groq.com/`. The official Sanity-hosted McLaren Formula 1 partner
lockup from the same site was source-reviewed and rejected for standalone Groq
usage.

Latest Moonshot AI note: C-10 uses
`assets/logos/moonshot-ai/moonshot-inline-logo.png`, extracted from the official
Moonshot AI homepage JavaScript chunk at `https://www.moonshot.cn/` /
`https://statics.moonshot.cn/moonshot-ai/assets/chunks/chunk-CKQj9p3E.js`.
The official white transparent logo is placed unchanged on a plain dark-blue
composition plate for visibility.

Latest Z.ai note: C-11 uses `assets/logos/z-ai/z-ai-logo-official.svg` from the
official Z.ai homepage (`https://z.ai/`, asset
`https://z-cdn.chatglm.cn/z-ai/static/logo.svg`). The overlay uses
`assets/logos/z-ai/z-ai-logo-official.512.png`, rendered from the official SVG
for crisp edges.
D-45 GLM uses the same official Z.ai icon as a developer/organization overlay
because the entry identifies GLM as a Z.ai model family. A dedicated GLM product
logo was not confirmed.

Latest Kimi note: D-44 uses `assets/logos/kimi/kimi-icon-official.webp`, from
the official Moonshot AI homepage (`https://www.moonshot.cn/`, asset
`https://statics.moonshot.cn/moonshot-ai/assets/static/kimi-icon.ByIGCGon.webp`).

Latest Qwen note: D-43 uses
`assets/logos/qwen/qwen-logo-official-light-header.png`, exported by the
official Qwen site JS module `58809` in
`https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.60/js/9496.js` from
`https://qwen.ai/`. The lighter/darker official variants were both saved under
`assets/logos/qwen/`; the white-canvas overlay uses the darker readable one.

Latest DeepSeek note: D-46 and D-47 use
`assets/logos/deepseek/deepseek-logo-official.png` from the official DeepSeek
homepage (`https://www.deepseek.com/`, asset
`https://cdn.deepseek.com/logo.png?x-image-process=image%2Fresize%2Cw_1920`).

Latest OpenAI note: B-3 ChatGPT, B-8 Codex, and B-51 ChatGPT の料金プラン now use
the same imported official OpenAI wordmark as C-1 and the OpenAI model entries:
`assets/logos/openai/openai_wordmark_black_official_template_layer.png`, taken
from the official OpenAI partnership template package
`https://cdn.openai.com/brand/OpenAI-Partnership-Templates-2025.zip`. Dedicated
ChatGPT/Codex lockups were not imported, so these remain review-pending
OpenAI-brand overlays.

Latest xAI note: D-30 uses `assets/logos/xai/xai-favicon.ico`, the official
root favicon from `https://x.ai/favicon.ico`. The broader xAI site remained
Cloudflare-protected from local shell access, so this favicon overlay remains
review-pending.

Latest Google DeepMind note: D-60 uses
`assets/logos/google-deepmind/google_deepmind_48dp.svg`, the official icon from
`https://deepmind.google/`, asset
`https://storage.googleapis.com/gdm-deepmind-com-prod-public/icons/google_deepmind_48dp.svg`.
D-42 Gemma, D-51 Imagen, and D-53 Veo use the same official Google DeepMind
icon as a review-pending organization icon overlay. The official Google
DeepMind models page (`https://deepmind.google/models/`) lists Gemma, Imagen,
and Veo in the Google DeepMind model family.

Latest Llama note: D-40 uses
`assets/logos/llama/llama-official-favicon.svg`, the official Meta icon
referenced by `https://www.llama.com/` as
`https://static.xx.fbcdn.net/rsrc.php/yf/r/-7pQO6hUGK_.svg`. The saved preload
SVG is the official Meta wordmark, but no dedicated Llama product lockup was
confirmed in this pass. Treat D-40 as a review-pending organization icon
overlay, not a Llama-specific product logo.

Do not promote any generated base to `assets/ponchi/final/` without explicit
approval.
