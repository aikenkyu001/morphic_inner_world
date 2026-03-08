import re
from ast App, Var, Literal, Lambda, Let, If, Fix, ListNode, TreeNode

class MorphicBridge:
    """外界 (MSP) から内界 (AST) への架け橋"""

    def parse_msp(self, msp_text: str, params=None):
        """MSP 形式のテキストを AST オブジェクトに変換する"""
        lines = [line.strip() for line in msp_text.splitlines() if line.strip()]
        
        inputs = []
        logic_steps = []
        output_expr_str = ""
        
        current_section = None
        for line in lines:
            if line.startswith("INPUT:"):
                current_section = "INPUT"
                params_in_msp = line.replace("INPUT:", "").split(",")
                inputs = [p.strip() for p in params_in_msp if p.strip()]
                continue
            elif line.startswith("LOGIC:"):
                current_section = "LOGIC"
                continue
            elif line.startswith("OUTPUT:"):
                current_section = "OUTPUT"
                output_expr_str = line.replace("OUTPUT:", "").strip()
                continue
            
            if current_section == "LOGIC":
                match = re.match(r"LET\s+(\w+)\s*=\s*(.+)", line)
                if match:
                    var_name, expr_str = match.groups()
                    logic_steps.append((var_name.strip(), expr_str.strip()))
            elif current_section == "OUTPUT":
                output_expr_str += " " + line
        
        # 引数リストの確定
        if not inputs and params:
            inputs = params

        # AST クラス群 + 引数名を Var として解決するコンテキスト
        context = {
            "App": App, "Var": Var, "Literal": Literal, 
            "Lambda": Lambda, "Let": Let, "If": If, "Fix": Fix,
            "ListNode": ListNode, "TreeNode": TreeNode
        }
        
        # 引数名や LET で定義された変数を Var として解決できるようにする
        # (eval 時の NameError 回避)
        class VarProtector(dict):
            def __getitem__(self, key):
                if key in context: return context[key]
                return Var(key) # 未知の記号は Var とみなす
        
        protected_context = VarProtector()

        final_body = eval(output_expr_str, {"__builtins__": {}}, protected_context)
        
        for var_name, expr_str in reversed(logic_steps):
            val_expr = eval(expr_str, {"__builtins__": {}}, protected_context)
            final_body = Let(var_name, val_expr, final_body)
            
        for param in reversed(inputs):
            final_body = Lambda(param, final_body)
            
        return final_body

    def to_msp(self, inputs, logic_steps, output_expr):
        lines = ["INPUT: " + ", ".join(inputs)]
        lines.append("LOGIC:")
        for var, expr in logic_steps:
            lines.append(f"  LET {var} = {expr}")
        lines.append("OUTPUT:")
        lines.append(f"  {output_expr}")
        return "\n".join(lines)
