# DSA Problem 130

'''
Problem Statement:
You are given a list of integers and a positive integer k. Your task is to find the maximum average value of any subarray of length k. If the list has fewer elements than k, return 0.0.

For example, if the list is [1, 12, -5, -6, 50, 3] and k = 4, the maximum average value of a subarray of length 4 is (12 + -5 + -6 + 50) / 4 = 10.25.
'''

Solution:
```python
def max_average_subarray(nums, k):
    if len(nums) < k:
        return 0.0

    # Calculate initial window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window across the array
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k

# Example check
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(max_average_subarray(nums, k))  # Expected output: 10.25
```

This solution uses a sliding window approach to find the maximum sum of any subarray of length `k`, and then calculates the average. It efficiently calculates the sum of each subarray of length `k` by adjusting the window sum when moving from one subarray to the next, instead of summing the subarray elements from scratch.