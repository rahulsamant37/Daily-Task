# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

A palindromic substring is a string that reads the same forwards and backward.

Example:
Input: "babad"
Output: "bab" or "aba" (either is acceptable)

Input: "cbbd"
Output: "bb"

Input: "a"
Output: "a"

Input: "ac"
Output: "a"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """
    if not s:
        return ""

    n = len(s)
    longest = ""

    # Helper function to expand around the center
    def expand_around_center(left, right):
        """
        Expands around the center to find the longest palindrome.

        Args:
            left: The left index.
            right: The right index.

        Returns:
            The palindromic substring.
        """
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # Iterate through each character as a potential center
    for i in range(n):
        # Odd length palindromes (e.g., "aba")
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1

        # Even length palindromes (e.g., "abba")
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

# Test cases
def test_longest_palindrome():
    """
    Tests the longest_palindrome function with various test cases.
    """
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("") == ""
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("aaaa") == "aaaa"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()