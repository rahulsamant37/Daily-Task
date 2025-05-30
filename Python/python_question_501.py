# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab" or "aba"

Input: "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    Approach:
    This solution uses dynamic programming. We create a 2D boolean table dp,
    where dp[i][j] is True if the substring s[i:j+1] is a palindrome, and False otherwise.

    1. Initialize dp table:
       - All single characters are palindromes (dp[i][i] = True).
       - Check for palindromes of length 2.

    2. Iterate through substrings of increasing length (k from 3 to n):
       - For each substring s[i:j+1] of length k, check if s[i] == s[j] and
         if the substring s[i+1:j] is a palindrome (dp[i+1][j-1] is True).
         If both conditions are met, then s[i:j+1] is a palindrome (dp[i][j] = True).

    3. Keep track of the start index and maximum length of the longest palindrome found so far.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring in s.
    """

    n = len(s)
    if n < 2:
        return s  # Empty or single-character string is a palindrome

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromes of length 3 or more
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1  # End index of the substring

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
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaa") == "aaaa"
    assert longest_palindrome("abbcccdddde") == "ddddd"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()