# 誌面デザインたたき台（A4 / 印刷品質向け HTML モック）

3案を同じ3ページ（Gemini ／ Gemini 2.5 系モデル比較 ／ TypeScript）で作成。
いずれもブラウザで開いて「印刷 → PDF に保存」すると A4 縦でそのまま出力できる。

## 3 案の比較

| 案 | ファイル | ひと言 | 向いている印象 | 迷ったら |
| --- | --- | --- | --- | --- |
| **A v2** Human (採用) | `design_A_v2_human.html` | A をベースに、図の中に人物＋吹き出しを統合 | **2026-04-22 採用**：概念や用語がどう人に映るかを主役にした版 | **現時点の標準** |
| A v1 Clean Zukan | `design_A_zukan.html` | 白背景＋青系2色、端正な図鑑（人物なし） | A v2 の比較用。構造図のみで読む純粋なレイアウト検証に | レイアウトの素地を確認したいとき |
| **B** Editorial Navy | `design_B_editorial.html` | 紺の帯と大きな № 表示、書籍寄り | 「本として出す」の重みが欲しい／冊子・配布物で押し出しを出したい | 書籍化を意識するなら |
| **C** Blueprint | `design_C_blueprint.html` | 薄いグリッド＋等幅記号、技術資料 | テック感・精度感が欲しい／社内勉強会・エンジニア混在の場 | 技術側の読者も意識するなら |

### 採用方針（2026-04-22）

**A v2 Human** を現時点の標準候補にする。理由：A のレイアウトをベースに、図解の中へ棒人間＋吹き出しを統合し、「人が使ってどうなるか／どう感じるか」を主役にしたため。この本の差別化は「感想と体験を持った語彙集」であり、抽象的な構造図・グラフだけでは意図が死ぬ。A v1 はレイアウト検証用に残す。

全案で共通：

- A4 縦、上下左右の余白をしっかり確保
- 1ページ1項目
- 上部に ID／カテゴリ／評価日、下部に関連語＋ページ番号
- 図は SVG（解像度が落ちない）

## PDF 化の手順（最短）

1. `.html` をブラウザ（Chrome / Edge 推奨）で開く
2. `Ctrl + P` で印刷ダイアログ
3. 送信先：**PDF に保存**
4. 用紙：**A4**
5. 余白：**なし**（CSS 側で余白を持たせているため「なし」で正解）
6. **背景のグラフィック：オン**（これを忘れると色が飛ぶ）
7. 保存

## 高品質 PDF が必要な場合（任意）

Chrome の「PDF 保存」で十分印刷に耐えるが、より安定した出力が欲しければ：

```sh
# 例: Playwright で HTML → PDF
npx playwright install chromium
node -e "
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file:///d:/dev/VibeCodingDictionary/drafts/prototypes/mockups/design_A_v2_human.html', { waitUntil: 'networkidle' });
  await p.pdf({ path: 'design_A_v2_human.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
"
```

## 各案の実装メモ

### A v2 — Human Clean Zukan（採用）

- Palette A（#2563EB / #DBEAFE / #1E3A8A）＋ 差し色の warn (#F59E0B)
- 3 ページすべての図に、棒人間キャラクター＋吹き出しを統合
- サービス頁（101 Gemini）：3 入口それぞれに使う人を置き、心の声で意味を示す
- モデル頁（201 Gemini 2.5）：2 軸マップに「どれ使う？」と迷う学び手を置き、各ドット横に仕事別キャラクター
- 用語頁（302 TypeScript）：同一キャラクターの Before（驚く）／After（気付く）を左右に配置

### A v1 — Clean Zukan（人物なし）

- Palette A（#2563EB / #DBEAFE / #1E3A8A）
- 見出しには `■` 風のキューブを添え、図鑑の索引カードの雰囲気
- A v2 採用前のレイアウト検証用として保持

### B — Editorial Navy（エディトリアル）

- Palette C（#1D4ED8 / #0B1F3A）＋ 控えめなゴールド `#C8A45A` をアクセント
- 見出しに明朝（Noto Serif JP）を使い、書籍らしい重み
- 大きな `№ 101` を図案要素として使用
- 図の角には L 字のコーナーマーク。見開き印刷や冊子化に耐える

### C — Blueprint（青写真・テックノート）

- Palette B（#0F72B8 / #06B6D4）
- 紙に 10mm グリッドのうっすらした下地
- コーナーに位置合わせマーク、等幅フォントで座標系ラベル
- 技術資料の手触り。勉強会の配布資料との親和性が高い

## 次にやるとよいこと（提案）

1. A v2 のキャラクターを誌面共通の「案内役」として定型化する（Before/After、動作イメージ、困りごと→解決 の各シーンで同じ顔が再登場する運用）
2. 吹き出しの口調と心の声の書き分けガイドを編集スタイルに追加
3. 既存エントリ（JavaScript / ESLint / React / Next.js）を A v2 に流し込み、量が増えたときの読み疲れを確認
4. 表紙・目次・奥付・裏表紙を足して、書籍としての通し感を確認
5. 印刷見本（家のプリンタでよい）を1部刷って、紙で見たときの青の深さ・文字の細さ・人物線の太さを確認
