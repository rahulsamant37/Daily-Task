# Python Question: Find the Longest Common Subsequence (LCS) of Three Strings
'''
Given three strings, `str1`, `str2`, and `str3`, find the length of the longest common subsequence (LCS) present in all three strings.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example:
Input: str1 = "geeks", str2 = "geeksforgeeks", str3 = "geeksforgeeks"
Output: 5 (The longest common subsequence is "geeks")

Input: str1 = "abcd", str2 = "efgh", str3 = "ijkl"
Output: 0 (There is no common subsequence)

Input: str1 = "abc", str2 = "abc", str3 = "abc"
Output: 3 ("abc" is the longest common subsequence)
'''

# Solution
def solution():
    def lcs_three_strings(str1, str2, str3):
        """
        Finds the length of the longest common subsequence of three strings.

        Args:
            str1: The first string.
            str2: The second string.
            str3: The third string.

        Returns:
            The length of the longest common subsequence.
        """

        n1 = len(str1)
        n2 = len(str2)
        n3 = len(str3)

        # Create a 3D DP table to store lengths of LCS
        dp = [[[0 for _ in range(n3 + 1)] for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        # Iterate through the strings to populate the DP table
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                for k in range(1, n3 + 1):
                    # If characters match, increment the LCS length
                    if str1[i - 1] == str2[j - 1] == str3[k - 1]:
                        dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                    # Otherwise, take the maximum LCS length from previous states
                    else:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

        # The result is stored in the bottom-rightmost cell of the DP table
        return dp[n1][n2][n3]

    return lcs_three_strings
# Test cases
def test_solution():
    lcs_three_strings = solution()

    # Test case 1
    str1 = "geeks"
    str2 = "geeksforgeeks"
    str3 = "geeksforgeeks"
    expected_output = 5
    assert lcs_three_strings(str1, str2, str3) == expected_output, f"Test Case 1 Failed: Expected {expected_output}, Got {lcs_three_strings(str1, str2, str3)}"

    # Test case 2
    str1 = "abcd"
    str2 = "efgh"
    str3 = "ijkl"
    expected_output = 0
    assert lcs_three_strings(str1, str2, str3) == expected_output, f"Test Case 2 Failed: Expected {expected_output}, Got {lcs_three_strings(str1, str2, str3)}"

    # Test case 3
    str1 = "abc"
    str2 = "abc"
    str3 = "abc"
    expected_output = 3
    assert lcs_three_strings(str1, str2, str3) == expected_output, f"Test Case 3 Failed: Expected {expected_output}, Got {lcs_three_strings(str1, str2, str3)}"

    # Test case 4
    str1 = "apple"
    str2 = "pineapple"
    str3 = "applause"
    expected_output = 4
    assert lcs_three_strings(str1, str2, str3) == 4, f"Test Case 4 Failed: Expected 4, Got {lcs_three_strings(str1, str2, str3)}"

    # Test case 5
    str1 = "AGGT12"
    str2 = "12TXAYB"
    str3 = "12XAZ"
    expected_output = 2
    assert lcs_three_strings(str1, str2, str3) == expected_output, f"Test Case 5 Failed: Expected {expected_output}, Got {lcs_three_strings(str1, str2, str3)}"

    # Test case 6: Empty strings
    str1 = ""
    str2 = ""
    str3 = ""
    expected_output = 0
    assert lcs_three_strings(str1, str2, str3) == expected_output, f"Test Case 6 Failed: Expected {expected_output}, Got {lcs_three_strings(str1, str2, str3)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()