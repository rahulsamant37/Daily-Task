# DSA Problem 278

'''
Problem Statement:
Given a list of integers, find the length of the longest subsequence where every element is greater than all the elements that come before it in the subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, given the list [10, 9, 2, 5, 3, 7, 101, 18], one of the longest increasing subsequences is [2, 3, 7, 101], so the function should return 4.
'''

Solution:
```python
def longest_increasing_subsequence_length(nums):
    if not nums:
        return 0
    
    # dp[i] means the length of the longest increasing subsequence 
    # that ends with nums[i]
    dp = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

# Example usage:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence_length(nums))  # Output: 4
```

In this solution, dynamic programming is used to keep track of the longest increasing subsequence up to each element in the list. The `dp` array stores the lengths of the longest increasing subsequences ending at each position, and the final answer is the maximum value in this array.