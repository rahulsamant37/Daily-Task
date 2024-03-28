# Python Question: Word Ladder
'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

Return 0 if no such transformation sequence exists.

Example:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log"]

Output: 0

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

        wordList = set(wordList)  # Convert to set for faster lookup
        queue = deque([(beginWord, 1)])  # Initialize queue with (word, level)
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

        return 0  # No transformation sequence found
    return word_ladder
    # Test cases
def test_solution():
    word_ladder = solution()
    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    assert word_ladder(beginWord1, endWord1, wordList1) == 5

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    assert word_ladder(beginWord2, endWord2, wordList2) == 0

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    assert word_ladder(beginWord3, endWord3, wordList3) == 2

    # Test case 4
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","dot"]
    assert word_ladder(beginWord4, endWord4, wordList4) == 3

    # Test case 5 (empty wordList)
    beginWord5 = "hit"
    endWord5 = "cog"
    wordList5 = []
    assert word_ladder(beginWord5, endWord5, wordList5) == 0

    # Test case 6 (beginWord == endWord)
    beginWord6 = "hit"
    endWord6 = "hit"
    wordList6 = ["hot", "hit"]
    assert word_ladder(beginWord6, endWord6, wordList6) == 1

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()