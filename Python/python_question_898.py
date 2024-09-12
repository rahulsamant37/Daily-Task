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
    Finds the length of the longest palindromic subsequence in a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a DP table to store the lengths of longest palindromic subsequences
    # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate through substrings of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # If the characters at the ends are equal, then the longest palindromic subsequence
            # is the longest palindromic subsequence of the substring without these characters, plus 2
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                # Otherwise, the longest palindromic subsequence is the maximum of the longest palindromic
                # subsequences of the substrings excluding either the first or the last character
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    # The result is stored in dp[0][n-1], which represents the longest palindromic subsequence of the entire string
    return dp[0][n-1]

# Test cases
def test_longest_palindrome_subsequence():
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("") == 0
    assert longest_palindrome_subsequence("aba") == 3
    assert longest_palindrome_subsequence("abcabcabcabc") == 4
    assert longest_palindrome_subsequence("aaaaaaaa") == 8
    assert longest_palindrome_subsequence("abcdefgh") == 1
    assert longest_palindrome_subsequence("racecar") == 7
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome_subsequence()