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
        return s  # If the string is empty or has only one character, it's a palindrome.

    # dp[i][j] will be true if the substring s[i:j+1] is a palindrome, otherwise false.
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes.
    for i in range(n):
        dp[i][i] = True

    start = 0  # Start index of the longest palindromic substring.
    max_len = 1  # Length of the longest palindromic substring.

    # Check for substrings of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for substrings of length 3 or more.
    for k in range(3, n + 1):  # k is the length of the substring.
        for i in range(n - k + 1):  # i is the starting index of the substring.
            j = i + k - 1  # j is the ending index of the substring.
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_len:
                    start = i
                    max_len = k

    return s[start:start + max_len]

# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaaaaaa") == "aaaaaaaa"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()