# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (either is a valid answer)

Input: s = "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    The approach used is dynamic programming. We create a 2D table dp where
    dp[i][j] is True if the substring s[i:j+1] is a palindrome, and False otherwise.

    The base cases are:
    - dp[i][i] is always True (a single character is a palindrome).
    - dp[i][i+1] is True if s[i] == s[i+1] (two adjacent characters are a palindrome if they are equal).

    For substrings of length 3 or more, dp[i][j] is True if s[i] == s[j] and dp[i+1][j-1] is True.

    We keep track of the start and end indices of the longest palindrome found so far,
    and update them whenever we find a longer palindrome.
    """
    n = len(s)
    if n < 2:
        return s  # Empty string or single character string is a palindrome

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

    # Check for substrings of length 3 or more
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):  # i is the starting index
            j = i + k - 1  # j is the ending index
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
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaa") == "aaaa"
    assert longest_palindrome("abcdefg") in ("a", "b", "c", "d", "e", "f", "g")
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()