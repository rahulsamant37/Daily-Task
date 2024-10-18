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

def solution(beginWord, endWord, wordList):
    """
    Finds the length of the shortest transformation sequence from beginWord to endWord.

    Args:
        beginWord (str): The starting word.
        endWord (str): The target word.
        wordList (list): A list of valid words.

    Returns:
        int: The length of the shortest transformation sequence, or 0 if no such sequence exists.
    """

    if endWord not in wordList:
        return 0

    wordSet = set(wordList)  # Convert wordList to a set for faster lookup
    queue = deque([(beginWord, 1)])  # Initialize the queue with the starting word and its level (1)
    visited = {beginWord}  # Keep track of visited words to avoid cycles

    while queue:
        word, level = queue.popleft()

        if word == endWord:
            return level

        for i in range(len(word)):  # Iterate through each character position in the word
            for char_code in range(ord('a'), ord('z') + 1):  # Iterate through all possible lowercase characters
                new_word = word[:i] + chr(char_code) + word[i+1:]  # Create a new word by replacing the character at position i

                if new_word in wordSet and new_word not in visited:  # Check if the new word is in the word list and hasn't been visited
                    queue.append((new_word, level + 1))  # Add the new word to the queue with the next level
                    visited.add(new_word)  # Mark the new word as visited

    return 0  # If the queue is empty and the endWord hasn't been reached, there's no transformation sequence

# Test cases
def test_solution():
    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected1 = 5
    assert solution(beginWord1, endWord1, wordList1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {solution(beginWord1, endWord1, wordList1)}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    expected2 = 0
    assert solution(beginWord2, endWord2, wordList2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {solution(beginWord2, endWord2, wordList2)}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]
    expected3 = 2
    assert solution(beginWord3, endWord3, wordList3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {solution(beginWord3, endWord3, wordList3)}"

    # Test case 4
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","cog","pot","dot"]
    expected4 = 3
    assert solution(beginWord4, endWord4, wordList4) == 3, f"Test Case 4 Failed: Expected {3}, got {solution(beginWord4, endWord4, wordList4)}"

    # Test case 5: No transformation possible
    beginWord5 = "red"
    endWord5 = "tax"
    wordList5 = ["ted","tex","red","tax","tad","den","rex","pee"]
    expected5 = 4
    assert solution(beginWord5, endWord5, wordList5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {solution(beginWord5, endWord5, wordList5)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()