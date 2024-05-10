# Python Question: Word Break Problem with Dictionary
'''
Given a string `s` and a dictionary of words `wordDict`, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: True
Explanation: Return True because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: True
Explanation: Return True because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: False
'''

# Solution
def solution():
    def wordBreak(s, wordDict):
        """
        Determines if a string can be segmented into a space-separated sequence of dictionary words.

        Args:
            s: The input string.
            wordDict: A list of valid words (dictionary).

        Returns:
            True if the string can be segmented, False otherwise.
        """
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] is True if s[:i] can be segmented
        dp[0] = True  # Empty string can always be segmented

        for i in range(1, n + 1):
            for j in range(i):
                # Check if s[:j] can be segmented (dp[j] is True)
                # and if s[j:i] is a valid word in the dictionary
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break  # No need to check other prefixes for this i

        return dp[n]

    return wordBreak

# Test cases
def test_solution():
    wordBreak = solution()

    # Test case 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    assert wordBreak(s1, wordDict1) == True, "Test Case 1 Failed"

    # Test case 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    assert wordBreak(s2, wordDict2) == True, "Test Case 2 Failed"

    # Test case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    assert wordBreak(s3, wordDict3) == False, "Test Case 3 Failed"

    # Test case 4
    s4 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict4 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    assert wordBreak(s4, wordDict4) == False, "Test Case 4 Failed"

    # Test case 5
    s5 = "cars"
    wordDict5 = ["car","ca","rs"]
    assert wordBreak(s5, wordDict5) == True, "Test Case 5 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()