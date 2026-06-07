# レイアウト決定ログ

## 2026-04-22 時点の仮決定

### 決定候補
- 本文構造は共通化する。
- レイアウトは `figure_type` で分岐する。
- 初期標準は `structure`, `comparison`, `before_after` の3種類に絞る。
- `workflow` と `timeline` はサンプルが増えてから正式化する。
- 色は Palette A: Clean Blue を第一候補にする。

### 保留
- 出典メモを公開ページに出すか、裏台帳だけにするか。
- コミュニティ補完メモを公開ページに出すか、制作メモにするか。
- 誌面サイズをA4、B5、スライド比率のどれに寄せるか。
- 最終レイアウトをHTML/CSSで作るか、デザインツールに渡すか。

## 判断理由
1テンプレだけにすると、比較項目やBefore/After項目が窮屈になる。

一方で、項目ごとに完全自由にすると量産しにくい。したがって、本文は共通、見た目は数種類の型に制限するのがよい。

## 次に確認すること
- 7本のサンプルを読んで、本文量が多いか少ないかを見る。
- デザイン案A/B/C/Dのどれが一番「図鑑らしい」かを見る。
- 公開面と裏台帳の情報分離を決める。

## 参照入口
- `drafts/prototypes/template_review_hub.html`
- `drafts/prototypes/mockups/index.html`
- `drafts/prototypes/preview/`
