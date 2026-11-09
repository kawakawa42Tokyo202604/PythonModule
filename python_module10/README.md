# Python Module 10

## English

Python exercises in composing behavior by passing functions as arguments or returning them from other functions. They start with sorting and filtering and progress to functions that retain settings and reuse cached results.

The decorator exercise adds timing around a function and displays its result and execution time. It demonstrates separating the original computation from additional behavior.

### Exercises

| Location | Exercise |
| --- | --- |
| [ex0](ex0/) | Sort, filter, and transform with lambdas |
| [ex1](ex1/) | Functions that accept or return functions |
| [ex2](ex2/) | Closures and scope |
| [ex3](ex3/) | reduce, partial, caching, and type-based dispatch |
| [ex4](ex4/) | A timing decorator |

### Run

Requires Python 3.10 or newer, with no additional packages. Run from this directory.

```sh
python3 ex0/lambda_spells.py
python3 ex3/functools_artifacts.py
make run ENTRY=ex4/main.py
```

`ex4/main.py` runs a decorated function and displays its result and execution time.

With Make, `make` checks syntax and `make run` runs `ex0/lambda_spells.py`. Set `ENTRY` and `ARGS` to choose a script and its arguments.

## 日本語

関数を引数として渡したり、別の関数から返したりして、処理を組み合わせるPython演習です。値の並べ替えや絞り込みから始め、設定を覚えた関数や、結果を再利用する仕組みを作ります。

例えばデコレータの演習では、関数に計測処理を付け足し、実行結果と処理時間を表示します。元の関数と追加の役割を分けて扱う方法を学びます。

### 演習

| 場所 | 内容 |
| --- | --- |
| [ex0](ex0/) | lambdaによる並べ替え・絞り込み・変換 |
| [ex1](ex1/) | 関数を受け取る・返す高階関数 |
| [ex2](ex2/) | クロージャとスコープ |
| [ex3](ex3/) | reduce・partial・キャッシュ・型別ディスパッチ |
| [ex4](ex4/) | 実行時間を計測するデコレータ |

### 実行

Python 3.10以降を使用します。追加パッケージは不要です。このディレクトリで実行します。

```sh
python3 ex0/lambda_spells.py
python3 ex3/functools_artifacts.py
make run ENTRY=ex4/main.py
```

`ex4/main.py` はデコレータを適用した関数を実行し、結果と処理時間を表示します。

Make を使う場合、`make` で構文を確認し、`make run` で `ex0/lambda_spells.py` を実行できます。`ENTRY` と `ARGS` で起動ファイルと引数を指定できます。
