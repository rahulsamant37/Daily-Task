# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A palindrome is a string that reads the same backward as forward.

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
    Finds the length of the longest palindromic subsequence in a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate through substrings of increasing length
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                # If the characters at the ends are the same,
                # the length of the LPS is 2 + LPS of the substring without those characters
                dp[i][j] = 2 + dp[i+1][j-1] if i+1 <= j-1 else 2 #handle i+1>j-1 case
            else:
                # If the characters at the ends are different,
                # the length of the LPS is the maximum of the LPS of the substring without the first character
                # and the LPS of the substring without the last character
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1]
    return dp[0][n-1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("aa") == 2
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("abcabcabcabc") == 7
    assert longest_palindromic_subsequence("character") == 5
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()