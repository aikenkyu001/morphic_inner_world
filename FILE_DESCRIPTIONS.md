# File Descriptions: Morphic Inner World (Multi-Kernel Edition)

This document provides a comprehensive map of the **Morphic Inner World** framework, ensuring absolute transparency of the system's structure.

## 1. Complete Directory Tree

```text
/private/test/morphic_inner_world/
├── .gitignore
├── FILE_DESCRIPTIONS.md
├── LICENSE
├── README.md
├── requirements.txt
├── Benchmark/
│   ├── activity_selection/ (Example Task)
│   │   ├── problem.nl (English Spec)
│   │   ├── problem_jp.nl (Japanese Spec)
│   │   └── test_solution.py (Truth-set)
│   └── ... (Total 60 Tasks, including v8000, d15, n20)
├── Implementations/
│   ├── python/ (Synthesized Python solutions)
│   └── fortran/ (Synthesized Fortran interfaces)
├── Log/ (Execution and synthesis logs)
├── References/
│   ├── REFERENCE_LIST.md
│   └── papers/ (8 Verified Academic PDFs)
├── Reports/
│   ├── academic_paper_en.md
│   ├── academic_paper_jp.md
│   ├── BENCHMARK_RESULTS_LOG.json
│   ├── METHODOLOGY_DIAGRAMS.md
│   ├── MORPHIC_DETERMINISTIC_INTELLIGENCE_SPEC.md
│   └── images/
├── Scripts/
│   ├── align_interfaces.py
│   ├── clean_all.sh
│   ├── clear_artifacts.py
│   ├── morphic_synthesizer.py
│   ├── rebuild_solutions_bilingual.py
│   ├── run_benchmark.py
│   ├── sync_en_specs.py
│   ├── verify_all_honest_cycles_en.py
│   ├── verify_all_honest_cycles_jp.py
│   └── verify_all.sh
├── Theory/
│   ├── CORE_LANGUAGE_SPEC.md
│   ├── GEOMETRIC_NL_SPEC_PROTOCOL.md
│   ├── semantic_dictionary.json
│   └── wisdom_base.json
└── VM/
    ├── python/
    │   ├── morphic_ast.py
    │   └── evaluator.py
    └── fortran/
        ├── fpm.toml
        └── src/
            └── morphic_types.f90 (Real-time Evaluation Engine)
```

## 2. Component Detailed Analysis

### 2.1 Benchmark/ (The Testing Ground)
- Contains 60 algorithmic challenges ranging from classic combinatorial problems to synthetic scaling tests.
- **`problem*.nl`**: These are the "Geometric Specifications" that serve as the only input to the system.
- **`test_solution.py`**: Independent Python scripts used to verify that the synthesized code produces the correct result.

### 2.2 VM/ (The Inner World Kernels)
- **`python/evaluator.py`**: A reference implementation of the lambda calculus with environments and closures.
- **`fortran/src/morphic_types.f90`**: A high-performance execution engine that replicates the Python evaluator's logic in Modern Fortran to prove implementation invariance.

### 2.3 Theory/ (The Cognitive Mapping)
- **`semantic_dictionary.json`**: The absolute 1:1 mapping between natural language phrases and logical primitives. This is the "dictionary of the mind."
- **`GEOMETRIC_NL_SPEC_PROTOCOL.md`**: The strict grammatical rules that govern how specifications must be written to be correctly projected.

### 2.4 Scripts/ (The Orchestration)
- **`verify_all.sh`**: The master verification script that executes Phase 1 (Python) and Phase 2 (Fortran Real-Time Execution) for all 120 bilingual task instances.
- **`morphic_synthesizer.py`**: The "bridge" that performs the geometric projection from NL to AST.

## 3. Verification Integrity
Every file listed above is essential for the **100% Deterministic Success** reported in our findings. No hidden scripts or external APIs are used during the execution cycle.
