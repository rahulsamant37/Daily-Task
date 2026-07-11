# Python Question: Word Ladder
'''
Given two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the wordList.

Return 0 if no such transformation sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
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
        endWord: The ending word.
        wordList: A list of valid words.

    Returns:
        The length of the shortest transformation sequence, or 0 if no such sequence exists.
    """

    if endWord not in wordList:
        return 0

    wordList = set(wordList)  # Convert to set for faster lookup
    queue = deque([(beginWord, 1)])  # Initialize queue with (word, level)
    visited = {beginWord}

    while queue:
        word, level = queue.popleft()

        if word == endWord:
            return level

        for i in range(len(word)):
            for char_code in range(ord('a'), ord('z') + 1):
                char = chr(char_code)
                new_word = word[:i] + char + word[i+1:]

                if new_word in wordList and new_word not in visited:
                    queue.append((new_word, level + 1))
                    visited.add(new_word)

    return 0

# Test cases
def test_solution():
    assert ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert ladderLength("a", "c", ["a","b","c"]) == 2
    assert ladderLength("hot", "dog", ["hot","dog"]) == 0 # Missing intermediate word
    assert ladderLength("hot", "dog", ["hot","dog","dot"]) == 3
    assert ladderLength("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]) == 0
    assert ladderLength("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ca","sr","pc","to","ly","hr","ea","ad","cs","ms","la","ti","ep","sg","ly","st","er","am","zc","ex","sk","gy","ed","qa","sw","sq","nr","az"]) == 5


if __name__ == "__main__":
    test_solution()