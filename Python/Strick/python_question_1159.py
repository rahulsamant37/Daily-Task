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
def longest_palindrome_subsequence(s):
    """
    Calculates the length of the longest palindromic subsequence in the given string.

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
    for cl in range(2, n + 1):  # cl is the length of the substring
        for i in range(n - cl + 1):
            j = i + cl - 1  # j is the ending index of the substring

            # If the characters at the ends of the substring match
            if s[i] == s[j]:
                # The length of the longest palindromic subsequence is 2 + the length of the longest palindromic subsequence of the substring without the end characters
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                # The length of the longest palindromic subsequence is the maximum of the lengths of the longest palindromic subsequences of the substrings without the first character and without the last character
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1]
    return dp[0][n - 1]

# Test cases
def test_longest_palindrome_subsequence():
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("aa") == 2
    assert longest_palindrome_subsequence("aba") == 3
    assert longest_palindrome_subsequence("racecar") == 7
    assert longest_palindrome_subsequence("leetcode") == 3
    assert longest_palindrome_subsequence("") == 0
    assert longest_palindrome_subsequence("abcabcabcabc") == 4

    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome_subsequence()