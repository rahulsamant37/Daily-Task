# Python Question: Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """
    if not s:
        return ""

    n = len(s)
    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise.
    dp = [[False] * n for _ in range(n)]

    # Initialize single-character palindromes
    for i in range(n):
        dp[i][i] = True

    # Initialize two-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True

    # Build up the dp table for longer substrings
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

    # Find the start and end indices of the longest palindrome
    start = 0
    max_length = 1
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] and (j - i + 1) > max_length:
                start = i
                max_length = j - i + 1

    return s[start:start + max_length]


# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("") == ""
    assert longest_palindrome("bananas") in ("anana", "nanan")
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome()