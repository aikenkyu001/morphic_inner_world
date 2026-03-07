import os, re

def align():
    tasks = sorted([d for d in os.listdir("Benchmark") if os.path.isdir(f"Benchmark/{d}")])
    for t in tasks:
        test_path = f"Benchmark/{t}/test_solution.py"
        nl_path = f"Benchmark/{t}/problem_jp.nl"
        if not os.path.exists(test_path) or not os.path.exists(nl_path): continue
        
        with open(test_path, "r") as f: test_content = f.read()
        # test_solution.py からメソッド名を抽出
        # sol.methodName(...) or getattr(sol, "methodName")
        method_match = re.search(r"sol\.([a-zA-Z0-9_]+)\(", test_content)
        if not method_match:
            method_match = re.search(r"getattr\(sol, \"([a-zA-Z0-9_]+)\"\)", test_content)
        
        if method_match:
            target_method = method_match.group(1)
            with open(nl_path, "r") as f: nl_content = f.read()
            
            # インターフェース行を置換
            # 旧: インターフェース: solve(self, arg1)
            # 新: インターフェース: target_method(self, arg1)
            new_nl = re.sub(r"(インターフェース|INTERFACE): \w+\(", f"\\1: {target_method}(", nl_content)
            
            if new_nl != nl_content:
                with open(nl_path, "w") as f: f.write(new_nl)
                print(f"Aligned {t}: -> {target_method}")

if __name__ == "__main__":
    align()
