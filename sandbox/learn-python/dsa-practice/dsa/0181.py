# DSA Problem 181

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, find the maximum sum of any contiguous subarray of size exactly `k`. For example, given the list `[1, 4, 2, 10, 23, 3, 1, 0, 20]` and `k = 4`, the maximum sum of a subarray of size 4 is 39 (from subarray `[2, 10, 23, 3]`).

Constraints:
- The list will contain at least `k` integers.
- All integers are non-negative.
- 1 <= k <= len(nums)
'''

Solution:
```python
def max_sum_subarray(nums, k):
    # Initialize the maximum sum with the sum of the first window
    max_sum = sum(nums[:k])
    current_sum = max_sum
    
    # Slide the window from start to the end of the array
    for i in range(len(nums) - k):
        # Update the current sum by subtracting the element that is left behind
        # and adding the new element in the window
        current_sum += nums[i + k] - nums[i]
        
        # Update the maximum sum if the current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sum_subarray(nums, k))  # Output: 39
```

This solution efficiently finds the maximum sum of any contiguous subarray of size `k` using a sliding window approach, which optimizes the problem by avoiding unnecessary re-computation of subarray sums.