# Ponchi Logo Application Audit 2026-06-01

## 目的

`docs/ponchi_logo_requirement_matrix_2026-06-01.md` で `official_logo_applied` とした項目について、実際に本番画像へ公式ロゴが入っているかを確認する。

## 対象

| entry_id | title | final image | official asset | status |
| :-- | :-- | :-- | :-- | :-- |
| `B-5` | GitHub Copilot | `assets/ponchi/final/B-5.webp` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Copilot_Lockup_Black_Clearspace.png` | applied |
| `F-60` | GitHub | `assets/ponchi/final/F-60.webp` | `assets/logos/github/GitHub_Logos/GitHub Logos/PNG/GitHub_Lockup_Black_Clearspace.png` | applied |

## 目視確認

比較用 contact sheet:

`assets/ponchi/experiments/regeneration/logo-application-audit-2026-06-01/logo_application_contact_sheet.png`

上から順に:

1. `B-5` の旧 HEAD 画像。1:1 で、現在の 2:1 ロゴ合成方針に合わない。
2. `B-5` の作業ツリー画像。公式 GitHub Copilot lockup 入りの 2:1。
3. `F-60` の本番画像。公式 GitHub lockup 入りの 2:1。

## 寸法監査

```powershell
python scripts\audit_image_sizes.py --suffix .webp
```

結果:

- 350 images scanned
- `1254x627`: 349
- `1024x512`: 1
- aspect `2:1`: 350

個別確認:

```powershell
magick identify assets\ponchi\final\B-5.webp assets\ponchi\final\F-60.webp
```

結果:

- `B-5.webp`: `1254x627`
- `F-60.webp`: `1254x627`

## 判断

ローカル公式素材があり、今回の台帳対象でロゴを入れるべきものは `B-5` と `F-60`。どちらも AI 生成ロゴではなく、公式素材の後合成として扱う。`B-1`, `B-2`, `B-3`, `B-4`, `B-8` は公式素材と利用条件が未確定なので、引き続きブロックする。
