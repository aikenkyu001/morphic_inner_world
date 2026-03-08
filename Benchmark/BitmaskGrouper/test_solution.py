from solution import Solution

def test_bitmask_grouper():
    sol = Solution()
    # Test case: group by common set bits (simplified logic for demonstration)
    # The actual algorithm 'bitmask_group' logic depends on VM/evaluator.py builtins
    arg = [1, 2, 4, 8] 
    res = sol.groupNums(arg)
    assert res is not None
    print(f"Result for [1, 2, 4, 8]: {res}")

if __name__ == "__main__":
    test_bitmask_grouper()
