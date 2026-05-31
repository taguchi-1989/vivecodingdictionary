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
- Status: blocked for local asset download in this environment because the page
  presents a browser/cookie challenge to script access.
- Working rule:
  - Do not generate OpenAI, ChatGPT, or Codex logos, marks, icons, or product UI
    from prompts.
  - Keep B-3 and B-8 in `blocked_brand_asset` until official downloadable assets
    are available locally.

## Anthropic / Claude

- Status: not yet confirmed in local assets.
- Working rule:
  - Do not generate Claude or Anthropic marks, icons, or brand-style substitutes
    from prompts.
  - Keep B-2 and B-7 in `blocked_brand_asset` until official assets and usage
    guidance are recorded.

## Google / Gemini

- Status: not yet confirmed in local assets.
- Working rule:
  - Do not generate Gemini, Google, Android, Gmail, Docs, or Google Cloud marks,
    icons, logos, app UI, or brand-color substitutes from prompts.
  - Keep B-1 in `blocked_brand_asset` until official assets and usage guidance
    are recorded.

## Cursor / Windsurf

- Status: not yet confirmed in local assets.
- Working rule:
  - Do not generate Cursor or Windsurf marks, icons, logos, or product UI from
    prompts.
  - Keep B-4 and B-6 in `blocked_brand_asset` until official assets and usage
    guidance are recorded.
