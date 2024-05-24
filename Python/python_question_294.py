# Python Question: Word Ladder Transformation
'''
Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the `wordList`.

Return 0 if no such transformation sequence exists.

Note:

*   Return the length of the shortest transformation sequence as an integer.
*   All words have the same length.
*   All words contain only lowercase alphabetic characters.
*   You may assume no duplicates in the wordList.
*   `beginWord` and `endWord` are non-empty and are not the same.

Example:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

# Solution
from collections import deque

def ladderLength(beginWord, endWord, wordList):
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

    wordList = set(wordList)  # Convert to set for faster lookup
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

                if new_word in wordList and new_word not in visited:
                    queue.append((new_word, level + 1))
                    visited.add(new_word)

    return 0

# Test cases
def test_solution():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    assert ladderLength(beginWord, endWord, wordList) == 5

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    assert ladderLength(beginWord, endWord, wordList) == 0

    beginWord = "a"
    endWord = "c"
    wordList = ["a","b","c"]
    assert ladderLength(beginWord, endWord, wordList) == 2

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot","dog"]
    assert ladderLength(beginWord, endWord, wordList) == 0

    beginWord = "leet"
    endWord = "code"
    wordList = ["lest","leet","lose","code","lode","robe","lost"]
    assert ladderLength(beginWord, endWord, wordList) == 6

if __name__ == "__main__":
    test_solution()