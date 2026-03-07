import os, subprocess, sys, json, datetime, argparse

def verify(is_bilingual=False):
    os.makedirs("Log", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = f"Log/benchmark_{timestamp}.log"
    
    tasks = sorted([d for d in os.listdir("Benchmark") if os.path.isdir(f"Benchmark/{d}")])
    sc_en = 0
    sc_jp = 0
    results_log = []
    start_time = datetime.datetime.now()
    
    with open(log_file_path, "w", encoding="utf-8") as log_f:
        def log_print(msg):
            print(msg)
            log_f.write(msg + "\n")

        log_print(f"--- Morphic Inner World Benchmark Execution ---")
        log_print(f"Started at: {start_time.isoformat()}")
        log_print(f"Bilingual Mode: {is_bilingual}")
        log_print("-" * 55)
        
        if is_bilingual:
            log_print(f"{'Task':<40} | {'EN':<5} | {'JP':<5}")
        else:
            log_print(f"{'Task':<40} | {'Status':<10}")
        log_print("-" * 55)
        
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.abspath(os.getcwd())
        # Enable VM tracing
        env["MORPHIC_TRACE"] = "1"
        
        for t in tasks:
            path = f"Benchmark/{t}"
            
            # Verify EN (always)
            log_f.write(f"\n{'='*80}\n[Task: {t} EN Verification Start]\n")
            
            # Record the source code
            sol_path = f"{path}/solution.py"
            if os.path.exists(sol_path):
                with open(sol_path, "r") as f:
                    log_f.write(f"\n--- [solution.py SOURCE] ---\n{f.read()}\n")
            
            # Detailed PyTest Execution (-v -s)
            r_en = subprocess.run([sys.executable, "-m", "pytest", "test_solution.py", "-v", "-s", "--tb=short"], cwd=path, capture_output=True, env=env)
            ok_en = (r_en.returncode == 0)
            if ok_en: sc_en += 1
            
            log_f.write(f"\n--- [PyTest OUTPUT] ---\n")
            log_f.write(r_en.stdout.decode() + "\n")
            if r_en.stderr:
                log_f.write(f"\n--- [PyTest STDERR] ---\n")
                log_f.write(r_en.stderr.decode() + "\n")
            
            ok_jp = None
            if is_bilingual:
                log_f.write(f"\n[Task: {t} JP Verification Start]\n")
                sol_jp_path = f"solution_jp.py"
                sol_tmp_path = f"solution_en.tmp"
                
                # Check within the task directory
                if os.path.exists(f"{path}/{sol_jp_path}"):
                    with open(f"{path}/{sol_jp_path}", "r") as f:
                        log_f.write(f"\n--- [solution_jp.py SOURCE] ---\n{f.read()}\n")
                    
                    # Operations relative to 'path'
                    os.rename(f"{path}/solution.py", f"{path}/{sol_tmp_path}")
                    os.rename(f"{path}/{sol_jp_path}", f"{path}/solution.py")
                    r_jp = subprocess.run([sys.executable, "-m", "pytest", "test_solution.py", "-v", "-s", "--tb=short"], cwd=path, capture_output=True, env=env)
                    ok_jp = (r_jp.returncode == 0)
                    if ok_jp: sc_jp += 1
                    
                    log_f.write(f"\n--- [PyTest OUTPUT] ---\n")
                    log_f.write(r_jp.stdout.decode() + "\n")
                    if r_jp.stderr:
                        log_f.write(f"\n--- [PyTest STDERR] ---\n")
                        log_f.write(r_jp.stderr.decode() + "\n")
                        
                    os.rename(f"{path}/solution.py", f"{path}/{sol_jp_path}")
                    os.rename(f"{path}/{sol_tmp_path}", f"{path}/solution.py")
                else:
                    log_f.write("SKIP JP: solution_jp.py not found.\n")
                    ok_jp = False
            
            if is_bilingual:
                status_en = "✅" if ok_en else "❌"
                status_jp = "✅" if ok_jp else "❌"
                log_print(f"{t:<40} | {status_en:<5} | {status_jp:<5}")
            else:
                status = "✅ OK" if ok_en else "❌ FAIL"
                log_print(f"{t:<40} | {status}")
                
            results_log.append({
                "task": t,
                "status_en": "OK" if ok_en else "FAIL",
                "status_jp": "OK" if ok_jp else "FAIL" if is_bilingual else "N/A"
            })
                
        log_print("-" * 55)
        if is_bilingual:
            log_print(f"Total Success - EN: {sc_en} / {len(tasks)}, JP: {sc_jp} / {len(tasks)}")
        else:
            log_print(f"Total Success: {sc_en} / {len(tasks)}")
        
        end_time = datetime.datetime.now()
        log_print(f"Finished at: {end_time.isoformat()}")
        log_print(f"Duration: {end_time - start_time}")

    final_report = {
        "timestamp": start_time.isoformat(),
        "mode": "bilingual" if is_bilingual else "single",
        "summary": {
            "total_tasks": len(tasks),
            "success_en": sc_en,
            "success_jp": sc_jp if is_bilingual else None
        },
        "details": results_log
    }
    
    report_path = "Reports/BENCHMARK_RESULTS_LOG.json"
    os.makedirs("Reports", exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(final_report, f, indent=2, ensure_ascii=False)
    
    print(f"\nExecution log saved to: {log_file_path}")
    print(f"Structured results saved to: {report_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deterministic AI Benchmark Runner")
    parser.add_argument("-b", "--bilingual", action="store_true", help="Run both EN and JP solutions")
    args = parser.parse_args()
    
    verify(is_bilingual=args.bilingual)
