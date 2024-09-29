# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length in `s`.
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
def longest_palindromic_subsequence(s):
    """
    Finds the length of the longest palindromic subsequence in a given string.

    Approach:
    We use dynamic programming to solve this problem.
    Let dp[i][j] be the length of the longest palindromic subsequence of s[i:j+1].
    If s[i] == s[j], then dp[i][j] = dp[i+1][j-1] + 2.
    Otherwise, dp[i][j] = max(dp[i+1][j], dp[i][j-1]).

    Base case:
    dp[i][i] = 1 for all i.

    We iterate through the string from the bottom up, and for each i, we iterate through the string from i+1 to the end.
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base case: single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate through the string from the bottom up
    for i in range(n - 1, -1, -1):
        # Iterate through the string from i+1 to the end
        for j in range(i + 1, n):
            # If the characters at i and j are the same, then the length of the longest palindromic subsequence is 2 + the length of the longest palindromic subsequence of the substring between i+1 and j-1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            # Otherwise, the length of the longest palindromic subsequence is the maximum of the length of the longest palindromic subsequence of the substring between i+1 and j, and the length of the longest palindromic subsequence of the substring between i and j-1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1]
    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("abcabcabcabc") == 4
    assert longest_palindromic_subsequence("character") == 5
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("agbdba") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()