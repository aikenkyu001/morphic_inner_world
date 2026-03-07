from solution import Solution
def test_task():
    sol = Solution()
    res = sol.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    assert len(res) == 2
