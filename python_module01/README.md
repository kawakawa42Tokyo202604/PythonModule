# Python Module 01

## English

Exercises in Python classes through programs that manage plant names, heights, and other properties. Data and actions such as growing a plant are grouped together.

Later exercises add inheritance for different plant types and validation to reject invalid values. Running the demos displays plant information, growth, and summary results.

### Exercises

| Location | Exercise |
| --- | --- |
| [ex0](ex0/) | Display plant information |
| [ex1](ex1/) | Define a Plant class |
| [ex2](ex2/) | Grow plants and update state |
| [ex3](ex3/) | Create plants |
| [ex4](ex4/) | Validate values and protect data |
| [ex5](ex5/) | Inherit behavior for plant types |
| [ex6](ex6/) | Summarize plant data |

### Run

Requires Python 3.10 or newer, with no additional packages. Run from this directory.

```sh
python3 ex0/ft_garden_intro.py
python3 ex5/ft_plant_types.py
```

With Make, `make` checks syntax and `make run` runs `ex0/ft_garden_intro.py`. Set `ENTRY` and `ARGS` to choose a script and its arguments.

## 日本語

植物の名前・高さなどをまとめて管理するプログラムを作り、Pythonのクラスを学ぶ演習です。植物ごとのデータと、成長させるなどの操作を1つにまとめます。

演習が進むと、種類に応じて振る舞いを変える継承や、不正な値を受け付けないための検証を加えます。実行すると、植物の情報や成長・集計の結果を表示します。

### 演習

| 場所 | 内容 |
| --- | --- |
| [ex0](ex0/) | 植物情報の表示 |
| [ex1](ex1/) | Plantクラス |
| [ex2](ex2/) | 成長と状態の更新 |
| [ex3](ex3/) | 植物の生成 |
| [ex4](ex4/) | 値の検証とデータの保護 |
| [ex5](ex5/) | 植物の種類ごとの継承 |
| [ex6](ex6/) | 植物データの集計 |

### 実行

Python 3.10以降を使用します。追加パッケージは不要です。このディレクトリで実行します。

```sh
python3 ex0/ft_garden_intro.py
python3 ex5/ft_plant_types.py
```

Make を使う場合、`make` で構文を確認し、`make run` で `ex0/ft_garden_intro.py` を実行できます。`ENTRY` と `ARGS` で起動ファイルと引数を指定できます。
