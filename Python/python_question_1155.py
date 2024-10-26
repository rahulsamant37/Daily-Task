# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

A palindrome is a string that reads the same backward as forward.

Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

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

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """

    n = len(s)
    if n < 2:
        return s

    # dp[i][j] will be true if the substring s[i:j+1] is a palindrome, false otherwise.
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

    # Check for palindromes of length 3 or greater
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
    assert longest_palindrome("level") == "level"
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaa") == "aaaa"
    assert longest_palindrome("abcda") == "a"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()