# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence (LPS) in `s`.

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

    # Create a DP table to store lengths of LPS for substrings.
    # dp[i][j] stores the length of the LPS of substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate through substrings of increasing length.
    for cl in range(2, n + 1):  # cl: current length of substring
        for i in range(n - cl + 1):  # i: starting index of substring
            j = i + cl - 1  # j: ending index of substring

            if s[i] == s[j]:
                # If the first and last characters of the substring match,
                # the LPS length is 2 plus the LPS length of the substring
                # without these two characters (s[i+1:j]).
                if cl == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # If the first and last characters don't match, the LPS length
                # is the maximum of the LPS lengths of the substrings without
                # the first character (s[i+1:j+1]) and without the last character (s[i:j]).
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of the LPS of the entire string is stored in dp[0][n-1].
    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("") == 0
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("abcdefg") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("bananas") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()