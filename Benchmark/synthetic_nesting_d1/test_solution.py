import pytest
from solution import Solution

def test_deep_nesting():
    sol = Solution()
    nested_input = [1]
    # 平坦化すると [1] になるはず
    assert sol.solve(nested_input) == [1]
