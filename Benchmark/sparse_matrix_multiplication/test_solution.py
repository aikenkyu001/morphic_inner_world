from solution import Solution
def test_task():
    sol = Solution()
    A = [[1, 0, 0], [-1, 0, 3]]
    B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    # Expected: [[7, 0, 0], [-7, 0, 3]]
    assert sol.multiply(A, B) == [[7, 0, 0], [-7, 0, 3]]
