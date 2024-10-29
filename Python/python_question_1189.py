# Python Question: Word Ladder Length
'''
Given two words, beginWord and endWord, and a dictionary wordList, find the length of the shortest transformation sequence from beginWord to endWord, such that:

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
'''

# Solution
from collections import deque

def solution():
    def word_ladder_length(beginWord, endWord, wordList):
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
        queue = deque([(beginWord, 1)])  # Queue of (word, level) pairs
        visited = {beginWord}  # Set of visited words

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char_code in range(ord('a'), ord('z') + 1):
                    new_word = word[:i] + chr(char_code) + word[i+1:]

                    if new_word in wordList and new_word not in visited:
                        queue.append((new_word, level + 1))
                        visited.add(new_word)

        return 0

    return word_ladder_length
    # Test cases
def test_solution():
    word_ladder_length = solution()

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    assert word_ladder_length(beginWord1, endWord1, wordList1) == 5

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    assert word_ladder_length(beginWord2, endWord2, wordList2) == 0

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    assert word_ladder_length(beginWord3, endWord3, wordList3) == 2

    # Test case 4
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","cog","pot","dot"]
    assert word_ladder_length(beginWord4, endWord4, wordList4) == 3

    # Test case 5
    beginWord5 = "leet"
    endWord5 = "code"
    wordList5 = ["lest","leet","lose","code","lode","robe","lost"]
    assert word_ladder_length(beginWord5, endWord5, wordList5) == 6

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()