# DSA Problem 224

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward. Given a string `s` consisting of lowercase English letters, find the length of the longest palindromic subsequence in `s`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
1 <= s.length <= 1000
`s` consists only of lowercase English letters.
'''

Solution:
def longest_palindromic_subsequence(s: str) -> int:
    n = len(s)
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        next_row = [0] * n
        next_row[i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                next_row[j] = 2 + dp[j - 1]
            else:
                next_row[j] = max(dp[j], next_row[j - 1])
        dp = next_row
    return dp[n - 1]

# Example check (You can run these lines to verify the solution)
print(longest_palindromic_subsequence("bbbab"))  # Expected output: 4
print(longest_palindromic_subsequence("cbbd"))   # Expected output: 2