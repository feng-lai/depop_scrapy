[English](README.md) | [العربية](README-ar.md) | [Português](README-pt.md) | [Español](README-es.md)

# Depop 商品スクレーパー

## 概要
この Python スクリプトは、Selenium と BeautifulSoup を使用して Depop.com から製品情報を自動的に抽出します。タイトル、価格、説明、画像、オプション、レビューなどの製品詳細を収集し、JSON 形式で構造化されたデータとして出力します。

## 主な機能

- **自動データ収集**：Selenium WebDriver により Depop 製品ページを操作し、データを抽出
- **詳細な製品情報の取得**：
  - 製品タイトルと価格
  - 製品説明
  - 最大8枚の製品画像
  - 利用可能なオプション/バリエーション
  - 顧客レビューと評価
- **画像URL処理**：正規表現で画像URLを抽出・加工
- **JSON統合**：
  - `upload_results.json` からアップロード済み画像URLを読み込み
  - 元の画像URLを置き換え
  - 完全な製品情報を `product_info.json` に出力

## 技術仕様

- **Selenium WebDriver**：動的なコンテンツ処理とブラウザ自動化
- **BeautifulSoup**：複雑なHTML説明文の解析
- **WebDriverWait**：要素の読み込み完了を待機
- **JSON処理**：読み書きの両方に対応
- **例外処理**：各データ項目に対する堅牢なエラーハンドリング

## 使用方法

1. `product_page_url` にターゲット製品URLを設定
2. ChromeDriver が ChromeDriverManager 経由で正しくインストールされていることを確認
3. スクリプトを実行して以下を行う：
   - 製品ページを開く
   - 必要なデータ項目を抽出
   - データを処理・変換
   - 構造化されたJSONを出力
4. 実行完了後、ブラウザは自動的に閉じられます

## 出力構造（JSON例）
```json
{
  "price": "extracted_price",
  "itm_name": "product_title",
  "img1"〜"img8": "processed_image_names",
  "itm_dsc": "product_description",
  "cat_id": "category_id",
  "s_id": "seller_id",
  "attr": ["option1", "option2"],
  "eva": [{"name": "reviewer", "content": "review", "level": 5}]
}
