# DSA Problem 276

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. You need to find the maximum sum of a subarray of size exactly `k`. A subarray is a contiguous part of an array.

For example, if `nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]` and `k = 4`, the output should be 39 because the subarray `[10, 23, 3, 1]` has the maximum sum of 39.

Write a function `max_subarray_sum(nums, k)` that returns the maximum sum possible for any subarray of size `k`.
'''

Solution:
def max_subarray_sum(nums, k):
    if not nums or k <= 0:
        return 0
    max_sum = current_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example check (uncomment to test)
# nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
# k = 4
# print(max_subarray_sum(nums, k))  # Expected output: 39
'''
This solution efficiently computes the maximum sum of any subarray of size `k` by using a sliding window approach to avoid recalculating the sum for overlapping parts of the array, achieving a time complexity of O(n).
'''