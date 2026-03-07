from solution import Solution
def test_task():
    sol = Solution()
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("([)]") is False
