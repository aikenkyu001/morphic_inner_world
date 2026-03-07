from solution import Solution
def test_task():
    sol = Solution()
    # [1,1,2] -> [[1,1,2], [1,2,1], [2,1,1]]
    res = sol.permuteUnique([1, 1, 2])
    assert len(res) == 3
    assert [1, 1, 2] in res
    assert [1, 2, 1] in res
    assert [2, 1, 1] in res
