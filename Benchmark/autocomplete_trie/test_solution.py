from solution import Solution
def test_task():
    sol = Solution()
    sentences = ["i love you", "island", "ironman", "i love leetcode"]
    # For prefix "i ", should return matches starting with "i "
    # Here, simplified: prefix "i l" should match "i love you" and "i love leetcode"
    result = sol.query(sentences, ["i l"])
    assert len(result[0]) == 2
    assert "i love you" in result[0]
    assert "i love leetcode" in result[0]
