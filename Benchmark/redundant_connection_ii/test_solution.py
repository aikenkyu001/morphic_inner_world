from solution import Solution
def test_task():
    sol = Solution()
    edges = [[1,2],[1,3],[2,3]]
    assert sol.findRedundantDirectedConnection(edges) == [2, 3]
