# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

A palindromic substring is a string that reads the same backward as forward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (either is acceptable)

Input: s = "cbbd"
Output: "bb"
'''

# Solution
def longestPalindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """
    n = len(s)
    if n < 2:
        return s  # Single character or empty string is a palindrome

    # dp[i][j] is True if the substring s[i:j+1] is a palindrome, False otherwise.
    dp = [[False] * n for _ in range(n)]

    # All single characters are palindromes.
    for i in range(n):
        dp[i][i] = True

    # Initialize the start and max length of the longest palindrome.
    start = 0
    max_length = 1

    # Check for palindromes of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromes of length 3 or more.  Iterate through all possible substring lengths
    # and starting positions.
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):  # i is the starting index of the substring
            j = i + k - 1  # j is the ending index of the substring

            # Check if the substring s[i:j+1] is a palindrome.
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

                # Update the start and max length if a longer palindrome is found.
                if k > max_length:
                    start = i
                    max_length = k

    # Return the longest palindromic substring.
    return s[start:start + max_length]

# Test cases
def test_longestPalindrome():
    assert longestPalindrome("babad") in ("bab", "aba")
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a"
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("bananas") == "anana"
    assert longestPalindrome("level") == "level"
    assert longestPalindrome("") == ""
    assert longestPalindrome("abaaba") == "abaaba"
    assert longestPalindrome("abcda") == "a"

    print("All test cases passed!")

if __name__ == "__main__":
    test_longestPalindrome()