# semantic-regen-002 ponchi prompts

These prompts target wave 2 semantic fixes. Generate base images only. Keep official-logo clearspace blank for deterministic overlays where applicable.

## J-72 H100

```yaml
entry_id: J-72
title: H100
subject_type: hardware_product
subject_stack:
  entry_subject: H100
  visual_subject: deployed Hopper-generation data-center GPU product scaled from one accelerator board into an H100 cluster for LLM training and inference
  supporting_subjects: engineer submitting a large training job; cloud GPU instance boundary; NVLink-like interconnect lanes; stacked server racks
  logo_subject: no logo; product name must be inferred from H100-specific cluster/product role
  excluded_subjects: readable text, fake logos, official icons, NVIDIA marks, brand colors, Blackwell generation timeline, GB200 superchip, consumer RTX card, generic CPU
brand_asset:
  mode: logo_avoid
  asset_name: none
composition_family: semantic_regen
composition_type: product_cluster_structure
view_mode: no_logo
scene_goal: make H100 identifiable as a deployed data-center GPU product and cluster workhorse, not the Blackwell next-generation architecture
main_symbols: one large accelerator board expands into many identical rack GPU modules, joined by thick parallel interconnect lanes, then a large LLM training job and inference endpoint
avoid: readable text, fake logos, official icons, NVIDIA marks, brand colors, Blackwell generation timeline, GB200 superchip, consumer RTX card, generic CPU
```

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for J-72 H100. The image should read as a specific deployed data-center GPU product: left side shows one large accelerator board with stacked memory blocks; center shows many identical accelerator modules connected inside server racks by thick parallel interconnect lanes; right side shows a large model training job flowing into an inference endpoint. Include a small engineer submitting the job. Do not include logos or readable labels.
Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.
Do not use yellow, green, red, purple, brown, orange, rainbow colors, cyan, teal, purple-blue, arbitrary blue variants, decorative blue sparkles, blue background fills, product UI colors, photo thumbnails, colorful charts, or brand colors.
Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading. No readable text, no watermark.

## J-73 Blackwell

```yaml
entry_id: J-73
title: Blackwell
subject_type: hardware_architecture_generation
subject_stack:
  entry_subject: Blackwell
  visual_subject: next-generation NVIDIA GPU architecture after Hopper shown as a timeline and architecture leap toward B200 and GB200-style high-density AI compute
  supporting_subjects: previous-generation accelerator node on the left; next-generation dual-GPU superchip/rack-scale module on the right; FP4-like compact compute tiles; faster interconnect fabric
  logo_subject: no logo; generation must be inferred from next-generation architecture role
  excluded_subjects: readable text, fake logos, official icons, NVIDIA marks, brand colors, plain H100 cluster only, single generic GPU, CPU-only diagram, consumer gaming card
brand_asset:
  mode: logo_avoid
  asset_name: none
composition_family: semantic_regen
composition_type: generation_timeline_comparison
view_mode: no_logo
scene_goal: make Blackwell identifiable as the post-H100 architecture generation and rack-scale leap, not just another H100 cluster
main_symbols: five-step architecture timeline ending in a larger next-generation module, two accelerator dies bridged together, CPU-plus-GPU superchip silhouette, denser memory blocks, faster interconnect fabric, lower-cost inference arrows
avoid: readable text, fake logos, official icons, NVIDIA marks, brand colors, plain H100 cluster only, single generic GPU, CPU-only diagram, consumer gaming card
```

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for J-73 Blackwell. The image should read as a GPU architecture generation after the H100 era: a left-to-right generation timeline leads from smaller prior accelerator blocks to a large next-generation module on the right. The final module should show two accelerator dies bridged together, dense memory stacks, a CPU-plus-GPU superchip silhouette, and rack-scale interconnect fabric. Show inference cost or throughput improving with abstract arrows, not readable labels. Do not include logos or readable generation names.
Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.
Do not use yellow, green, red, purple, brown, orange, rainbow colors, cyan, teal, purple-blue, arbitrary blue variants, decorative blue sparkles, blue background fills, product UI colors, photo thumbnails, colorful charts, or brand colors.
Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading. No readable text, no watermark.

## F-84 Ghostty

```yaml
entry_id: F-84
title: Ghostty
subject_type: terminal_app
subject_stack:
  entry_subject: Ghostty
  visual_subject: GPU-rendered terminal emulator as the fast outer app that hosts shells and long AI-agent output
  supporting_subjects: terminal app frame with tabs and split panes; shell prompt strokes inside; smooth scrolling output strip; settings panel for font and theme; developer at laptop
  logo_subject: official Ghostty brand overlay after source review
  excluded_subjects: readable text, fake logos, official icons, brand colors, real product UI, black full-screen terminal block, shell itself as the main subject, WSL system diagram, AI IDE
brand_asset:
  mode: official_overlay_required
  asset_name: Ghostty
composition_family: semantic_regen
composition_type: terminal_layer_comparison_with_logo_clearspace
view_mode: logo_clearspace
clearspace:
  required: yes
  location: rightmost 40% of top 25% kept completely blank
scene_goal: make Ghostty identifiable as a fast terminal emulator outer app, not bash, WSL, PowerShell, or a generic black terminal
main_symbols: terminal outer window frame around shell panes, tab strip, split panes, long output scroll path, GPU rendering chip feeding smooth screen refresh, settings sliders
avoid: readable text, fake logos, official icons, brand colors, real product UI, black full-screen terminal block, shell itself as the main subject, WSL system diagram, AI IDE
```

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for F-84 Ghostty. Show a terminal emulator as an outer application window, not a black screen: a clean light terminal frame with tabs, split panes, small shell prompt strokes, a long AI-agent output scroll path, and a settings panel for font/theme. Add a small GPU rendering chip icon feeding smooth screen refresh lines into the terminal window. Keep the upper-right logo clearspace blank white.
Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.
Do not use yellow, green, red, purple, brown, orange, rainbow colors, cyan, teal, purple-blue, arbitrary blue variants, decorative blue sparkles, blue background fills, product UI colors, photo thumbnails, colorful charts, or brand colors.
Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading. No readable text, no watermark.

## D-51 Imagen

```yaml
entry_id: D-51
title: Imagen
subject_type: image_generation_model
subject_stack:
  entry_subject: Imagen
  visual_subject: Google DeepMind still-image generation foundation model producing high-quality image outputs from prompts and references
  supporting_subjects: prompt card and reference image card enter a central image model engine; still image gallery output; quality and safety review loop; Gemini or Vertex access shown only as small connector blocks
  logo_subject: official Google DeepMind brand overlay after source review
  excluded_subjects: readable text, fake logos, official icons, brand colors, real product UI, video timeline, playhead, camera movement, scene builder, Flow studio workflow, Whisk remix funnel
brand_asset:
  mode: official_overlay_required
  asset_name: Google DeepMind
composition_family: semantic_regen
composition_type: still_image_model_with_logo_clearspace
view_mode: logo_clearspace
clearspace:
  required: yes
  location: rightmost 40% of top 25% kept completely blank
scene_goal: make Imagen identifiable as a static image generation model, not Flow, Veo, Whisk, or a creative workflow client
main_symbols: prompt and reference image feed a central model engine, one polished still image and controlled variations exit as image cards, no timeline or video controls
avoid: readable text, fake logos, official icons, brand colors, real product UI, video timeline, playhead, camera movement, scene builder, Flow studio workflow, Whisk remix funnel
```

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for D-51 Imagen. The center is a still-image generation model engine. A prompt card and one reference image card enter from the left. The output on the right is a gallery of polished still-image cards plus small controlled variations and a quality/safety review loop. Gemini and Vertex access can appear only as tiny generic connector blocks. Do not show a timeline, playhead, camera path, storyboard, or video editing UI. Keep the upper-right logo clearspace blank white.
Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.
Do not use yellow, green, red, purple, brown, orange, rainbow colors, cyan, teal, purple-blue, arbitrary blue variants, decorative blue sparkles, blue background fills, product UI colors, photo thumbnails, colorful charts, or brand colors.
Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading. No readable text, no watermark.

## D-57 Flow

```yaml
entry_id: D-57
title: Flow
subject_type: creative_video_tool
subject_stack:
  entry_subject: Flow
  visual_subject: Google creator-facing video production studio that orchestrates scene building, camera controls, asset management, and Veo-powered clip generation
  supporting_subjects: browser studio window; scene cards in order; camera-control sliders; asset bin; video clip timeline; Veo model engine as a small backend block
  logo_subject: official Flow brand overlay after source review
  excluded_subjects: readable text, fake logos, official icons, brand colors, real product UI, single still-image generation engine, Imagen-only output gallery, Whisk-style reference remix funnel, generic video model only
brand_asset:
  mode: official_overlay_required
  asset_name: Flow
composition_family: semantic_regen
composition_type: creator_studio_workflow_with_logo_clearspace
view_mode: logo_clearspace
clearspace:
  required: yes
  location: rightmost 40% of top 25% kept completely blank
scene_goal: make Flow identifiable as a video production client/UI that operates Veo and Imagen, not Imagen itself or a generic video model
main_symbols: scene builder cards arranged into a storyboard, camera-control sliders, asset management bin, video timeline, small backend model block, export arrow
avoid: readable text, fake logos, official icons, brand colors, real product UI, single still-image generation engine, Imagen-only output gallery, Whisk-style reference remix funnel, generic video model only
```

Use case: infographic-diagram
Asset type: VibeCodingDictionary ponchi image
Primary request: Create a 2:1 horizontal technical-book ponchi illustration for D-57 Flow. Show a creator-facing video production studio window. Inside it, scene builder cards are arranged into a storyboard, camera-control sliders adjust a shot, an asset bin holds reference images, and a video timeline assembles generated clips. A small backend model engine block sits behind the studio window, making clear the subject is the tool/client layer, not just the model. Keep the upper-right logo clearspace blank white.
Color palette: strict white/black/gray plus approved blue accents only: #FFFFFF, #F7F9FC, #1A1A1A, #6B7280, #EAF1FB, #D6E6FA, #8DB7E8, #3F7FD1, #123E82.
Do not use yellow, green, red, purple, brown, orange, rainbow colors, cyan, teal, purple-blue, arbitrary blue variants, decorative blue sparkles, blue background fills, product UI colors, photo thumbnails, colorful charts, or brand colors.
Style: clean simple editorial line illustration, smooth uniform black lines, flat light gray fills, minimal shading. No readable text, no watermark.

### D-57 focused retry note

The first D-57 candidate was top1 guessed as `D-53 Veo` with confidence 64. The retry must reduce "video model" cues and increase "creator client/tool" cues.

- Make the browser-like studio workspace dominate the canvas: scene list, shot cards, camera control sliders, asset drawer, version history thumbnails, publish/export tray.
- Keep the model engine as a small backstage block, not the central subject.
- Avoid making the video timeline or generated cinematic clips the main feature.
- Add a clear "tool surface controls the backend" structure through cursor/handles/sliders/cards, without readable UI text.

## J-72 focused retry note

The first J-72 candidate was top1 correct but low confidence at 63 because it still competed with Blackwell. The retry must feel like "installed H100 cards powering an AI cluster" rather than a generation architecture.

- Show many identical physical accelerator cards installed in a cluster/rack and rented as cloud GPU instances.
- Add a purchase/provisioning pipeline from cloud instance to training job, then inference endpoint.
- Use dense repeated cards and rack modules, but avoid a left-to-right architecture evolution timeline.
- Avoid next-generation superchip, two-die bridge, CPU+GPU superchip, or performance-generation charts.
