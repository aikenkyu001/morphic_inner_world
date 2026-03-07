from solution import Solution
def test_task():
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # Rotated: [[7,4,1],[8,5,2],[9,6,3]]
    sol.rotate(matrix)
    assert matrix == [[7,4,1],[8,5,2],[9,6,3]]
