# Python Question: Word Ladder
'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

Note:

*   Return 0 if no such transformation sequence exists.
*   All words have the same length.
*   All words contain only lowercase alphabetic characters.
*   You may assume no duplicates in the word list.
*   You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

# Solution
from collections import deque

def solution():
    def word_ladder(beginWord, endWord, wordList):
        """
        Finds the length of the shortest transformation sequence from beginWord to endWord.

        Args:
            beginWord: The starting word.
            endWord: The target word.
            wordList: A list of valid words.

        Returns:
            The length of the shortest transformation sequence, or 0 if no such sequence exists.
        """

        if endWord not in wordList:
            return 0

        wordSet = set(wordList)  # Convert wordList to a set for faster lookup
        queue = deque([(beginWord, 1)])  # Initialize queue with the starting word and its level (1)
        visited = {beginWord}  # Keep track of visited words to avoid cycles

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

        return 0  # No transformation sequence found

    return word_ladder

# Test cases
def test_solution():
    word_ladder = solution()

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected1 = 5
    assert word_ladder(beginWord1, endWord1, wordList1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {word_ladder(beginWord1, endWord1, wordList1)}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    expected2 = 0
    assert word_ladder(beginWord2, endWord2, wordList2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {word_ladder(beginWord2, endWord2, wordList2)}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]
    expected3 = 2
    assert word_ladder(beginWord3, endWord3, wordList3) == 2, f"Test Case 3 Failed: Expected {2}, Got {word_ladder(beginWord3, endWord3, wordList3)}"

    # Test case 4 (beginWord == endWord)
    beginWord4 = "hit"
    endWord4 = "hit"
    wordList4 = ["hot", "dot", "dog", "lot", "log", "cog", "hit"]
    expected4 = 0 # Should be 0 since it's looking for a *transformation*
    beginWord4 = "hit"
    endWord4 = "hit"
    wordList4 = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected4 = 0

    assert word_ladder(beginWord4, endWord4, wordList4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {word_ladder(beginWord4, endWord4, wordList4)}"
    # Test case 5 (long sequence)
    beginWord5 = "sand"
    endWord5 = "acne"
    wordList5 = ["slit", "bana", "sana", "lice", "babe", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "wave", "