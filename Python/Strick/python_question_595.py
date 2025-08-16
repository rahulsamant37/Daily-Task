# Python Question: Longest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
A palindrome is a sequence that reads the same backward as forward.

Example:
Input: "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

# Solution
def longest_palindrome_subsequence_length(s):
    """
    Calculates the length of the longest palindromic subsequence of a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.

    Approach:
    This solution uses dynamic programming. We create a 2D table `dp` where `dp[i][j]`
    stores the length of the longest palindromic subsequence of the substring `s[i:j+1]`.

    The base cases are:
    - `dp[i][i] = 1` for all i (a single character is a palindrome of length 1).

    The recursive relation is:
    - If `s[i] == s[j]`, then `dp[i][j] = dp[i+1][j-1] + 2` (we can extend the palindrome by 2).
    - Otherwise, `dp[i][j] = max(dp[i+1][j], dp[i][j-1])` (we take the maximum length from either excluding
      the first or the last character).
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base cases: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate over increasing lengths of substrings
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

# Test cases
def test_solution():
    assert longest_palindrome_subsequence_length("bbbab") == 4
    assert longest_palindrome_subsequence_length("cbbd") == 2
    assert longest_palindrome_subsequence_length("a") == 1
    assert longest_palindrome_subsequence_length("ac") == 1
    assert longest_palindrome_subsequence_length("aba") == 3
    assert longest_palindrome_subsequence_length("racecar") == 7
    assert longest_palindrome_subsequence_length("") == 0
    assert longest_palindrome_subsequence_length("abcabcabcabc") == 7 # "abcabca" or "bcabcab"
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()