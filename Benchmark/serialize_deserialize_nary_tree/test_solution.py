from solution import Solution
from VM.ast import TreeNode
def test_task():
    sol = Solution()
    root = TreeNode(1)
    root.children = [TreeNode(2)]
    s = sol.serialize(root)
    d = sol.deserialize(s)
    assert d.val == 1
    assert d.children[0].val == 2
