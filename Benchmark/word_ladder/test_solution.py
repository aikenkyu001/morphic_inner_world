from solution import Solution
def test_task():
    sol = Solution()
    # hit -> hot -> dot -> dog -> cog : 5
    assert sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
