# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"
Output: "bab" or "aba"

Input: "cbbd"
Output: "bb"
'''

# Solution
def longestPalindrome(s):
    """
    Finds the longest palindromic substring in the given string s.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring in s.
    """
    if not s:
        return ""

    n = len(s)
    longest_palindrome = ""

    # Helper function to expand around the center
    def expand_around_center(left, right):
        """
        Expands around the center (left, right) to find the longest palindrome.

        Args:
            left: The left index.
            right: The right index.

        Returns:
            The longest palindrome centered at (left, right).
        """
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # Iterate through each character as a potential center
    for i in range(n):
        # Odd length palindromes
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1

        # Even length palindromes
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2

    return longest_palindrome

# Test cases
def test_longestPalindrome():
    assert longestPalindrome("babad") in ("bab", "aba")
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a"
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("") == ""
    assert longestPalindrome("bananas") == "anana"
    assert longestPalindrome("aaaaaaaaa") == "aaaaaaaaa"
    print("All test cases passed")

if __name__ == "__main__":
    test_longestPalindrome()