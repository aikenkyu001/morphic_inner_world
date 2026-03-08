#!/bin/bash
# Get the root directory of the project
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "--- Morphic Inner World: GLOBAL PURGE Starting from $ROOT_DIR ---"

# 1. Purge Language-Specific Implementations (Generated Artifacts)
if [ -d "Implementations" ]; then
    echo "Clearing Implementations directory..."
    rm -rf Implementations/python/*
    rm -rf Implementations/fortran/*
    # Keep directory structure but remove files
    touch Implementations/python/.gitkeep
    touch Implementations/fortran/.gitkeep
fi

# 2. Cleanup Legacy Artifacts in Benchmark folders
echo "Removing any legacy solutions in Benchmark folders..."
find Benchmark -name "solution.py" -delete
find Benchmark -name "solution_jp.py" -delete
find Benchmark -name "sol_*.tmp" -delete

# 3. Purge Python Execution Logs and Reports
echo "Clearing logs and dynamic reports..."
rm -rf Log/*.log
rm -f Reports/BENCHMARK_RESULTS_LOG.json

# 4. Global Cache Purge
echo "Purging all __pycache__ and .pytest_cache..."
find . -name "__pycache__" -type d -exec rm -rf {} +
rm -rf .pytest_cache

# 5. Fortran Build Cleanup
if [ -d "VM/fortran/build" ]; then
    echo "Removing Fortran build directory..."
    rm -rf VM/fortran/build
fi

echo "--- Environment is now MATHEMATICALLY PURE (Logic Cores Only) ---"
