# DSA Problem 113

'''
Problem Statement:
You have been given a list of integers. Your task is to find the maximum sum of a contiguous subarray within the list, such that the sum is exactly divisible by a given integer k. If no such subarray exists, return -1.

For example, given the list [2, 6, 4, 1, 5, 3] and k = 5, the contiguous subarray with the maximum sum that is divisible by 5 is [6, 4, 1, 5] with a sum of 16, which is divisible by 5.

Note:
- 1 <= len(list) <= 10^5
- -10^4 <= list[i] <= 10^4
- 1 <= k <= 10^2
'''

Solution:
```python
def max_subarray_sum_divisible(nums, k):
    """
    Finds the maximum sum of a contiguous subarray that is divisible by k.
    If no such subarray exists, it returns -1.
    """
    n = len(nums)
    prefix_sums = [0] * (n + 1)
    min_indices = [0] * k
    max_sum = float('-inf')
    
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
        remainder = prefix_sums[i] % k
        
        if min_indices[remainder] == 0:
            min_indices[remainder] = i
        else:
            subarray_sum = prefix_sums[i] - prefix_sums[min_indices[remainder]]
            if subarray_sum % k == 0:
                max_sum = max(max_sum, subarray_sum)
    
    return max_sum if max_sum != float('-inf') else -1

# Check function to verify the correctness of the solution
def check():
    assert max_subarray_sum_divisible([2, 6, 4, 1, 5, 3], 5) == 16
    assert max_subarray_sum_divisible([1, 2, 3, 4, 5], 7) == 7
    assert max_subarray_sum_divisible([-1, 2, 3, -4, 1, 2], 3) == 6
    assert max_subarray_sum_divisible([1, -1, -1, -1], 3) == -1
    print("All test cases passed successfully.")

check()
```

This code snippet defines a function `max_subarray_sum_divisible` that calculates the maximum sum of a contiguous subarray which is divisible by a given integer `k`. The solution uses the concept of prefix sums and a greedy approach to minimize the starting index for each remainder when the prefix sum is divided by `k`. This allows efficient calculation of subarray sums that are divisible by `k`.