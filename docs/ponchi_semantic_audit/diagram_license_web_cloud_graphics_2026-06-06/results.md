# Diagram, license, web, cloud, and graphics review

Date: 2026-06-06

Cluster: `F-diagram-license-web-cloud-graphics`
Pass mode: `type_distinction`

## Judgment

The remaining F chapter entries pass as type/category diagrams. Exact legal-license names are same-family and caption-supported, while diagram tools, web rendering modes, AWS service roles, graphics APIs, subroutine, and Rust are visually distinguishable.

## Findings

| group | entries | visual status | action |
| --- | --- | --- | --- |
| Diagram tools | `F-140`, `F-141` | Mermaid and PlantUML are both diagram generators, but flowchart vs UML/class/sequence motifs separate them. | keep |
| Licenses and OSS | `F-150` - `F-154` | MIT/Apache/GPL/CC/OSS form a close legal cluster; permission/notice/copy/share/community motifs are present, with exact names caption-supported. | keep |
| Web foundation | `F-160`, `F-161`, `F-162` | DOM tree, server-rendered HTML, and build-time static generation are distinct. | keep |
| Cloud services | `F-170`, `F-171`, `F-172` | EC2 compute, S3 object storage, and IAM identity/policy differ clearly with official AWS icons. | keep; official icon color notes are non-semantic |
| Graphics and remaining terms | `F-180`, `F-181`, `F-190`, `F-200` | OpenGL/WebGL differ by native vs browser graphics context; subroutine and Rust are distinct. | keep |

## Decision

No regeneration in this unit. The residual ambiguities are acceptable within the unit's `type_distinction` pass mode.

## Artifacts

- Blind sheet: `docs/ponchi_semantic_audit/diagram_license_web_cloud_graphics_2026-06-06/diagram_license_web_cloud_graphics_blind_sheet.png`
- Labeled sheet: `docs/ponchi_semantic_audit/diagram_license_web_cloud_graphics_2026-06-06/diagram_license_web_cloud_graphics_labeled_sheet.png`
- Candidates: `docs/ponchi_semantic_audit/diagram_license_web_cloud_graphics_2026-06-06/candidates.csv`
- Answer key: `docs/ponchi_semantic_audit/diagram_license_web_cloud_graphics_2026-06-06/answer_key.csv`
- Response template: `docs/ponchi_semantic_audit/diagram_license_web_cloud_graphics_2026-06-06/response_template.csv`
