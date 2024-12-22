# DSA Problem 294

'''
Problem Statement:
You are given a list of positive integers and a target sum. Your task is to find out if there is a subset of the given list whose sum is exactly equal to the target sum. You can assume that the list can contain at most 20 integers and the target sum can be at most 10000. Return True if such a subset exists, otherwise return False.

For example, given the list [3, 34, 4, 12, 5, 2] and a target sum of 9, the function should return True because the subset [4, 5] sums up to 9.
'''

Solution:
```python
def is_subset_sum_possible(numbers, target_sum):
    n = len(numbers)
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    
    # Initialize the dp array, the first column is True as sum 0 is always possible
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for s in range(1, target_sum + 1):
            if numbers[i-1] > s:
                dp[i][s] = dp[i-1][s]
            else:
                dp[i][s] = dp[i-1][s] or dp[i-1][s-numbers[i-1]]
    
    return dp[n][target_sum]

# Check function
def check():
    assert is_subset_sum_possible([3, 34, 4, 12, 5, 2], 9) == True
    assert is_subset_sum_possible([3, 34, 4, 12, 5, 2], 30) == False
    assert is_subset_sum_possible([1, 5, 11, 5], 11) == True
    assert is_subset_sum_possible([1, 2, 3, 4, 5], 15) == True
    assert is_subset_sum_possible([1, 2, 3, 4, 5], 16) == False
    print("All test cases passed successfully.")

check()
```

This Python solution uses dynamic programming to determine if a subset of the given numbers can sum up to the target sum. It initializes a 2D boolean array `dp` where `dp[i][s]` indicates whether a subset with sum `s` can be formed using the first `i` numbers. The solution iteratively fills the `dp` array based on whether the current number can be included in the subset or not.