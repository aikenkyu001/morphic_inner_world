from solution import Solution
def test_task():
    sol = Solution()
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    # Should find "oath", "eat"
    result = sol.findWords(board, words)
    assert "oath" in result
    assert "eat" in result
