# Ponchi Color Acceptance Gate

This gate turns the existing color rule into a production checkpoint. It does
not replace visual review; it prevents obviously off-policy candidates from
being counted as finished.

## Color Classes

### Body Palette

All generated illustration pixels outside official asset overlays must stay in
the shared ponchi palette:

- `#FFFFFF`
- `#F7F9FC`
- `#1A1A1A`
- `#6B7280`
- `#EAF1FB`
- `#D6E6FA`
- `#8DB7E8`
- `#3F7FD1`
- `#123E82`

Antialiasing, subtle shadows, and resampling may create nearby neutral or
approved-blue pixels, but they must still read as white, black, gray, or the
approved blue range.

### Official Asset Exception

Official logos, official icons, and official marks may keep their original
colors only when all of the following are true:

- the asset source is recorded in `docs/brand_usage_audit.md`;
- the asset is composited after generation, not drawn by image generation;
- the asset shape, color, aspect ratio, and built-in clearspace are preserved;
- off-palette color is limited to the composited asset pixels.

Official asset color is an exception to the body palette, not a general
permission to use brand colors in the illustration.

### Reject Colors

Generated body illustration pixels must not contain yellow, green, red, purple,
brown, orange, rainbow colors, teal/cyan drift, colorful charts, colorful
screenshots, photo thumbnails, product UI, or brand color schemes.

## Status Semantics

- `base_audit`: size, density, and clearspace checks passed.
- `overlay_audit`: deterministic official asset overlay and structural audit
  passed.
- `color_audit_pass`: generated body pixels pass the color gate.
- `color_audit_review`: minor off-palette pixels exist; visual review or
  rerender is required before final promotion.
- `color_audit_fail`: off-palette pixels are materially present; rerender or
  deterministic recolor/rebuild is required.

`overlay_audit` is not a final-quality status by itself. A candidate is not
ready for promotion into `assets/ponchi/final/` until color policy is also
verified.

## Audit Policy

Prompt files must pass `scripts/ponchi_prompt_lint.py` before a new generation
batch is treated as eligible for image generation. The lint gate requires the
strict palette tokens, explicit reject-color language, and no loose color
phrases such as generic "blue-gray" or logo-bearing scene instructions.

For overlay candidates, audit the generated base image whenever the matching
`*_base_1254x627.png` exists. This excludes official asset colors from the
body-palette check while still catching generated photo/UI/brand-color drift.

Mechanical thresholds:

- `color_audit_pass`: off-palette body pixels are `<= 1.0%` of inspected pixels.
- `color_audit_review`: off-palette body pixels are `> 1.0%` and `<= 2.0%`.
- `color_audit_fail`: off-palette body pixels are `> 2.0%`.

The pass threshold exists for antialiasing, resampling, and subtle line/fill
interpolation. It is not permission to introduce visible reject colors.

For future overlay runs, `scripts/composite_official_logo.py` should write a
small JSON sidecar with the official asset path and overlay rectangle. That
sidecar allows direct overlay-image audits when the base source is missing or
when checking that off-palette color is confined to the official asset area.

Known high-risk patterns:

- image-model entries that show natural photo thumbnails;
- video-model entries that show multicolor preview frames;
- local generator palettes that use red, yellow, green, purple, or orange;
- official icon entries where the icon exception leaks into nearby decoration.
