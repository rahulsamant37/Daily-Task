# DSA Problem 251

'''
Problem Statement:
A list of integers `nums` is given, where each element in the list represents the maximum number of steps you can jump forward from that position. Write a function `canReachEnd(nums)` that returns `True` if you can reach the last index starting from the first index, and `False` otherwise. You can only move forward from any index.

For example, given `nums = [2, 3, 1, 1, 4]`, the function should return `True` because you can jump from index 0 to 1, then to index 4, which is the last index.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- 0 <= nums[i] <= 10^5

Note: This problem is a variation of the "Jump Game" problem.
'''

Solution:
```python
def canReachEnd(nums):
    max_reach = 0
    target = len(nums) - 1
    
    for i in range(len(nums)):
        # If current index is greater than max reach, it means we cannot move forward
        if i > max_reach:
            return False
        # Update max reach
        max_reach = max(max_reach, i + nums[i])
        # If at any point max reach is equal to or exceeds the target, return True
        if max_reach >= target:
            return True
    
    return False

# Check function to verify the correctness of the solution
def check():
    assert canReachEnd([2, 3, 1, 1, 4]) == True
    assert canReachEnd([3, 2, 1, 0, 4]) == False
    assert canReachEnd([2, 0, 0]) == True
    assert canReachEnd([0, 2, 3]) == False
    print("All test cases passed.")

check()
```

This Python function and the check function demonstrate the solution to the problem, ensuring that the code works as expected with a few test cases.