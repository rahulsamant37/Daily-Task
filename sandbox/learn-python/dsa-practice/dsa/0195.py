# DSA Problem 195

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a non-empty subsequence of `nums` such that for every pair of consecutive integers in the subsequence, the second integer is at least `k` times the first integer.

For example, if `nums = [1, 4, 3, 16]` and `k = 2`, the subsequence [1, 4, 16] is valid because 4 >= 2*1 and 16 >= 2*4. The sum is 21.

Write a function `max_subseq_sum(nums, k)` that returns the maximum sum of a valid subsequence. If no such subsequence exists, return 0.
'''

Solution:
```python
def max_subseq_sum(nums, k):
    # Sort the numbers in descending order to prioritize larger numbers
    nums.sort(reverse=True)
    
    n = len(nums)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = nums[i - 1]
        for j in range(1, i):
            if nums[i - 1] >= k * nums[j - 1]:
                dp[i] = max(dp[i], dp[j] + nums[i - 1])
    
    return max(dp)

# Example check function
def check_solution():
    assert max_subseq_sum([1, 4, 3, 16], 2) == 21
    assert max_subseq_sum([1, 2, 3, 4], 1) == 10
    assert max_subseq_sum([5, 4, 3, 2], 2) == 5
    print("All tests passed.")

check_solution()
```

This solution sorts the input list in descending order to first consider the largest numbers, which are more likely to be included in the subsequence for maximizing the sum. It then uses dynamic programming to find the maximum sum of a valid subsequence.