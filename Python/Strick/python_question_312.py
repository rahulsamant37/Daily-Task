# Python Question: Find the Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

A palindromic substring is a substring that reads the same backward as forward.

Example:

Input: "babad"
Output: "bab" or "aba" (either one is acceptable)

Input: "cbbd"
Output: "bb"
'''

# Solution
def longestPalindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """

    n = len(s)
    if n < 2:
        return s  # Empty or single-character string is a palindrome

    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise
    dp = [[False] * n for _ in range(n)]

    # All single-character substrings are palindromes
    for i in range(n):
        dp[i][i] = True

    start = 0  # Starting index of the longest palindrome
    max_length = 1  # Length of the longest palindrome

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromes of length 3 or more
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):  # i is the starting index of the substring
            j = i + k - 1  # j is the ending index of the substring

            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k

    return s[start:start + max_length]

# Test cases
def test_longestPalindrome():
    assert longestPalindrome("babad") in ("bab", "aba")
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a"
    assert longestPalindrome("bb") == "bb"
    assert longestPalindrome("bananas") == "anana"
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("") == ""
    assert longestPalindrome("ababa") == "ababa"
    assert longestPalindrome("abcba") == "abcba"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longestPalindrome()