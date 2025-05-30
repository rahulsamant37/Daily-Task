# Python Question: Find the Longest Palindromic Subsequence
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
def longest_palindromic_subsequence(s):
    """
    Finds the length of the longest palindromic subsequence of a string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store the lengths of longest palindromic subsequences.
    # dp[i][j] will store the length of the longest palindromic subsequence of s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Base case: A single character is a palindrome of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate over the lengths of the substrings, starting from length 2.
    for length in range(2, n + 1):
        # Iterate over the starting indices of the substrings.
        for i in range(n - length + 1):
            # Calculate the ending index of the substring.
            j = i + length - 1

            # If the characters at the start and end of the substring are equal,
            # then the length of the longest palindromic subsequence is 2 plus the
            # length of the longest palindromic subsequence of the substring without
            # these two characters.
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0) # Handle edge case when i+1 > j-1

            # Otherwise, the length of the longest palindromic subsequence is the
            # maximum of the lengths of the longest palindromic subsequences of the
            # substrings without the first or last character.
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the longest palindromic subsequence of the entire string is
    # stored in dp[0][n-1].
    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("aa") == 2
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("abcdefg") == 1
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("") == 0
    assert longest_palindromic_subsequence("agbdba") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()