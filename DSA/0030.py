# DSA Problem 30

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward. Given a string `s` consisting of lowercase letters, find the length of the longest palindromic subsequence in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, given the string `s = "bbbab"`, the longest palindromic subsequence is "bbbb", which has a length of 4.

Write a function `longest_palindromic_subsequence` that returns the length of the longest palindromic subsequence in the given string `s`.

Constraints:
- `1 <= s.length <= 1000`
- `s` consists only of lowercase English letters.
'''

Solution:
def longest_palindromic_subsequence(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]

# Example check
print(longest_palindromic_subsequence("bbbab"))  # Expected output: 4
print(longest_palindromic_subsequence("cbbd"))   # Expected output: 2

# Explanation:
# This solution uses dynamic programming to solve the problem. The `dp` array stores the length of the longest palindromic subsequence for substrings of `s`. The outer loop iterates backward from the end of the string, and the inner loop iterates forward. If the characters at the current indices are the same, it adds 2 to the length of the longest palindromic subsequence of the substring without these two characters. If they are different, it takes the maximum value between excluding the current character from the start or from the end.