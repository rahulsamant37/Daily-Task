# Python Question: Find the Largest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (both are valid longest palindromic substrings)

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
        Finds the longest palindromic substring in the given string.

        Args:
            s: The input string.

        Returns:
            The longest palindromic substring.
        """

        n = len(s)
        if n < 2:
            return s  # Single character or empty string is a palindrome

        # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise
        dp = [[False] * n for _ in range(n)]

        # Initialize single-character palindromes
        for i in range(n):
            dp[i][i] = True

        # Initialize two-character palindromes
        start = 0  # Starting index of the longest palindrome
        max_len = 1  # Length of the longest palindrome

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check for palindromes of length 3 or greater
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
    assert longestPalindrome("babad") in ["bab", "aba"]
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a"
    assert longestPalindrome("bananas") == "anana"
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("level") == "level"
    assert longestPalindrome("") == ""
    assert longestPalindrome("abcda") == "a"
    assert longestPalindrome("aaaa") == "aaaa"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()