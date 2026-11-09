# Python Module 00

## English

Small Python functions that accept input, calculate values, and display results using gardens and plants as examples. Plot areas, harvest totals, and watering decisions introduce conditions and loops.

The supplied launcher selects an exercise. For example, the area exercise asks for length and width and displays the calculated area.

### Exercises

| Location | Exercise |
| --- | --- |
| [ex0](ex0/) | Print a greeting |
| [ex1](ex1/) | Read a garden name |
| [ex2](ex2/) | Calculate a plot area |
| [ex3](ex3/) | Sum harvest amounts |
| [ex4](ex4/) | Evaluate plant growth days |
| [ex5](ex5/) | Decide whether watering is needed |
| [ex6](ex6/) | Count days using loops and recursion |
| [ex7](ex7/) | Display seed inventory from arguments |

### Run

Requires Python 3.10 or newer and Make. Select an exercise using the supplied [main.py](main.py).

```sh
make
make run
make run ARGS=2
make run ARGS="7 --seed-type carrot --quantity 10 --unit packets"
```

The first item in `ARGS` is the exercise number, from `0` to `7`. Use `6-recursive` for the recursive harvest countdown. For interactive exercises, enter values when prompted.

## 日本語

庭や植物を題材に、値を入力し、計算して表示する小さなPython関数を作る演習です。面積の計算、収穫量の合計、水やりの判定などを通じて、条件分岐や繰り返しを扱います。

付属の起動プログラムで演習を選べます。例えば面積の演習では、縦と横の長さを入力すると、計算した面積が表示されます。

### 演習

| 場所 | 内容 |
| --- | --- |
| [ex0](ex0/) | 挨拶を表示する関数 |
| [ex1](ex1/) | 庭の名前を入力 |
| [ex2](ex2/) | 区画の面積を計算 |
| [ex3](ex3/) | 収穫量を合計 |
| [ex4](ex4/) | 植物の成長日数を判定 |
| [ex5](ex5/) | 水やりの要否を判定 |
| [ex6](ex6/) | 繰り返し・再帰で収穫日まで数える |
| [ex7](ex7/) | 引数を使った種の在庫表示 |

### 実行

Python 3.10以降・Make を使用します。付属の [main.py](main.py) から演習を選択できます。

```sh
make
make run
make run ARGS=2
make run ARGS="7 --seed-type carrot --quantity 10 --unit packets"
```

`ARGS` の先頭は演習番号です。`0`〜`7` を指定し、再帰版の収穫カウントは `6-recursive` を指定します。入力を使う演習では、起動後の案内に従って値を入力します。
