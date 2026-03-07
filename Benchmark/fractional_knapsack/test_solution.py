from solution import Solution
def test_task():
    sol = Solution()
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50
    # Val/Weight: (6, 5, 4). Full (60, 10), Full (100, 20), 20/30 of (120, 30) = 80. Total = 240.
    assert sol.fractionalKnapsack(items, capacity) == 240.0
