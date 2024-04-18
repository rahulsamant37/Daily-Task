# Python Question: Find the Longest Palindromic Substring with K Distinct Characters
'''
Given a string `s` and an integer `k`, find the longest palindromic substring of `s` that contains at most `k` distinct characters.

Example:
Input: s = "abcba", k = 2
Output: "abcba"

Input: s = "abcbab", k = 2
Output: "bcb"

Input: s = "aabba", k = 1
Output: "aa"
'''

# Solution
def longest_palindrome_with_k_distinct(s, k):
    """
    Finds the longest palindromic substring of s with at most k distinct characters.

    Args:
        s: The input string.
        k: The maximum number of distinct characters allowed in the palindrome.

    Returns:
        The longest palindromic substring of s with at most k distinct characters.
    """

    n = len(s)
    if n == 0 or k == 0:
        return ""

    longest_palindrome = ""

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            distinct_chars = len(set(substring))

            # Check if the substring is a palindrome and has at most k distinct characters
            if substring == substring[::-1] and distinct_chars <= k:
                if len(substring) > len(longest_palindrome):
                    longest_palindrome = substring

    return longest_palindrome

# Test cases
def test_solution():
    assert longest_palindrome_with_k_distinct("abcba", 2) == "abcba"
    assert longest_palindrome_with_k_distinct("abcbab", 2) == "bcb"
    assert longest_palindrome_with_k_distinct("aabba", 1) == "aa"
    assert longest_palindrome_with_k_distinct("aaaa", 1) == "aaaa"
    assert longest_palindrome_with_k_distinct("abc", 1) == "a" or longest_palindrome_with_k_distinct("abc", 1) == "b" or longest_palindrome_with_k_distinct("abc", 1) == "c"
    assert longest_palindrome_with_k_distinct("aabbcc", 2) == "bb" or longest_palindrome_with_k_distinct("aabbcc", 2) == "aa" or longest_palindrome_with_k_distinct("cc" ,2) == "cc"
    assert longest_palindrome_with_k_distinct("", 2) == ""
    assert longest_palindrome_with_k_distinct("aba", 0) == ""
    assert longest_palindrome_with_k_distinct("aabbccddeeff", 3) in ["aa", "bb", "cc", "dd", "ee", "ff"]
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()