# DSA Problem 23

'''
Problem Statement:
You are given a list of integers and a positive integer k. Your task is to find the maximum sum of a subarray with a length of exactly k. A subarray is a contiguous part of an array. 

For example, if the list is [1, 4, 2, 10, 23, 3, 1, 0, 20] and k is 4, then the subarray with the maximum sum is [10, 23, 3, 1] with a sum of 37.

Write a function `max_subarray_sum(arr, k)` that returns the maximum sum of any subarray of length k.
'''

Solution:
def max_subarray_sum(arr, k):
    # Initialize the maximum sum to be the sum of the first k elements
    max_sum = sum(arr[:k])
    current_sum = max_sum
    
    # Slide the window across the array to find the maximum sum
    for i in range(len(arr) - k):
        # Update the current_sum by subtracting the element that is left out and adding the new element
        current_sum = current_sum - arr[i] + arr[i + k]
        # Update max_sum if the current_sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example check
print(max_subarray_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))  # Output: 37
print(max_subarray_sum([-1, 4, -2, 5, -5], 3))  # Output: 7
# Explanation: In the first example, the subarray [10, 23, 3, 1] has the maximum sum of 37.
# In the second example, the subarray [4, -2, 5] has the maximum sum of 7.
'''

This solution uses a sliding window approach to efficiently find the maximum sum of any subarray of length k. It first calculates the sum of the first window, then slides over the array, updating the sum by subtracting the element that is left out of the window and adding the new element that enters the window. This way, it avoids recalculating the sum from scratch for each subarray, which would be less efficient.
'''