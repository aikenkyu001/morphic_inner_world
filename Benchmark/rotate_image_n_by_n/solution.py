import sys, os
project_root = '/home/miyata/project/morphic_inner_world'
if project_root not in sys.path: sys.path.insert(0, project_root)
from VM.ast import Literal, Var, App, Let, Lambda, ListNode, TreeNode
from VM.evaluator import Evaluator, VLiteral

class Solution:
    def rotate(self, arg1):
        vm = Evaluator('/home/miyata/project/morphic_inner_world/Theory/wisdom_base.json')
        res = vm.evaluate(App(Var('rotate_matrix'), Var('arg1')), {'arg1': VLiteral(arg1)})
        r = res.value
        for i in range(len(arg1)): 
            for j in range(len(arg1)): arg1[i][j] = r[i][j]