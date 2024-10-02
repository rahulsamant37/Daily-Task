# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

A palindrome is a string that reads the same backward as forward.

Example:
Input: "babad"
Output: "bab" or "aba"

Input: "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring within a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
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
            The palindromic substring found by expanding around the center.
        """
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Extract substring excluding the mismatched characters

    for i in range(n):
        # Odd length palindromes: Expand around a single character
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1

        # Even length palindromes: Expand around two characters
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2

    return longest_palindrome

# Test cases
def test_longest_palindrome():
    """
    Tests the longest_palindrome function with various test cases.
    """
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("bb") == "bb"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("racecar") == "racecar"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()