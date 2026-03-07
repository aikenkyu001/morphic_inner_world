from solution import Solution
def test_task():
    sol = Solution()
    graph = {1: [(2, 1), (3, 4)], 2: [(3, 2), (4, 6)], 3: [(4, 3)]}
    # Dijkstra from node 1: [0 (1), 1 (2), 3 (3), 6 (4)]
    assert sol.shortestPath(graph, 1, 4) == [0, 1, 3, 6]
