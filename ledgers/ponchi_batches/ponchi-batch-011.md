# ponchi-batch-011 review

## Gate

- Do not promote any item to final until this batch is reviewed.
- Generate or update scene briefs first, then lint prompts, then generate base images.
- Stop brand entries at `overlay_wait` until official assets are imported and recorded.

## Items

| # | entry | title | stage | logo status | next action | confirmation |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `F-123` | ORM | `brief_needed` | `logo_avoid` | generate generic object-relational mapping scene; no database/product logos | `not_reviewed` |
| 2 | `F-130` | OAuth | `brief_needed` | `logo_avoid` | generate generic authorization handoff scene; no provider logos | `not_reviewed` |
| 3 | `F-140` | Mermaid | `overlay_wait` | `official_logo_source_review_required` | generate neutral diagram base with blank logo clearspace; review official Mermaid asset before overlay | `not_reviewed` |
| 4 | `F-141` | PlantUML | `overlay_wait` | `official_logo_source_review_required` | generate neutral UML diagram base with blank logo clearspace; review official PlantUML asset before overlay | `not_reviewed` |
| 5 | `F-150` | MIT ライセンス | `brief_needed` | `logo_avoid` | generate generic permissive license scene; no institutional marks | `not_reviewed` |
| 6 | `F-151` | Apache 2.0 | `brief_needed` | `logo_avoid` | generate generic license obligations scene; no Apache marks | `not_reviewed` |
| 7 | `F-152` | GPL | `brief_needed` | `logo_avoid` | generate generic copyleft license scene; no GNU or FSF marks | `not_reviewed` |
| 8 | `F-153` | Creative Commons | `overlay_wait` | `official_logo_source_review_required` | generate neutral license-sharing base with blank logo clearspace; review official CC icons before overlay | `not_reviewed` |
| 9 | `F-154` | OSS | `brief_needed` | `logo_avoid` | generate generic open-source collaboration scene; no foundation logos | `not_reviewed` |
| 10 | `F-160` | DOM | `brief_needed` | `logo_avoid` | generate browser document tree scene; no browser or framework logos | `not_reviewed` |
| 11 | `F-161` | SSR | `brief_needed` | `logo_avoid` | generate server-to-browser rendering flow; no framework logos | `not_reviewed` |
| 12 | `F-162` | SSG | `brief_needed` | `logo_avoid` | generate build-time static page flow; no framework logos | `not_reviewed` |
| 13 | `F-170` | EC2 | `overlay_wait` | `official_logo_source_review_required` | generate neutral cloud compute base with blank logo clearspace; review official AWS EC2 icon before overlay | `not_reviewed` |
| 14 | `F-171` | S3 | `overlay_wait` | `official_logo_source_review_required` | generate neutral object storage base with blank logo clearspace; review official AWS S3 icon before overlay | `not_reviewed` |
| 15 | `F-172` | IAM | `overlay_wait` | `official_logo_source_review_required` | generate neutral identity-permission base with blank logo clearspace; review official AWS IAM icon before overlay | `not_reviewed` |
| 16 | `F-180` | OpenGL | `overlay_wait` | `official_logo_source_review_required` | generate neutral graphics pipeline base with blank logo clearspace; review official OpenGL logo before overlay | `not_reviewed` |
| 17 | `F-181` | WebGL | `overlay_wait` | `official_logo_source_review_required` | generate neutral browser graphics base with blank logo clearspace; review official WebGL logo before overlay | `not_reviewed` |
| 18 | `F-190` | サブルーチン | `brief_needed` | `logo_avoid` | generate generic function-call reuse scene; no language logos | `not_reviewed` |
| 19 | `F-200` | Rust | `overlay_wait` | `official_logo_source_review_required` | generate neutral systems-programming base with blank logo clearspace; review official Rust logo before overlay | `not_reviewed` |
| 20 | `G-1` | Context (コンテキスト) | `prompt_review` | `logo_avoid` | lint prompt, generate 2:1 base, audit density | `not_reviewed` |

## Batch Commands

```powershell
python scripts\ponchi_batch_plan.py --batch-size 20
python scripts\ponchi_batch_report.py ponchi-batch-011
python scripts\ponchi_prompt_lint.py <prompt-files>
```
