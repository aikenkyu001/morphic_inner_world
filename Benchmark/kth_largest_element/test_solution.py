from solution import Solution
def test_task():
    sol = Solution()
    # 2nd largest: 5
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
