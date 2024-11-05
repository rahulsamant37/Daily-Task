# DSA Problem 247

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the length of the shortest, non-empty, contiguous subarray of `nums` with a sum of at least `k`. If there is no such subarray, return 0.

For example, given nums = [2,3,1,2,4,3] and k = 7, the shortest subarray with sum at least 7 is [4,3], which has a length of 2.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= k <= 10^9
'''

Solution:
```python
from collections import deque

def shortest_subarray(nums, k):
    """
    Finds the length of the shortest contiguous subarray with sum at least k.
    """
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    shortest = float('inf')
    dq = deque()
    
    for i in range(n + 1):
        while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
            shortest = min(shortest, i - dq.popleft())
        while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
            dq.pop()
        dq.append(i)
    
    return shortest if shortest != float('inf') else 0

# Example check
print(shortest_subarray([2,3,1,2,4,3], 7))  # Output: 2
```

This Python solution uses a deque to keep track of the indices of the prefix sums that could potentially form the shortest subarray with a sum of at least `k`. It iterates through the prefix sums and uses the deque to maintain the shortest subarray length dynamically.