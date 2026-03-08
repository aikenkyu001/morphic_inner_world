import os, sys
# Ensure the Scripts directory is in path to import MorphicSynthesizer
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

from Scripts.morphic_synthesizer import MorphicSynthesizer

def rebuild_all():
    tasks = sorted([d for d in os.listdir("Benchmark") if os.path.isdir(f"Benchmark/{d}")])
    out_dir = os.path.join(project_root, "Implementations", "python")
    os.makedirs(out_dir, exist_ok=True)
    
    synth = MorphicSynthesizer()
    
    for t in tasks:
        # Rebuild EN and JP solutions
        for lang in ["en", "jp"]:
            suffix = "" if lang == "en" else "_jp"
            nl_file = os.path.join(project_root, "Benchmark", t, f"problem{suffix}.nl")
            if not os.path.exists(nl_file): continue
            
            with open(nl_file, "r", encoding="utf-8") as f:
                nl_text = f.read()
            
            python_code = synth.synthesize_from_nl(nl_text)
            if python_code:
                # Update import paths in generated code to the new standardized structure
                python_code = python_code.replace("from VM.ast", "from VM.python.morphic_ast")
                python_code = python_code.replace("from VM.evaluator", "from VM.python.evaluator")
                
                out_file = os.path.join(out_dir, f"{t}_solution{suffix}.py")
                with open(out_file, "w", encoding="utf-8") as f:
                    f.write(python_code)
        
        # Copy the test file to the centralized implementation directory
        test_src = os.path.join(project_root, "Benchmark", t, "test_solution.py")
        if os.path.exists(test_src):
            with open(test_src, "r", encoding="utf-8") as f:
                test_code = f.read()
            # Update test code imports
            test_code = test_code.replace("from VM.ast", "from VM.python.morphic_ast")
            test_code = test_code.replace("from VM.morphic_ast", "from VM.python.morphic_ast")
            
            test_dst = os.path.join(out_dir, f"{t}_test.py")
            with open(test_dst, "w", encoding="utf-8") as f:
                f.write(test_code)
        
        print(f"REBUILT: {t}")

if __name__ == '__main__':
    rebuild_all()
