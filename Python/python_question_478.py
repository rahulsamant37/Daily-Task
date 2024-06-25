# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A palindrome is a sequence that reads the same backward as forward.

Example:
Input: "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

# Solution
def longest_palindromic_subsequence(s):
    """
    Finds the length of the longest palindromic subsequence of a string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a 2D DP table to store the lengths of the longest palindromic subsequences.
    # dp[i][j] represents the length of the longest palindromic subsequence of s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Base case: A single character is a palindrome of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate over the string in increasing order of substring length.
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # If the characters at the start and end of the substring are the same,
            # then the length of the longest palindromic subsequence is 2 plus the length
            # of the longest palindromic subsequence of the substring without those characters.
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)  # Handle edge case where subsequence is of length 2
            # Otherwise, the length of the longest palindromic subsequence is the maximum
            # of the lengths of the longest palindromic subsequences of the substrings
            # without the start character and without the end character.
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1].
    return dp[0][n - 1]

# Test cases
def test_solution():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("aa") == 2
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("leetcode") == 3
    assert longest_palindromic_subsequence("character") == 5
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()