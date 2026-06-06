# semantic-regen-014 generation prompts

Date: 2026-06-06

Purpose: regenerate weak `U024 J-law-ethics` ponchi candidates without touching
`assets/ponchi/final/`.

Current blocker: built-in `image_gen` returned `TooManyRequests` twice while
starting `J-50`. Retry with the built-in tool first when quota is available.
Do not switch to CLI/API fallback unless the user explicitly approves it and
`OPENAI_API_KEY` is available.

## Save And Audit Flow

For each generated item:

```powershell
python scripts/ponchi_save_latest_generated.py <ENTRY_ID> --batch-id semantic-regen-014
```

After all four normalized PNGs exist:

```powershell
python scripts/ponchi_image_audit.py `
  assets/ponchi/experiments/batches/semantic-regen-014/J-50_base_1254x627.png `
  assets/ponchi/experiments/batches/semantic-regen-014/J-52_base_1254x627.png `
  assets/ponchi/experiments/batches/semantic-regen-014/J-53_base_1254x627.png `
  assets/ponchi/experiments/batches/semantic-regen-014/J-54_base_1254x627.png `
  --ledger ledgers/ponchi_generation_batches.csv `
  --batch-id semantic-regen-014 `
  --out-csv docs/ponchi_semantic_audit/semantic_regen_014/image_audit.csv `
  --out-md docs/ponchi_semantic_audit/semantic_regen_014/image_audit.md `
  --contact-sheet docs/ponchi_semantic_audit/semantic_regen_014/contact_sheet.png
```

Then add `semantic-regen-014` rows to
`ledgers/ponchi_generation_batches.csv`, stage final candidates with:

```powershell
python scripts/ponchi_stage_final_candidates.py semantic-regen-014 --include-logo-avoid-base
```

Run color audit before any final promotion.

## Shared Constraints

- Raster ponchi illustration, not SVG-like vector art.
- Concrete scene or metaphor, not box-line-node diagrams.
- No official logos, brand marks, product UI, or readable text.
- Wide 2:1 composition with meaningful subject coverage.
- Leave the top-right corner relatively clean.
- Avoid single-hue purple/blue dominance.
- Do not overwrite `assets/ponchi/final/`.

## J-50 AI Ethics

```text
Use case: illustration-story
Asset type: VibeCodingDictionary ponchi entry image, 2:1 horizontal educational illustration
Primary request: Create a raster ponchi-style illustration for the term "AI ethics". Show one concrete AI system being reviewed through four visible governance checks: fairness, safety, transparency, and accountability.
Scene/backdrop: A clean review desk or lab bench with a central friendly AI model device/dashboard being inspected by reviewers. Around it, use concrete non-text visual signals: balanced scales for fairness, shield/check for safety, transparent magnifying glass over the model for transparency, and signed responsibility clipboard for accountability.
Style/medium: polished hand-drawn raster editorial illustration, warm human-made texture, soft ink outlines, light paper-like background, not vector art.
Composition/framing: wide 2:1 composition, subject fills the frame with meaningful details, no excessive empty padding, leave the top-right corner relatively clean.
Lighting/mood: bright, thoughtful, trustworthy, production-quality.
Color palette: balanced multi-color palette with warm neutrals, teal, red accents, yellow notes, and dark ink; avoid single-hue purple/blue dominance.
Text: no readable text, no labels, no brand names.
Constraints: Must look like a concrete scene/metaphor, not an abstract diagram. No official logos, no product UI, no company marks, no watermark.
Avoid: SVG-like flat boxes, simple node-link diagrams, icon-only abstraction, dense meaningless screens, tiny subject, repeated generic PC desk composition.
```

## J-52 Sycophancy

```text
Use case: illustration-story
Asset type: VibeCodingDictionary ponchi entry image, 2:1 horizontal educational illustration
Primary request: Create a raster ponchi-style illustration for "sycophancy" in AI assistants. The core visual should be an assistant agreeing too much with a dubious user premise while truth and safety evidence is ignored.
Scene/backdrop: A desk-like conversation review scene. One user presents a questionable idea on a card; a cheerful assistant leans forward with excessive agreement gestures. Nearby, a fact-check lamp, warning marker, and evidence cards are visibly pushed aside or ignored.
Style/medium: polished hand-drawn raster editorial illustration, expressive but professional, soft ink outlines, textured paper background, not vector art.
Composition/framing: wide 2:1 composition with the over-agreeing assistant and ignored evidence both clearly visible; no large empty padding; top-right corner relatively clean.
Lighting/mood: slightly comic but critical, clear educational metaphor, production-quality.
Color palette: warm neutrals with teal, amber, red warning accents, and dark ink; avoid one-note purple/blue.
Text: no readable text, no labels, no brand names.
Constraints: The image must read as "over-agreeing despite evidence", not just a generic chat interface. No official logos, no product UI, no watermark.
Avoid: generic speech bubble graph, simple conversation nodes, icon-only abstraction, dense meaningless screens, tiny characters, brand-like assistant UI.
```

## J-53 Copyright Law Article 30-4

```text
Use case: illustration-story
Asset type: VibeCodingDictionary ponchi entry image, 2:1 horizontal educational illustration
Primary request: Create a raster ponchi-style illustration for Japan Copyright Law Article 30-4: a legal boundary between permitted analysis/training use and protected expression.
Scene/backdrop: A Japanese legal review table with two clearly separated zones. On one side, abstract data patterns and training/analysis tokens flow into a learning machine. On the other side, protected creative works such as manuscript pages, music sheets, and artwork are kept behind a respectful boundary marker. A legal reviewer compares the boundary with a stamp and checklist.
Style/medium: polished hand-drawn raster editorial illustration, warm paper texture, soft ink outlines, not vector art.
Composition/framing: wide 2:1 composition showing the boundary as the main visual idea; subject fills the frame; top-right corner relatively clean.
Lighting/mood: careful, legal, balanced, educational, production-quality.
Color palette: warm paper, navy ink, red legal stamp accents, teal analysis flow, muted yellow; avoid single-hue dominance.
Text: no readable statute text, no labels, no brand names.
Constraints: Must show Japanese legal context and a use-boundary metaphor without relying on readable text. No official logos, no product UI, no watermark.
Avoid: illegible law-document diagram, generic courthouse only, simple node chart, icon-only abstraction, dense meaningless panels.
```

## J-54 ISO/IEC 42001

```text
Use case: illustration-story
Asset type: VibeCodingDictionary ponchi entry image, 2:1 horizontal educational illustration
Primary request: Create a raster ponchi-style illustration for ISO/IEC 42001 as an audited AI management system.
Scene/backdrop: An AI governance operations room. A central AI workflow board is connected to a policy binder, risk register, control checklist, audit stamp, and review calendar. A reviewer inspects the system as a managed process rather than a generic certificate.
Style/medium: polished hand-drawn raster editorial illustration, soft ink outlines, tactile office materials, paper texture, not vector art.
Composition/framing: wide 2:1 composition with policy, risk, controls, and workflow governance all visible; no excessive padding; top-right corner relatively clean.
Lighting/mood: orderly, procedural, trustworthy, production-quality.
Color palette: warm gray paper, teal workflow, amber notes, red audit marks, dark ink; avoid dominant purple/blue.
Text: no readable text, no labels, no brand names.
Constraints: Must read as "AI management system under audit", not just certification nodes. No official logos, no product UI, no watermark.
Avoid: generic certificate badge, simple node-link diagram, icon-only abstraction, dense meaningless dashboard, tiny subject.
```
