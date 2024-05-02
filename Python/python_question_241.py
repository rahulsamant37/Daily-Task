# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.
A palindromic substring is a string that reads the same backward as forward.

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
    Finds the longest palindromic substring in a given string s.

    Args:
        s (str): The input string.

    Returns:
        str: The longest palindromic substring.
    """
    if not s:
        return ""

    n = len(s)
    longest = ""

    # Helper function to expand around the center
    def expand_around_center(left, right):
        """
        Expands outwards from a center point to find the largest palindrome.

        Args:
            left (int): The left index of the center.
            right (int): The right index of the center.

        Returns:
            str: The palindromic substring found.
        """
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Return the palindrome

    # Iterate through each character as a potential center
    for i in range(n):
        # Odd length palindromes
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1

        # Even length palindromes
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
    assert longest_palindrome("") == ""
    assert longest_palindrome("bananas") == "anana"
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome()