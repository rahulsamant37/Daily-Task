# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

A palindromic substring is a sequence of characters that reads the same backward as forward.

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
    Finds the longest palindromic substring within a given string.

    Args:
        s (str): The input string.

    Returns:
        str: The longest palindromic substring.
    """
    if not s:
        return ""

    n = len(s)
    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise.
    dp = [[False] * n for _ in range(n)]

    # Initialize single-character palindromes
    for i in range(n):
        dp[i][i] = True

    # Initialize two-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True

    # Build up palindromes of length 3 or more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

    # Find the starting and ending indices of the longest palindrome
    start = 0
    end = 0
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] and (j - i + 1) > (end - start + 1):
                start = i
                end = j

    return s[start:end + 1]

# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("") == ""
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("abracadabra") == "aca"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()