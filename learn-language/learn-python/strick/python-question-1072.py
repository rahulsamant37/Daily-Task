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

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"
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
        return s

    # dp[i][j] will be true if the substring s[i...j] is a palindrome, otherwise false.
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes.
    for i in range(n):
        dp[i][i] = True

    # longest palindrome found so far
    start = 0
    max_len = 1

    # Check for substrings of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for substrings of length greater than 2. k is substring length
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
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("abcba") == "abcba"
    assert longest_palindrome("") == ""
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()