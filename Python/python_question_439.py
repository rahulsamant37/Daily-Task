# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

A palindrome is a string that reads the same backward as forward.

Example:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring within a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring found within the input string.
    """

    n = len(s)
    if n < 2:
        return s  # A string of length 0 or 1 is a palindrome

    longest = ""

    # Helper function to expand around the center
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Return the palindromic substring

    for i in range(n):
        # Odd length palindromes, centered at i
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1

        # Even length palindromes, centered between i and i+1
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaaaaaaaa") == "aaaaaaaaaa"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()