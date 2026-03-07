from solution import Solution
def test_task():
    sol = Solution()
    ops = [("put", 1, 1), ("get", 1)]
    assert sol.lru_ops(ops, 1) == [None, 1]
