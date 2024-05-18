# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab" or "aba" (either is a valid answer)

Input: "cbbd"
Output: "bb"
'''

# Solution
def longestPalindrome(s):
    """
    Finds the longest palindromic substring within a given string.

    The approach uses dynamic programming. A table dp[i][j] is constructed
    where dp[i][j] is True if the substring s[i:j+1] is a palindrome, and False otherwise.

    The table is filled as follows:
    - dp[i][i] is always True (single characters are palindromes).
    - dp[i][i+1] is True if s[i] == s[i+1].
    - For lengths greater than 2, dp[i][j] is True if s[i] == s[j] and dp[i+1][j-1] is True.

    The longest palindrome is tracked during the table construction.
    """
    n = len(s)
    if n < 2:
        return s

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

    # Check for lengths greater than 2. k is the length of substring
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
def test_solution():
    assert longestPalindrome("babad") in ("bab", "aba")
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a"
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("bananas") == "anana"
    assert longestPalindrome("") == ""
    assert longestPalindrome("aaaa") == "aaaa"
    assert longestPalindrome("abcda") == "a"
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()