# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

A palindromic substring is a substring that reads the same backward as forward.

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

    n = len(s)
    if n < 2:
        return s  # Empty or single-character string is a palindrome

    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise
    dp = [[False] * n for _ in range(n)]

    # All single-character substrings are palindromes
    for i in range(n):
        dp[i][i] = True

    # Initialize the longest palindrome to the first character
    longest_start = 0
    longest_len = 1

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            longest_start = i
            longest_len = 2

    # Check for palindromes of length 3 or more
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):  # i is the starting index
            j = i + k - 1  # j is the ending index
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > longest_len:
                    longest_start = i
                    longest_len = k

    return s[longest_start:longest_start + longest_len]

# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("level") == "level"
    assert longest_palindrome("bananas") in ("anana", "nanan")
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaaaaaaaa") == "aaaaaaaaaa"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()