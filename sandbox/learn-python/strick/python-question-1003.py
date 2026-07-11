# Python Question: Longest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.

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
    def longest_palindromic_subsequence_length(s):
        """
        Calculates the length of the longest palindromic subsequence of a given string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)

        # Create a DP table to store the lengths of LPS for substrings
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate through substrings of increasing lengths
        for cl in range(2, n + 1):  # cl: current length of substring
            for i in range(n - cl + 1):  # i: starting index of substring
                j = i + cl - 1  # j: ending index of substring

                # If the characters at the ends of the substring match
                if s[i] == s[j]:
                    # The LPS length is 2 (for the matching characters) + LPS length of the inner substring
                    dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2
                else:
                    # Otherwise, the LPS length is the maximum of the LPS lengths of the substrings without the first or last character
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The length of the LPS of the entire string is stored in dp[0][n-1]
        return dp[0][n - 1]

    return longest_palindromic_subsequence_length

# Test cases
def test_solution():
    longest_palindromic_subsequence_length = solution()
    assert longest_palindromic_subsequence_length("bbbab") == 4
    assert longest_palindromic_subsequence_length("cbbd") == 2
    assert longest_palindromic_subsequence_length("a") == 1
    assert longest_palindromic_subsequence_length("ac") == 1
    assert longest_palindromic_subsequence_length("abca") == 3
    assert longest_palindromic_subsequence_length("agbdba") == 5
    assert longest_palindromic_subsequence_length("character") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()