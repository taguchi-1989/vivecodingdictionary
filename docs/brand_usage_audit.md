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
- Local status: no local asset imported yet.
- Working rule:
  - Do not generate OpenAI, ChatGPT, or Codex logos, marks, icons, or product UI
    from prompts.
  - Keep B-3 and B-8 in `official_logo_source_review_required` until the exact
    asset choice is decided: OpenAI wordmark, ChatGPT-specific asset, or a
    Codex-specific asset if one is officially published.

## Anthropic / Claude

- Source checked: `https://www.anthropic.com/news`
- Source status: official newsroom confirms a media assets / press kit path.
- Local status: no local asset imported yet.
- Working rule:
  - Do not generate Claude or Anthropic marks, icons, or brand-style substitutes
    from prompts.
  - Treat B-2, B-7, and D-12 as logo-required Claude-family entries once the
    press-kit asset is imported and recorded.

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
- Windsurf status: not yet confirmed in local assets.
- Working rule:
  - Do not generate Cursor or Windsurf marks, icons, logos, or product UI from
    prompts.
  - Move B-4 to official source import before overlay.
  - Keep B-6 blocked until an official Windsurf source is confirmed and recorded.
