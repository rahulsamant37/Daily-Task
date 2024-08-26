# Python Question: Longest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence's length. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a string that reads the same backward as forward.

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

    # Create a DP table to store the lengths of longest palindromic subsequences.
    # dp[i][j] will store the length of the longest palindromic subsequence of s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Initialize the diagonal elements.  A single character is a palindrome of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate through subsequences of increasing length.
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # If the characters at the start and end of the subsequence are the same,
            # then the length of the longest palindromic subsequence is 2 plus the length
            # of the longest palindromic subsequence of the substring without those characters.
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            # Otherwise, the length of the longest palindromic subsequence is the maximum of
            # the lengths of the longest palindromic subsequences of the substrings obtained
            # by removing either the start or the end character.
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The result is stored in dp[0][n-1], which represents the length of the longest
    # palindromic subsequence of the entire string.
    return dp[0][n - 1]


# Test cases
def test_solution():
    assert longest_palindromic_subsequence_length("bbbab") == 4
    assert longest_palindromic_subsequence_length("cbbd") == 2
    assert longest_palindromic_subsequence_length("a") == 1
    assert longest_palindromic_subsequence_length("ac") == 1
    assert longest_palindromic_subsequence_length("aba") == 3
    assert longest_palindromic_subsequence_length("racecar") == 7
    assert longest_palindromic_subsequence_length("agbdba") == 5
    assert longest_palindromic_subsequence_length("abcdefghij") == 1
    assert longest_palindromic_subsequence_length("abcdefghih") == 3
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()