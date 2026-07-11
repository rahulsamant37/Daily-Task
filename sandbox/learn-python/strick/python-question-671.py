# Python Question: Word Ladder
'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

Note:

*   Return 0 if there is no such transformation sequence.
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

def word_ladder(beginWord, endWord, wordList):
    """
    Finds the length of the shortest transformation sequence from beginWord to endWord.

    Args:
        beginWord: The starting word.
        endWord: The ending word.
        wordList: A list of valid words to transform into.

    Returns:
        The length of the shortest transformation sequence, or 0 if no such sequence exists.
    """
    if endWord not in wordList:
        return 0

    wordList = set(wordList)  # Convert to set for faster lookup
    queue = deque([(beginWord, 1)])  # Queue of (word, level) tuples
    visited = {beginWord}  # Keep track of visited words

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

    return 0  # No transformation sequence found


# Test cases
def test_word_ladder():
    assert word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert word_ladder("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert word_ladder("a", "c", ["a","b","c"]) == 2
    assert word_ladder("hot", "dog", ["hot","dog","dot"]) == 3
    assert word_ladder("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]) == 0
    assert word_ladder("sand", "acne", ["sand","acne","tand","cane","send","dane","line","dene","toed","sans"]) == 0

    print("All test cases passed!")

if __name__ == "__main__":
    test_word_ladder()