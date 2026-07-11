# Python Question: Given a list of integers, find the maximum sum in a contiguous sublist
'''
Given an integer array, find the maximum sum among all contiguous subarrays present in it.

For example, consider the following array:

Input: [1, 3, -5, 2, -1, 4, -3]

The contiguous subarrays with the maximum sum are:

1. [1, 3, -5, 2, -1] with a sum of 9
2. [3, -5, 2, -1] with a sum of 8
3. [1, 3, -5, 2] with a sum of 10

Output: 10
'''

def max_subarray_sum(arr):
    # Find the minimum value in the array
    min_value = min(arr)
    
    # Initialize maximum sum with array's first element
    max_sum = arr[0]
    
    # Iterate from the second element to the end of the array
    for i in range(1, len(arr)):
        # Find the maximum of current element and the sum of previous elements minus the minimum value
        curr_sum = arr[i] - min_value + max_sum[i - 1]
        max_sum = max(curr_sum, max_sum)
    
    return max_sum

# Test cases
arr1 = [1, 3, -5, 2, -1, 4, -3]
print("The maximum sum is", max_subarray_sum(arr1))

arr2 = [-10, -3, -5, -1]
print("The maximum sum is", max_subarray_sum(arr2))

arr3 = [-1, 2, 1, -3, -100]
print("The maximum sum is", max_subarray_sum(arr3))