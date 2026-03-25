# Python Question: Find the Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.
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
def solution():
    def longest_palindromic_subsequence(s):
        """
        Finds the length of the longest palindromic subsequence of a string.

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

        # Iterate through different lengths of substrings
        for length in range(2, n + 1):
            # Iterate through all possible starting positions for substrings of the current length
            for i in range(n - length + 1):
                j = i + length - 1  # Calculate the ending position of the substring

                # If the characters at the start and end of the substring are equal,
                # then the longest palindromic subsequence is 2 (for the two characters)
                # plus the longest palindromic subsequence of the substring between them
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2 #Handle edge case of length 2 palindrome
                # Otherwise, take the maximum of the longest palindromic subsequences
                # of the substrings without the start character and without the end character
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The result is the length of the longest palindromic subsequence of the entire string
        return dp[0][n - 1]

    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution() # Get the solution function
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("aa") == 2
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("leetcode") == 3
    assert longest_palindromic_subsequence("character") == 5
    assert longest_palindromic_subsequence("abcabcabcabc") == 7
    assert longest_palindromic_subsequence("agbdba") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()