# Python Question: Find the Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.

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
def longest_palindrome_subsequence(s):
    """
    Finds the length of the longest palindromic subsequence of a string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store lengths of LPS for substrings.
    # dp[i][j] will store the length of LPS for substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: Single character substrings are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate over substring lengths starting from 2
    for cl in range(2, n + 1):  # cl: current length

        # Iterate over starting indices of substrings
        for i in range(n - cl + 1):
            j = i + cl - 1  # Ending index of the substring

            # If the first and last characters of the substring are the same
            if s[i] == s[j]:
                # LPS length is 2 + LPS length of the substring without the first and last characters
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                # If the first and last characters are different,
                # LPS length is the maximum of LPS length of the substring without the first character
                # and LPS length of the substring without the last character.
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of the LPS for the entire string is stored in dp[0][n-1]
    return dp[0][n - 1]

# Test cases
def test_longest_palindrome_subsequence():
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("ac") == 1
    assert longest_palindrome_subsequence("aba") == 3
    assert longest_palindrome_subsequence("racecar") == 7
    assert longest_palindrome_subsequence("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome_subsequence()