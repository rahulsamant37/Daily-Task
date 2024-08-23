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
    longest = ""

    # Helper function to expand around the center
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Return the palindrome found

    for i in range(n):
        # Odd length palindromes: expand around a single character
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1

        # Even length palindromes: expand around two characters
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("abcda") == "a"
    assert longest_palindrome("abacab") == "bacab"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()