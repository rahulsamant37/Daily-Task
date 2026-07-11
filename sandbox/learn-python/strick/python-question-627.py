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
def solution():
    def longestPalindromeSubseq(s: str) -> int:
        """
        Calculates the length of the longest palindromic subsequence in a given string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)
        # Create a DP table to store the lengths of palindromic subsequences.
        # dp[i][j] stores the length of the longest palindromic subsequence in s[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Base case: A single character is a palindrome of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate over the lengths of the substrings.
        for length in range(2, n + 1):
            # Iterate over the starting indices of the substrings.
            for i in range(n - length + 1):
                # Calculate the ending index of the substring.
                j = i + length - 1

                # If the characters at the start and end of the substring are equal,
                # then the length of the longest palindromic subsequence is 2 plus
                # the length of the longest palindromic subsequence of the substring
                # excluding the start and end characters.
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                # Otherwise, the length of the longest palindromic subsequence is the
                # maximum of the lengths of the longest palindromic subsequences of the
                # substrings excluding the start and end characters, respectively.
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1].
        return dp[0][n - 1]
    
    return longestPalindromeSubseq

# Test cases
def test_solution():
    test_cases = [
        ("bbbab", 4),
        ("cbbd", 2),
        ("a", 1),
        ("ac", 1),
        ("aba", 3),
        ("racecar", 7),
        ("leetcode", 1),
        ("character", 3),
        ("abcabcabcabc", 7),
        ("", 0)
    ]
    
    longestPalindromeSubseq = solution()
    
    for s, expected in test_cases:
        result = longestPalindromeSubseq(s)
        print(f"Input: {s}, Expected: {expected}, Result: {result}")
        assert result == expected, f"Test failed for input {s}. Expected {expected}, got {result}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()