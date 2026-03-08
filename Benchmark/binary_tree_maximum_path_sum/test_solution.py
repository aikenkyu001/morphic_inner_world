from solution import Solution
from VM.morphic_ast import TreeNode
def test_task():
    sol = Solution()
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(-25)
    root.right.right.left = TreeNode(3)
    root.right.right.right = TreeNode(4)
    # Max path: 20 + 2 + 10 + 10 = 42
    assert sol.maxPathSum(root) == 42
