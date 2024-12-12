# DSA Problem 284

'''
Problem Statement:
You are given an array of positive integers and an integer k. Your task is to find the maximum number of non-overlapping subarrays such that the sum of elements in each subarray is less than or equal to k. Return the maximum number of such subarrays.

For example, if the input array is [2,1,3,4,5] and k is 7, the subarrays that meet the conditions are [2,1], [3], and [4]. Thus, the maximum number of such subarrays is 3.
'''

Solution:
def maxSubarrays(arr, k):
    count = 0
    i = 0
    n = len(arr)
    while i < n:
        sum_subarray = 0
        while i < n and sum_subarray + arr[i] <= k:
            sum_subarray += arr[i]
            i += 1
        count += 1
    return count if sum_subarray <= k else count - 1

# Test the function
arr = [2, 1, 3, 4, 5]
k = 7
print(maxSubarrays(arr, k))  # Output: 3

# Explanation:
# The function iterates through the array, trying to find the longest subarray from the current position whose sum is less than or equal to k. It then moves to the next position after the found subarray and repeats the process. The count of such subarrays is returned as the result.
# This solution efficiently finds the maximum number of non-overlapping subarrays with the given sum condition.
'''
This example problem is designed to test the ability to handle array and subarray problems with constraints, a common topic in algorithmic challenges.
'''