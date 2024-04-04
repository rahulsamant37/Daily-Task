# Python Question: Find the Largest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a sequence of characters within a string that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (both are valid)

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
        return s  # Empty or single-character string is a palindrome

    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise
    dp = [[False] * n for _ in range(n)]

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    start = 0  # Starting index of the longest palindrome
    max_len = 1 # Length of the longest palindrome

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for palindromes of length 3 or more
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):
            j = i + k - 1  # Ending index of the substring
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
    assert longest_palindrome("abcda") == "a"
    assert longest_palindrome("abacdfgdcaba") == "aba"
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome()