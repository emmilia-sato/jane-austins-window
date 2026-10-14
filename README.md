# emmilia-sato.vercel.app — サイトのソース

静的な HTML/CSS だけで構成されたサイトです（ビルド不要）。

```
index.html                  トップページ
assets/site.css             サイト共通のスタイル（全ページ）
assets/img/                 画像（JPEG と WebP）。出典・ライセンスは assets/img/CREDITS.md
assets/img/placeholder.svg  テンプレート用の仮画像
credits/index.html          「画像について」ページ（フッターからリンク）
notes/index.html            研究ノート一覧ページ（新しい順）
notes/_template/index.html  記事ページのテンプレート（コピー元。公開用ではありません）
notes/sample-article/       サンプル記事（差し替え・削除してください）
.vercelignore               README・テンプレート・STRATEGY_ROADMAP.md・generate_site.py・archive/ をデプロイ対象から外す設定
```

## 新しい研究ノートを追加する手順

1. **テンプレートをコピーする**
   `notes/_template/` フォルダを丸ごとコピーし、記事用の名前を付けます。
   フォルダ名は URL になるため、半角英数字とハイフンにします（例: `notes/2026-11-pride-and-prejudice/`）。

   ```sh
   cp -r notes/_template notes/2026-11-my-note
   ```

2. **記事ページを編集する**（`notes/2026-11-my-note/index.html`）
   - `【記事タイトル】` を2か所（`<title>` と `<h1>`）置き換える
   - `【記事の短い説明】`（meta description）を置き換える
   - 日付：`datetime="YYYY-MM-DD"` と表示用の `YYYY年M月D日` を置き換える
   - ヘッダー画像：`<figure class="article-header-figure">` の `href`・`src`・`alt`・キャプションを差し替える（使わない場合は figure ごと削除）。画像クリックで拡大表示になります
   - 本文中の図版：`<figure class="framed">`（中央）または `<figure class="framed float-right">`（右寄せ）。`a.zoomable` の `href` は拡大する画像、`img` には `loading="lazy"` を付ける
   - 本文・小見出し・引用・参考文献を書く（不要なブロックは削除）
   - 末尾の移動ナビ：`← 研究ノート一覧へ` は残す。前の記事・次の記事は実在する記事だけ残し、無い側のリンクは削除する
   - 公開する記事では `<meta name="robots" content="noindex" />` の行を削除する

3. **一覧ページに追加する**（`notes/index.html`）
   `<ol class="note-list">` の**先頭**（一番上）に次のブロックを追加します。一覧は新しい順です。

   ```html
   <li class="note-item">
     <a class="note-thumb" href="/notes/2026-11-my-note/" aria-label="記事タイトル">
       <img src="/assets/img/サムネイル画像.jpg" width="480" height="360" loading="lazy" decoding="async" alt="" />
     </a>
     <div>
       <time datetime="2026-11-01">2026年11月1日</time>
       <h2><a href="/notes/2026-11-my-note/">記事タイトル</a></h2>
       <p>一覧に表示する短い抜粋（1〜2文）。</p>
       <a class="more" href="/notes/2026-11-my-note/">続きを読む &rarr;</a>
     </div>
   </li>
   ```

   サムネイルは横長（4:3 程度、幅 480px 前後）が適しています。画像がない場合は `/assets/img/placeholder.svg` を指定できます。

4. **画像のクレジットを追記する**
   新しい画像を使ったら、`assets/img/CREDITS.md` と `credits/index.html` に作品名・作者・年代・出典 URL・ライセンスを追加します。
   画像はパブリックドメインまたは CC0 のもの（Wikimedia Commons のファイルページで確認）だけを使ってください。

5. **サンプル記事を消す場合**
   `notes/sample-article/` フォルダを削除し、`notes/index.html` からサンプルの `<li class="note-item">` ブロックを削除します。
   サンプル専用の画像（`assets/img/sample-*`）も不要なら削除し、クレジットからも外します。

## ローカルで確認する

リンクはサイトのルートから始まるパス（`/notes/` など）なので、ファイルを直接開くのではなく、
このフォルダでローカルサーバーを起動して確認してください。

```sh
python3 -m http.server 8000
# → http://localhost:8000/ と http://localhost:8000/notes/
```

## SEO（記事を公開するときの追加作業）

- 記事ページの `<head>` 冒頭のコメントに従い、`<title>`・description・canonical・`og:*`・`twitter:*`・
  JSON-LD（BlogPosting）の `【 】` / `SLUG` / `YYYY-MM-DD` をすべて置き換え、`noindex` の行を削除する。
- OG 画像は 1200×630 の JPEG を `assets/img/og-記事名.jpg` として作ると、SNS でのリンク表示がきれいになります（なければ `og-notes.jpg` のままで可）。
- `sitemap.xml` に記事の URL を `<url><loc>…</loc><lastmod>YYYY-MM-DD</lastmod></url>` で追加する。
  テンプレート（`notes/_template/`）とサンプル記事は sitemap に入れないでください。
- 公開後、Google Search Console / Bing Webmaster Tools で sitemap（`https://emmilia-sato.vercel.app/sitemap.xml`）を送信すると反映が早くなります。

その他のファイル：`robots.txt`（全クロール許可＋sitemap の場所）、`404.html`（存在しない URL で表示）、
`favicon.svg` / `favicon-32.png` / `favicon.ico` / `apple-touch-icon.png`（ブラウザのタブ・ホーム画面のアイコン）。
