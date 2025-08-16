# Python Question: Word Ladder Length
'''
Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the `wordList`.

Return 0 if no such transformation sequence exists.

Note:
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the wordList.
- You may assume beginWord and endWord are non-empty and are not the same.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
'''

# Solution
from collections import deque

def word_ladder_length(beginWord, endWord, wordList):
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

    word_set = set(wordList)  # Convert wordList to a set for faster lookup
    queue = deque([(beginWord, 1)])  # Store (word, level) pairs
    visited = {beginWord}  # Keep track of visited words to avoid cycles

    while queue:
        word, level = queue.popleft()

        if word == endWord:
            return level

        for i in range(len(word)):
            for char_code in range(ord('a'), ord('z') + 1):  # Iterate through all possible characters
                new_char = chr(char_code)
                new_word = word[:i] + new_char + word[i+1:]  # Generate a new word by changing one character

                if new_word in word_set and new_word not in visited:
                    queue.append((new_word, level + 1))
                    visited.add(new_word)

    return 0  # No transformation sequence found

# Test cases
def test_solution():
    assert word_ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert word_ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert word_ladder_length("a", "c", ["a","b","c"]) == 2
    assert word_ladder_length("hot", "dog", ["hot","dog","cog","pot","dot"]) == 3
    assert word_ladder_length("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]) == 0
    assert word_ladder_length("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]) == 4
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()