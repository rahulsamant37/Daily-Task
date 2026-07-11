# Python Question: Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (either is acceptable)

Input: s = "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    The algorithm uses dynamic programming to efficiently determine if a substring
    is a palindrome.  It builds a table `dp` where `dp[i][j]` is True if the
    substring `s[i:j+1]` is a palindrome, and False otherwise.

    The table is filled in diagonally, starting with substrings of length 1, then
    length 2, and so on.  This ensures that when checking if a substring of length
    `k` is a palindrome, the substrings of length `k-2` within it have already
    been checked.
    """
    n = len(s)
    if n < 2:
        return s  # Single character or empty string is a palindrome

    dp = [[False] * n for _ in range(n)]  # dp[i][j] is True if s[i:j+1] is palindrome
    start = 0  # Start index of the longest palindromic substring
    max_length = 1  # Length of the longest palindromic substring

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for substrings of length 3 or more
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1  # Ending index of the substring s[i:j+1]
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k

    return s[start:start + max_length]


# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaaaaaa") == "aaaaaaaa"
    assert longest_palindrome("ababa") == "ababa"

if __name__ == "__main__":
    test_longest_palindrome()