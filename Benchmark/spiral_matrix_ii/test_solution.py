from solution import Solution
def test_task():
    sol = Solution()
    assert sol.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
