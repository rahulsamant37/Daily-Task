# Python Question: Word Ladder Transformation
'''
Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord` such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the `wordList`.

Return 0 if no such transformation sequence exists.

Note:

*   Return the length of the shortest transformation sequence.
*   All words have the same length.
*   All words contain only lowercase alphabetic characters.
*   You may assume no duplicates in the wordList.
*   You may assume `beginWord` and `endWord` are non-empty and are not the same.

Example:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length.

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log"]

Output: 0

'''

# Solution
from collections import deque

def solution():
    def ladderLength(beginWord, endWord, wordList):
        """
        Finds the length of the shortest transformation sequence from beginWord to endWord.

        Args:
            beginWord (str): The starting word.
            endWord (str): The ending word.
            wordList (list[str]): A list of valid words.

        Returns:
            int: The length of the shortest transformation sequence, or 0 if no such sequence exists.
        """

        if endWord not in wordList:
            return 0

        wordSet = set(wordList)  # Convert to set for faster lookup
        queue = deque([(beginWord, 1)])  # (word, level)
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char_code in range(ord('a'), ord('z') + 1):
                    new_char = chr(char_code)
                    new_word = word[:i] + new_char + word[i+1:]

                    if new_word in wordSet and new_word not in visited:
                        queue.append((new_word, level + 1))
                        visited.add(new_word)

        return 0

    return ladderLength  # Return the inner function

# Test cases
def test_solution():
    ladderLength = solution()

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    expected1 = 5
    assert ladderLength(beginWord1, endWord1, wordList1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {ladderLength(beginWord1, endWord1, wordList1)}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    expected2 = 0
    assert ladderLength(beginWord2, endWord2, wordList2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {ladderLength(beginWord2, endWord2, wordList2)}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    expected3 = 2
    assert ladderLength(beginWord3, endWord3, wordList3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {ladderLength(beginWord3, endWord3, wordList3)}"

    # Test case 4
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","cog","pot","dot"]
    expected4 = 3
    assert ladderLength(beginWord4, endWord4, wordList4) == 3, f"Test Case 4 Failed: Expected {3}, Got {ladderLength(beginWord4, endWord4, wordList4)}"

    # Test case 5
    beginWord5 = "leet"
    endWord5 = "code"
    wordList5 = ["lest","leet","lose","code","lode","robe","lost"]
    expected5 = 6
    assert ladderLength(beginWord5, endWord5, wordList5) == 6, f"Test Case 5 Failed: Expected {6}, Got {ladderLength(beginWord5, endWord5, wordList5)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()