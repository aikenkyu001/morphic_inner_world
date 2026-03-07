import sys, os
project_root = '/home/miyata/project/morphic_inner_world'
if project_root not in sys.path: sys.path.insert(0, project_root)
from VM.ast import Literal, Var, App, Let, Lambda, ListNode, TreeNode
from VM.evaluator import Evaluator, VLiteral

class Solution:
    def shortestPath(self, graph, start, n):
        vm = Evaluator('/home/miyata/project/morphic_inner_world/Theory/wisdom_base.json')
        res = vm.evaluate(App(App(App(Var('dijkstra'), Var('graph')), Var('start')), Var('n')), {'graph': VLiteral(graph), 'start': VLiteral(start), 'n': VLiteral(n)})
        return res.value