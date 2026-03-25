# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (either is a valid answer)

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
    Finds the longest palindromic substring within a given string.

    The approach uses dynamic programming to efficiently determine
    whether a substring is a palindrome.  A 2D boolean table dp[i][j]
    is constructed where dp[i][j] is True if the substring s[i:j+1]
    is a palindrome, and False otherwise.

    The table is filled in a bottom-up manner, starting with single-character
    substrings and then expanding to longer substrings.
    """
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for palindromes of length 3 or more
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
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
    assert longest_palindrome("madam") == "madam"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("level") == "level"
    assert longest_palindrome("noon") == "noon"
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaaaaaa") == "aaaaaaaa"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()