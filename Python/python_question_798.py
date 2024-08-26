# Python Question: Find the Largest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a sequence that reads the same backward as forward.

Example:
Input: "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: "cbbd"
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
        # Create a DP table to store the lengths of longest palindromic subsequences
        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate through substrings of increasing length
        for cl in range(2, n + 1):  # cl = current length
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j]:
                    # If the first and last characters are the same,
                    # the longest palindromic subsequence includes these two characters
                    # and the longest palindromic subsequence of the substring s[i+1:j]
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # If the first and last characters are different,
                    # the longest palindromic subsequence is the maximum of the
                    # longest palindromic subsequences of s[i+1:j+1] and s[i:j]
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1]
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
    assert longest_palindromic_subsequence("pneumonoultramicroscopicsilicovolcanoconiosis") == 15
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()