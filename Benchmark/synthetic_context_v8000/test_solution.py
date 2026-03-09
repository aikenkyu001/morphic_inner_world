import pytest
from solution import Solution
def test_large_context():
    sol = Solution()
    state = {}
    ops = [("key_" + str(i), i) for i in range(8000)]
    res = sol.solve(state, ops)
    expected = { "key_" + str(i): i for i in range(8000) }
    assert res == expected
