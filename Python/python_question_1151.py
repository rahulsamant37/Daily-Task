# Python Question: Find the Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a sequence of characters that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (Both are valid longest palindromic substrings)

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
    Finds the longest palindromic substring in the input string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """
    if not s:
        return ""

    n = len(s)
    if n == 1:
        return s

    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    start = 0
    max_length = 1
    for i in range(n - 1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_length = 2

    # Check for substrings of length 3 or more
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):
            j = i + k - 1  # j is the end index of the substring
            if s[i] == s[j] and dp[i+1][j-1]:
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
    assert longest_palindrome("abcda") in ("a","b","c","d")

if __name__ == "__main__":
    test_longest_palindrome()