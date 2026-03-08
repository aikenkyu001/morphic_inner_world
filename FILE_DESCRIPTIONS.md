# File Descriptions: Morphic Inner World (Multi-Kernel Edition)

This document provides a map of the **Morphic Inner World** framework, including the new cross-platform Kernel structure.

## Root Directory
- **README.md**: Main project overview and latest multi-kernel benchmark results.
- **FILE_DESCRIPTIONS.md**: This document (Logical map).

## VM/ (The Morphic Core)
The engine of the "Inner World," now supporting multiple language implementations.
- **python/**: The reference implementation.
  - **morphic_ast.py**: Definition of the Geometric AST nodes (renamed from ast.py to avoid conflicts).
  - **evaluator.py**: The deterministic reduction engine.
  - **bridge.py**: Synthesizes AST objects from MSP/NL.
- **fortran/**: The high-performance kernel.
  - **fpm.toml**: Fortran Package Manager configuration.
  - **src/morphic_types.f90**: Fortran implementation of Morphic Logic and Deterministic Types.
  - **app/main.f90**: CLI for executing logic on the Fortran Kernel.

## Implementations/
Language-specific generated artifacts.
- **python/**: Python solutions generated from NL specifications.
- **fortran/**: Fortran binaries and modules for algorithmic execution.

## Benchmark/
The 60 core tasks serving as the "Logic Reservoir."
- **problem.nl / _jp.nl**: Language-neutral logic specifications.
- **test_solution.py**: Pytest suites (updated to support new Morphic AST paths).

## Scripts/
- **rebuild_solutions_bilingual.py**: Synthesis tool for generating multi-language implementations.
- **run_benchmark.py**: The primary verification engine, now with integrated logging and report generation.
- **morphic_synthesizer.py**: The NL-to-AST translation logic.

## Theory/
- **FUTURE_ROADMAP.md**: Strategy for SMT integration and self-organizing intelligence.
- **semantic_dictionary.json**: 1:1 mapping of language phrases to logical symbols.
