# RepoEdit セットアップ手順（スマホ編集 PWA）

*[Taguchi-1989/RepoEdit](https://github.com/Taguchi-1989/RepoEdit) を本リポジトリに適応するための初期セットアップ手順です。v0.1（2026-05-17）。*

## 1. これは何か

RepoEdit は、GitHub リポジトリ内の Markdown ファイルの「user-input ブロック」だけをスマホ／ノート PC から編集できる PWA + Cloudflare Worker です。本書では以下の運用を想定しています。

- **編集対象**：`content/entries/**/*.md` 内の 2 ブロック
  - `key="stumble"`：「非エンジニアのつまずき」
  - `key="my_comment"`：「私のコメント」（🙂 / 👍 / 👎 / 👥）
- **編集者**：田口本人のみ（GitHub OAuth で本人ログインを確認）
- **書き戻し先**：`main` ではなく専用ブランチ `mobile-drafts`（後で PC でレビューしてから `main` にマージ）
- **トークン秘匿**：ブラウザは GitHub PAT を持たない。Worker が Cloudflare Secrets に保管した PAT で Contents API を叩く

これにより、`docs/mobile_inbox_requirements.md` で計画した Obsidian Mobile + 自前 `mobile_inbox/` の二段運用は不要になります（必要なら併用も可）。

## 2. 事前にできていること

このリポジトリ側：

- `templates/entry_template.md` と `templates/skeleton_template.md` に `<!-- user-input:start/end key="stumble" -->` と `key="my_comment"` を埋め込み済み
- `content/entries/**/*.md`（A-1〜A-11 の序文・凡例を除く全 316 件）に同マーカーを埋め込み済み（`scripts/add_user_input_markers.py`）
- 新規エントリは `scripts/generate_skeleton.py` を経由すれば自動でマーカーが入る

## 3. やること（一度きり）

### 3.1 RepoEdit のクローンとインストール

```sh
git clone https://github.com/Taguchi-1989/RepoEdit
cd RepoEdit
pnpm install
```

### 3.2 Cloudflare 側

1. Cloudflare アカウント作成（無料プラン可）
2. `wrangler login`
3. D1 データベース作成：

   ```sh
   cd worker
   wrangler d1 create repoedit
   ```

   出力された `database_id = "..."` を `worker/wrangler.toml` の `[[d1_databases]]` セクションの `REPLACE_ME` と差し替え。

4. マイグレーション適用：

   ```sh
   wrangler d1 migrations apply repoedit --local
   wrangler d1 migrations apply repoedit --remote
   ```

### 3.3 GitHub Fine-grained PAT

[github.com/settings/personal-access-tokens](https://github.com/settings/personal-access-tokens) で新規発行：

- Repository access: **Only select repositories** → `Taguchi-1989/VibeCodingDictionary` ※リポ名 typo に注意
- Repository permissions:
  - **Contents: Read and write**
- 有効期限：90 日（更新カレンダーに入れておく）

発行したトークンを Worker Secret に登録：

```sh
wrangler secret put GITHUB_TOKEN
```

### 3.4 GitHub OAuth App（本人確認用）

[github.com/settings/developers](https://github.com/settings/developers) で新規 OAuth App：

- **Homepage URL**：PWA をホストする URL（後述）
- **Authorization callback URL**：`https://<your-worker>.workers.dev/api/auth/callback`

Worker Secrets：

```sh
wrangler secret put GITHUB_OAUTH_CLIENT_ID
wrangler secret put GITHUB_OAUTH_CLIENT_SECRET
# 32 バイト以上のランダム文字列
openssl rand -hex 32 | wrangler secret put SESSION_SECRET
```

### 3.5 リポジトリ設定を VibeCodingDictionary に向ける

`worker/wrangler.toml` の `[vars]`：

```toml
[vars]
ALLOWED_ORIGIN = "https://<your-pwa-host>"
WEB_ORIGIN = "https://<your-pwa-host>"
GITHUB_REPO_OWNER = "Taguchi-1989"
GITHUB_REPO_NAME = "VibeCodingDictionary"   # 既存のリポ名（typo を含む）
GITHUB_BRANCH = "mobile-drafts"
ALLOWED_LOGIN = "Taguchi-1989"               # 本人のみ通す
```

※ 変数名は RepoEdit 側の実装に合わせて適宜読み替えてください。Worker のソース（`worker/src/`）を確認するのが確実です。

### 3.6 デプロイ

Worker:

```sh
cd worker
wrangler deploy
```

PWA:

```sh
pnpm --filter @repoedit/web build
# web/dist/ を Cloudflare Pages or Netlify などにアップロード
```

### 3.7 `mobile-drafts` ブランチを作る

ローカルから：

```sh
cd /d/dev/VibeCodingDictionary
git fetch origin
git checkout -b mobile-drafts
git push -u origin mobile-drafts
```

## 4. 日常運用

### スマホ側

- ホーム画面に PWA URL を「ホームに追加」しておく
- 開く → GitHub ログイン → エントリ一覧 → 該当エントリを開く
- 「非エンジニアのつまずき」「私のコメント」のブロックだけが編集可能
- 保存ボタン or 一定時間アイドルで自動コミット（`mobile-drafts` ブランチ）

### PC 側

```sh
git fetch origin
git checkout mobile-drafts -- content/entries/  # 部分取り込み
# または PR ベースで mobile-drafts → main をマージ
```

PR 経由でのレビュー運用が安全：

```sh
gh pr create --base main --head mobile-drafts --title "Sync author notes from mobile" --body "..."
```

レビュー後、validator が緑なら自動昇格（drafting → needs_review）が走り、`ledgers/revision_queue.md` も更新されます。

## 5. user-input マーカーを増やしたいとき

「備考」「コミュニティ補完メモ」も外出先で書きたくなったら、`scripts/add_user_input_markers.py` の `BLOCKS` 定数に追加して再実行すれば全エントリにべき等で追加されます。新しい key を入れた場合は templates も合わせて更新を忘れずに。

## 6. 制約・注意

- **マーカーを絶対に消さない**：本文 markdown 側で `<!-- user-input:start key="..." -->` を削除すると、その後の編集が PWA から不可能になります（RepoEdit が編集領域を見失う）
- **キーの重複禁止**：1 ファイル内で同じ `key` を 2 回使えません
- **ネスト禁止**：start...end の中に別の start を入れない
- **大量改行に注意**：保存時のバイト整合性は厳密。マーカー外のスペース・改行は Worker 側で byte-preserve される
- **PAT 失効に備える**：90 日ごとに更新。期限切れに気づくのは保存失敗時なので、カレンダーに入れる

## 7. mobile_inbox との関係

- 旧計画（`docs/mobile_inbox_requirements.md`）の Obsidian Mobile + `mobile_inbox/` 二段運用は **本手順の代替**として位置づけます
- RepoEdit が安定稼働するまでは旧手順も残します。新方式に完全移行した時点で `mobile_inbox/` 系ドキュメントを「廃止」マークに変更する予定

## 8. 関連

- 上流リポジトリ：<https://github.com/Taguchi-1989/RepoEdit>
- 上流仕様：[`REQUIREMENTS.md`](https://github.com/Taguchi-1989/RepoEdit/blob/main/REQUIREMENTS.md)
- マーカー埋め込みスクリプト：[scripts/add_user_input_markers.py](../scripts/add_user_input_markers.py)
- 旧モバイル運用：[mobile_inbox_requirements.md](mobile_inbox_requirements.md)

## 履歴

- v0.1（2026-05-17）: 初版。マーカー埋め込み完了時点のスナップショット。
