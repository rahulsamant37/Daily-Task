# Python Question: Find the Largest Palindromic Subsequence

'''
Given a string `s`, find the length of the longest palindromic subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a string that reads the same forwards and backward.

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

        # Create a DP table to store the lengths of the longest palindromic subsequences.
        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate over the lengths of the subsequences.
        for length in range(2, n + 1):
            # Iterate over the starting indices of the subsequences.
            for i in range(n - length + 1):
                # Calculate the ending index of the subsequence.
                j = i + length - 1

                # If the characters at the start and end of the subsequence are equal,
                # then the length of the longest palindromic subsequence is 2 plus the
                # length of the longest palindromic subsequence of the substring without
                # these two characters.
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # Otherwise, the length of the longest palindromic subsequence is the
                # maximum of the lengths of the longest palindromic subsequences of the
                # two substrings obtained by removing either the first or the last character.
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The length of the longest palindromic subsequence of the entire string is stored
        # in dp[0][n-1].
        return dp[0][n - 1]
    
    return longest_palindromic_subsequence

# Test cases
def test_solution():
    lps = solution()
    assert lps("bbbab") == 4
    assert lps("cbbd") == 2
    assert lps("a") == 1
    assert lps("ac") == 1
    assert lps("aba") == 3
    assert lps("racecar") == 7
    assert lps("leetcode") == 3
    assert lps("character") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()