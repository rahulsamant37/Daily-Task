# DSA Problem 85

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward. Given a string `s` consisting of lowercase English letters, your task is to find the length of the longest palindromic substring that can be formed by deleting at most two characters from `s`. 

For example, in the string "raceecar", the longest palindromic substring that can be formed by deleting at most two characters is "racecar" (deleting the 'e' and 'e'), which has a length of 7.

You are to implement a function `longest_palindrome_with_deletions(s: str) -> int` that returns the length of the longest palindromic substring achievable under the given conditions.

Constraints:
- The length of `s` is between 3 and 1000 characters.
- `s` is composed of lowercase English letters.
'''

Solution:
```python
def longest_palindrome_with_deletions(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            if j - i + 1 - dp[i][j] <= 2:
                return j - i + 1
    return max(max(row) for row in dp)

# Example check (This part is not part of the solution code)
print(longest_palindrome_with_deletions("raceecar"))  # Expected output: 7
```

This Python solution uses dynamic programming to find the longest palindromic substring that can be formed by deleting at most two characters from the given string `s`. The function `longest_palindrome_with_deletions` computes and returns the length of this substring.