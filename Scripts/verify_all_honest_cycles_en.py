import sys, os, re, json
sys.path.insert(0, os.path.abspath(os.getcwd()))
from Scripts.morphic_synthesizer import MorphicSynthesizer

def verify_all_cycles_en():
    print("=== Morphic Grand Honest Cycle Verification EN (100.0% Goal) ===")
    synthesizer = MorphicSynthesizer()
    dict_path = "Theory/semantic_dictionary.json"
    with open(dict_path, "r") as f: dictionary = json.load(f)
    
    valid_builtins = set(dictionary["ARITY"].keys())
    # EN辞書を使って逆引き
    rev_dict = {v: k for k, v in dictionary["EN"].items()}
    
    tasks = sorted([d for d in os.listdir("Benchmark") if os.path.isdir(f"Benchmark/{d}")])
    results = []
    
    for t in tasks:
        nl_file = f"Benchmark/{t}/problem.nl"
        if not os.path.exists(nl_file): continue
            
        with open(nl_file, "r", encoding="utf-8") as f:
            original_nl = f.read()
            
        # 1. 1. sort by... のような行を抽出
        original_steps = [line.split(".")[1].strip() for line in original_nl.splitlines() if re.match(r"^\s*\d+\.", line)]
        
        # 2. 合成
        code = synthesizer.synthesize_from_nl(original_nl)
        if not code:
            results.append((t, "FAIL: Synthesis"))
            continue
            
        # 3. 復元
        method_blocks = re.split(r"    def \w+\(self,.*?\):", code)[1:]
        recovered_steps = []
        
        for block in method_blocks:
            eval_match = re.search(r"vm\.evaluate\((.*),\s*\{", block, re.S)
            if eval_match:
                logic_ast_str = eval_match.group(1).strip()
                builtins = re.findall(r"Var\('(\w+)'\)", logic_ast_str)
                ops = [b for b in builtins if b in valid_builtins]
                ops.reverse()
                recovered_steps.extend([rev_dict.get(op, op) for op in ops])
            
        # 比較
        if original_steps == recovered_steps:
            print(f"✅ {t:<40} : MATCH")
            results.append((t, "MATCH"))
        else:
            print(f"❌ {t:<40} : MISMATCH")
            print(f"   Original : {original_steps}")
            print(f"   Recovered: {recovered_steps}")
            results.append((t, "MISMATCH"))

    success_count = sum(1 for _, res in results if res == "MATCH")
    total = len(results)
    print("\n" + "="*55)
    print(f"Grand Cycle Success Rate (EN): {success_count} / {total} ({ (success_count/total)*100 if total > 0 else 0 }%)")
    print("="*55)

if __name__ == "__main__":
    verify_all_cycles_en()
