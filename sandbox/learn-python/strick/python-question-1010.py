# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

A palindromic substring is a substring that reads the same forwards and backward.

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
    Finds the longest palindromic substring within the given string s.

    The approach uses dynamic programming. A table dp[i][j] is constructed
    where dp[i][j] is True if the substring s[i:j+1] is a palindrome,
    and False otherwise.

    The table is filled in a bottom-up manner.  dp[i][i] is always True.
    dp[i][i+1] is True if s[i] == s[i+1].  For longer substrings,
    dp[i][j] is True if s[i] == s[j] and dp[i+1][j-1] is True.

    The longest palindromic substring is tracked as the table is filled.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring found in s.
    """
    n = len(s)
    if n < 2:
        return s  # Empty or single-char string is a palindrome

    dp = [[False] * n for _ in range(n)]
    start = 0  # Starting index of the longest palindromic substring
    max_len = 1  # Length of the longest palindromic substring

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
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaa") == "aaaa"
    assert longest_palindrome("ababa") == "ababa"
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome()