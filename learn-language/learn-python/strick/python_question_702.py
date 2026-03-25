# Python Question: Find the Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
A palindrome is a sequence that reads the same backward as forward.

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
        Finds the length of the longest palindromic subsequence of a string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)
        # Create a DP table to store the lengths of the longest palindromic subsequences
        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Base case: Single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate over substrings of increasing length
        for cl in range(2, n + 1):  # cl: current length
            for i in range(n - cl + 1): # i: starting index
                j = i + cl - 1 # j: ending index

                # If the characters at the start and end of the substring match
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2 # Extend the palindrome by 2
                else:
                    # Otherwise, take the maximum of the longest palindromic subsequences
                    # of the substrings excluding the start and end characters respectively
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1]
        return dp[0][n-1]
    
    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    assert longest_palindromic_subsequence(s1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {longest_palindromic_subsequence(s1)}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    assert longest_palindromic_subsequence(s2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {longest_palindromic_subsequence(s2)}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    assert longest_palindromic_subsequence(s3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {longest_palindromic_subsequence(s3)}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    assert longest_palindromic_subsequence(s4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {longest_palindromic_subsequence(s4)}"

    # Test case 5
    s5 = "character"
    expected5 = 5
    assert longest_palindromic_subsequence(s5) == 5, f"Test Case 5 Failed: Expected {5}, Got {longest_palindromic_subsequence(s5)}"
    
    # Test case 6
    s6 = "racecar"
    expected6 = 7
    assert longest_palindromic_subsequence(s6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {longest_palindromic_subsequence(s6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()