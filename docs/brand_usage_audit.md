# Brand usage audit for ponchi regeneration

This audit records only confirmed sources that can be used for deterministic
brand asset overlays. It is not permission advice; it is a working ledger for
avoiding AI-generated fake logos, icons, marks, mascots, and brand-style
substitutes.

## GitHub / GitHub Copilot

- Source checked: `https://brand.github.com/foundations/logo`
- Official asset package: `https://brand.github.com/GitHub_Logos.zip`
- Local path: `assets/logos/github/GitHub_Logos/`
- Relevant local assets:
  - `GitHub Logos/SVG/GitHub_Invertocat_Black.svg`
  - `GitHub Logos/SVG/GitHub_Lockup_Black.svg`
  - `GitHub Logos/SVG/GitHub_Copilot_Lockup_Black.svg`
  - `GitHub Logos/PNG/Copilot_Icon_Black_Clearspace.png`
- Working rule:
  - Use unchanged official files only.
  - Prefer black marks on white backgrounds for this book's image palette.
  - Do not modify the mark shape or recolor it.
  - Do not imply GitHub sponsorship or endorsement.

## OpenAI / ChatGPT / Codex

- Source checked: `https://openai.com/brand/`
- Source status: official brand guidance confirmed. The page identifies the
  OpenAI name/logo plus ChatGPT and GPT brands as OpenAI trademarks, describes
  wordmark and Blossom usage, and exposes logo downloads subject to OpenAI marks
  terms.
- Official asset package checked: `https://cdn.openai.com/brand/OpenAI-Partnership-Templates-2025.zip`
- Local package: `assets/logos/openai/OpenAI-Partnership-Templates-2025.zip`
- Local extracted source:
  - `assets/logos/openai/OpenAI-Partnership-Templates-2025/02.03_Brand Partnerships_Templates/Brand Partnerships_Template_Horizontal.psb`
- Relevant local asset:
  - `assets/logos/openai/openai_wordmark_black_official_template_layer.png`
- Local status: OpenAI wordmark layer imported from the official partnership
  template. ChatGPT-specific and Codex-specific lockups are still not imported.
- Working rule:
  - Do not generate OpenAI, ChatGPT, or Codex logos, marks, icons, or product UI
    from prompts.
  - Use the OpenAI wordmark only where OpenAI brand identification is acceptable.
  - Keep B-3 and B-8 in `official_logo_source_review_required` until the exact
    asset choice is decided: OpenAI wordmark, ChatGPT-specific asset, or a
    Codex-specific asset if one is officially published.
  - Current chapter trials using this asset:
    - `C-1_openai_chapter_trial_v3_official_openai_logo_480w_1254x627.png`
    - `H-53_chatgpt-launch_chapter_trial_v3_official_openai_logo_480w_1254x627.png`

## Anthropic / Claude

- Source checked: `https://www.anthropic.com/news`
- Official asset package checked: `https://anthropic.com/press-kit`
- Local package: `assets/logos/anthropic/anthropic-media-resources.zip`
- Local extracted source:
  - `assets/logos/anthropic/anthropic-media-resources/Anthropic media resources/Anthropic logos/`
- Relevant local assets:
  - `Claude logos/1 Claude logo/PNG/Claude logo - Slate.png`
  - `Claude logos/2 Claude Code logo/PNG/Claude Code logo - Slate.png`
- Local status: Claude and Claude Code official logo assets imported.
- Working rule:
  - Do not generate Claude or Anthropic marks, icons, or brand-style substitutes
    from prompts.
  - Use the official Claude logo for B-2 and the official Claude Code logo for
    B-7.
  - Treat D-12 as a Claude-family logo item only after deciding whether the
    Claude logo or a model-family-specific treatment is appropriate.

## Google / Gemini

- Source checked: `https://about.google/brand-resource-center/`
- Source status: official Google Brand Resource Center exists and redirects to
  Partner Marketing Hub. Gemini still needs a concrete official product
  icon/lockup selection and any required permission review before use.
- Local status: no local Gemini asset imported yet.
- Working rule:
  - Do not generate Gemini, Google, Android, Gmail, Docs, or Google Cloud marks,
    icons, logos, app UI, or brand-color substitutes from prompts.
  - Keep B-1 in `official_logo_source_review_required` until the exact Gemini
    asset and usage conditions are recorded.

## Cursor / Windsurf

- Cursor source checked: `https://cursor.com/brand`
- Cursor source status: official brand guidelines confirm downloadable brand
  assets, including logos, app icons, avatars, and a preferred horizontal lockup.
- Cursor official asset package checked:
  `https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/brand/cursor-brand-assets.zip`
- Cursor local package: `assets/logos/cursor/cursor-brand-assets.zip`
- Cursor local extracted source: `assets/logos/cursor/cursor-brand-assets/`
- Relevant local asset:
  - `General Logos/Lockup Horizontal/PNG/LOCKUP_HORIZONTAL_2D_LIGHT.png`
- Windsurf status: not yet confirmed in local assets.
- Working rule:
  - Do not generate Cursor or Windsurf marks, icons, logos, or product UI from
    prompts.
  - Use the official Cursor horizontal lockup for B-4.
  - Keep B-6 blocked until an official Windsurf source is confirmed and recorded.

## Vercel / v0

- Source checked: `https://vercel.com/design/brands`
- v0 product docs checked: `https://vercel.com/docs/v0`
- Source status: Vercel publishes brand guidelines and identifies the v0 name
  and logo as Vercel trademarks. The v0 docs confirm v0 as a Vercel product.
- Official v0 asset package checked:
  `https://k2mkucxia43oc7fa.public.blob.vercel-storage.com/front/press/v0-assets.zip`
- Official Vercel asset package checked:
  `https://assets.vercel.com/image/upload/v1662130559/front/press/vercel-assets.zip`
- Local packages:
  - `assets/logos/vercel/v0-assets.zip`
  - `assets/logos/vercel/vercel-assets.zip`
- Local extracted sources:
  - `assets/logos/vercel/v0-assets/v0/`
  - `assets/logos/vercel/vercel-assets/Vercel/`
- Relevant local asset:
  - `Light/v0-logo-light.png`
  - `logotype/light/vercel-logotype-light.png`
- Local status: v0 and Vercel official logo assets imported.
- Working rule:
  - Do not generate v0 or Vercel marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official v0 light logo for B-9 on white logo clearspace.
  - Use the official Vercel light logotype for B-20 on white logo clearspace.

## StackBlitz / Bolt.new

- Source checked: `https://stackblitz.com/github/stackblitz/bolt.new`
- Official repository asset checked:
  `https://github.com/stackblitz/bolt.new/blob/main/icons/logo-text.svg`
- Local assets:
  - `assets/logos/bolt/bolt-logo-text-official.svg`
  - `assets/logos/bolt/bolt-logo-text-official-512.png`
  - `assets/logos/bolt/bolt-public-logo-official.svg`
- Local status: official Bolt wordmark asset imported from the official
  StackBlitz `bolt.new` repository and applied to B-11. A distinct `.new`
  suffix lockup was not used.
- Working rule:
  - Do not generate Bolt.new marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official Bolt wordmark from the StackBlitz `bolt.new` repository
    on white logo clearspace.
  - Do not synthesize a `.new` wordmark suffix.

## Perplexity

- Source checked: `https://www.perplexity.ai/hub/about`
- Official brand guidelines checked: `https://live.standards.site/perplexity`
- Official asset checked:
  `https://firebasestorage.googleapis.com/v0/b/standards-site-beta.appspot.com/o/documents%2F6t12iheczyb%2F732776432bb%2FPerplexity-Primary-Lockup-Offblack.svg?alt=media&token=d99f057b-1d7e-46b5-92d7-545a258ff0f5`
- Local assets:
  - `assets/logos/perplexity/Perplexity-Primary-Lockup-Offblack.svg`
  - `assets/logos/perplexity/Perplexity-Primary-Lockup-Offblack-512.png`
- Local status: Perplexity official primary offblack lockup imported and
  applied to B-12.
- Working rule:
  - Do not generate Perplexity marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official offblack primary lockup for B-12 on white logo clearspace.

## Netlify

- Source checked: `https://www.netlify.com/press/`
- Official asset package checked:
  `https://www.netlify.com/assets/logos/netlify-logo-full.zip`
- Local package: `assets/logos/netlify/netlify-logo-full.zip`
- Local extracted source:
  - `assets/logos/netlify/netlify-logo-full/netlify-logo-full/`
- Relevant local asset:
  - `large/lightmode/logo-netlify-large-monochrome-lightmode.png`
- Local status: Netlify official full logo asset imported.
- Working rule:
  - Do not generate Netlify marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official monochrome lightmode logo for B-21 on white logo
    clearspace.

## Cloudflare

- Source checked: `https://www.cloudflare.com/logo/`
- Official asset package checked:
  `https://cf-assets.www.cloudflare.com/slt3lc6tev37/7c5EBeF7oxPPYzZiDkSEMM/b8c81838b468bf520767aa47347ac8f3/Cloudflare_logo_kit.zip`
- Local package: `assets/logos/cloudflare/Cloudflare_logo_kit.zip`
- Local extracted source:
  - `assets/logos/cloudflare/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare_logo_kit/Cloudflare logo/`
- Relevant local asset:
  - `png/CF_logo_horizontal_singlecolor_blk.png`
- Local status: Cloudflare official logo assets imported.
- Working rule:
  - Do not generate Cloudflare marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official single-color black horizontal logo for B-22 on white logo
    clearspace.

## Render

- Source checked: `https://render.com/press`
- Official logo source checked:
  `https://render.com/brand/render_1105076560.svg`
- Local source:
  - `assets/logos/render/render_1105076560.svg`
  - `assets/logos/render/render-wordmark-from-press.svg`
- Relevant local asset:
  - `assets/logos/render/render-wordmark-from-press.png`
- Local status: Render official wordmark imported from the official press page
  header SVG, with black fill applied for white clearspace compositing.
- Working rule:
  - Do not generate Render marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official Render wordmark for B-28 on white logo clearspace.

## Supabase

- Source checked: `https://supabase.com/brand-assets`
- Official asset package checked:
  `https://supabase.com/brand-assets.zip`
- Local package: `assets/logos/supabase/brand-assets.zip`
- Local extracted source:
  - `assets/logos/supabase/brand-assets/`
- Relevant local asset:
  - `supabase-logo-wordmark--light.png`
- Local status: Supabase official logo assets imported.
- Working rule:
  - Do not generate Supabase marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official Supabase light wordmark for B-29 on white logo
    clearspace.

## ElevenLabs

- Source checked: `https://elevenlabs.io/press`
- Official logo assets checked:
  - `ElevenLabs Logo black (SVG)`
  - `Download all`
- Local assets:
  - `assets/logos/elevenlabs/elevenlabs-logo-black.svg`
  - `assets/logos/elevenlabs/elevenlabs-logos.zip`
- Local status: ElevenLabs official black SVG imported from the official press
  page and applied to B-13.
- Working rule:
  - Do not generate ElevenLabs marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use the official black SVG for B-13 on white logo clearspace.

## Genspark

- Source checked: `https://www.genspark.ai/brand`
- Source status: official brand guidelines confirmed. The page documents logo
  variants, light/dark usage, co-branding rules, and official downloads in
  Figma, Adobe Illustrator, and PDF formats.
- Local status: official source is confirmed, but local asset import is still
  incomplete because direct local download is blocked by the site's Cloudflare
  challenge in the shell environment.
- Working rule:
  - Do not generate Genspark marks, icons, logos, product UI, or brand-color
    substitutes from prompts.
  - Use only the full official lockup on light background once the official
    asset file is imported.

## Batch 002 unresolved source decisions

These items remain blocked because the official-source question is not the same
as having a recognizable logo somewhere on the web.

- Microsoft / Copilot / Azure:
  - Source checked: `https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks`
  - Source status: Microsoft confirms that product names, logos, app icons, and
    related designs are Microsoft brand assets and that many logo/app-icon uses
    require a license first.
  - Working decision: keep B-15, B-16, B-17, B-25, and B-26 in
    `official_logo_source_review_required` until the specific product mark and
    permitted usage are confirmed.
- Google Cloud / Vertex AI:
  - Sources checked:
    - `https://about.google/brand-resource-center/`
    - `https://cloud.google.com/icons/`
  - Source status: Google has brand guidance and an official Google Cloud
    product icon library, but B-24 and B-27 still need a policy-correct choice
    between a brand lockup, product icon, or no-logo treatment.
  - Working decision: keep B-24 and B-27 in
    `official_logo_source_review_required`.
- AWS:
  - Source checked: `https://aws.amazon.com/trademark-guidelines/`
  - Source status: AWS trademark guidance covers AWS marks and AWS logos. The
    local AWS Architecture Icons package is useful for architecture diagrams but
    is not the same as a primary AWS brand lockup for B-23.
  - Working decision: keep B-23 in `official_logo_source_review_required`.
- Claude Cowork:
  - Sources checked:
    - `https://support.claude.com/en/articles/9266767-what-is-the-claude-team-plan`
    - `https://claude.com/pricing/team`
  - Source status: official sources use Claude Team / Team plan language. A
    distinct official `Claude Cowork` product logo has not been confirmed.
  - Working decision: keep B-19 in `official_logo_source_review_required`; do
    not apply the generic Claude logo until the entry naming decision is made.
