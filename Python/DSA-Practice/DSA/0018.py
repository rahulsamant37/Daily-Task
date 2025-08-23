# DSA Problem 18

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, return the maximum sum of any contiguous subarray of size exactly `k`. If there are no subarrays of size `k`, return 0.

Example:
Input:
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
Output:
Explanation: The subarray [4, 2, 10, 23] has the maximum sum of 39.
'''

Solution:
def max_sum_subarray(nums, k):
    """
    Find the maximum sum of any contiguous subarray of size exactly k.
    """
    if not nums or k <= 0 or len(nums) < k:
        return 0
    
    max_sum = float('-inf')
    window_sum = 0
    window_start = 0
    
    for window_end in range(len(nums)):
        window_sum += nums[window_end]  # add the next element
        
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead
            
    return max_sum if max_sum != float('-inf') else 0

# Check with provided data points
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sum_subarray(nums, k))  # Expected output: 39
'''

This problem involves finding the maximum sum of a subarray of a specific length using the sliding window technique, which is efficient and avoids recalculating the sum of the elements in the window repeatedly. The solution checks for edge cases and ensures that the sum is calculated only for valid subarrays.