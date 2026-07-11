# DSA Problem 198

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a contiguous subarray within `nums` such that the sum is divisible by `k`. If there are no such subarrays, return 0.

For example, if `nums = [2, 5, 7, -10, 1]` and `k = 3`, the subarray `[5, 7, -10]` has a sum of 2 which is the closest to zero and divisible by 3. Thus, the answer would be 2.

Note:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= 10^5
'''

Solution:
```python
def max_divisible_subarray_sum(nums, k):
    from collections import defaultdict
    
    n = len(nums)
    prefix_sum = 0
    max_sum = float('-inf')
    # Store the first occurrence of each mod value
    mod_map = defaultdict(lambda: float('inf'))
    mod_map[0] = -1  # Initialize with the mod 0 at index -1
    
    for i in range(n):
        prefix_sum += nums[i]
        mod = prefix_sum % k
        # Adjust mod to be positive
        if mod < 0:
            mod += k
        if mod not in mod_map:
            mod_map[mod] = i
        elif i - mod_map[mod] > 0:
            max_sum = max(max_sum, prefix_sum - (prefix_sum - nums[i]) if i > 0 else prefix_sum)
    
    return max_sum if max_sum != float('-inf') else 0

# Example check (Optional)
nums = [2, 5, 7, -10, 1]
k = 3
print(max_divisible_subarray_sum(nums, k))  # Output should be 2
```

This solution iterates through the list `nums` once, maintaining a running sum and tracking the earliest index at which each remainder (mod `k`) of this sum occurs. This allows us to find the maximum sum of a subarray that is divisible by `k` in O(n) time complexity, where n is the length of `nums`.