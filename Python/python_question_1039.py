# Python Question: Implement a Word Ladder Solver
'''
Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the `wordList`.

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
            beginWord (str): The starting word.
            endWord (str): The target word.
            wordList (list): A list of valid words.

        Returns:
            int: The length of the shortest transformation sequence, or 0 if no such sequence exists.
        """

        if endWord not in wordList:
            return 0

        wordSet = set(wordList) # Use a set for faster lookup
        queue = deque([(beginWord, 1)])  # Store the word and its level (distance from beginWord)
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char_code in range(ord('a'), ord('z') + 1):
                    char = chr(char_code)
                    new_word = word[:i] + char + word[i+1:]  # Create a new word by changing one letter

                    if new_word in wordSet and new_word not in visited:
                        queue.append((new_word, level + 1))
                        visited.add(new_word) # Mark as visited to avoid cycles

        return 0  # No transformation sequence found
    return word_ladder

# Test cases
def test_solution():
    word_ladder = solution()

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    expected1 = 5
    assert word_ladder(beginWord1, endWord1, wordList1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {word_ladder(beginWord1, endWord1, wordList1)}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    expected2 = 0
    assert word_ladder(beginWord2, endWord2, wordList2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {word_ladder(beginWord2, endWord2, wordList2)}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    expected3 = 2
    assert word_ladder(beginWord3, endWord3, wordList3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {word_ladder(beginWord3, endWord3, wordList3)}"

    # Test case 4: No transformation possible even if endWord is in wordList
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog"]
    expected4 = 0
    assert word_ladder(beginWord4, endWord4, wordList4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {word_ladder(beginWord4, endWord4, wordList4)}"

    # Test case 5: Same begin and end word
    beginWord5 = "hot"
    endWord5 = "hot"
    wordList5 = ["hot","dot","dog","lot","log","cog"]
    expected5 = 1
    assert word_ladder(beginWord5, endWord5, wordList5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {word_ladder(beginWord5, endWord5, wordList5)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()