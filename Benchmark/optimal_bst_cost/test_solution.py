from solution import Solution
def test_task():
    sol = Solution()
    freq = [34, 8, 50]
    assert sol.obst(freq) == 142
