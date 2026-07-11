# DSA Problem 32

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward. Given a string `s` consisting of lowercase English letters, find the length of the longest palindromic subsequence in `s`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, "ace" is a subsequence of "abcde" but not "aec" because the order of the elements is changed.

Constraints:
- 1 <= len(s) <= 1000
- s consists of lowercase English letters.

Example:
Input: "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
'''

Solution:
```python
def longest_palindromic_subseq(s):
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

# Example usage
print(longest_palindromic_subseq("bbbab"))  # Output: 4
```
This Python program uses dynamic programming to find the length of the longest palindromic subsequence in the given string `s`. The `dp` table is filled in a bottom-up manner, where `dp[i][j]` represents the length of the longest palindromic subsequence of the substring `s[i...j]`. The program efficiently computes the result with a time complexity of O(n^2) and space complexity of O(n^2), where `n` is the length of the string `s`.