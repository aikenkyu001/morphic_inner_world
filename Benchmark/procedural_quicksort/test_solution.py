from solution import Solution
def test_task():
    sol = Solution()
    assert sol.quickSort([3, 2, 1]) == [1, 2, 3]
