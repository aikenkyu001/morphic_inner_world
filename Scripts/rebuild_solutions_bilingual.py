import os, sys
sys.path.insert(0, os.path.abspath(os.getcwd()))
from Scripts.morphic_synthesizer import MorphicSynthesizer

def rebuild_bilingual():
    syn = MorphicSynthesizer()
    tasks = sorted([d for d in os.listdir("Benchmark") if os.path.isdir(f"Benchmark/{d}")])
    
    print(f"--- Rebuilding bilingual solutions for {len(tasks)} tasks ---")
    for t in tasks:
        # EN
        en_nl = f"Benchmark/{t}/problem.nl"
        if os.path.exists(en_nl):
            with open(en_nl, "r", encoding="utf-8") as f:
                content = f.read()
                code = syn.synthesize_from_nl(content)
            if code:
                with open(f"Benchmark/{t}/solution.py", "w", encoding="utf-8") as f:
                    f.write(code)
                print(f"SUCCESS (EN): {t}")
            else:
                print(f"FAIL (EN): {t}")
        
        # JP
        jp_nl = f"Benchmark/{t}/problem_jp.nl"
        if os.path.exists(jp_nl):
            with open(jp_nl, "r", encoding="utf-8") as f:
                content = f.read()
                code = syn.synthesize_from_nl(content)
            if code:
                with open(f"Benchmark/{t}/solution_jp.py", "w", encoding="utf-8") as f:
                    f.write(code)
                print(f"SUCCESS (JP): {t}")
            else:
                print(f"FAIL (JP): {t}")

if __name__ == "__main__":
    rebuild_bilingual()
