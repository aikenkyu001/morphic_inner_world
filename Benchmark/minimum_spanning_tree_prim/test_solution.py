from solution import Solution
def test_task():
    sol = Solution()
    # n=4, edges=(u, v, w)
    edges = [(1, 2, 1), (1, 3, 3), (2, 3, 1), (3, 4, 2)]
    # MST: (1,2,1), (2,3,1), (3,4,2) Total=4
    assert sol.minCostConnectPoints(4, edges) == 4
