# DSA Problem 336

'''
Problem Statement:
A sequence of positive integers is called a "good sequence" if and only if for every pair of consecutive elements, the second is a multiple of the first. For a given list of positive integers, find the length of the longest good subsequence that can be chosen from the list.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
'''

Solution:
```python
from bisect import bisect_left

def longest_good_subsequence(arr):
    arr.sort()
    dp = [1] * len(arr)
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] % arr[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example usage:
# arr = [10, 5, 2, 6, 100]
# print(longest_good_subsequence(arr))  # Output will depend on the input array.
```

This solution finds the longest subsequence of the given array where each element (except the first one) is a multiple of its predecessor. It uses dynamic programming to keep track of the longest subsequence length ending at each index.