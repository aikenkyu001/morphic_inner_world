import sys, os
project_root = '/home/miyata/project/morphic_inner_world'
if project_root not in sys.path: sys.path.insert(0, project_root)
from VM.ast import Literal, Var, App, Let, Lambda, ListNode, TreeNode
from VM.evaluator import Evaluator, VLiteral

class Solution:
    def lowestCommonAncestor(self, arg1, arg2, arg3):
        vm = Evaluator('/home/miyata/project/morphic_inner_world/Theory/wisdom_base.json')
        res = vm.evaluate(App(App(App(Var('lca_nary'), Var('arg1')), Var('arg2')), Var('arg3')), {'arg1': VLiteral(arg1), 'arg2': VLiteral(arg2), 'arg3': VLiteral(arg3)})
        return res.value