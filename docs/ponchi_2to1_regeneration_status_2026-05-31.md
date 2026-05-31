# ポンチ絵 2:1 再生成 引き継ぎメモ

作成日: 2026-05-31

## 現在地

`assets/ponchi/final/*.webp` の寸法統一は完了。現在の監査では 350 件すべてが 2:1。

```powershell
python scripts\audit_image_sizes.py --suffix .webp
```

結果:

| 対象 | 件数 | サイズ内訳 | アスペクト |
| :-- | --: | :-- | :-- |
| `assets/ponchi/final/*.webp` | 350 | `1254x627`: 349 / `1024x512`: 1 | 2:1: 350 |

ただし、これは主に機械的な変換。意味のある横長構図としての再生成はまだ途中。

## PNG 側の注意

`.png` は `.gitignore` 対象のローカル作業版。現在の監査では 347 件読めて、327 件が 2:1、20 件が 1:1。

読めない PNG:

- `B-2.png`
- `B-3.png`
- `B-4.png`

まだ 1:1 の PNG:

`E-25`, `E-26`, `E-27`, `E-30`, `E-50`, `H-1`, `H-5`, `H-6`, `H-7`, `H-8`, `I-2`, `I-3`, `I-4`, `I-5`, `J-100`, `J-81`, `J-90`, `J-91`, `J-92`, `J-93`

最終確認は WebP 側を正とする。

## 再生成タスクの状態

意味的な 2:1 再生成タスクは `docs/ponchi_regeneration_logo_todo.md` で管理中。

2026-05-31 追記: ロゴだけでなく、公式アイコン、公式マーク、公式マスコット、ブランドカラー風の代用品も AI 生成禁止として整理中。作業ルールは `docs/ponchi_brand_asset_rules.md` と `docs/ponchi_character_bible.md` を先に参照する。

完了済み:

- `B-5 GitHub Copilot` を 2:1 構図として再生成。
- AI 生成ではロゴを描かせず、公式 GitHub ロゴ ZIP 由来の素材を後合成。
- 最終ファイルは `assets/ponchi/final/B-5.webp`。
- 実験ファイルは `assets/ponchi/experiments/regeneration/`。
- 最終監査でも WebP 350 件すべて 2:1 を維持。

作成済みプロンプト:

- `assets/ponchi/prompts/B-5.md`
- `assets/ponchi/prompts/F-1.md`
- `assets/ponchi/prompts/F-60.md`
- `assets/ponchi/prompts/J-14.md`

## パイロットキュー

| entry_id | 状態 | 次アクション |
| :-- | :-- | :-- |
| `B-1 Gemini` | `blocked_logo_asset` | 公式ロゴ素材と利用条件の確認 |
| `B-2 Claude` | `blocked_logo_asset` | 公式ロゴ素材と利用条件の確認 |
| `B-3 ChatGPT` | `blocked_logo_asset` | OpenAI 公式素材の確認、後合成方針 |
| `B-4 Cursor` | `blocked_logo_asset` | 公式ロゴ素材と利用条件の確認 |
| `B-5 GitHub Copilot` | `pilot_regenerated` | 完了済み。品質基準の基準例 |
| `B-6 Windsurf` | `blocked_logo_asset` | 公式ロゴ素材と利用条件の確認 |
| `B-7 Claude Code` | `blocked_logo_asset` | 公式ロゴ素材と利用条件の確認 |
| `B-8 Codex` | `blocked_logo_asset` | OpenAI/Codex の公式素材確認 |
| `F-1 JavaScript` | `ready_for_regen` | ロゴなしで再生成可能 |
| `F-60 GitHub` | `blocked_logo_asset` | GitHub 公式ロゴ合成で進める候補 |

## ルールの入口

再生成時は次を必ず参照する。

- `docs/ponchi_image_generation_rules.md`
- `docs/ponchi_brand_asset_rules.md`
- `docs/ponchi_character_bible.md`
- `docs/ponchi_2to1_policy_todo.md`
- `docs/ponchi_regeneration_logo_todo.md`
- `docs/brand_usage_audit.md`

重要ルール:

- 白、黒、グレー、指定青だけを使う。
- 読める文字を画像内に入れない。
- 会社ロゴ、サービスロゴ、公式アイコン、公式マーク、実在 UI を AI 生成で描かせない。
- ロゴや公式アイコンが必要な場合は、公式素材を後合成する。
- `1254x627` の主ブランド lockup は横幅 `500-520px` 目安で大きく扱う。小さな飾りにしない。
- `1254x627` を標準サイズにする。
- 200px 程度でも意味が残る構図にする。

## 次にやること

1. `B-5` を品質基準として目視確認する。
2. ロゴ不要の `F-1 JavaScript` から再生成を続ける。
3. `F-60 GitHub` は公式 GitHub ロゴ素材を使った後合成で進める。
4. `B-1` から `B-8` のサービス系は、公式ロゴ素材と利用条件を確認してから進める。
5. 各差し替え後に必ず実行する。

```powershell
python scripts\audit_image_sizes.py --suffix .webp
```

## 完了条件

- WebP 350 件が 2:1 を維持している。
- 各画像が `OK`, `微修正`, `再生成`, `公式ロゴ合成待ち` のどれかに分類済み。
- `再生成` と `公式ロゴ合成待ち` の残件がゼロ、または残件として明示されている。
- プレビューと PDF で画像枠が崩れていない。
