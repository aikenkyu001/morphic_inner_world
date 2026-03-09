# Morphic Inner World: Quantifying "Deterministic Intelligence" through Geometric NL-AST-EVAL Pipeline

**Author:** Fumio Miyata  
**Date:** March 9, 2026  
**DOI:** [10.5281/zenodo.18905026](https://doi.org/10.5281/zenodo.18905026)  
**Repository:** [https://github.com/aikenkyu001/morphic_inner_world](https://github.com/aikenkyu001/morphic_inner_world)

This repository hosts the **Morphic Inner World**, a foundational framework designed to demonstrate and quantify **Deterministic Intelligence** through a Geometric NL-AST-EVAL pipeline.

## 1. Core Breakthrough: 100% Deterministic Reliability
We have established and verified **100.0% Reliability** across a bilingual benchmark of 60 complex algorithmic tasks. Unlike stochastic models (LLMs) that rely on probabilistic approximation, the Morphic framework ensures that logic is preserved with mathematical precision across different languages and execution kernels.

**[Updated March 9, 2026]**: Revised Academic Paper (v1.1) now available in `Reports/`, including formal algorithms and detailed benchmark specs.

## 2. Key Technical Features
- **Geometric Projection**: Mapping Natural Language (NL) to irreducible Abstract Syntax Trees (AST) using a structure-preserving morphism.
- **Scale Invariance**: Proved stability under extreme scaling:
  - **v8000**: Processing specifications exceeding 8,000 tokens with zero logical decay.
  - **d15**: Correct execution of 15-level recursive/nested structures.
  - **n20**: Simultaneous verification of 20+ independent logical constraints.
- **Bilingual Identity**: Absolute parity between English and Japanese task specifications.

## 3. Quick Start
To replicate the 100% success rate across all kernels:
```bash
# Requires Python 3.12+ and gfortran/fpm
./Scripts/verify_all.sh
```

## 4. Repository Map
- `Benchmark/`: 60 Task directories with bilingual specs (`.nl`) and truth-sets (`test_solution.py`).
- `VM/`: Execution kernels (Python Evaluator & Modern Fortran Engine).
- `Theory/`: Formal core language specs and the 1:1 Semantic Dictionary.
- `Scripts/`: Automation tools for synthesis, alignment, and global verification.
- `Reports/`: 
  - `academic_paper_en.md` / `jp.md`: Revised Paper (v1.1).
  - `BENCHMARK_SPEC.md`: Detailed metadata for 60 tasks.
  - `FORMAL_METHODOLOGY.md`: Morphic Primitives & Synthesis Algorithms.
  - `TRACE_EN_JP_PARITY.md`: Trace of language invariance.

---
**"Correct words form correct shapes. Protocol is the skeleton that supports the boundaries of intelligence."**
