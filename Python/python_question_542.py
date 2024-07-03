# Python Question: Find the Largest Palindromic Subsequence

'''
Given a string `s`, find the length of the largest palindromic subsequence.

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
    def longest_palindromic_subsequence(s):
        """
        Finds the length of the largest palindromic subsequence in a given string.

        Args:
            s: The input string.

        Returns:
            The length of the largest palindromic subsequence.
        """
        n = len(s)

        # Create a DP table to store the lengths of LPS for subproblems.
        # dp[i][j] stores the length of LPS of substring s[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Base case: Single characters are palindromes of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate over increasing substring lengths.
        for cl in range(2, n + 1):  # cl: current length
            for i in range(n - cl + 1):
                j = i + cl - 1  # End index of the substring

                # If the first and last characters of the substring are equal,
                # the LPS length is 2 + LPS length of the substring without those characters.
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                # Otherwise, the LPS length is the maximum of the LPS lengths of the
                # substrings obtained by removing either the first or the last character.
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The length of the LPS of the entire string is stored in dp[0][n-1].
        return dp[0][n - 1]

    return longest_palindromic_subsequence


# Test cases
def test_solution():
    lps = solution()
    assert lps("bbbab") == 4
    assert lps("cbbd") == 2
    assert lps("a") == 1
    assert lps("aa") == 2
    assert lps("aba") == 3
    assert lps("racecar") == 7
    assert lps("abcabcabcabc") == 4
    assert lps("character") == 5
    assert lps("agbdba") == 5
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()