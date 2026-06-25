# Python Projects

Pythonで作成した学習用プロジェクトをまとめたリポジトリです。

このリポジトリでは、コンソールアプリケーション、CSVファイルの操作、Turtleによる図形描画、関数、ループ、再帰処理などを扱っています。

## Projects

### 1. Japan Area Code Finder

日本の都市名と市外局番を検索・管理するコンソールアプリケーションです。

CSVファイルを使用してデータを保存し、都市名から市外局番を検索したり、市外局番から都市名を検索したりできます。

主な機能：

* 都市名から市外局番を検索
* 市外局番から都市名を検索
* データの一覧表示
* データの追加
* データの変更
* データの削除
* CSVファイルへの保存
* 入力チェック

使用技術：

* Python
* CSV
* Regular Expression
* pathlib

フォルダ：

japan-area-code-finder/

---

### 2. Turtle Fractal Generator

Pythonの`Turtle`モジュールを使用して、幾何学模様やフラクタル図形を描画するアプリケーションです。

回転する正方形、幾何学模様、コッホ曲線、コッホ雪片を描画できます。

主な機能：

* 回転する正方形の描画
* 幾何学模様の描画
* コッホ曲線の描画
* コッホ雪片の描画
* 再帰レベルの選択
* Turtleウィンドウでの描画

使用技術：

* Python
* Turtle
* Function
* for Loop
* Recursion
* Input Validation

フォルダ：

turtle-fractal-generator/

## Repository Structure

Python/
├── japan-area-code-finder/
│   ├── main.py
│   ├── city_codes.csv
│   └── README.md
├── turtle-fractal-generator/
│   ├── main.py
│   └── README.md
└── README.md

## 実行方法

各プロジェクトのフォルダに移動し、次のコマンドで実行します。

python main.py

詳しい使い方は、それぞれのプロジェクト内の`README.md`に記載しています。

## 学習した内容

このリポジトリのプロジェクトを通して、以下の内容を学習しました。

* Pythonの基本文法
* 関数を使用した処理の分割
* `while`と`for`を使用した繰り返し処理
* ユーザー入力の処理
* 入力値のチェック
* CSVファイルの読み込みと書き込み
* リストと辞書を使用したデータ管理
* 正規表現による文字列チェック
* Turtleを使用した図形描画
* 再帰処理によるフラクタル図形の作成


