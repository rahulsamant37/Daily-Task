# DSA Problem 141

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward. Given a string `s` consisting of lowercase English letters, determine the length of the longest palindromic subsequence in `s`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

Solution:
```python
def longest_palindromic_subseq(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                
    return dp[0][n - 1]

# Example test cases
print(longest_palindromic_subseq("bbbab"))  # Output: 4
print(longest_palindromic_subseq("cbbd"))  # Output: 2
```
This Python solution uses dynamic programming to find the longest palindromic subsequence. The `dp` array `dp[i][j]` represents the length of the longest palindromic subsequence in the string `s[i:j+1]`. The function iteratively fills this array and returns the value for the entire string.