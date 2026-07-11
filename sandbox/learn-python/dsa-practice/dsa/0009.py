# DSA Problem 9

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a subarray with at least `k` elements. A subarray is a contiguous part of an array. If no such subarray exists, return 0.

For example, if `nums = [1, -3, 2, 1, -1]` and `k = 2`, the maximum sum of a subarray with at least 2 elements is `3` (the subarray is `[2, 1]`).

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
'''

Solution:
```python
def max_subarray_sum(nums, k):
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    from collections import deque
    dq = deque()
    max_sum = float('-inf')
    
    for i in range(k, n + 1):
        while dq and dq[0] < i - k:
            dq.popleft()
        if dq:
            max_sum = max(max_sum, prefix_sum[i] - prefix_sum[dq[0]])
        while dq and prefix_sum[i] < prefix_sum[dq[-1]]:
            dq.pop()
        dq.append(i)
    
    return max_sum if max_sum != float('-inf') else 0

# Example usage
nums = [1, -3, 2, 1, -1]
k = 2
print(max_subarray_sum(nums, k))  # Output: 3
```

Explanation:
This solution uses a sliding window approach with a deque to maintain the indices of the prefix sums that might contribute to the maximum subarray sum with at least `k` elements. It iterates through the array, updating the deque to ensure that the minimum prefix sum within the sliding window is always at the front, allowing for the quick calculation of the maximum subarray sum for each possible subarray starting from each index.