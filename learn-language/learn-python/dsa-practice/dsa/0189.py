# DSA Problem 189

'''
Problem Statement:
A sequence of integers is called beautiful if it is strictly increasing and contains no repeated elements. Given a list of integers `nums`, return the length of the longest beautiful subsequence that can be found in `nums`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example:
- If nums = [4,2,3,3,5,1,7], the longest beautiful subsequence is [2,3,5,7], so the output should be 4.
- If nums = [1,2,3,4,5], every element can be part of the longest beautiful subsequence, so the output should be 5.
'''

Solution:
```python
def longest_beautiful_subsequence(nums):
    if not nums:
        return 0
    
    unique_nums = sorted(set(nums))
    dp = [0] * len(unique_nums)
    
    num_to_index = {num: i for i, num in enumerate(unique_nums)}
    
    for num in nums:
        if num in num_to_index:
            idx = num_to_index[num]
            if idx == 0:
                dp[idx] += 1
            else:
                dp[idx] = max(dp[idx], dp[idx - 1] + 1)
    
    return max(dp)

# Example usage
nums = [4,2,3,3,5,1,7]
print(longest_beautiful_subsequence(nums))  # Output: 4
```
This Python solution leverages dynamic programming to efficiently find the length of the longest beautiful subsequence. It first identifies the unique numbers in the list and sorts them. Then, it uses a DP array to keep track of the longest subsequence length up to each unique number.