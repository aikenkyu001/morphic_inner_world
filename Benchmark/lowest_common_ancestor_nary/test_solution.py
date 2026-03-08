from solution import Solution
from VM.morphic_ast import TreeNode
def test_task():
    sol = Solution()
    root = TreeNode(1)
    c1 = TreeNode(2)
    c2 = TreeNode(3)
    root.children = [c1, c2]
    # LCA of 2 and 3 is 1
    assert sol.lowestCommonAncestor(root, c1, c2) == root
