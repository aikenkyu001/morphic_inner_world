# Morphic Core 言語仕様 (Internal World Core)

内界（Inner World）における決定論的推論のためのコア言語仕様。

## 1. 型システム (Type System)
内界は強い型付けを持ち、以下の基本型から構成される。

- **Unit**: 単一の値 `()` を持つ型。
- **Bool**: `True` | `False`。
- **Int**: 整数（多倍長精度）。
- **List[T]**: 型 T の同次リスト。
- **Pair[A, B]**: 直積型。
- **Func[A, B]**: A から B への純粋関数。
- **Sheaf[X]**: 位相空間（被覆）上の構造を表す幾何学的型。

## 2. 抽象構文 (AST)
内界の VM が解釈する最小限の命令セット。

- `Literal(value)`: 定数。
- `Var(name)`: 変数参照。
- `Lambda(param, body)`: 関数定義（一変数）。
- `App(func, arg)`: 関数適用。
- `Let(name, value, body)`: 変数結合。
- `If(cond, then_br, else_br)`: 条件分岐。
- `Fix(name, body)`: 構造再帰（停止性が保証される範囲に限定）。
- `MorphicStep(prev_sheaf, delta)`: HLI における知識の増分操作。

## 3. 操作的意味論 (Operational Semantics)
- 全ての式は **正規化（Normal Form）** に至るまで決定論的に簡約される。
- `eval(expr, env) -> value` は外界の例外を投げず、必ず `Result[Value, Error]` を返す。
- 幾何学的整合性（Gluing Axiom）のチェックは型検査時に行われる。

---
**「内界において、真理は計算によって導かれるのではなく、型の一致によって自明となる。」**

## 4. Morphic Specification Protocol (MSP) v1
外界（自然言語）の曖昧さを内界（AST）へ橋渡しするための、厳格な仕様記述プロトコル。

### 文法 (Grammar)
仕様は以下の 3 つのセクションで構成される。

1. **INPUT**: 引数名の定義。
   - `INPUT: [param1], [param2], ...`
2. **LOGIC**: 変数結合（Let）の連鎖。
   - `LET [var_name] = [AST_Expression]`
   - AST_Expression 内では `App`, `Var`, `Literal`, `Lambda`, `If`, `Fix`, `Let` を使用可能。
3. **OUTPUT**: 最終的な評価結果。
   - `OUTPUT: [AST_Expression]`

### 記述例：活動選択問題 (activity_selection)
```text
INPUT: a
LOGIC:
  LET sorted = App(Var('sort_by_end'), Literal(a))
  LET filtered = App(Var('filter_overlapping'), Var('sorted'))
OUTPUT:
  App(Var('length'), Var('filtered'))
```

### 変換プロセス (Bridge Process)
1. 外界から MSP 形式のテキストを入力。
2. ブリッジ（パーサー）が LOGIC を `Let` の入れ子構造に変換。
3. 最外層から `Lambda` で包み、VM で実行可能な AST を生成。
