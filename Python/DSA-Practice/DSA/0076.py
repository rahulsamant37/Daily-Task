# DSA Problem 76

'''
Problem Statement:
You are given a list of integers, `nums`, and an integer `k`. You need to find the maximum sum of a contiguous subarray within `nums` that is less than or equal to `k`. If no such subarray exists, return -1.

For example, if nums = [1, 2, -1, 3] and k = 3, the subarray [1, 2] has a sum of 3 which is equal to `k`, making it the maximum sum subarray that does not exceed `k`.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- -10^5 <= k <= 10^5
'''

Solution:
```python
def max_subarray_sum(nums, k):
    n = len(nums)
    max_sum = float('-inf')
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += nums[end]
            if current_sum <= k:
                max_sum = max(max_sum, current_sum)
            else:
                break
    return max_sum if max_sum != float('-inf') else -1

# Example check (You can use this to test your solution)
nums = [1, 2, -1, 3]
k = 3
print(max_subarray_sum(nums, k))  # Output should be 3
```

Note: The provided solution follows a brute-force approach which might not be optimal for very large inputs due to its O(n^2) complexity. For a more efficient solution, consider using a prefix sum array combined with a binary search or a balanced binary search tree.