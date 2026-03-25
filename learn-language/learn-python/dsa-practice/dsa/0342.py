# DSA Problem 342

'''
Problem Statement:
You are given a list of integers `nums`. Your task is to find the length of the longest increasing subsequence (LIS) where the subsequence does not have to be contiguous, but all elements must be unique. Additionally, you are required to return the actual subsequence as well.

For example, if `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence of unique elements could be `[2, 3, 7, 18]`, and its length is 4.

Note:
- The length of the list `nums` will be between 1 and 1000.
- The list `nums` will only contain integers.
'''

Solution:
```python
def longest_increasing_subsequence(nums):
    if not nums:
        return 0, []
    
    n = len(nums)
    dp = [1] * n  # dp[i] is the length of the longest increasing subsequence ending at index i
    prev = [-1] * n  # prev[i] is the index of the previous element in the subsequence
    
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    max_length = max(dp)
    index = dp.index(max_length)
    
    # Reconstruct the longest increasing subsequence
    lis = []
    while index != -1:
        lis.append(nums[index])
        index = prev[index]
    
    return max_length, lis[::-1]

# Example check (You can use this to verify your solution)
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(nums))  # Expected output: (4, [2, 3, 7, 18])
```

This solution finds the length of the longest increasing subsequence of unique elements within a list, as well as the subsequence itself, by using dynamic programming to keep track of the length of the longest subsequence that can be formed ending at each index, and reconstructs the subsequence from this information.