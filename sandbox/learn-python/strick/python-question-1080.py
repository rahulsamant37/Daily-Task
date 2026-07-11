# Python Question: Longest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a sequence that reads the same backward as forward.

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
    def longest_palindromic_subsequence_length(s):
        """
        Calculates the length of the longest palindromic subsequence of a string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """

        n = len(s)
        # Create a DP table to store lengths of LPS for subproblems.
        # dp[i][j] stores the length of LPS of s[i...j]
        dp = [[0] * n for _ in range(n)]

        # Base case: Single characters are palindromes of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Fill the DP table diagonally.  l is length of substring
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    # If the first and last characters match, the LPS length is
                    # 2 + LPS length of the substring between them.
                    dp[i][j] = 2 + (dp[i+1][j-1] if i+1 <= j-1 else 0) # handle cases where i+1 > j-1
                else:
                    # If the first and last characters don't match, the LPS length is
                    # the maximum of the LPS lengths of the substrings excluding either
                    # the first or last character.
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        # The length of the LPS of the entire string is stored in dp[0][n-1].
        return dp[0][n-1]

    return longest_palindromic_subsequence_length

# Test cases
def test_solution():
    longest_palindromic_subsequence_length = solution()
    assert longest_palindromic_subsequence_length("bbbab") == 4
    assert longest_palindromic_subsequence_length("cbbd") == 2
    assert longest_palindromic_subsequence_length("a") == 1
    assert longest_palindromic_subsequence_length("ac") == 1
    assert longest_palindromic_subsequence_length("aba") == 3
    assert longest_palindromic_subsequence_length("racecar") == 7
    assert longest_palindromic_subsequence_length("") == 0
    assert longest_palindromic_subsequence_length("abcdefgh") == 1
    assert longest_palindromic_subsequence_length("abcbda") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()