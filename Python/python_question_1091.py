# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
A palindrome is a sequence that reads the same backward as forward.

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

    # Create a 2D array to store the lengths of the longest palindromic subsequences
    # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate over the lengths of the substrings
    for length in range(2, n + 1):
        # Iterate over the starting indices of the substrings
        for i in range(n - length + 1):
            j = i + length - 1  # Calculate the ending index

            # If the characters at the start and end of the substring are equal
            if s[i] == s[j]:
                # The longest palindromic subsequence is the longest palindromic subsequence of the substring without the start and end characters, plus 2
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # Otherwise, the longest palindromic subsequence is the maximum of the longest palindromic subsequences of the substrings without the start or end character
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1]
    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("aa") == 2
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("abcdefg") == 1
    assert longest_palindromic_subsequence("ababa") == 5
    assert longest_palindromic_subsequence("abcabcabc") == 3
    assert longest_palindromic_subsequence("character") == 3

if __name__ == "__main__":
    test_longest_palindromic_subsequence()