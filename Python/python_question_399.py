# Python Question: Longest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
A palindrome is a string that reads the same backward as forward.

Example:
Input: "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

# Solution
def longest_palindromic_subsequence_length(s):
    """
    Calculates the length of the longest palindromic subsequence of a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store the lengths of LPS for substrings.
    # dp[i][j] stores the length of the LPS for the substring s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate through substrings of increasing length.
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # If the characters at the start and end of the substring match,
            # then the LPS length is 2 plus the LPS length of the substring
            # without those characters.
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            # Otherwise, the LPS length is the maximum of the LPS lengths of
            # the substrings excluding either the start or the end character.
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The LPS length of the entire string is stored in dp[0][n-1].
    return dp[0][n - 1]

# Test cases
def test_solution():
    assert longest_palindromic_subsequence_length("bbbab") == 4
    assert longest_palindromic_subsequence_length("cbbd") == 2
    assert longest_palindromic_subsequence_length("a") == 1
    assert longest_palindromic_subsequence_length("ac") == 1
    assert longest_palindromic_subsequence_length("aba") == 3
    assert longest_palindromic_subsequence_length("abcdefg") == 1
    assert longest_palindromic_subsequence_length("racecar") == 7
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()