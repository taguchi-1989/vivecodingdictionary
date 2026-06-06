# semantic-regen-010 results

Date: 2026-06-06

Cluster: `I-browser-automation-mcp`
Pass mode: `exact_entry`

## Scope

| entry | title | action | result |
| --- | --- | --- | --- |
| `I-20` | Playwright MCP | recompose | staged candidate shows cross-browser test runner, trace/timeline, screenshots, and result cards |
| `I-21` | Puppeteer MCP | recompose | staged candidate shows one scripted browser with click/type/scrape/export flow |
| `I-22` | Chrome DevTools MCP | recompose | staged candidate shows browser inspection with elements, console, network waterfall, performance, and audit panels |

## Judgment

The original candidates were too abstract for exact-entry distinction. The regenerated set separates the three axes directly: cross-browser test automation, single-browser scripted automation, and DevTools diagnostics.

Mechanical audit passed:

- Base image audit: 3/3 pass, bbox 0.848 or higher.
- Base color audit: 3/3 pass.

The refreshed title-hidden sheet now uses the staged candidates from `semantic-regen-010`.
