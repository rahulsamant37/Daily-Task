# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a sequence that reads the same backward as forward.

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
    Calculates the length of the longest palindromic subsequence of a given string.

    Args:
    s (str): The input string.

    Returns:
    int: The length of the longest palindromic subsequence.
    """
    n = len(s)

    # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate through substrings of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # If the characters at the ends match, the LPS length is 2 + LPS of the inner substring
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            # Otherwise, the LPS length is the maximum of the LPS lengths of the two smaller substrings
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The result is the LPS length of the entire string
    return dp[0][n - 1]

# Test cases
def test_longest_palindrome_subsequence():
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("ac") == 1
    assert longest_palindrome_subsequence("aba") == 3
    assert longest_palindrome_subsequence("bananas") == 5
    assert longest_palindrome_subsequence("character") == 5
    assert longest_palindrome_subsequence("racecar") == 7

    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome_subsequence()