# Microsoft / Coding Assistant Cluster Review

作成日: 2026-06-06

対象:

- `B-4` Cursor
- `B-5` GitHub Copilot
- `B-6` Windsurf
- `B-7` Claude Code
- `B-8` Codex
- `B-15` Microsoft Copilot
- `B-16` Microsoft 365 Copilot
- `B-17` Edge Copilot
- `B-19` Claude Cowork

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/ms_copilot_cluster_2026-06-06/ms_copilot_cluster_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/ms_copilot_cluster_2026-06-06/ms_copilot_cluster_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/ms_copilot_cluster_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/ms_copilot_cluster_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/ms_copilot_cluster_2026-06-06/response_template.csv`

## Findings

| entry | current judgment | issue | action |
| --- | --- | --- | --- |
| `B-5` GitHub Copilot | keep | semantic-regen-001 candidate clearly shows GitHub repo/PR/completion flow | no regen |
| `B-6` Windsurf | keep | semantic-regen-001 candidate clearly shows cascade/multi-file workflow | no regen |
| `B-17` Edge Copilot | keep / light review | browser page plus sidebar makes Edge context visible | no regen unless stricter logo-hidden test fails |
| `B-15` Microsoft Copilot | weak | overlaps Microsoft 365 Copilot; too much work-doc/calendar/email vocabulary | recompose |
| `B-16` Microsoft 365 Copilot | weak | M365 meaning is present, but not sufficiently distinct from general Microsoft Copilot | recompose or paired redesign with B-15 |
| `B-7` Claude Code | weak | logo carries most of the identification; body is sparse and not clearly terminal/CLI coding | recompose |
| `B-4` Cursor | weak | logo carries most of the identification; body is sparse and can overlap Cursor Composer / generic editor | recompose |
| `B-8` Codex | review | OpenAI logo plus agentic flow is understandable, but body is not strongly Codex-specific | focus retest before regen |
| `B-19` Claude Cowork | review | collaborative scene is visible, but could still read as generic coworking assistant | focus retest before regen |

## MS-Specific Judgment

The next Microsoft-focused regeneration should treat the three Copilot entries as a paired set:

- `B-15` Microsoft Copilot: general everyday Microsoft AI assistant across personal search/chat/Windows-style task help.
- `B-16` Microsoft 365 Copilot: work graph, documents, email, calendar, meeting notes, and Office-style productivity flow.
- `B-17` Edge Copilot: browser page, side panel, web summarization, shopping/search/page Q&A.

Current `B-17` already has the strongest non-logo distinction. `B-15` and `B-16` need the most care because they currently share the same document/productivity vocabulary.

## Proposed Next Wave

Batch id: `semantic-regen-005`

Primary targets:

- `B-15`
- `B-16`
- `B-7`
- `B-4`

Secondary review targets:

- `B-8`
- `B-19`
- `B-17`

Do not regenerate `B-5` or `B-6` in this wave unless a later blind responder fails them; semantic-regen-001 already improved them.
