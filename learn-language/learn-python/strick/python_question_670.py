# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: "babad"
Output: "bab" or "aba" (both are valid)

Input: "cbbd"
Output: "bb"

Input: "a"
Output: "a"

Input: "ac"
Output: "a"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    The approach uses dynamic programming.  A 2D boolean array `dp` is created where
    dp[i][j] is True if the substring s[i:j+1] is a palindrome, and False otherwise.

    The `dp` array is filled diagonally.  The base cases are substrings of length 1 and 2.
    For substrings of length greater than 2, dp[i][j] is True if s[i] == s[j] and dp[i+1][j-1] is True.

    The longest palindrome found so far is tracked using `start` and `max_length`.
    """
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_length = 2

    # Check for substrings of length greater than 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k

    return s[start:start + max_length]

# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("ababa") == "ababa"
    assert longest_palindrome("abcba") == "abcba"
    assert longest_palindrome("aabbaa") == "aabbaa"
    assert longest_palindrome("") == ""
    print("All test cases passed")

if __name__ == "__main__":
    test_longest_palindrome()