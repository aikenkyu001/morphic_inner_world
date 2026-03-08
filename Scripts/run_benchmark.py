import os, subprocess, sys, json, datetime, argparse

def verify(is_bilingual=False):
    project_root = os.path.abspath(os.getcwd())
    os.makedirs("Log", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = f"Log/benchmark_{timestamp}.log"
    impl_dir = os.path.join(project_root, "Implementations", "python")
    
    tasks = sorted([d for d in os.listdir("Benchmark") if os.path.isdir(f"Benchmark/{d}")])
    sc_en = 0; sc_jp = 0
    results = []
    
    # Environment setup
    env = os.environ.copy()
    env["PYTHONPATH"] = project_root

    print("--- Morphic Final Benchmark (Standardized Structure) ---")
    
    for t in tasks:
        sol_en = os.path.join(impl_dir, f"{t}_solution.py")
        test_file = os.path.join(impl_dir, f"{t}_test.py")
        if not os.path.exists(sol_en): continue
        
        # Temp link for pytest to find 'solution'
        tmp_sol = os.path.join(impl_dir, "solution.py")
        
        # 1. EN Verification
        if os.path.exists(tmp_sol): os.remove(tmp_sol)
        os.link(sol_en, tmp_sol)
        r_en = subprocess.run([sys.executable, "-m", "pytest", f"{t}_test.py"], cwd=impl_dir, capture_output=True, env=env)
        ok_en = (r_en.returncode == 0)
        if ok_en: sc_en += 1
        
        # 2. JP Verification
        ok_jp = False
        sol_jp = os.path.join(impl_dir, f"{t}_solution_jp.py")
        if is_bilingual and os.path.exists(sol_jp):
            if os.path.exists(tmp_sol): os.remove(tmp_sol)
            os.link(sol_jp, tmp_sol)
            r_jp = subprocess.run([sys.executable, "-m", "pytest", f"{t}_test.py"], cwd=impl_dir, capture_output=True, env=env)
            ok_jp = (r_jp.returncode == 0)
            if ok_jp: sc_jp += 1
        
        if os.path.exists(tmp_sol): os.remove(tmp_sol)
        
        status_en = "✅" if ok_en else "❌"
        status_jp = "✅" if ok_jp else "❌"
        print(f"{t:<45} | EN: {status_en} | JP: {status_jp}")
        results.append({"task": t, "en": ok_en, "jp": ok_jp})

    print("-" * 65)
    print(f"Total Success: EN {sc_en}/{len(tasks)}, JP {sc_jp}/{len(tasks)}")
    
    # Save Report
    report_data = {
        "timestamp": timestamp,
        "summary": {"en": sc_en, "jp": sc_jp},
        "details": results
    }
    with open("Reports/BENCHMARK_RESULTS_LOG.json", "w") as f:
        json.dump(report_data, f, indent=2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bilingual", action="store_true")
    args = parser.parse_args()
    verify(is_bilingual=args.bilingual)
