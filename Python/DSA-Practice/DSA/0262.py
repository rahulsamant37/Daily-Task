# DSA Problem 262

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum average value of any subarray of length `k`. Subarray here means a contiguous part of the array. Return this maximum average as a float.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= k <= nums.length
- -10^4 <= nums[i] <= 10^4

Example:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Subarray with maximum average is [12, -5, -6, 50] with average (12 - 5 - 6 + 50) / 4 = 12.75.
'''

Solution:
```python
def findMaxAverage(nums, k):
    # Calculate the sum of the initial window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window over the array
    for i in range(len(nums) - k):
        # Update the window sum by subtracting the element that is left behind
        # and adding the new element that enters the window
        window_sum += nums[i + k] - nums[i]
        # Update the maximum sum if the current window sum is greater
        max_sum = max(max_sum, window_sum)
    
    # Return the maximum average
    return max_sum / k

# Example check (You can use this to test your solution)
nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))  # Output should be 12.75
```
This solution uses a sliding window approach to find the maximum sum of any subarray of length `k`, which is then used to calculate the maximum average. It runs in O(n) time, where n is the length of the input list `nums`.