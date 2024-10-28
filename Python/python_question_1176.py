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
    # Function to find the length of the longest palindromic subsequence
    def longest_palindromic_subsequence(s):
        n = len(s)
        # Create a DP table to store the lengths of LPS for substrings
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate through substrings of increasing length
        for cl in range(2, n + 1):  # cl is the current length of substring
            for i in range(n - cl + 1):
                j = i + cl - 1  # j is the end index of the substring
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2  # If ends match, add 2 to inner LPS length
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])  # Else, take max of excluding either end

        return dp[0][n-1]  # Result is the LPS length for the entire string

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
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()