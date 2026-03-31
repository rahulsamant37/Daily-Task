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

    # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate through lengths of substrings
    for length in range(2, n + 1):
        # Iterate through starting indices
        for i in range(n - length + 1):
            j = i + length - 1  # Ending index of substring

            # If the characters at the ends of the substring are equal,
            # the length of the LPS is 2 + LPS of the substring without those characters
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            # Otherwise, the length of the LPS is the maximum of the LPS of the
            # substring without the first character and the LPS of the substring
            # without the last character
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the LPS of the entire string is stored in dp[0][n-1]
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
    assert longest_palindrome_subsequence("abcdefgh") == 1
    assert longest_palindrome_subsequence("racecar") == 7
    assert longest_palindrome_subsequence("") == 0

    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome_subsequence()