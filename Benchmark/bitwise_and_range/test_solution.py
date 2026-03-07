from solution import Solution
def test_task():
    sol = Solution()
    # Range [5, 7]: 5 (101) & 6 (110) & 7 (111) = 4 (100)
    assert sol.rangeBitwiseAnd(5, 7) == 4
    # Range [0, 1]: 0
    assert sol.rangeBitwiseAnd(0, 1) == 0
