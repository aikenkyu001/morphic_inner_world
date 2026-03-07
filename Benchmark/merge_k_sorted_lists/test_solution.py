from solution import Solution
from VM.ast import ListNode
def test_task():
    sol = Solution()
    l1 = ListNode(1); l1.next = ListNode(4)
    l2 = ListNode(1); l2.next = ListNode(3)
    res = sol.mergeKLists([l1, l2])
    vals = []
    while res:
        vals.append(res.val)
        res = res.next
    assert vals == [1, 1, 3, 4]
