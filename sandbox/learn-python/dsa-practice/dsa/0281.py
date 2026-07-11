# DSA Problem 281

'''
Problem Statement:
Given a list of integers, write a function `find_max_subarray_with_k` that returns the maximum sum of any subarray of length exactly k. For instance, given a list [1, 4, 2, 10, 23, 3, 1, 0, 20] and k = 4, the function should return 39, as the subarray [10, 23, 3, 1] has the maximum sum of 37. Ensure your solution is efficient for large lists and values of k.
'''

Solution:
def find_max_subarray_with_k(nums, k):
    # Initialize the sum of the first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window from start to end of the array
    for i in range(len(nums) - k):
        # Subtract the element going out of the window and add the new element
        window_sum = window_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example check
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(find_max_subarray_with_k(nums, k))  # Expected output: 39

# The function finds the maximum sum of any subarray of length exactly k, using a sliding window technique to efficiently calculate the sum of each subarray of length k without recalculating the sum from scratch for each subarray.
'''
This problem and solution are designed to test understanding of sliding window technique for sum calculation in arrays, a common and efficient approach for subarray problems in competitive programming and algorithm design. The provided example with input values and expected output allows for quick verification of the solution's correctness.
'''