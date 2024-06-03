# Python Question: Word Break with Dictionary

'''
Given a string `s` and a dictionary of strings `wordDict`, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: True
Explanation: Return True because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: True
Explanation: Return True because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: False
'''

# Solution
def solution(s, wordDict):
    """
    Determines if a string can be segmented into a space-separated sequence of words from a dictionary.

    Args:
        s: The input string.
        wordDict: A list of strings representing the dictionary.

    Returns:
        True if the string can be segmented, False otherwise.
    """

    # Create a set for faster word lookup.
    word_set = set(wordDict)

    # dp[i] is True if s[:i] can be segmented, False otherwise.
    dp = [False] * (len(s) + 1)

    # An empty string can always be segmented.
    dp[0] = True

    # Iterate through the string, building up the dp table.
    for i in range(1, len(s) + 1):
        # Check all possible prefixes ending at index i.
        for j in range(i):
            # If the prefix s[:j] can be segmented and the substring s[j:i] is in the dictionary,
            # then s[:i] can be segmented.
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # No need to check further prefixes for this i

    # The result is stored in dp[len(s)].
    return dp[len(s)]

# Test cases
def test_solution():
    assert solution("leetcode", ["leet", "code"]) == True
    assert solution("applepenapple", ["apple", "pen"]) == True
    assert solution("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert solution("aaaaaaa", ["aaaa","aaa"]) == True
    assert solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == False
    assert solution("", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == True
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()