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
        Finds the length of the longest palindromic subsequence in a string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """

        n = len(s)
        # Create a DP table to store lengths of LPS for subproblems.
        # dp[i][j] stores the length of the LPS of s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate over lengths of substrings, starting from length 2
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # If the first and last characters are equal,
                # the LPS length is 2 + LPS length of the substring without those characters.
                if s[i] == s[j]:
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)  # Handle edge case where i+1 > j-1
                else:
                    # If the first and last characters are not equal,
                    # the LPS length is the maximum of the LPS lengths of the substrings
                    # without the first or last character.
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The length of the LPS of the entire string is stored in dp[0][n-1]
        return dp[0][n - 1]

    return longest_palindromic_subsequence

# Test cases
def test_solution():
    lps = solution()
    assert lps("bbbab") == 4
    assert lps("cbbd") == 2
    assert lps("a") == 1
    assert lps("ac") == 1
    assert lps("abcda") == 3
    assert lps("bananas") == 5
    assert lps("character") == 5
    assert lps("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()