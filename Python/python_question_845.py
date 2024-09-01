# Python Question: Word Ladder
'''
Given two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the wordList.

Return 0 if no such transformation sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

# Solution
from collections import deque

def solution(beginWord, endWord, wordList):
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

    wordList = set(wordList)  # Convert to set for faster lookups
    queue = deque([(beginWord, 1)])  # Queue to store (word, level) pairs
    visited = {beginWord}  # Set to keep track of visited words

    while queue:
        word, level = queue.popleft()

        if word == endWord:
            return level

        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i + 1:]

                if new_word in wordList and new_word not in visited:
                    queue.append((new_word, level + 1))
                    visited.add(new_word)

    return 0  # No transformation sequence found

# Test cases
def test_solution():
    assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert solution("hot", "dog", ["hot","dog","dot"]) == 3
    assert solution("a", "c", ["a","b","c"]) == 2
    assert solution("sand", "acne", ["sand","acnd","acne","sand"]) == 0
    assert solution("sand", "acne", ["sand","acnd","acne","sand","cand","send","sane"]) == 0

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()