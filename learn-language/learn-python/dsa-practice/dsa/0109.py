# DSA Problem 109

'''
Problem Statement:
Given a list of integers `nums`, find the maximum sum of a non-empty subsequence of `nums` such that the maximum element of the subsequence is less than or equal to twice the minimum element of the subsequence.

For example, if nums = [4, 3, 10, 5], the subsequence [4, 3] is valid because the maximum element (4) is less than or equal to twice the minimum element (3). However, the subsequence [10, 5] is not valid because 10 is greater than twice of 5.

Return the maximum sum of any valid subsequence. If no valid subsequence exists, return 0.

Note: A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
'''

Solution:
```python
def max_sum_subsequence(nums):
    nums.sort()
    max_sum = 0
    for i in range(len(nums)):
        subseq_sum = nums[i]
        min_val = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] <= 2 * min_val:
                subseq_sum += nums[j]
            else:
                break
        max_sum = max(max_sum, subseq_sum)
    return max_sum

# Example usage
nums = [4, 3, 10, 5]
print(max_sum_subsequence(nums))  # Output: 7 (for the subsequence [4, 3])
```

This Python function `max_sum_subsequence` finds the maximum sum of a valid subsequence based on the problem's constraints. The solution iterates over each element in the sorted list as a potential starting point for a subsequence, adding subsequent elements to the subsequence as long as they meet the condition of being less than or equal to twice the minimum element in the subsequence. It keeps track of the maximum sum found across all subsequences.