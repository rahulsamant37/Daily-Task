# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

A palindrome is a string that reads the same backward as forward.

Example:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
'''

# Solution
def longestPalindrome(s: str) -> str:
    """
    Finds the longest palindromic substring within a given string.

    The algorithm uses dynamic programming to determine if a substring is a palindrome.
    It maintains a 2D boolean table dp where dp[i][j] is True if the substring
    s[i:j+1] is a palindrome, and False otherwise.

    The table is filled diagonally, starting with substrings of length 1 and 2,
    and then expanding to longer substrings.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring found in s.
    """
    n = len(s)
    if n < 2:
        return s  # Single character string is a palindrome

    dp = [[False] * n for _ in range(n)]
    start = 0  # Start index of the longest palindrome
    max_len = 1  # Length of the longest palindrome

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
def test_longestPalindrome():
    assert longestPalindrome("babad") in ("bab", "aba")
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a"
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("bananas") == "anana"
    assert longestPalindrome("") == ""
    assert longestPalindrome("aaaaaaaa") == "aaaaaaaa"

    print("All test cases passed!")

if __name__ == "__main__":
    test_longestPalindrome()