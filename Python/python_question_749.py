# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A palindrome is a string that reads the same backward as forward.

Example:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

# Solution
def solution():
    def longest_palindromic_subsequence(s):
        """
        Finds the length of the longest palindromic subsequence in a given string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)

        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate through different lengths of substrings
        for length in range(2, n + 1):
            # Iterate through the starting indices of substrings
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of the substring

                # If the characters at the start and end are the same
                if s[i] == s[j]:
                    # Then the longest palindromic subsequence length is
                    # 2 (for the two matching characters) + the length of the
                    # longest palindromic subsequence of the substring between them
                    dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2
                else:
                    # Otherwise, the longest palindromic subsequence length is the maximum of
                    # the lengths of the longest palindromic subsequences of the substrings
                    # formed by excluding either the start or the end character
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The result is stored in dp[0][n-1]
        return dp[0][n - 1]
    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    assert longest_palindromic_subsequence(s1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longest_palindromic_subsequence(s1)}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    assert longest_palindromic_subsequence(s2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longest_palindromic_subsequence(s2)}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    assert longest_palindromic_subsequence(s3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {longest_palindromic_subsequence(s3)}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    assert longest_palindromic_subsequence(s4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {longest_palindromic_subsequence(s4)}"
    
    # Test case 5
    s5 = "character"
    expected5 = 5
    assert longest_palindromic_subsequence(s5) == 5, f"Test Case 5 Failed: Expected {expected5}, got {longest_palindromic_subsequence(s5)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()