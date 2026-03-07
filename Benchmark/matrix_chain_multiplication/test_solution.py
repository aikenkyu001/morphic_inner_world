from solution import Solution
def test_task():
    sol = Solution()
    p = [10, 30, 5, 60]
    # (10*30*5) + (10*5*60) = 1500 + 3000 = 4500
    assert sol.matrixChainOrder(p) == 4500
