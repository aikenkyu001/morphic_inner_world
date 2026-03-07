from solution import Solution
def test_task():
    sol = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    L = 16
    res = sol.fullJustify(words, L)
    assert res[0] == "This    is    an"
