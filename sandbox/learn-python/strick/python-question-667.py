# Python Question:  Find the Longest Palindromic Substring with K Distinct Characters
'''
Given a string 's' and an integer 'k', find the longest palindromic substring of 's' that contains at most 'k' distinct characters. If no such substring exists, return an empty string.

Example:
Input: s = "abcbaba", k = 2
Output: "abcbaba"

Input: s = "abcabcbb", k = 2
Output: "bcb"

Input: s = "aaaa", k = 1
Output: "aaaa"
'''

# Solution
def longest_palindrome_with_k_distinct(s, k):
    """
    Finds the longest palindromic substring of s with at most k distinct characters.

    Args:
        s: The input string.
        k: The maximum number of distinct characters allowed in the palindrome.

    Returns:
        The longest palindromic substring with at most k distinct characters.
    """

    n = len(s)
    if n == 0 or k == 0:
        return ""

    longest_palindrome = ""

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # Check if the substring has at most k distinct characters
                distinct_chars = len(set(substring))
                if distinct_chars <= k:
                    # Update the longest palindrome if the current substring is longer
                    if len(substring) > len(longest_palindrome):
                        longest_palindrome = substring

    return longest_palindrome

# Test cases
def test_solution():
    assert longest_palindrome_with_k_distinct("abcbaba", 2) == "abcbaba"
    assert longest_palindrome_with_k_distinct("abcabcbb", 2) == "bcb"
    assert longest_palindrome_with_k_distinct("aaaa", 1) == "aaaa"
    assert longest_palindrome_with_k_distinct("abac", 1) == "a"
    assert longest_palindrome_with_k_distinct("abac", 2) == "aba"
    assert longest_palindrome_with_k_distinct("abac", 3) == "abac"
    assert longest_palindrome_with_k_distinct("", 2) == ""
    assert longest_palindrome_with_k_distinct("a", 1) == "a"
    assert longest_palindrome_with_k_distinct("a", 0) == ""
    assert longest_palindrome_with_k_distinct("aabbcc", 1) == "aa"
    assert longest_palindrome_with_k_distinct("aabbcc", 2) == "bb"
    assert longest_palindrome_with_k_distinct("aabbcc", 3) == "aabbcc"
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()