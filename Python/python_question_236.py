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
    Finds the longest palindromic substring in a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring in s.
    """
    n = len(s)
    if n < 2:
        return s  # Single character or empty string is a palindrome

    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise
    dp = [[False] * n for _ in range(n)]

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # The longest palindrome found so far
    start = 0
    max_len = 1

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for palindromes of length 3 or more
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
def test_longestPalindrome():
    assert longestPalindrome("babad") in ["bab", "aba"]
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a"
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("") == ""
    assert longestPalindrome("bananas") == "anana"
    assert longestPalindrome("abracadabra") in ["aca", "ada"]

    print("All test cases passed!")

if __name__ == "__main__":
    test_longestPalindrome()