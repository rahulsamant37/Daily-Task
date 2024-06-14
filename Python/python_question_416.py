# Python Question: Find the Longest Palindromic Substring with k Distinct Characters
'''
Given a string `s` and an integer `k`, find the longest palindromic substring of `s` that contains at most `k` distinct characters.

Example:
Input: s = "abcbca", k = 2
Output: "bcb"

Input: s = "aabbaa", k = 1
Output: "aabbaa"

Input: s = "abcabcbb", k = 2
Output: "bcb"

Input: s = "aaaa", k = 1
Output: "aaaa"

Input: s = "eceba", k = 2
Output: "ece"
'''

# Solution
def longest_palindrome_k_distinct(s, k):
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

            if distinct_chars <= k and substring == substring[::-1]:
                if len(substring) > len(longest_palindrome):
                    longest_palindrome = substring

    return longest_palindrome

# Test cases
def test_longest_palindrome_k_distinct():
    assert longest_palindrome_k_distinct("abcbca", 2) == "bcb"
    assert longest_palindrome_k_distinct("aabbaa", 1) == "aabbaa"
    assert longest_palindrome_k_distinct("abcabcbb", 2) == "bcb"
    assert longest_palindrome_k_distinct("aaaa", 1) == "aaaa"
    assert longest_palindrome_k_distinct("eceba", 2) == "ece"
    assert longest_palindrome_k_distinct("world", 4) == "w"
    assert longest_palindrome_k_distinct("abc", 0) == ""
    assert longest_palindrome_k_distinct("", 2) == ""
    assert longest_palindrome_k_distinct("abacaba", 2) == "abacaba"
    assert longest_palindrome_k_distinct("abacaba", 1) == "aba"
    assert longest_palindrome_k_distinct("tattarrattat", 3) == "tattarrattat"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome_k_distinct()