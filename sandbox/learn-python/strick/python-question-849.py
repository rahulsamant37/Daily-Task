# Python Question: Word Break with Dictionary
'''
Given a string `s` and a dictionary of strings `wordDict`, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words.

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
def solution(s, wordDict):
    """
    Determines if a string can be segmented into words from a dictionary.

    Args:
        s: The input string.
        wordDict: A list of words representing the dictionary.

    Returns:
        True if the string can be segmented, False otherwise.
    """
    n = len(s)
    dp = [False] * (n + 1)  # dp[i] is True if s[:i] can be segmented
    dp[0] = True  # Empty string can be segmented

    for i in range(1, n + 1):
        for j in range(i):
            # Check if s[:j] can be segmented AND s[j:i] is in the dictionary
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break  # No need to check further if we find a valid segmentation

    return dp[n]

# Test cases
def test_solution():
    assert solution("leetcode", ["leet", "code"]) == True
    assert solution("applepenapple", ["apple", "pen"]) == True
    assert solution("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert solution("catsandog", ["cats", "dog", "sand", "and", "cat", "sandog"]) == True
    assert solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == False
    assert solution("a", ["a"]) == True
    assert solution("ab", ["a", "b"]) == True
    assert solution("abc", ["a", "b"]) == False
    assert solution("", ["a", "b"]) == True

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()