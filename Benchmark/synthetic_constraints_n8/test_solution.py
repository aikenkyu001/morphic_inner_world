import pytest
from solution import Solution
def test_constraints():
    sol = Solution()
    # 偶数かつ2より大きいという制約の実装に合わせる
    assert sol.solve(4) is True
    assert sol.solve(1) is False
