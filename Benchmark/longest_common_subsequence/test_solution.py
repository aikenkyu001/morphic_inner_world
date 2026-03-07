from solution import Solution
def test_task():
    sol = Solution()
    # LCS of "abcde" and "ace" is "ace", length 3
    assert sol.longestCommonSubsequence("abcde", "ace") == 3
