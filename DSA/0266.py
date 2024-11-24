# DSA Problem 266

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, write a function `find_max_subarray` that returns the maximum sum of any contiguous subarray of size exactly `k`. If the list is empty or `k` is larger than the list length, return 0.

For example, if `nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]` and `k = 4`, the function should return 39 because the subarray with the largest sum is `[10, 23, 3, 1]`.

Constraints:
- 0 <= len(nums) <= 10^5
- 0 <= k <= len(nums)
- -10^4 <= nums[i] <= 10^4
'''

Solution:
def find_max_subarray(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(len(nums) - k):
        window_sum = window_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage:
# nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
# k = 4
# print(find_max_subarray(nums, k))  # Output: 39

'''
This solution uses a sliding window technique to find the maximum sum of any subarray of size `k`. It first calculates the sum of the first `k` elements as the initial window sum, then slides the window across the array, updating the sum and maximum sum as it goes.
'''