from solution import Solution
def test_task():
    sol = Solution()
    nums = [1, 2, 4, 8, 3, 6, 12]
    # 1&3!=0, 2&3!=0, 2&6!=0, 4&6!=0, 4&12!=0, 8&12!=0
    # All are connected through bitwise AND chains.
    # Grouping results can vary but should be a single group here.
    result = sol.groupNums(nums)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(nums)
