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

        # Create a 2D table to store lengths of palindromic subsequences.
        # dp[i][j] will store the length of LPS in substring s[i...j]
        dp = [[0] * n for _ in range(n)]

        # Base case: Single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Fill the table diagonally.  cl is the length of the subsequence.
        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2  # If ends match, add 2 to inner LPS
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])  # If ends don't match, take max of LPS without either end

        return dp[0][n - 1]  # Result is stored in dp[0][n-1]

    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution()
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("abcbca") == 5
    assert longest_palindromic_subsequence("abcdefg") == 1
    assert longest_palindromic_subsequence("racecar") == 7
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()