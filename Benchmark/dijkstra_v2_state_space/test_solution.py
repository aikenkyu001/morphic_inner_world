from solution import Solution
def test_task():
    sol = Solution()
    graph = {1: [(2, 1)], 2: [(3, 1)], 3: [(4, 1)]}
    assert sol.solve(graph, 1, 4) == [0, 1, 2, 3]
