# YouTubers review

Date: 2026-06-06

Cluster: `C-youtubers`
Pass mode: `exact_entry` with source-backed channel avatar overlay; exact channel identity is caption/official-avatar assisted.

## Judgment

The four entries all represent Japanese AI information channels. They should not be judged by generated host likeness. The useful discriminator is the saved official YouTube avatar plus a secondary scene motif. On that basis, the cluster is usable, but exact recognition without the overlay would be weak.

## Findings

| entry | title | blind/semantic status | action |
| --- | --- | --- | --- |
| `C-80` | AI大学 | Official avatar anchors the channel; scene reads as general AI learning/news. | keep, overlay_required |
| `C-81` | にゃんた | Official avatar anchors the channel; scene reads as practical AI operations. | keep, overlay_required |
| `C-82` | まさお | Official avatar anchors the channel; scene is visually denser and still carries prior color-review risk. | keep, overlay_required, monitor color |
| `C-83` | AI の羅針盤 | Official avatar anchors the channel; compass/research motif fits. Source page title is `AI時代の羅針盤`. | keep, overlay_required, naming_note |

## Decision

No image regeneration in this unit. The existing official-avatar overlays are the meaningful identity signal. The final images remain acceptable as channel entries, with C-83 naming mismatch preserved as a final-review note and C-82 color risk carried forward.

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/youtubers_2026-06-06/youtubers_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/youtubers_2026-06-06/youtubers_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/youtubers_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/youtubers_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/youtubers_2026-06-06/response_template.csv`
