# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence.
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

    # Iterate through increasing lengths of substrings
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                # If the characters at the beginning and end are the same,
                # add 2 to the length of the longest palindromic subsequence
                # of the substring without those characters.
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                # If the characters are different, take the maximum of the lengths
                # of the longest palindromic subsequences of the substrings
                # without the first character and without the last character.
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("abba") == 4
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("agbdba") == 5
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()