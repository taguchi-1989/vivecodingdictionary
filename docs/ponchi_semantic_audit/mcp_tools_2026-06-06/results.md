# MCP tools review

Date: 2026-06-06

Cluster: `I-mcp-tools`
Pass mode: `exact_entry`

## Judgment

The images pass as tool-category diagrams. They are simplified, so exact product/tool names are caption-supported, but the operational domains are distinguishable.

## Findings

| group | entries | visual status | action |
| --- | --- | --- | --- |
| Reference integrations | `I-10`, `I-11`, `I-12`, `I-13` | Filesystem, GitHub, Git, and Slack MCPs differ by file access, repo/PR board, branch graph, and chat/workspace panels. | keep |
| Browser/dev automation | `I-20`, `I-21`, `I-22`, `I-23`, `I-24` | Playwright/Puppeteer/DevTools/Serena/Context7 separate into browser automation, script automation, diagnostics, codebase navigation, and docs/context lookup. | keep |
| Collab/data/cloud | `I-30`, `I-41`, `I-50` | Notion, SQLite, and AWS MCPs are distinct by workspace database, local DB cylinder, and cloud-resource fanout. | keep |

## Decision

No new regeneration in this unit. Existing staged improvements for `I-20` - `I-22` remain available from `semantic-regen-010`; this unit does not overwrite final assets.

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/mcp_tools_2026-06-06/mcp_tools_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/mcp_tools_2026-06-06/mcp_tools_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/mcp_tools_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/mcp_tools_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/mcp_tools_2026-06-06/response_template.csv`
