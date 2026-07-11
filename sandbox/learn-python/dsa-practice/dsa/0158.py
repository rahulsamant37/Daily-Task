# DSA Problem 158

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of any non-empty subarray of `nums` such that the sum of the subarray is a multiple of `k`. If no such subarray exists, return 0.

A subarray is a contiguous part of an array. A sum of a subarray is a multiple of `k` if the sum modulo `k` equals 0.

Example:
Input: nums = [2, 3, -1, 4], k = 6
Output: 6
Explanation: The subarray [3, -1, 4] has a sum of 6, which is a multiple of 6.
'''

Solution:
def maxSubarrayMultiple(nums, k):
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    min_val = [float('inf')] * k
    max_sum = float('-inf')
    min_val[0] = 0

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        remainder = prefix_sum[i + 1] % k
        if min_val[remainder] == float('inf'):
            min_val[remainder] = i + 1
        else:
            max_sum = max(max_sum, prefix_sum[i + 1] - prefix_sum[min_val[remainder]])

    return max_sum if max_sum != float('-inf') else 0

# Example usage
nums = [2, 3, -1, 4]
k = 6
print(maxSubarrayMultiple(nums, k))  # Output: 6

# Explanation of the solution:
# This solution uses the concept of prefix sums and a modulo operation to efficiently find the maximum sum of a subarray that is a multiple of k.
# We keep track of the minimum index for each possible remainder when the prefix sum is divided by k, which helps in calculating the maximum sum subarray.
# If no valid subarray exists, the function returns 0.