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
    Calculates the length of the longest palindromic subsequence in a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store the lengths of LPS for substrings.
    # dp[i][j] stores the length of LPS of substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table diagonally.
    # l is the length of the substring (from 2 to n).
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1  # Ending index of the substring

            # If the end characters of the substring are the same,
            # then the LPS length is 2 + LPS length of the substring without these end characters.
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)  # Handle edge case where i+1 > j-1 (empty substring)
            # Otherwise, the LPS length is the maximum of the LPS lengths of the two substrings,
            # one excluding the first character, and the other excluding the last character.
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the LPS of the entire string is stored in dp[0][n-1]
    return dp[0][n - 1]


# Test cases
def test_solution():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("aa") == 2
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("abcabcabcabc") == 4
    assert longest_palindromic_subsequence("character") == 5
    assert longest_palindromic_subsequence("leetcode") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()