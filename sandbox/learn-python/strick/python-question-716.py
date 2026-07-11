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

Example:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
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

        wordList = set(wordList) # Convert to set for faster lookup
        queue = deque([(beginWord, 1)]) # Store word and its level (distance from beginWord)
        visited = {beginWord} # Keep track of visited words to avoid cycles

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)): # Iterate through each character in the word
                for char in 'abcdefghijklmnopqrstuvwxyz': # Try all possible characters
                    new_word = word[:i] + char + word[i+1:] # Create a new word by replacing the character

                    if new_word in wordList and new_word not in visited: # Check if the new word is valid and not visited
                        queue.append((new_word, level + 1)) # Add the new word to the queue with incremented level
                        visited.add(new_word) # Mark the new word as visited

        return 0 # If no path is found

    return word_ladder

# Test cases
def test_solution():
    word_ladder = solution()

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    expected1 = 5
    assert word_ladder(beginWord1, endWord1, wordList1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {word_ladder(beginWord1, endWord1, wordList1)}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    expected2 = 0
    assert word_ladder(beginWord2, endWord2, wordList2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {word_ladder(beginWord2, endWord2, wordList2)}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    expected3 = 2
    assert word_ladder(beginWord3, endWord3, wordList3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {word_ladder(beginWord3, endWord3, wordList3)}"

    # Test case 4
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","cog","pot","dot"]
    expected4 = 3
    assert word_ladder(beginWord4, endWord4, wordList4) == 3, f"Test Case 4 Failed: Expected 3, Got {word_ladder(beginWord4, endWord4, wordList4)}"

    # Test case 5: Empty word list
    beginWord5 = "hit"
    endWord5 = "cog"
    wordList5 = []
    expected5 = 0
    assert word_ladder(beginWord5, endWord5, wordList5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {word_ladder(beginWord5, endWord5, wordList5)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()