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
            endWord: The ending word.
            wordList: A list of valid words.

        Returns:
            The length of the shortest transformation sequence, or 0 if no such sequence exists.
        """

        if endWord not in wordList:
            return 0

        wordSet = set(wordList)  # Convert wordList to a set for faster lookup
        queue = deque([(beginWord, 1)])  # Initialize a queue with the starting word and its initial length (1)
        visited = {beginWord}  # Keep track of visited words to avoid cycles

        while queue:
            word, length = queue.popleft()  # Dequeue the current word and its length

            if word == endWord:
                return length  # If we've reached the endWord, return the length

            for i in range(len(word)):  # Iterate through each character in the current word
                for char_code in range(ord('a'), ord('z') + 1):  # Iterate through all possible lowercase letters
                    new_word = word[:i] + chr(char_code) + word[i+1:]  # Create a new word by replacing the i-th character
                    if new_word in wordSet and new_word not in visited:  # Check if the new word is in the wordList and hasn't been visited
                        queue.append((new_word, length + 1))  # Enqueue the new word with an incremented length
                        visited.add(new_word)  # Mark the new word as visited

        return 0  # If the queue becomes empty without finding the endWord, return 0

    return word_ladder

# Test cases
def test_solution():
    word_ladder = solution()

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected1 = 5
    assert word_ladder(beginWord1, endWord1, wordList1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {word_ladder(beginWord1, endWord1, wordList1)}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    expected2 = 0
    assert word_ladder(beginWord2, endWord2, wordList2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {word_ladder(beginWord2, endWord2, wordList2)}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]
    expected3 = 2
    assert word_ladder(beginWord3, endWord3, wordList3) == 2, f"Test Case 3 Failed: Expected {2}, got {word_ladder(beginWord3, endWord3, wordList3)}"

    # Test case 4
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","cog","pot","dot"]
    expected4 = 3
    assert word_ladder(beginWord4, endWord4, wordList4) == 3, f"Test Case 4 Failed: Expected {3}, got {word_ladder(beginWord4, endWord4, wordList4)}"

    # Test case 5 (Longer word list)
    beginWord5 = "sand"
    endWord5 = "acne"
    wordList5 = ["sand","acnd","acne","mand","sand","cand","sand","band","sand"]
    expected5 = 4
    assert word_ladder(beginWord5, endWord5, wordList5) == 4, f"Test Case 5 Failed: Expected {4}, got {word_ladder(beginWord5, endWord5, wordList5)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()