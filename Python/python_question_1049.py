# Python Question: Word Ladder
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

        wordList = set(wordList)  # Convert to set for faster lookup
        queue = deque([(beginWord, 1)])  # Store word and its level
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

        return 0
    return word_ladder

# Test cases
def test_solution():
    word_ladder = solution()
    # Test case 1
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    expected_output = 5
    assert word_ladder(beginWord, endWord, wordList) == expected_output, f"Test Case 1 Failed: Expected {expected_output}, got {word_ladder(beginWord, endWord, wordList)}"

    # Test case 2
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    expected_output = 0
    assert word_ladder(beginWord, endWord, wordList) == expected_output, f"Test Case 2 Failed: Expected {expected_output}, got {word_ladder(beginWord, endWord, wordList)}"

    # Test case 3
    beginWord = "a"
    endWord = "c"
    wordList = ["a","b","c"]
    expected_output = 2
    assert word_ladder(beginWord, endWord, wordList) == 2, f"Test Case 3 Failed: Expected {2}, got {word_ladder(beginWord, endWord, wordList)}"

    # Test case 4
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot","dog","dot"]
    expected_output = 3
    assert word_ladder(beginWord, endWord, wordList) == 3, f"Test Case 4 Failed: Expected {3}, got {word_ladder(beginWord, endWord, wordList)}"

    # Test case 5
    beginWord = "red"
    endWord = "tax"
    wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    expected_output = 4
    assert word_ladder(beginWord, endWord, wordList) == 4, f"Test Case 5 Failed: Expected {4}, got {word_ladder(beginWord, endWord, wordList)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()