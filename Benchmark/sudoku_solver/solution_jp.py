import sys, os
project_root = '/home/miyata/project/morphic_inner_world'
if project_root not in sys.path: sys.path.insert(0, project_root)
from VM.ast import Literal, Var, App, Let, Lambda, ListNode, TreeNode
from VM.evaluator import Evaluator, VLiteral

class Solution:
    def solveSudoku(self, arg1):
        vm = Evaluator('/home/miyata/project/morphic_inner_world/Theory/wisdom_base.json')
        res = vm.evaluate(App(Var('solve_sudoku'), Var('arg1')), {'arg1': VLiteral(arg1)})
        solved = res.value
        for i in range(9): 
            for j in range(9): arg1[i][j] = solved[i][j]