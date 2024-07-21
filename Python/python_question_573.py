# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.
A palindromic substring is a substring that reads the same backward as forward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (both are valid longest palindromic substrings)

Input: s = "cbbd"
Output: "bb"
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
    n = len(s)
    if n < 2:
        return s  # Empty or single-character string is a palindrome

    longest_palindrome = ""

    # Helper function to expand around the center
    def expand_around_center(left, right):
        """
        Expands outwards from a center point to find the longest palindrome.

        Args:
            left: The left index of the center.
            right: The right index of the center.

        Returns:
            The palindromic substring found.
        """
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Extract the palindrome

    for i in range(n):
        # Odd length palindromes (e.g., "aba")
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1

        # Even length palindromes (e.g., "abba")
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2

    return longest_palindrome

# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("ccc") == "ccc"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()