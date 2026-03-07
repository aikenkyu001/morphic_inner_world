# File Descriptions: Morphic Inner World

This document provides a detailed overview of the directory structure and file functions within the **Morphic Inner World** project, a framework for **Deterministic Intelligence**.

## Root Directory

- **README.md**: The main documentation file providing project overview, "Geometric Projection" methodology, architecture, and benchmark results.
- **FILE_DESCRIPTIONS.md**: This file, providing a map of the project's components and logical structure.

## Benchmark/

This directory contains the core benchmark suite, consisting of 60 algorithmic tasks used to verify deterministic execution across various complexity gradients. Each subdirectory typically includes:
- **problem.nl**: English natural language specification of the task logic.
- **problem_jp.nl**: Japanese natural language specification of the task logic.
- **test_solution.py**: Pytest suite used to validate the behavioral correctness of generated solutions.

### Categories include:
- **Algorithmic Tasks**: `activity_selection`, `sudoku_solver`, `dijkstra_shortest_path`, `lru_cache`, `matrix_chain_multiplication`, etc.
- **Synthetic Scale-Invariance**: `synthetic_constraints_n*` (multi-constraint), `synthetic_nesting_d*` (deep recursion), `synthetic_context_v*` (large-volume context).
- **Composite Logic**: `task_60` (dynamic synthesis of multiple logical primitives).

## Log/

Stores detailed execution traces from benchmark runs.
- **benchmark_[timestamp].log**: Comprehensive trace of the synthesis and verification process, including VM evaluation steps (when `MORPHIC_TRACE=1`).

## Reports/

Aggregated findings and scientific documentation.
- **MORPHIC_DETERMINISTIC_INTELLIGENCE_SPEC.md**: The final scientific report detailing the theoretical proof and 100% success rate results.
- **BENCHMARK_RESULTS_LOG.json**: (Generated) Structured summary of the latest benchmark run, used for automated reporting.

## Scripts/

The operational engine of the project, containing tools for synthesis, synchronization, and verification.

### Synthesis & Rebuild
- **morphic_synthesizer.py**: The core synthesis engine that transforms NL specifications into Morphic AST code using longest-match and arity-based stacking.
- **rebuild_solutions_bilingual.py**: Orchestrates the bulk generation of `solution.py` and `solution_jp.py` for all 60 tasks across both languages.

### Verification & Benchmarking
- **run_benchmark.py**: Main entry point for executing the full test suite. Uses `sys.executable` to ensure consistent environment usage.
- **verify_all_honest_cycles_jp.py / _en.py**: Proves the integrity of the bridge by reconstructing original logic steps from the generated AST (Honest Cycle).

### Maintenance & Synchronization
- **align_interfaces.py**: Synchronizes method signatures between `test_solution.py` and `.nl` specifications.
- **sync_en_specs.py**: Propagates interface and logic changes from Japanese specifications to English counterparts.
- **clear_artifacts.py**: Comprehensive cleanup script for removing caches (`__pycache__`, `.pytest_cache`), log files, and generated solutions.

## Theory/

The theoretical foundation and knowledge base of the Morphic framework.
- **CORE_LANGUAGE_SPEC.md**: Formal definition of the Morphic Core (Internal World) type system and operational semantics.
- **GEOMETRIC_NL_SPEC_PROTOCOL.md**: Rules for writing unambiguous natural language specifications for deterministic projection.
- **FUTURE_ROADMAP.md**: Strategic evolution plan for next-generation Morphic engines (JS/C++/Fortran) and SMT integration.
- **semantic_dictionary.json**: Maps NL phrases to internal logical symbols with arity information for both EN and JP.
- **wisdom_base.json**: The registry that grounds task IDs to specific deterministic primitives within the VM.

## VM/ (The Morphic Core)

The "Inner World" execution environment.
- **ast.py**: Definition of the Morphic Expression (AST) classes (Literal, Var, Lambda, App, Let, If, Fix).
- **bridge.py**: The parser that materializes MSP text into a live AST object.
- **evaluator.py**: The pure functional VM that reduces ASTs to Normal Form and executes the deterministic logic.
