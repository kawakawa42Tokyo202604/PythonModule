# Python Module 07

## English

Python exercises in switching object types and behavior through creature battles. They combine factories that create creatures by type, abilities such as healing or transformation, and attack or defense strategies.

The demos show created creatures and the behavior of selected abilities and strategies.

### Exercises

| Location | Exercise |
| --- | --- |
| [ex0](ex0/) | Creature classes and factories |
| [ex1](ex1/) | Healing and transformation abilities |
| [ex2](ex2/) | Normal, attack, and defense strategies |

### Run

Requires Python 3.10 or newer, with no additional packages. Run from this directory.

```sh
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

`battle.py` demonstrates the basic factory, `capacitor.py` adds abilities, and `tournament.py` combines battle strategies.

With Make, `make` checks syntax and `make run` runs `battle.py`. Set `ENTRY` and `ARGS` to choose a script and its arguments.

## 日本語

生物同士の戦闘を題材に、作成する種類や行動を切り替えられるPythonプログラムを作る演習です。種類を指定して生物を生成するファクトリ、回復・変身の能力、攻撃・防御などの戦略を組み合わせます。

付属のデモを実行すると、生成した生物や、選んだ能力・戦略を使う動作を確認できます。

### 演習

| 場所 | 内容 |
| --- | --- |
| [ex0](ex0/) | 生物クラスとファクトリ |
| [ex1](ex1/) | 回復・変身の能力を持つ生物 |
| [ex2](ex2/) | 通常・攻撃・防御の戦略 |

### 実行

Python 3.10以降を使用します。追加パッケージは不要です。このディレクトリで実行します。

```sh
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

`battle.py` は基本ファクトリ、`capacitor.py` は追加能力、`tournament.py` は戦略を組み合わせたデモです。

Make を使う場合、`make` で構文を確認し、`make run` で `battle.py` を実行できます。`ENTRY` と `ARGS` で起動ファイルと引数を指定できます。
