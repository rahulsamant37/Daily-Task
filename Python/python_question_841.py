# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A palindrome is a string that reads the same backward as forward.

Example:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

# Solution
def solution():
    """
    Calculates the length of the longest palindromic subsequence of a given string.

    The approach uses dynamic programming.  We create a 2D array `dp` where `dp[i][j]` stores
    the length of the longest palindromic subsequence of the substring `s[i:j+1]`.

    The base cases are:
    - `dp[i][i] = 1` for all `i` (a single character is a palindrome of length 1).

    The recurrence relation is:
    - If `s[i] == s[j]`, then `dp[i][j] = dp[i+1][j-1] + 2` (we can extend the palindrome by 2).
    - If `s[i] != s[j]`, then `dp[i][j] = max(dp[i+1][j], dp[i][j-1])` (we take the longest palindrome
      from either excluding `s[i]` or excluding `s[j]`).

    Finally, `dp[0][n-1]` contains the length of the longest palindromic subsequence of the entire string.
    """
    s = s_global  # Access the global variable s
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base cases: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate over increasing lengths of substrings
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

# Test cases
def test_solution():
    global s_global  # Declare s_global as global

    s_global = "bbbab"
    assert solution() == 4

    s_global = "cbbd"
    assert solution() == 2

    s_global = "a"
    assert solution() == 1

    s_global = "abcabcabcabc"
    assert solution() == 7

    s_global = "character"
    assert solution() == 5

    s_global = "racecar"
    assert solution() == 7

    s_global = ""
    assert solution() == 0

if __name__ == "__main__":
    # Initialize s_global here, though it is updated in test_solution
    s_global = ""
    test_solution()