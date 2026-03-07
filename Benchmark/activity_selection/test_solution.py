from solution import Solution
def test_task():
    sol = Solution()
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    # Selected: (1, 4), (5, 7), (8, 11), (12, 14) -> 4 activities
    assert sol.maxActivities(activities) == 4
