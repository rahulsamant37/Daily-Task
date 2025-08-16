# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

A palindrome is a string that reads the same backward as forward.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

# Solution
def longestPalindrome(s: str) -> str:
    """
    Finds the longest palindromic substring within a given string.

    The approach used is dynamic programming. We create a table dp where dp[i][j] is True if the substring s[i:j+1]
    is a palindrome, and False otherwise.

    The base cases are single-character substrings (dp[i][i] = True) and two-character substrings (dp[i][i+1] = True if s[i] == s[i+1]).

    Then, we iterate through substrings of increasing length, checking if they are palindromes based on the previous results
    in the dp table.
    """
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for substrings of length greater than 2
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):  # i is the starting index of the substring
            j = i + k - 1  # j is the ending index of the substring
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_len:
                    start = i
                    max_len = k

    return s[start:start + max_len]


# Test cases
def test_solution():
    assert longestPalindrome("babad") in ("bab", "aba")
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") in ("a", "c")
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("bananas") == "anana"
    assert longestPalindrome("") == ""
    assert longestPalindrome("aaaa") == "aaaa"
    assert longestPalindrome("abcda") in ("a", "b", "c", "d")

if __name__ == "__main__":
    test_solution()