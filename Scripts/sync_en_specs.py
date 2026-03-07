import os, re

def sync():
    tasks = sorted([d for d in os.listdir("Benchmark") if os.path.isdir(f"Benchmark/{d}")])
    for t in tasks:
        en_path = f"Benchmark/{t}/problem.nl"
        jp_path = f"Benchmark/{t}/problem_jp.nl"
        if not os.path.exists(en_path) or not os.path.exists(jp_path): continue
        
        with open(jp_path, "r") as f: jp_content = f.read()
        with open(en_path, "r") as f: en_content = f.read()
        
        # JP版からインターフェース行を抽出
        jp_iface = re.search(r"(?:インターフェース|INTERFACE): (.*)", jp_content)
        jp_input = re.search(r"(?:入力|INPUT): (.*)", jp_content)
        
        if jp_iface:
            # EN版のインターフェース行を置換
            en_content = re.sub(r"(?:INTERFACE|インターフェース): .*", f"INTERFACE: {jp_iface.group(1)}", en_content)
        if jp_input:
            # EN版の入力行を置換
            en_content = re.sub(r"(?:INPUT|入力): .*", f"INPUT: {jp_input.group(1)}", en_content)
            
        # Synthetic系の論理フロー名もEN辞書に合わせて修正
        if t.startswith("synthetic_constraints"):
            en_content = re.sub(r"1\..*", "1. check constraints", en_content)
        elif t.startswith("synthetic_context"):
            en_content = re.sub(r"1\..*", "1. process context", en_content)
        elif t.startswith("synthetic_nesting"):
            en_content = re.sub(r"1\..*", "1. flatten nesting", en_content)
        elif t == "task_60":
            en_content = re.sub(r"1\..*", "1. ultimate dynamic logic synthesis", en_content)

        with open(en_path, "w") as f: f.write(en_content)
        print(f"Synced EN spec for {t}")

if __name__ == "__main__":
    sync()
