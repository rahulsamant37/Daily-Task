# DSA Problem 346

'''
Problem Statement:
A sequence of integers is called *alternating* if the difference between every two consecutive elements is alternately positive and negative. For example, the sequence [3, 5, 2, 6, 1] is alternating because the differences (5-3), (2-5), (6-2), and (1-6) are alternately positive and negative.

Given an array `nums` of integers, return the maximum length of an alternating subsequence that can be formed from the elements of `nums`. A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^6

Example:
Input: nums = [2, 3, 4, 3, 4]
Output: 4
Explanation: The longest alternating subsequence is [2, 3, 4, 3] or [3, 4, 3, 4].
'''

Solution:
```python
def maxAlternatingSubsequenceLength(nums):
    n = len(nums)
    if n < 2:
        return n
    
    # up[i] = Length of longest alternating subsequence ending at i and ending with a positive difference
    # down[i] = Length of longest alternating subsequence ending at i and ending with a negative difference
    up = [1] * n
    down = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                up[i] = max(up[i], down[j] + 1)
            elif nums[i] < nums[j]:
                down[i] = max(down[i], up[j] + 1)
    
    return max(max(up), max(down))

# Example usage
nums = [2, 3, 4, 3, 4]
print(maxAlternatingSubsequenceLength(nums))  # Output: 4
```

This solution iterates through the array and uses dynamic programming to calculate the longest alternating subsequence that can be formed, considering both positive and negative differences to end the sequence.