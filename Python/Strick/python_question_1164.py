# Python Question: Find the Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.

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
def solution():
    def longest_palindromic_subsequence(s):
        """
        Finds the length of the longest palindromic subsequence in a string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """

        n = len(s)

        # Create a DP table to store the lengths of palindromic subsequences.
        # dp[i][j] stores the length of the longest palindromic subsequence
        # in the substring s[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Initialize the DP table for single-character subsequences.
        # A single character is a palindrome of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate through the DP table in increasing order of substring length.
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # If the characters at the beginning and end of the substring are equal,
                # then the longest palindromic subsequence includes these characters,
                # and its length is 2 plus the length of the longest palindromic subsequence
                # in the substring without these characters.
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # Otherwise, the longest palindromic subsequence is the longer of the
                # longest palindromic subsequences in the substrings obtained by
                # removing either the first or the last character.
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The length of the longest palindromic subsequence in the entire string
        # is stored in dp[0][n-1].
        return dp[0][n - 1]
    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution()
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("abcda") == 3
    assert longest_palindromic_subsequence("character") == 5

if __name__ == "__main__":
    test_solution()