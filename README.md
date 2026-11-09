# Python Modules

## English

Small programs for learning Python through garden management, game scores, files, and spacecraft crew data. The series covers basic syntax through program organization.

`python_module00` through `python_module10` are learning topics; `ex0`, `ex1`, and similar directories contain individual exercises. Most files include demonstrations that print their results.

### Modules

| Module | Topic |
| --- | --- |
| [Module 00](python_module00/README.md) | Functions, input, conditions, and loops |
| [Module 01](python_module01/README.md) | Classes, inheritance, and data protection |
| [Module 02](python_module02/README.md) | Exceptions and cleanup |
| [Module 03](python_module03/README.md) | Collections, arguments, and generators |
| [Module 04](python_module04/README.md) | Files and standard streams |
| [Module 05](python_module05/README.md) | Abstract classes, polymorphism, and pipelines |
| [Module 06](python_module06/README.md) | Modules, packages, and imports |
| [Module 07](python_module07/README.md) | Creating creatures and switching abilities or strategies |
| [Module 08](python_module08/README.md) | Virtual environments, dependencies, and environment variables |
| [Module 09](python_module09/README.md) | Data validation with Pydantic |
| [Module 10](python_module10/README.md) | Passing, returning, and wrapping functions |

### Examples

Requires Python 3.10 or newer. Each module is independent.

```sh
python3 python_module01/ex0/ft_garden_intro.py
python3 python_module03/ex1/ft_score_analytics.py 10 20 30
```

The score example displays a total of 60, an average of 20.0, and a highest score of 30, among other results. Filenames follow each exercise's theme.

Module 00 uses a supplied `main.py` to select exercises. Module 08's visualization uses pandas, NumPy, and Matplotlib; Module 09 uses Pydantic 2.x.

## 日本語

小さなプログラムを作りながらPythonを学ぶ演習集です。庭の管理、ゲームのスコア集計、ファイルの読み書き、宇宙船の乗組員データなどを題材に、基礎文法からプログラムの構成方法までを扱います。

`python_module00`〜`python_module10` が学習テーマ、各ディレクトリの `ex0`・`ex1` などが個別の演習です。多くのファイルは実行用のデモを含み、処理の結果を端末で確認できます。

### モジュール

| モジュール | 内容 |
| --- | --- |
| [Module 00](python_module00/README.md) | 関数・入力・条件分岐・繰り返し |
| [Module 01](python_module01/README.md) | クラス・継承・データの保護 |
| [Module 02](python_module02/README.md) | 例外処理と後片付け |
| [Module 03](python_module03/README.md) | コレクション・引数・ジェネレータ |
| [Module 04](python_module04/README.md) | ファイル操作と標準入出力 |
| [Module 05](python_module05/README.md) | 抽象クラス・多態性・処理の組み合わせ |
| [Module 06](python_module06/README.md) | モジュール・パッケージ・インポート |
| [Module 07](python_module07/README.md) | 生物の生成と、能力・戦闘方法の切り替え |
| [Module 08](python_module08/README.md) | 仮想環境・依存関係・環境変数 |
| [Module 09](python_module09/README.md) | Pydanticによるデータ検証 |
| [Module 10](python_module10/README.md) | 関数を渡す・返す・処理を付け足す |

### 実行例

Python 3.10以降を使用します。各モジュールは独立した演習です。

```sh
python3 python_module01/ex0/ft_garden_intro.py
python3 python_module03/ex1/ft_score_analytics.py 10 20 30
```

スコア集計の例では、合計60・平均20.0・最高点30などを表示します。各ファイル名は演習の題材に合わせています。

Module 00 は付属の `main.py` から演習を選んで起動できます。Module 08のデータ可視化にはpandas・NumPy・Matplotlib、Module 09にはPydantic 2系を使います。
