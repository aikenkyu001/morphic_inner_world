# Methodology Diagrams: Morphic Inner World (Mermaid Source)

This document contains the FINAL, verified Mermaid source code for the academic paper. Each figure is strictly ONE single-panel diagram.

## 1. English Diagrams (EN)

### 1.1 Global Architecture
```mermaid
graph TD
    Input[Natural Language Input] --> Tok(Longest-Match Tokenizer)
    Tok --> Filt(MSP Noise Filter)
    Filt --> Dict(Semantic Dictionary)
    Dict --> AST{Formal AST}
    AST --> VM[Morphic VM Kernels]
    VM --> Truth[Normal Form / Truth]
    style Truth fill:#f9f,stroke:#333,stroke-width:2px
```

### 1.2 Recursive Folding Logic
```mermaid
graph LR
    Phrases[Linear NL Phrases] --> Arity{Arity Check}
    Arity -->|Partial| Closures[VClosures]
    Arity -->|Complete| AST[Irreducible AST]
    Closures --> Arity
```

### 1.3 Deterministic Kernel Parity
```mermaid
graph TD
    AST{Unified AST} --> Python[Python Kernel]
    AST --> Fortran[Modern Fortran Kernel]
    Python --> Parity{Bit-Identical?}
    Fortran --> Parity
    Parity --> Result[Normal Form]
    style Result fill:#f9f,stroke:#333
```

### 1.4 Execution Trace Pipeline
```mermaid
graph LR
    NL["'sort, filter'"] --> Map["ID: 1, 2"]
    Map --> App["App(filter, App(sort, arg))"]
    App --> Res["VLiteral(Result)"]
```

### 1.5 Substrate Independence Layer
```mermaid
graph TD
    Spec[Logical Spec] --> WB(Wisdom Base)
    WB --> Py[Python Implementation]
    WB --> Ft[Fortran Implementation]
```

### 1.6 Scaling Reliability
```mermaid
graph LR
    Complexity[v8000 / d15 / n20] --> Morphic[Morphic: 100%]
    Complexity -.-> LLM[LLM: Stochastic Decay]
    style Morphic fill:#dfd,stroke:#333
```

### 1.7 Language Invariance Manifold
```mermaid
graph TD
    EN[English Spec] -->|Projection| AST((Universal AST))
    JP[Japanese Spec] -->|Projection| AST
    AST --> Result[Normalized Truth]
    style AST fill:#f9f,stroke:#333
```

### 1.8 Deterministic Error Flow
```mermaid
graph TD
    Eval[Evaluation] --> Logic{Valid?}
    Logic -->|Yes| NF[Normal Form]
    Logic -->|No| VError[VError Value]
```
