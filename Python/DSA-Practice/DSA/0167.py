# DSA Problem 167

'''
Problem Statement:
You are given a list of integers and a target integer k. Your task is to find the length of the shortest, non-empty, contiguous subarray of the list whose sum is strictly greater than k. If there is no such subarray, return 0.

For example, given the list [2,3,1,2,4,3] and k = 7, the answer is 2 because the subarray [4,3] is the shortest and its sum is 7 which is strictly greater than 7.

Note:
- The length of the list will be between 1 and 10^5.
- The elements of the list and k will be between -10^5 and 10^5.
'''

Solution:
```python
from collections import deque

def shortest_subarray(nums, k):
    """
    Finds the length of the shortest, non-empty, contiguous subarray
    of 'nums' whose sum is strictly greater than 'k'.
    """
    dq = deque()
    res = len(nums) + 1
    s = 0
    
    for i, num in enumerate(nums):
        s += num
        while dq and s - nums[dq[0]] > k:
            dq.popleft()
        while dq and s <= s + nums[dq[-1]]:
            dq.pop()
        if s > k:
            res = min(res, i - (dq[0] if dq else -1))
        dq.append(i)
    
    return res if res <= len(nums) else 0

# Check function to verify the solution with provided data points
def check():
    assert shortest_subarray([2,3,1,2,4,3], 7) == 2
    assert shortest_subarray([1,2,3,4,5], 11) == 3
    assert shortest_subarray([1,2,3,4,5], 15) == 5
    assert shortest_subarray([1,2,3,4,5], 16) == 0
    print("All tests passed!")

check()
```

This solution uses deque to keep track of potential starting points for the subarray and iterates through the list while maintaining a running sum to find the shortest subarray with a sum greater than `k`.