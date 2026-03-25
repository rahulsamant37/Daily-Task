# Python Question: Longest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence.
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
def longest_palindromic_subsequence_length(s):
    """
    Calculates the length of the longest palindromic subsequence of a given string.

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
        # Iterate through starting indices of substrings
        for i in range(n - length + 1):
            j = i + length - 1  # Ending index of the substring

            # If the characters at the ends of the substring match
            if s[i] == s[j]:
                # Then the length of the longest palindromic subsequence is 2 + the length of the longest palindromic subsequence of the substring without these end characters
                dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2  #Handle edge case where i+1 == j
            else:
                # Otherwise, the length of the longest palindromic subsequence is the maximum of the lengths of the longest palindromic subsequences of the substrings excluding either the first or the last character
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The result is stored in dp[0][n-1]
    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence_length():
    assert longest_palindromic_subsequence_length("bbbab") == 4
    assert longest_palindromic_subsequence_length("cbbd") == 2
    assert longest_palindromic_subsequence_length("a") == 1
    assert longest_palindromic_subsequence_length("aa") == 2
    assert longest_palindromic_subsequence_length("aba") == 3
    assert longest_palindromic_subsequence_length("racecar") == 7
    assert longest_palindromic_subsequence_length("leetcode") == 3
    assert longest_palindromic_subsequence_length("") == 0
    assert longest_palindromic_subsequence_length("abcabcabcabc") == 4
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence_length()