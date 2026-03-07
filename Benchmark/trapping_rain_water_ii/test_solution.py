from solution import Solution
def test_task():
    sol = Solution()
    matrix = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    assert sol.trapRainWater(matrix) == 4
