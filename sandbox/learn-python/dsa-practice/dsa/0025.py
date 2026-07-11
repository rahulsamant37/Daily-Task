# DSA Problem 25

'''
Problem Statement:
Given a list of integers `nums`, you are to find the maximum sum of a contiguous subarray within the list. However, there's a twist. You are allowed to exclude at most one element from the subarray to maximize the sum. 

For example, if the list is [1, -2, 3, 4, -5, 6], the maximum sum subarray with the option to exclude at most one element would be [1, -2, 3, 4, 6] with a sum of 12 (excluding -5).

Write a function `max_sum_subarray` that takes a list of integers and returns the maximum sum that can be achieved under the given conditions.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
'''

Solution:
def max_sum_subarray(nums):
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    
    # Initialize two dp arrays to keep track of max sum without excluding any element and with excluding one element
    dp_included = [0] * n
    dp_excluded = [0] * n
    
    dp_included[0] = nums[0]
    dp_excluded[0] = 0
    
    max_sum = nums[0]
    
    for i in range(1, n):
        dp_included[i] = max(nums[i], dp_included[i-1] + nums[i])
        dp_excluded[i] = max(dp_included[i-1], dp_excluded[i-1] + nums[i])
        
        max_sum = max(max_sum, dp_included[i], dp_excluded[i])
    
    return max_sum

# Testing the function
print(max_sum_subarray([1, -2, 3, 4, -5, 6]))  # Expected output: 12
print(max_sum_subarray([-1, -2, -3, -4]))  # Expected output: -1
print(max_sum_subarray([5, 4, -1, 7, 8]))  # Expected output: 23 (since excluding -1 gives a higher sum)
print(max_sum_subarray([1]))  # Expected output: 1
print(max_sum_subarray([-1, -1, 2, -1, 1, -1, 1]))  # Expected output: 4 (excluding the first -1)
'''

This problem incorporates dynamic programming to find the maximum subarray sum with the twist of excluding at most one element. The solution involves maintaining two separate DP arrays to track sums with and without exclusions and updating the maximum sum at each step.
'''