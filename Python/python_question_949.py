# Python Question: Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same backward as forward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (either is acceptable)

Input: s = "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    The approach uses dynamic programming to efficiently determine if a substring is a palindrome.
    A 2D table dp[i][j] stores whether the substring s[i:j+1] is a palindrome.

    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    n = len(s)
    if n < 2:
        return s

    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, else False
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # longest_palindrome_start and max_len track the start index and length
    # of the longest palindromic substring found so far.
    longest_palindrome_start = 0
    max_len = 1

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            longest_palindrome_start = i
            max_len = 2

    # Check for substrings of length 3 or more
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):  # i is the starting index
            j = i + k - 1  # j is the ending index
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_len:
                    longest_palindrome_start = i
                    max_len = k

    return s[longest_palindrome_start:longest_palindrome_start + max_len]

# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("abracadabra") in ("aca", "ada")
    assert longest_palindrome("") == ""
    assert longest_palindrome("ccc") == "ccc"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()