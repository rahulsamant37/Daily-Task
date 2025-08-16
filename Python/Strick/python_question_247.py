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
    Calculates the length of the longest palindromic subsequence in the given string s.

    Args:
      s: The input string.

    Returns:
      The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a DP table to store the lengths of LPS for substrings
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate through substrings of increasing length
    for cl in range(2, n + 1):  # cl: current length of substring
        for i in range(n - cl + 1):  # i: starting index of substring
            j = i + cl - 1  # j: ending index of substring

            # If the first and last characters are the same
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # Otherwise, take the maximum of the LPS of the substring
                # without the first character or the last character
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of the LPS for the entire string is stored in dp[0][n-1]
    return dp[0][n - 1]

# Test cases
def test_solution():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("bananas") == 5
    assert longest_palindromic_subsequence("character") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()