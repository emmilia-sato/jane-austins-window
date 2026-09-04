import os

def generate_austin_window_site():
    # プロジェクトのコンセプト設定
    site_config = {
        "title": "ジェイン・オースティンの窓",
        "subtitle": "19世紀リージェンシー・スタイルと文学の風景を辿る",
        "concept": "オースティン文学における『窓』を切り口に、当時のライフスタイル、建築、そして彼女が見た風景を紐解く専門メディア。",
        "sections": [
            {
                "id": "research",
                "title": "文学的リサーチ",
                "content": "作品に登場する窓辺の描写や、ハンプシャー、チョートンの史実を深く掘り下げます。"
            },
            {
                "id": "contents",
                "title": "デジタルコンテンツ",
                "content": "YouTubeやTikTokを通じ、視覚的に美しいリージェンシー・スタイルの日常を提案します。"
            },
            {
                "id": "management",
                "title": "商業マネジメント",
                "content": "ファンコミュニティの構築から、世界観を反映したオリジナル雑貨の展開まで。"
            }
        ],
        "color_theme": "#fdfaf5",  # 淡いアイボリー（アンティーク調）
        "accent_color": "#5d6d7e"  # クラシックなブルーグレー
    }

    # HTMLテンプレート
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{site_config['title']}</title>
        <style>
            body {{
                font-family: 'Georgia', 'Times New Roman', serif;
                background-color: {site_config['color_theme']};
                color: #333;
                line-height: 1.8;
                margin: 0;
                padding: 0;
            }}
            header {{
                text-align: center;
                padding: 100px 20px;
                background-color: {site_config['accent_color']};
                color: white;
            }}
            h1 {{ font-size: 3em; margin-bottom: 10px; letter-spacing: 2px; }}
            .subtitle {{ font-style: italic; font-size: 1.2em; opacity: 0.9; }}
            .container {{ max-width: 900px; margin: 0 auto; padding: 50px 20px; }}
            .concept {{ text-align: center; font-size: 1.4em; margin-bottom: 60px; color: #555; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; }}
            .card {{
                background: white;
                padding: 30px;
                border: 1px solid #ddd;
                box-shadow: 5px 5px 15px rgba(0,0,0,0.05);
                text-align: center;
                transition: transform 0.3s;
            }}
            .card:hover {{ transform: translateY(-10px); }}
            .card h3 {{ color: {site_config['accent_color']}; border-bottom: 1px solid #eee; padding-bottom: 10px; }}
            footer {{ text-align: center; padding: 40px; font-size: 0.9em; color: #888; }}
        </style>
    </head>
    <body>
        <header>
            <h1>{site_config['title']}</h1>
            <div class="subtitle">{site_config['subtitle']}</div>
        </header>
        <div class="container">
            <p class="concept">{site_config['concept']}</p>
            <div class="grid">
                {''.join([f'<div class="card"><h3>{s["title"]}</h3><p>{s["content"]}</p></div>' for s in site_config['sections']])}
            </div>
        </div>
        <footer>
            &copy; 2026 {site_config['title']} Project. All rights reserved.
        </footer>
    </body>
    </html>
    """

    # HTMLファイル生成
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("index.html の作成が完了しました。ブラウザで開いて確認してください。")


# 正しいエントリーポイント
if __name__ == "__main__":
    generate_austin_window_site()
