# DSA Problem 142

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of any subarray of `nums` such that the sum is divisible by `k`. If no such subarray exists, return 0.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= 10^4
'''

Solution:
```python
def max_subarray_divisible_by_k(nums, k):
    """
    Finds the maximum sum of a subarray where the sum is divisible by k.
    """
    from collections import defaultdict

    prefix_sums = defaultdict(lambda: float('inf'))
    prefix_sums[0] = -1
    max_length = float('-inf')
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num
        mod = current_sum % k

        if mod not in prefix_sums:
            prefix_sums[mod] = i
        elif i - prefix_sums[mod] > max_length:
            max_length = i - prefix_sums[mod]

    if max_length == float('-inf'):
        return 0

    return sum(nums[max_length - i - 1 for i in range(max_length + 1)])

# Example check (This is not part of the solution, just for verification)
nums = [5, 2, 3, 1, 4]
k = 3
print(max_subarray_divisible_by_k(nums, k))  # Expected output depends on the nums and k
```

Note: The solution provided is a template for solving the given problem. The correctness of the solution code is not verified and might require adjustments based on specific requirements or edge cases.