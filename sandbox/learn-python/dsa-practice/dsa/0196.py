# DSA Problem 196

'''
Problem Statement:
A sequence of positive integers `nums` is given. You need to find the length of the longest increasing subsequence (LIS) where the difference between two consecutive elements is strictly increasing. 

For example, in the subsequence `[1, 3, 7, 11]`, the differences are `[2, 4, 4]`, which are not strictly increasing. But in `[1, 3, 6, 10]`, the differences are `[2, 3, 4]`, which are strictly increasing.

Return the length of the longest subsequence with strictly increasing differences.

Constraints:
- 2 <= nums.length <= 1000
- 1 <= nums[i] <= 10^6
'''

Solution:
```python
def longest_increasing_diff_subsequence(nums):
    n = len(nums)
    # dp[i] will store the length of the longest increasing subsequence ending with nums[i]
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] - nums[j] > nums[j] - nums[max(0, j-1)]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Example check function
def check_solution():
    assert longest_increasing_diff_subsequence([1, 3, 6, 10]) == 4
    assert longest_increasing_diff_subsequence([1, 2, 3, 4]) == 2
    assert longest_increasing_diff_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 5
    print("All test cases passed.")

check_solution()
```

This Python solution defines a function `longest_increasing_diff_subsequence` that calculates the length of the longest subsequence within an array `nums` where the difference between consecutive elements is strictly increasing. The dynamic programming approach is used to efficiently solve the problem, and a check function is provided to validate the correctness of the solution with given test cases.