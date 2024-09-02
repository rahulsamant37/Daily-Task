# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a sequence that reads the same backward as forward.

Example:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

# Solution
def longest_palindromic_subsequence(s):
    """
    Calculates the length of the longest palindromic subsequence of a given string.

    The approach uses dynamic programming. dp[i][j] stores the length of the
    longest palindromic subsequence of the substring s[i:j+1].

    If s[i] == s[j], then dp[i][j] = dp[i+1][j-1] + 2.
    Otherwise, dp[i][j] = max(dp[i+1][j], dp[i][j-1]).

    The base cases are:
    - dp[i][i] = 1 (a single character is a palindrome of length 1)
    - dp[i][i+1] = 2 if s[i] == s[i+1], 1 otherwise (two characters)
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base cases: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate through substrings of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("abba") == 4
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("bananas") == 5
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindromic_subsequence()