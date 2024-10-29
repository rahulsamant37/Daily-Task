# Python Question: Longest Palindromic Subsequence Length
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
def longest_palindromic_subsequence_length(s):
    """
    Calculates the length of the longest palindromic subsequence in the given string.

    The approach uses dynamic programming.  We create a 2D table `dp` where `dp[i][j]` stores
    the length of the longest palindromic subsequence of the substring `s[i:j+1]`.

    Base case:
    - `dp[i][i] = 1` for all `i` (a single character is a palindrome of length 1).

    Recursive relation:
    - If `s[i] == s[j]`:  `dp[i][j] = dp[i+1][j-1] + 2` (extend the palindrome by including both characters)
    - If `s[i] != s[j]`:  `dp[i][j] = max(dp[i+1][j], dp[i][j-1])` (take the maximum length from either excluding `s[i]` or `s[j]`)

    The final result is stored in `dp[0][n-1]`, where `n` is the length of the string.
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table diagonally
    for cl in range(2, n + 1): # cl is the current length of the substring
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                if cl == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

# Test cases
def test_solution():
    assert longest_palindromic_subsequence_length("bbbab") == 4
    assert longest_palindromic_subsequence_length("cbbd") == 2
    assert longest_palindromic_subsequence_length("a") == 1
    assert longest_palindromic_subsequence_length("aa") == 2
    assert longest_palindromic_subsequence_length("aba") == 3
    assert longest_palindromic_subsequence_length("character") == 5
    assert longest_palindromic_subsequence_length("leetcode") == 3
    assert longest_palindromic_subsequence_length("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()