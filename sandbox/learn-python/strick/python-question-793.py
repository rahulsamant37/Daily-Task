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
        Finds the length of the longest palindromic subsequence of a given string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)

        # Create a DP table to store the lengths of LPS for substrings.
        # dp[i][j] stores the length of LPS for substring s[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Initialize the diagonal elements of the DP table.
        # A single character is always a palindrome of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate over the substrings of increasing lengths.
        for cl in range(2, n + 1):  # cl is the current length of the substring
            for i in range(n - cl + 1):
                j = i + cl - 1  # j is the end index of the substring

                # If the first and last characters of the substring are the same,
                # then the LPS length is 2 plus the LPS length of the substring
                # without the first and last characters.
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Otherwise, the LPS length is the maximum of the LPS lengths
                    # of the substrings without the first character and without the
                    # last character.
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The length of the LPS of the entire string is stored in dp[0][n-1].
        return dp[0][n - 1]
    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution()
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("bananas") == 5
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()