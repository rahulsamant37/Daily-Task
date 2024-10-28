# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

A string is a palindrome if it reads the same backward as forward.

Example:
Input: "babad"
Output: "bab" or "aba"

Input: "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring within a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring in s.
    """

    if not s:
        return ""

    n = len(s)
    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise
    dp = [[False] * n for _ in range(n)]

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True

    # Check for palindromes of length 3 or greater
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

    # Find the longest palindromic substring
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
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("abcda") == "a"
    assert longest_palindrome("aaaaa") == "aaaaa"

if __name__ == "__main__":
    test_longest_palindrome()