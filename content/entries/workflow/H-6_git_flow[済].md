---
id: H-6
title: Git Flow
title_reading: ギット フロー
category: workflow
subtype: methodology
experience_level: partial
reader_level: 3-4
importance: D
figure_type: comparison
page_layout: spread_v1
start_date:
end_date:
version_status: active
pricing_note: none
evaluation_date: 2026-04-30
related_terms:
  - git
  - branch
  - Pull Request
  - CI/CD
status: ready
---

# Git Flow

<!-- ━━━━━━━━ 左ページ ━━━━━━━━ -->

## tagline

リリースサイクルが明確な製品開発に向く、代表的なブランチ運用パターンです。

## 何をしてくれるか

`main` と `develop` を常設し、`feature/*`・`release/*`・`hotfix/*` を目的別に切り分けます。複数人の並行開発を整理できます。

## どこで出会うか

チーム開発のオンボーディング資料やブランチ命名規則の説明で目にします。「うちは Git Flow を採用している」とは、このモデルのブランチ管理を指します。

## メイン図

### 図の狙い

Git Flow のブランチ構造を並べて、GitHub Flow などシンプルなモデルとの違いを対比で示す。

### B. 登場シーン（figure_type: comparison）

- シーン1: リリース計画がある製品チームが develop → release → main の流れで本番反映
- シーン2: GitHub Flow を採用したチームが main + 短命 feature だけで継続デプロイ
- シーン3: AI が多数 PR を作る環境で Git Flow の複雑さが摩擦になる場面
- 並べる基準: ブランチ数・リリース頻度の違いを横並びで示す

## 会話での使い方例

「Git Flow をやめて GitHub Flow にしたら、AI の PR で詰まらなくなりました。」


<!-- ━━━━━━━━ 右ページ ━━━━━━━━ -->

## この用語の見どころ

### 1. 役割

git リポジトリでのブランチ運用を体系化したモデルです。

### 2. うれしさ

ブランチの目的が明確で、複数人の並行作業を整理しやすいです。

### 3. 注意点

提案者本人が 2020 年に「継続デプロイには複雑すぎる」と注釈を出しています。

### 4. どこで役立つか

バージョン管理が必要な製品や、リリース日が決まっている開発に向きます。

### 5. はじめに

git の標準ではなく、選択肢の 1 つである点を押さえておきます。

### 6. 深掘り先

GitHub Flow、Trunk-Based Development、CI/CD

## 開発フローでの位置（必須）

1. 機能着手 — `develop` から `feature/*` を切り実装します
2. 統合 — `feature/*` を `develop` にマージし動作を確認します
3. リリース準備 — `release/*` を切り最終調整と品質確認を行います
4. 本番反映 — `release/*` を `main` にマージしタグを打ちます
5. 緊急修正 — 本番障害は `main` から `hotfix/*` で対応します

## 関連用語

- git
- branch
- Pull Request
- CI/CD


<!-- ━━━━━━━━ 著者記入欄（AI は触らない） ━━━━━━━━ -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 非エンジニアのつまずき

<!-- user-input:start key="stumble" -->
- そもそも馴染みのない言葉で、図を見ても自分の作業にどう紐づくのかが掴みにくいです
<!-- user-input:end key="stumble" -->

<!-- AUTHOR: user_only / AI-ASSIST: no -->
## 私のコメント

<!-- user-input:start key="my_comment" -->
- 🙂 第一印象: 今回初めて聞いた言葉です
- 👍 良い点: ブランチ運用の形としては綺麗にまとまっている感じがあります
- 👎 ダメな点: 人間が運用すると認知コストが高く、ひとり開発だと過剰になりがちです
- 👥 誰向けか: チームで明確なリリース管理が必要な現場向けで、個人開発には重い印象です
<!-- user-input:end key="my_comment" -->


<!-- ━━━━━━━━ 裏台帳メモ（誌面には出さない） ━━━━━━━━ -->

## 誌面ポンチ絵メモ

### メイン図（左ページ中段 / figure_type: comparison）

- 描く内容: Git Flow（5 本ブランチ）と GitHub Flow（2 本ブランチ）の横並び比較図
- 登場人物: 開発者 1 名がブランチ図を見て困惑している左側と、すっきり整理された右側
- 吹き出し・心の声: 左「どのブランチに入れるんだっけ…」/ 右「feature 切って PR するだけです」
- 中央に置くキーワード/ラベル: Git Flow vs GitHub Flow

### 6 視点アイコン（右ページ上段）

- 共通アイコン流用

### 開発フロー図（右ページ下段）

- Step 1 のアイコン/絵柄: 枝分かれアイコン（feature ブランチ）
- Step 2 のアイコン/絵柄: 合流アイコン（develop へのマージ）
- Step 3 のアイコン/絵柄: チェックリスト（release 準備）
- Step 4 のアイコン/絵柄: タグアイコン（main へのマージ）
- Step 5 のアイコン/絵柄: 救急マーク（hotfix）
- 矢印で示す流れの意図: 機能追加 → 統合 → リリース → 本番という段階的な流れ


## コミュニティ補完メモ

- F-50 git との住み分け：F-50 は git コマンド・バージョン管理の仕組みそのもの。H-6 はその上に乗るブランチ運用ルールのモデル。「git を使う前提で、どう管理するか」がスコープ。
- F-53 branch との住み分け：F-53 はブランチという概念の説明。H-6 はブランチをどう命名・運用するかの体系。
- GitHub Flow・Trunk-Based Development はエントリ候補として別 ID で取り扱う想定。本エントリの「派生モデル」として比較軸で言及するにとどめる。
- AI がバイブコーディングで PR を多数作る現代では、Git Flow の複雑さが摩擦になりやすい。この観点はブリーフにあるため「注意点」と「どこで出会うか」に短く反映した。詳細は備考参照。


## 出典メモ

- Vincent Driessen "A successful Git branching model" (2010) — nvie.com — checked 2026-04-30
- 同記事の 2020 年追記（"Note of reflection"）— nvie.com — checked 2026-04-30


## 備考

- Git Flow は 2010 年に Vincent Driessen がブログ記事で提案したモデル。2020 年に本人が追記し、「Web アプリ等、継続的デリバリーが主流な現代には GitHub Flow の方が向く場面が多い」と言及している。
- AI コーディングツール（Cursor、Claude Code 等）が大量に PR を生成するバイブコーディング環境では、ブランチが増えるほど管理コストが増す。Trunk-Based Development や GitHub Flow に切り替えるチームが増えている。
- 「Git Flow = git の標準ワークフロー」という誤解が読者に多い。実態は複数ある運用モデルの 1 つ。
