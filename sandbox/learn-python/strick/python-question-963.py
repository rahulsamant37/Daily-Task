# Python Question: Word Break Problem with Memoization
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
def solution():
    def word_break(s: str, wordDict: list[str]) -> bool:
        """
        Determines if a string can be segmented into a space-separated sequence of words from a dictionary.

        Args:
            s: The string to be segmented.
            wordDict: A list of valid words.

        Returns:
            True if the string can be segmented, False otherwise.
        """
        word_set = set(wordDict)  # Convert list to set for faster lookup
        memo = {}  # Use memoization to store results of subproblems

        def can_break(start_index: int) -> bool:
            """
            Recursively checks if the substring starting at start_index can be broken into words.

            Args:
                start_index: The starting index of the substring.

            Returns:
                True if the substring can be broken, False otherwise.
            """
            if start_index == len(s):
                return True  # Base case: Reached the end of the string

            if start_index in memo:
                return memo[start_index]  # Return memoized result

            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]
                if word in word_set and can_break(end_index):
                    memo[start_index] = True  # Memoize the result
                    return True

            memo[start_index] = False  # Memoize the result
            return False

        return can_break(0)

    return word_break

# Test cases
def test_solution():
    word_break = solution()
    # Test case 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    assert word_break(s1, wordDict1) == True

    # Test case 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    assert word_break(s2, wordDict2) == True

    # Test case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    assert word_break(s3, wordDict3) == False

    # Test case 4
    s4 = "aaaaaaa"
    wordDict4 = ["aaaa", "aaa"]
    assert word_break(s4, wordDict4) == True

    # Test case 5
    s5 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict5 = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    assert word_break(s5, wordDict5) == False

    # Test case 6
    s6 = "cars"
    wordDict6 = ["car","ca","rs"]
    assert word_break(s6, wordDict6) == True

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()