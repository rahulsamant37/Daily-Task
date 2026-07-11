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
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    The approach used is dynamic programming. We create a 2D boolean array
    'dp' where dp[i][j] is True if the substring s[i:j+1] is a palindrome,
    and False otherwise.

    We iterate through the string and fill the dp array.  The base cases are
    single characters (length 1) and pairs of characters (length 2).  Then,
    for substrings of length greater than 2, we check if the outer characters
    match and if the inner substring is also a palindrome.

    We keep track of the start index and maximum length of the longest
    palindrome found so far.
    """

    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # Base case: Single character palindromes
    for i in range(n):
        dp[i][i] = True

    # Base case: Two character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for palindromes of length greater than 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_len:
                    start = i
                    max_len = k

    return s[start:start + max_len]


# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("level") == "level"
    assert longest_palindrome("noon") == "noon"
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaaa") == "aaaaa"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()