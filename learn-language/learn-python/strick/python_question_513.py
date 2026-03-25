# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A palindrome is a string that reads the same forward and backward.

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

    # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate over lengths of subsequences, starting from length 2
    for length in range(2, n + 1):
        # Iterate over the starting indices of subsequences
        for i in range(n - length + 1):
            j = i + length - 1  # Calculate the ending index

            # If the characters at the start and end are the same,
            # then the longest palindromic subsequence is 2 + the longest
            # palindromic subsequence of the substring in between
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2
            # Otherwise, the longest palindromic subsequence is the maximum of
            # the longest palindromic subsequences of the substrings excluding
            # either the start or the end character
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The result is stored in dp[0][n-1], which represents the longest
    # palindromic subsequence of the entire string
    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("leetcode") == 3
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()