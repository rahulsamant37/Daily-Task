# Python Question: Word Break with Dynamic Programming
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
def word_break(s, wordDict):
    """
    Determines if a string can be segmented into a space-separated sequence of words from a dictionary.

    Args:
        s: The input string.
        wordDict: A list of strings representing the dictionary.

    Returns:
        True if the string can be segmented, False otherwise.
    """
    n = len(s)
    dp = [False] * (n + 1)  # dp[i] is True if s[:i] can be segmented
    dp[0] = True  # Empty string can always be segmented

    # Iterate through all possible lengths of substrings
    for i in range(1, n + 1):
        # Iterate through all possible starting positions of the substring
        for j in range(i):
            # If s[:j] can be segmented and the substring s[j:i] is in the dictionary
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True  # Then s[:i] can be segmented
                break  # No need to check other starting positions for this length

    return dp[n]  # Return whether the entire string s can be segmented

# Test cases
def test_word_break():
    assert word_break("leetcode", ["leet", "code"]) == True
    assert word_break("applepenapple", ["apple", "pen"]) == True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert word_break("cars", ["car", "ca", "rs"]) == True
    assert word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == False
    assert word_break("", []) == True
    assert word_break("a", ["a"]) == True
    assert word_break("ab", ["a"]) == False
    print("All test cases passed!")

if __name__ == "__main__":
    test_word_break()