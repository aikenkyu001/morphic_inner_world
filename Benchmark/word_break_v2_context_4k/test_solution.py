from solution import Solution
def test_task():
    sol = Solution()
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True
