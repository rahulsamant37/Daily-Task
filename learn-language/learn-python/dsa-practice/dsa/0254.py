# DSA Problem 254

'''
Problem Statement:
A palindrome is a string that reads the same backward as forward, e.g., "radar".
Given a string `s`, find the length of the longest palindromic subsequence in it.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
For example, "ace" is a subsequence of "abcde".

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
def longest_palindromic_subseq(s: str) -> int:
    n = len(s)
    # dp[i][j] represents the length of the longest palindromic subsequence in s[i...j]
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the dp table
    for length in range(2, n + 1):  # length is the length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]

# Testing the function with provided data points
print(longest_palindromic_subseq("bbbab"))  # Output: 4
print(longest_palindromic_subseq("cbbd"))   # Output: 2
'''

This problem involves dynamic programming to find the longest palindromic subsequence in a given string. The solution uses a 2D array `dp` to store the results of subproblems, where `dp[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`.