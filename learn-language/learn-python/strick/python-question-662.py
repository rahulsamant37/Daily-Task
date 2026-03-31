# Python Question: Find the Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

A palindromic substring is a substring that reads the same backward as forward.

Example:
Input: "babad"
Output: "bab" or "aba" (either one is acceptable)

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

    The approach is dynamic programming. We create a 2D table dp where dp[i][j] is True if the substring s[i:j+1] is a palindrome,
    and False otherwise. The base cases are single characters (dp[i][i] = True) and two adjacent characters (dp[i][i+1] = True if s[i] == s[i+1]).
    Then, we iterate through substrings of increasing length, checking if the substring is a palindrome based on the previous smaller substring.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """
    n = len(s)
    if n < 2:
        return s

    # dp[i][j] is True if s[i:j+1] is a palindrome, False otherwise
    dp = [[False] * n for _ in range(n)]

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    start = 0
    max_len = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for palindromes of length 3 or more
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
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("ababa") == "ababa"
    assert longest_palindrome("level") == "level"
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome()