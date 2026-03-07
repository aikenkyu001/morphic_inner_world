import pytest
from solution import Solution

def test_multiple_constraints():
    sol = Solution()
    # 4, 6, 8... は True, 1, 2, 3... は False
    inputs = [i for i in range(1, 3 + 1)]
    res = sol.solve(inputs)
    expected = [ (i > 2 and i % 2 == 0) for i in range(1, 3 + 1) ]
    assert res == expected
