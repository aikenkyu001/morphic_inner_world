import sys, os
project_root = '/home/miyata/project/morphic_inner_world'
if project_root not in sys.path: sys.path.insert(0, project_root)
from VM.ast import Literal, Var, App, Let, Lambda, ListNode, TreeNode
from VM.evaluator import Evaluator, VLiteral

class Solution:
    def solve(self, arg1):
        vm = Evaluator('/home/miyata/project/morphic_inner_world/Theory/wisdom_base.json')
        res = vm.evaluate(App(Var('identity'), App(Var('identity'), App(Var('identity'), App(Var('flatten_nesting'), Var('arg1'))))), {'arg1': VLiteral(arg1)})
        return res.value