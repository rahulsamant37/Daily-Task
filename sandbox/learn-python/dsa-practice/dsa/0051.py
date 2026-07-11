# DSA Problem 51

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a subarray with a length that is exactly `k`. A subarray is a contiguous part of an array. You need to return the maximum sum you can achieve.

For example, given `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, the subarray with the maximum sum of length 3 is `[5, 3, 6]`, which gives a sum of 14.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
'''

Solution:
```python
def max_sum_subarray(nums, k):
    if not nums or k <= 0:
        return 0
    
    max_sum = float('-inf')
    window_sum = 0
    
    for i in range(len(nums)):
        window_sum += nums[i]  # Add the next element to the window
        # When we hit the window of size k
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)  # Update max_sum if needed
            window_sum -= nums[i - k + 1]  # Slide the window forward
    
    return max_sum

# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sum_subarray(nums, k))  # Output: 14
```
This solution uses a sliding window approach to compute the maximum sum of any subarray of length `k`. It iterates through the array once, making it efficient with a time complexity of O(n).