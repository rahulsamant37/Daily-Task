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
    Calculates the length of the longest palindromic subsequence in a given string.

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

    # Iterate through substrings of increasing lengths
    for cl in range(2, n + 1):  # cl: current length of the substring
        for i in range(n - cl + 1):
            j = i + cl - 1  # j: end index of the substring

            # If the characters at the start and end of the substring are equal
            if s[i] == s[j]:
                # The LPS length is 2 plus the LPS length of the substring without those characters
                dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j -1 else 2 # Handles the case when i+1 > j-1
            else:
                # Otherwise, the LPS length is the maximum of the LPS lengths of the substrings
                # excluding either the start or the end character
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The LPS length of the entire string is stored in dp[0][n - 1]
    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("abcabcabcabc") == 4
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()