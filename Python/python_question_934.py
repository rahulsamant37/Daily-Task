# Python Question: Find the Largest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a string that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"
'''

# Solution
def solution():
    def longestPalindrome(s: str) -> str:
        """
        Finds the longest palindromic substring in a given string.

        Args:
            s: The input string.

        Returns:
            The longest palindromic substring.
        """

        n = len(s)
        if n < 2:
            return s  # Single character or empty string is a palindrome

        # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise.
        dp = [[False] * n for _ in range(n)]

        # All substrings of length 1 are palindromes.
        for i in range(n):
            dp[i][i] = True

        # Initialize the start and max_len for the longest palindrome found so far.
        start = 0
        max_len = 1

        # Check substrings of length 2.
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check substrings of length 3 or greater.
        for k in range(3, n + 1):  # k is the length of the substring
            for i in range(n - k + 1):  # i is the starting index of the substring
                j = i + k - 1  # j is the ending index of the substring
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if k > max_len:
                        start = i
                        max_len = k

        return s[start:start + max_len]

    return longestPalindrome

# Test cases
def test_solution():
    longestPalindrome = solution()

    assert longestPalindrome("babad") in ("bab", "aba")
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a"
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("bananas") == "anana"
    assert longestPalindrome("") == ""
    assert longestPalindrome("ababa") == "ababa"
    assert longestPalindrome("abba") == "abba"
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()