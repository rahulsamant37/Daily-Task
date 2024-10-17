# Python Question: Longest Palindromic Subsequence
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
def longest_palindromic_subsequence(s):
    """
    Calculates the length of the longest palindromic subsequence of a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a DP table to store lengths of LPS for subproblems.
    # dp[i][j] stores the length of LPS of substring s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate over different lengths of substrings (length = 2 to n)
    for length in range(2, n + 1):
        # Iterate over starting indices of substrings
        for i in range(n - length + 1):
            # Calculate the ending index of the substring
            j = i + length - 1

            # If the first and last characters of the substring are the same
            if s[i] == s[j]:
                # The LPS length is 2 + LPS length of the substring without the first and last characters
                dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2
            else:
                # If the first and last characters are different,
                # the LPS length is the maximum of LPS lengths of the substring without the first character
                # and the substring without the last character.
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The final result is stored in dp[0][n-1], representing the LPS length of the entire string.
    return dp[0][n - 1]


# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("aa") == 2
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("agbdba") == 5
    assert longest_palindromic_subsequence("abcabcabcabc") == 4
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindromic_subsequence()