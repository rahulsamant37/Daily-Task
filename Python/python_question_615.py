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
def solution():
    def longest_palindromic_subsequence(s):
        """
        Calculates the length of the longest palindromic subsequence in a given string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)

        # Create a DP table to store the lengths of LPS for subproblems.
        # dp[i][j] stores the length of LPS in s[i...j].
        dp = [[0] * n for _ in range(n)]

        # Base case: Single characters are palindromes of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate through subproblems of increasing length.
        for cl in range(2, n + 1):  # cl: current length of the subsequence
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j]:
                    # If the characters at the ends match, the LPS length is 2 + LPS of the inner substring.
                    dp[i][j] = 2 + dp[i + 1][j - 1] if cl > 2 else 2 #handle the case where cl ==2, to avoid accessing out of bounds indices
                else:
                    # If the characters at the ends don't match, the LPS length is the maximum of LPS of two subproblems.
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The result is stored in dp[0][n-1], which represents the LPS length of the entire string.
        return dp[0][n - 1]
    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution()
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("aa") == 2
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("agbdba") == 5
    assert longest_palindromic_subsequence("abcdefg") == 1
    assert longest_palindromic_subsequence("") == 0

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()