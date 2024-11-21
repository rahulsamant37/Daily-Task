# DSA Problem 263

'''
Problem Statement:
A palindrome is a string that reads the same backward as forward, e.g., "radar" or "madam". Given a string `s`, you need to find the length of the longest palindromic subsequence in `s`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, "ace" is a subsequence of "abcde" while "aec" is not.

Write a function `longest_palindrome_subseq` that takes a string `s` as input and returns the length of the longest palindromic subsequence.

Constraints:
- 1 <= s.length <= 1000
- `s` consists of only lowercase English letters.

Example:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
'''

Solution:
```python
def longest_palindrome_subseq(s: str) -> int:
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

# Test the function
print(longest_palindrome_subseq("bbbab"))  # Output: 4
```

This solution uses dynamic programming to efficiently find the length of the longest palindromic subsequence. The `dp` array is used to store the length of the longest palindromic subsequence for substrings of `s`.