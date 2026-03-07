from solution import Solution
def test_task():
    sol = Solution()
    ops = [("put", 1, 1), ("put", 2, 2), ("get", 1), ("put", 3, 3), ("get", 2)]
    # cap=2: [1:1, 2:2] -> [2:2, 1:1] (get 1) -> [1:1, 3:3] (put 3, evict 2) -> get 2 is -1
    assert sol.lru_ops(ops, 2) == [None, None, 1, None, -1]
