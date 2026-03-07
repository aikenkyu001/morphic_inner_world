from solution import Solution
def test_task():
    sol = Solution()
    assert sol.isMatch("aa", "a*") is True
    assert sol.isMatch("ab", ".*") is True
    assert sol.isMatch("mississippi", "mis*is*p*.") is False
