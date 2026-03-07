from solution import Solution
def test_task():
    sol = Solution()
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    expected = [(1, 6), (8, 10), (15, 18)]
    assert sol.merge(intervals) == expected
