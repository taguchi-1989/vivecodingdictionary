# semantic-regen-002 results

Wave 2 regenerated five semantic-risk ponchi images:

- `J-72` H100
- `J-73` Blackwell
- `F-84` Ghostty
- `D-51` Imagen
- `D-57` Flow

## Gate Summary

| entry | final candidate | mechanical color | blind result | decision |
| --- | --- | --- | --- | --- |
| `J-72` H100 | `assets/ponchi/final_candidates/semantic-regen-002/J-72_candidate.png` | pass | v2 top1 `J-72`, confidence 82 | pass |
| `J-73` Blackwell | `assets/ponchi/final_candidates/semantic-regen-002/J-73_candidate.png` | pass | top1 `J-73`, confidence 72; v2 focus confidence 86 | pass |
| `F-84` Ghostty | `assets/ponchi/final_candidates/semantic-regen-002/F-84_candidate.png` | pass | top1 `F-84`, confidence 92 | pass |
| `D-51` Imagen | `assets/ponchi/final_candidates/semantic-regen-002/D-51_candidate.png` | pass | top1 `D-51`, confidence 78; v2 focus confidence 74 | pass |
| `D-57` Flow | `assets/ponchi/final_candidates/semantic-regen-002/D-57_candidate.png` | pass | v2 top1 `D-57`, confidence 78 | pass |

## Iteration Notes

- `J-72` first candidate was top1 correct but weak (`63`) because it still competed with `J-73` Blackwell. v2 shifted the visual from generic datacenter GPU to cloud-provisioned, installed H100 rack modules and passed at `82`.
- `D-57` first candidate was guessed as `D-53` Veo (`64`) because the video/timeline cues dominated. v2 made the browser-like studio, scene cards, controls, asset drawer, and export tray the main subject. It passed at `78`.
- `J-73` passed as a next-generation architecture/system-scaling visual. In v2 focus it scored `86`, confirming the H100/Blackwell split after the `J-72` retry.
- `F-84` passed strongly after reducing the black terminal surface and making the terminal emulator app frame, panes, settings controls, and official Ghostty mark visible.
- `D-51` passed as a still-image model: prompt/reference inputs into a central model engine and still-image outputs, without video timeline cues.

## Artifacts

- Prompt brief: `assets/ponchi/pipeline_prompts/semantic-regen-002/semantic-regen-002.md`
- Final candidates: `assets/ponchi/final_candidates/semantic-regen-002/`
- Final candidates contact sheet: `assets/ponchi/final_candidates/semantic-regen-002/final_candidates_contact_sheet.png`
- Batch audit: `docs/ponchi_batch_audits/semantic-regen-002.md`
- Final candidate audit: `docs/ponchi_batch_audits/semantic-regen-002-final-candidates.md`
- Base image audit: `docs/ponchi_semantic_audit/semantic_regen_002/base_image_audit.md`
- Base color audit: `docs/ponchi_semantic_audit/semantic_regen_002/color_audit.md`
- Overlay image audit: `docs/ponchi_semantic_audit/semantic_regen_002/overlay_image_audit.md`
- Blind retest packs: `docs/ponchi_semantic_audit/semantic_regen_002/blind_retest/`

## Residual Review Notes

- `J-72` / `J-73`: no official product logos were applied. This is intentional because the blind target is the semantic product-vs-generation distinction, and the existing ledger marks both as `logo_avoid`.
- `D-51`: overlay color audit is `review` because the official Google DeepMind asset introduces off-palette blue. The generated body color audit is pass.
- `F-84`: the official Ghostty social-card overlay is visually dark. The base image was kept light and terminal-emulator-specific so the mark does not dominate the semantic read.
