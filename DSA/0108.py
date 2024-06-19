# DSA Problem 108

'''
Problem Statement:
Arun has a collection of n unique stamps, each with a distinct integer value. He is trying to organize these stamps into two separate albums. The goal is to distribute the stamps between the two albums in such a way that the sum of the values of the stamps in each album is as close as possible to each other without exceeding a given maximum capacity M. The capacity M is the same for both albums.

Write a function `minimize_difference(stamps, M)` where:
- `stamps` is a list of integers representing the values of the stamps.
- `M` is the maximum capacity for each album.

The function should return the minimum possible difference between the sum of the values of the stamps in the two albums, without any album exceeding the capacity M. If it's not possible to distribute the stamps between the two albums without exceeding the capacity, return -1.

Example:
- For `stamps = [5, 1, 6, 2, 8]` and `M = 10`, the function should return 2, as one possible distribution is [5, 5] and [1, 6, 2], with sums 10 and 8 respectively.
'''

Solution:
```python
def minimize_difference(stamps, M):
    total_sum = sum(stamps)
    n = len(stamps)
    dp = [[False] * (M + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(M + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= stamps[i - 1]:
                dp[i][j] |= dp[i - 1][j - stamps[i - 1]]
    
    min_diff = float('inf')
    for j in range(M + 1):
        if dp[n][j]:
            if abs(total_sum - 2 * j) < min_diff:
                min_diff = abs(total_sum - 2 * j)
    
    return min_diff if min_diff != float('inf') else -1

# Example check
print(minimize_difference([5, 1, 6, 2, 8], 10))  # Expected output: 2
```

Explanation:
The solution uses dynamic programming (DP) to find the subset of the stamps that can be placed in the first album such that its sum does not exceed M. The DP table `dp[i][j]` is True if a subset with sum `j` can be formed from the first `i` stamps. The solution iterates through all possible sums up to M and checks the minimum difference in sums achievable between the two albums without exceeding the capacity M. If no such subset exists, the function returns -1.