# Python Question: Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" (or "aba")

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    Approach:
    The solution uses dynamic programming. A 2D boolean array `dp` is created,
    where `dp[i][j]` is True if the substring `s[i:j+1]` is a palindrome, and False otherwise.

    The `dp` array is populated as follows:
    1. Single-character substrings are palindromes (dp[i][i] = True).
    2. Two-character substrings are checked for palindrome property (s[i] == s[i+1]).
    3. For substrings of length 3 or more, dp[i][j] is True if s[i] == s[j] and dp[i+1][j-1] is True.

    The longest palindromic substring is tracked during the population of the `dp` array.
    """
    n = len(s)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for sub-string of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for lengths greater than 2. k is length of substring
    for k in range(3, n + 1):
        # Fix the starting index
        for i in range(n - k + 1):
            # Get the ending index of substring from starting index i and length k
            j = i + k - 1

            # checking for sub-string from ith index to jth index if s[i+1] to s[j-1] is a palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

                if k > max_len:
                    start = i
                    max_len = k

    return s[start:start + max_len]


# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("banana") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("abracadabra") == "aca"
    assert longest_palindrome("aaaaaaaa") == "aaaaaaaa"
    assert longest_palindrome("abcdefg") == "a"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()