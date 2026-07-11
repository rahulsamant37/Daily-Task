# Python Question: Find the Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

A palindromic substring is a substring that reads the same backward as forward.

Example:
Input: "babad"
Output: "bab" or "aba" (either is acceptable)

Input: "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    The approach used is dynamic programming. A 2D table dp is created where dp[i][j]
    is True if the substring s[i:j+1] is a palindrome, and False otherwise.

    The table is filled as follows:
    1. All single characters are palindromes (dp[i][i] = True).
    2. Check for palindromes of length 2 (dp[i][i+1] = True if s[i] == s[i+1]).
    3. For lengths greater than 2, dp[i][j] = True if s[i] == s[j] and dp[i+1][j-1] is True.

    The longest palindromic substring is tracked during the filling of the table.

    Args:
        s (str): The input string.

    Returns:
        str: The longest palindromic substring.
    """
    n = len(s)
    if n == 0:
        return ""

    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    start = 0  # Starting index of the longest palindrome
    max_length = 1  # Length of the longest palindrome

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromes of length greater than 2
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):
            j = i + k - 1  # Ending index of the substring
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

                if k > max_length:
                    start = i
                    max_length = k

    return s[start:start + max_length]


# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("") == ""
    assert longest_palindrome("bananas") in ("anana", "nanan") # Corrected based on the prompt instructions
    assert longest_palindrome("level") == "level"
    assert longest_palindrome("madam") == "madam"
    assert longest_palindrome("rotor") == "rotor"

    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome()