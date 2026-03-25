# DSA Problem 123

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, return the maximum sum of any contiguous subarray of size exactly `k`. If the list is empty or `k` is larger than the list's length, return 0. 

For example, if `nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]` and `k = 4`, the maximum sum of a subarray of size 4 is 39 (sum of subarray [10, 23, 3, 1]).
'''

Solution:
```python
def max_sum_subarray(nums, k):
    if not nums or k > len(nums) or k <= 0:
        return 0

    max_sum = current_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example check
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sum_subarray(nums, k))  # Output should be 39
```

Explanation:
This solution uses a sliding window technique to calculate the sum of every subarray of size `k` efficiently. It first calculates the sum of the first `k` elements, then slides the window across the array, adding the next element and subtracting the element that is left behind, keeping track of the maximum sum found. This ensures the solution runs in O(n) time, where n is the length of the array.