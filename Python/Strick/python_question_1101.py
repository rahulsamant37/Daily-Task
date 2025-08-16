# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

A palindromic substring is a string that reads the same backward as forward.

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
    Finds the longest palindromic substring within a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """

    n = len(s)
    if n < 2:
        return s  # A string of length 0 or 1 is a palindrome

    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Start with length 2 and expand
    start = 0  # Starting index of the longest palindromic substring
    max_len = 1  # Length of the longest palindromic substring

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1  # Ending index of the substring

            if length == 2:
                if s[i] == s[j]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            else:
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False

            # Update the longest palindrome if needed
            if dp[i][j] and length > max_len:
                start = i
                max_len = length

    return s[start:start + max_len]


# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") in ("a", "c")
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("") == ""
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("level") == "level"
    assert longest_palindrome("noon") == "noon"
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome()