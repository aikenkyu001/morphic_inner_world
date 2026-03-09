# Methodology Diagrams: Morphic Inner World (Mermaid Source)

This document contains the original Mermaid source code for the diagrams used in the academic papers. These diagrams visualize the transition from Natural Language to Deterministic Logic.

## 1. English Diagrams (EN)

### 1.1 The Global Flow
```mermaid
graph TD
    A[Outer World: Ambiguous NL] -->|Longest-Match Tokenization| B(Semantic Bridge)
    B -->|Arity-based Folding| C{AST: Formal Logic}
    C -->|Deterministic Reduction| D[VM: Pure Evaluator]
    D -->|Normalization| E[Inner World: Truth/Result]
    style E fill:#f9f,stroke:#333,stroke-width:4px
```

### 1.2 Arity-based Folding
```mermaid
graph LR
    subgraph Synthesis
    P1[Phrase A: Arity 1] --- V1[Var 1]
    P2[Phrase B: Arity 2] --- P1
    P2 --- V2[Var 2]
    end
    Synthesis -->|Fold| AST[AST Tree Structure]
```

### 1.3 Normal Form Reduction
```mermaid
stateDiagram-v2
    [*] --> Expression
    Expression --> Evaluation: App(Func, Arg)
    Evaluation --> Simplified: Beta-Reduction
    Simplified --> Evaluation: Nested Structure
    Simplified --> NormalForm: Irreducible
    NormalForm --> [*]
```

---

## 2. Japanese Diagrams (JP)

### 2.1 全体フロー
```mermaid
graph TD
    A[外界: 曖昧な自然言語] -->|最長一致トークナイズ| B(架け橋)
    B -->|アリティに基づくフォールディング| C{AST: 形式論理}
    C -->|決定論的簡約| D[VM: 純粋評価器]
    D -->|正規化| E[内界: 真理/結果]
    style E fill:#f9f,stroke:#333,stroke-width:4px
```

### 2.2 アリティに基づく論理合成
```mermaid
graph LR
    subgraph Synthesis
    P1[フレーズA: アリティ1] --- V1[引数1]
    P2[フレーズB: アリティ2] --- P1
    P2 --- V2[引数2]
    end
    Synthesis -->|合成| AST[AST 木構造]
```

### 2.3 正規形への簡約
```mermaid
stateDiagram-v2
    [*] --> 式
    式 --> 評価: 関数適用
    評価 --> 簡約: ベータ簡約
    簡約 --> 評価: 入れ子構造
    簡約 --> 正規形: 最終結果
    正規形 --> [*]
```
