# モバイル（Android）セットアップ手引き

*著者本人が Android スマホで、`mobile_inbox/` に書き溜めを始められる状態にするまでの実作業手引きです。所要 30〜45 分。*

*前提仕様：[mobile_inbox_requirements.md](mobile_inbox_requirements.md)。全体像はそちらを読んでください。本ファイルは Phase 1 を 1 回で通すための具体手順に絞ります。*

## このドキュメントのゴール

30〜45 分後に、次の状態になることです。

- Android の Obsidian Mobile で、本リポジトリ（`VibeCodingDictionary`）を vault として開ける
- `mobile_inbox/YYYY-MM-DD.md` に書き込むと、自動で GitHub に push される
- PC で `git pull` すると、スマホで書いた内容が届いている

## 用意するもの

- Android スマホ（OS バージョンは特に制約なし）
- GitHub アカウント（既にこのリポジトリを push できている前提）
- 作業時間 30〜45 分

## 手順

### Step 1. Obsidian Mobile をインストール

1. Google Play ストアで **「Obsidian」** を検索
2. 緑紫のロゴの「Obsidian - Connected Notes」をインストール（Obsidian.md 社）
3. 起動してアカウント登録ダイアログが出ても、**Sync は使わないので "Skip" で閉じる**

### Step 2. GitHub Fine-grained PAT を作る

スマホの Chrome か、PC で次の操作をします。PC の方が圧倒的に楽なので、**PC 側で作ってスマホに送る**のを推奨。

1. <https://github.com/settings/personal-access-tokens/new> を開く（Fine-grained の新規作成ページ）
2. 次のように設定：
   - **Token name**: `obsidian-mobile-vibecoding`
   - **Expiration**: 90 days（最大）
   - **Repository access**: `Only select repositories` → **VibeCodingDictionary だけ**を選ぶ
   - **Repository permissions**:
     - **Contents**: `Read and write`
     - **Metadata**: `Read-only`（自動で付く）
3. 「Generate token」を押して、**表示されたトークン文字列をコピーしてスマホへ送る**（自分宛の Gmail 下書きや Keep メモに貼る）
4. **重要**：このページを閉じるとトークンは二度と表示されない。失くしたら作り直す

### Step 3. リポジトリをスマホに clone する（Obsidian Git のインストール後）

Obsidian Git プラグインは **isomorphic-git**（JavaScript 実装の git）を使うので、PC の git とは仕組みが違います。手順は Obsidian の中で完結します。

1. Obsidian で「+ Create new vault」ではなく、**「Open folder as vault」**を選ぶ
2. 新規フォルダを作る：ファイル名は適当に `VibeCodingDictionary`
   - 保存先は **内部ストレージ**（`Android/data/md.obsidian/` ではなく、`Documents/` 等のアクセスしやすい場所）
3. vault を開いたら、左下の **歯車 → コミュニティプラグイン** を開く
4. 「Turn on community plugins」を有効化
5. 「Browse」で **Obsidian Git** を検索 → インストール → 有効化

### Step 4. Obsidian Git でクローン

1. 左下歯車 → コミュニティプラグイン → **Obsidian Git** の設定を開く
2. 右サイドバーで **Obsidian Git のコマンドパレット**（アイコン）を開く、または左上ハンバーガーメニュー → コマンドパレット（`Ctrl+P` 相当）から `Obsidian Git: Clone an existing remote repo` を検索して実行
3. ダイアログが出たら：
   - **URL**: `https://<PAT>@github.com/Taguchi-1989/VibeCodingDictionary.git`
     - `<PAT>` のところに、Step 2 でコピーしたトークン文字列をそのまま埋め込む（前後の `@` と `https://` の間に入れる）
   - **Depth**: 空欄のまま
4. クローンが走る（初回は 1〜3 分かかる）
5. 完了すると、現在の vault のルートに本リポジトリの全ファイルが展開される

### Step 5. 認証情報とコミッターを設定

vault ルートに `.obsidian/plugins/obsidian-git/data.json` ができているが、直接触らなくて OK。設定画面から入力。

1. コミュニティプラグイン → Obsidian Git → 設定
2. **Authentication / Commit Author**:
   - Username: GitHub のユーザー名（例：`Taguchi-1989`）
   - Password/Personal Access Token: **Step 2 で作った PAT 文字列** を貼る
   - Author name to use for commits: `Taguchi (mobile)`
   - Author email to use for commits: GitHub に登録のメールアドレス
3. **Automatic**:
   - Vault backup interval (minutes): `10`（10 分おきに自動 commit & push）
   - Auto pull interval (minutes): `10`（同じ間隔で pull）
   - Auto pull on startup: **ON**
4. **Commit Author / Commit Message**:
   - Commit message on manual backup/commit: `mobile: {{date}}`
   - Commit message on auto backup/commit: `mobile auto: {{date}}`

### Step 6. 初回テスト

1. スマホの Obsidian で `mobile_inbox/` フォルダを開く
2. 右上の「+」→「New note」で `2026-04-24.md` を作る（日付は今日）
3. 以下をコピーして貼る：

```markdown
## B-2 / my_comment / first_impression
初見シンプル。ただ3つの入口があると知って最初は戸惑った。

## F-50 / stumble
最初は add と commit の違いが腑に落ちなかった。
```

4. 右サイドバーの Obsidian Git アイコン → **「Commit and push」** をタップ（または 10 分待って自動 push）
5. PC 側で：

```bash
cd d:/dev/VibeCodingDictionary
git pull
```

6. `mobile_inbox/2026-04-24.md` が届いていれば成功

### Step 7. PC 側で取り込みテスト

Claude Code で：

> import-comments 実行して

と伝える。`skills/import-comments.md` の手順通りに、B-2 Claude と F-50 git の該当欄に反映されます。

## トラブルシューティング

### clone 時に "authentication failed"

- PAT の有効期限切れ／権限不足が多い
- Fine-grained PAT の **Contents: Read and write** が付いているか確認
- URL に埋め込んだ PAT 文字列に余計な空白・改行が混じっていないか確認
- 最終手段：PAT を作り直し、Step 4 から再実行

### push はできるが pull で conflict

- PC 側で同じファイルを触っているケース
- 原則：**mobile_inbox/ は PC 側で触らない** のを自己ルール化（Claude Code にも伝わっているはず）
- conflict が起きたら、PC 側で `git pull` → 手動マージ → `git push`、その後スマホで Obsidian Git の「Pull」

### Obsidian アプリが重い／クラッシュ

- vault が巨大だと起きやすい
- 対策：`.obsidian/plugins/` 以外の不要ファイル（画像、PDF 等）を vault 外に移す
- 最軽量の対処：本 vault には `mobile_inbox/` と `content/entries/` だけを置き、他は無視する運用も可（ただし `content/` を見ながら書きたいなら避ける）

### PAT の期限が切れたら

- 90 日経つと push/pull が失敗し始める
- Step 2 の要領で PAT を作り直し、Step 5 の設定画面で新しい PAT に差し替える

## このあと

Phase 1 が回り始めたら、次は **実編集ワークフロー**（受信箱への書き溜めだけでなく、著者欄や裏台帳への直接編集）に進みます。手順は [mobile_editing_guide.md](mobile_editing_guide.md) にまとめてあります。

加えて、以下の TODO が残っていることだけ把握しておいてください。

- **スキル実装**：`skills/import-comments.md` は手順書。運用を重ねて、スクリプト化が必要になったら Phase 3 へ
- **テンプレ化**：スマホ側でのセクション挿入を Obsidian Templates プラグインで 1 タップ化できる（余裕があれば）

## 関連

- 実編集ワークフロー（次に読む）：[mobile_editing_guide.md](mobile_editing_guide.md)
- 全体像：[mobile_inbox_requirements.md](mobile_inbox_requirements.md)
- 取り込みスキル：[../skills/import-comments.md](../skills/import-comments.md)
- 受信箱 README：[../mobile_inbox/README.md](../mobile_inbox/README.md)

## 履歴

- v0.1（2026-04-24）: 初版。Android 向け Phase 1 を 1 回で通すための手引き。
