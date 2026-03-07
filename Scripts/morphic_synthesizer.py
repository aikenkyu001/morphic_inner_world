import os, sys, re, json

class MorphicSynthesizer:
    def __init__(self):
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        dict_path = os.path.join(root_dir, "Theory/semantic_dictionary.json")
        with open(dict_path, "r") as f: self.dictionary = json.load(f)
        self.arity_map = self.dictionary["ARITY"]
        # [重要] 最長一致を実現するため、フレーズの長い順にソートする
        jp_items = sorted(self.dictionary["JP"].items(), key=lambda x: len(x[0]), reverse=True)
        en_items = sorted(self.dictionary["EN"].items(), key=lambda x: len(x[0]), reverse=True)
        self.sorted_phrases = jp_items + en_items
        self.output_patterns = {**self.dictionary["OUTPUT_PATTERNS"]["JP"], **self.dictionary["OUTPUT_PATTERNS"]["EN"]}

    def synthesize_from_nl(self, nl_text):
        methods_code = []
        blocks = nl_text.split("---")
        root_dir = os.path.abspath(os.getcwd())
        wisdom_path = os.path.join(root_dir, "Theory", "wisdom_base.json")

        for block in blocks:
            if not block.strip(): continue
            if (("タスク:" in block or "TASK:" in block) and ("論理フロー:" not in block and "LOGIC:" not in block)): continue
            
            method_match = re.search(r"(?:メソッド|Method|インターフェース|INTERFACE):\s*(?:[\w\.]+\s+)?(\w+)\(", block, re.I)
            method_name = method_match.group(1) if method_match else "solve"
            
            input_match = re.search(r"(?:入力|INPUT):\s*(.*)", block, re.I)
            if not input_match:
                interface_args_match = re.search(r"\((.*?)\)", block)
                if interface_args_match:
                    input_vars = [v.strip() for v in interface_args_match.group(1).split(",") if "self" not in v]
                else:
                    input_vars = ["arg1"]
            else:
                input_vars = [v.strip() for v in input_match.group(1).split(",")]
            input_vars = [v for v in input_vars if v]

            found_builtins = []
            for line in block.splitlines():
                # セクションヘッダー行のみをスキップする厳格な条件
                line_stripped = line.strip()
                if not line_stripped: continue
                
                # ヘッダー行判定 (末尾がコロン、または特定のキーワードのみの行)
                is_header = False
                header_keywords = ["入力", "INPUT", "メソッド", "METHOD", "インターフェース", "INTERFACE", "出力", "OUTPUT", "LOGIC", "論理フロー"]
                
                # 1. "LOGIC:" のような形式
                if any(line_stripped.upper().startswith(k + ":") or line_stripped.upper().startswith(k + " ") for k in header_keywords):
                    is_header = True
                # 2. "LOGIC" 単独行など
                elif line_stripped.upper().replace(":", "") in header_keywords:
                    is_header = True
                
                if is_header: continue

                for phrase, builtin in self.sorted_phrases:
                    if phrase.lower() in line.lower():
                        found_builtins.append(builtin)
                        break

            if not found_builtins: continue

            def build_ast_deterministic(funcs, vars):
                v_idx = 0
                ast = None
                for f in funcs:
                    arity = self.arity_map.get(f, 1)
                    if ast is None:
                        ast = f"Var('{vars[v_idx]}')"
                        v_idx += 1
                        ast = f"App(Var('{f}'), {ast})"
                        for _ in range(1, arity):
                            if v_idx < len(vars):
                                ast = f"App({ast}, Var('{vars[v_idx]}'))"
                                v_idx += 1
                    else:
                        ast = f"App(Var('{f}'), {ast})"
                        for _ in range(1, arity):
                            if v_idx < len(vars):
                                ast = f"App({ast}, Var('{vars[v_idx]}'))"
                                v_idx += 1
                return ast

            logic_ast = build_ast_deterministic(found_builtins, input_vars)
            output_logic = "return res.value"
            for phrase, pattern in self.output_patterns.items():
                if phrase in block: output_logic = pattern; break
            
            env_bind = ", ".join([f"'{v}': VLiteral({v})" for v in input_vars])
            methods_code.append(f"""    def {method_name}(self, {', '.join(input_vars)}):
        vm = Evaluator('{wisdom_path}')
        res = vm.evaluate({logic_ast}, {{{env_bind}}})
        {output_logic}""")

        if not methods_code: return None
        full_code = f"import sys, os\nproject_root = '{root_dir}'\nif project_root not in sys.path: sys.path.insert(0, project_root)\nfrom VM.ast import Literal, Var, App, Let, Lambda, ListNode, TreeNode\nfrom VM.evaluator import Evaluator, VLiteral\n\nclass Solution:\n" + "\n".join(methods_code)
        return full_code
