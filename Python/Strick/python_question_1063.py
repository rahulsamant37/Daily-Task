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
            s (str): The input string.

        Returns:
            int: The length of the longest palindromic subsequence.
        """

        n = len(s)

        # Create a table to store lengths of longest palindromic subsequences of substrings
        dp = [[0] * n for _ in range(n)]

        # Base case: Single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate through substrings of increasing length
        for cl in range(2, n + 1):  # cl: current length of substring
            for i in range(n - cl + 1):
                j = i + cl - 1

                # If the first and last characters of the substring match
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # If they don't match, take the maximum length from subproblems
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The length of the longest palindromic subsequence of the entire string is at dp[0][n-1]
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
    assert longest_palindromic_subsequence("bananas") == 5
    assert longest_palindromic_subsequence("character") == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()