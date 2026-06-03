# ponchi-batch-011 audit

## Summary

- items: 20
- prompt files: 20
- prompt lint: `pass`
- base images: 20
- overlay images: 9
- contact sheets: 0
- base audit: `pass` 20

## Stage Counts

| stage | count |
| --- | ---: |
| `color_audit` | 11 |
| `overlay_audit` | 9 |

## Prompt Lint Output

```text
ok: 20 file(s)
```

## Generated Base Image Audit

Generated base images must pass size, density, and logo-clearspace checks before official logo overlays or final-candidate staging.

- image audit: `ponchi-batch-011-base-image-audit.md`
- contact sheet: `ponchi-batch-011-base-contact-sheet.png`

## Items

| # | entry | title | stage | prompt | base | base audit | overlay | confirmation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `F-123` | ORM | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 2 | `F-130` | OAuth | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 3 | `F-140` | Mermaid | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 4 | `F-141` | PlantUML | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 5 | `F-150` | MIT ライセンス | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 6 | `F-151` | Apache 2.0 | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 7 | `F-152` | GPL | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 8 | `F-153` | Creative Commons | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 9 | `F-154` | OSS | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 10 | `F-160` | DOM | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 11 | `F-161` | SSR | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 12 | `F-162` | SSG | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 13 | `F-170` | EC2 | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 14 | `F-171` | S3 | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 15 | `F-172` | IAM | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 16 | `F-180` | OpenGL | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 17 | `F-181` | WebGL | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 18 | `F-190` | サブルーチン | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
| 19 | `F-200` | Rust | `overlay_audit` | yes | yes | `pass` | yes | `not_reviewed` |
| 20 | `G-1` | Context (コンテキスト) | `color_audit` | yes | yes | `pass` | no | `not_reviewed` |
