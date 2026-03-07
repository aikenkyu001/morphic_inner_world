import pytest
from solution import Solution

def test_ultimate_composition():
    sol = Solution()
    # 5 & 7 -> 4. 4 を reconstruct_list すると ListNode(4). その length は 1.
    assert sol.solve(5, 7) == 1
