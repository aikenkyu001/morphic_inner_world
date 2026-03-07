import os, shutil, glob

def clear():
    print("--- Clearing previous experimental artifacts ---")
    
    # 1. Clear Generated Solutions in Benchmark/
    if os.path.exists("Benchmark"):
        tasks = [d for d in os.listdir("Benchmark") if os.path.isdir(f"Benchmark/{d}")]
        for t in tasks:
            for sol_file in ["solution.py", "solution_jp.py"]:
                path = f"Benchmark/{t}/{sol_file}"
                if os.path.exists(path):
                    try:
                        os.remove(path)
                        print(f"Removed generated solution: {path}")
                    except Exception as e:
                        print(f"Error removing {path}: {e}")

    # 2. Clear Python Cache
    for root, dirs, files in os.walk("."):
        for d in dirs:
            if d == "__pycache__" or d == ".pytest_cache":
                path = os.path.join(root, d)
                try:
                    shutil.rmtree(path)
                    print(f"Removed cache directory: {path}")
                except Exception as e:
                    print(f"Error removing cache {path}: {e}")
        for f in files:
            if f.endswith(".pyc"):
                path = os.path.join(root, f)
                try:
                    os.remove(path)
                    print(f"Removed cache file: {path}")
                except Exception as e:
                    print(f"Error removing cache file {path}: {e}")

    # 3. Clear Log directory
    if os.path.exists("Log"):
        for f in os.listdir("Log"):
            if f != ".gitkeep":
                path = os.path.join("Log", f)
                try:
                    if os.path.isfile(path): os.remove(path)
                    elif os.path.isdir(path): shutil.rmtree(path)
                    print(f"Removed log file: {path}")
                except Exception as e:
                    print(f"Error removing {path}: {e}")

    # 4. Clear Root Artifacts
    root_artifacts = ["synthesis_debug.log", "Reports/BENCHMARK_RESULTS_LOG.json"]
    for art in root_artifacts:
        if os.path.exists(art):
            os.remove(art)
            print(f"Removed root artifact: {art}")

    # 5. Clear .DS_Store
    for root, dirs, files in os.walk("."):
        for f in files:
            if f == ".DS_Store":
                path = os.path.join(root, f)
                os.remove(path)
                print(f"Removed system artifact: {path}")

    print("--- Cleanup complete ---")

if __name__ == "__main__":
    clear()
