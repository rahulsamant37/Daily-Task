# Python Question: Longest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence (LPS) that can be formed from `s`.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
A palindrome is a sequence that reads the same forwards and backward.

Example:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

# Solution
def longest_palindromic_subsequence_length(s):
    """
    Calculates the length of the longest palindromic subsequence of a given string.

    Args:
    s (str): The input string.

    Returns:
    int: The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store the lengths of LPS for different substrings.
    # dp[i][j] stores the length of the LPS of s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate over substrings of increasing length.
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # If the characters at the ends of the substring match,
            # then the LPS length is 2 plus the LPS length of the substring without those characters.
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)  # handle empty substring
            else:
                # Otherwise, the LPS length is the maximum of the LPS lengths of the two substrings
                # obtained by removing one character from either end.
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the LPS of the entire string is stored in dp[0][n-1].
    return dp[0][n - 1]

# Test cases
def test_solution():
    assert longest_palindromic_subsequence_length("bbbab") == 4
    assert longest_palindromic_subsequence_length("cbbd") == 2
    assert longest_palindromic_subsequence_length("a") == 1
    assert longest_palindromic_subsequence_length("ac") == 1
    assert longest_palindromic_subsequence_length("aba") == 3
    assert longest_palindromic_subsequence_length("racecar") == 7
    assert longest_palindromic_subsequence_length("leetcode") == 3
    assert longest_palindromic_subsequence_length("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()