# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
'''

# Solution
def longestPalindrome(s):
    """
    Finds the longest palindromic substring of a given string.

    The approach used is dynamic programming.  A 2D table `dp` is created where `dp[i][j]` is True if the substring
    s[i:j+1] is a palindrome, and False otherwise.

    The table is filled diagonally, starting with single characters and then expanding to longer substrings.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """
    n = len(s)
    if n < 2:
        return s

    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Initialize start and maxlen to track the longest palindrome
    start = 0
    maxLen = 1

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            maxLen = 2

    # Check for palindromes of length 3 or greater
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):  # i is the starting index
            j = i + k - 1  # j is the ending index

            # If the substring s[i+1:j] is a palindrome and the first and last characters are the same,
            # then s[i:j+1] is also a palindrome
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True

                if k > maxLen:
                    start = i
                    maxLen = k

    return s[start:start + maxLen]

# Test cases
def test_longestPalindrome():
    assert longestPalindrome("babad") in ["bab", "aba"]
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a"
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("bananas") == "anana"
    assert longestPalindrome("forgeeksskeegfor") == "geeksskeeg"
    assert longestPalindrome("") == ""
    assert longestPalindrome("ccc") == "ccc"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longestPalindrome()