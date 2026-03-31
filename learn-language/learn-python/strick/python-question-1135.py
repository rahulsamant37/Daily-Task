# Python Question: Word Ladder Transformation
'''
Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord` such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the `wordList`.

Return 0 if no such transformation sequence exists.

Note:
- `beginWord` and `endWord` do not need to be in `wordList`.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the `wordList`.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0

Explanation: The endWord "cog" is not reachable.
'''

# Solution
from collections import deque

def solution():
    def ladderLength(beginWord, endWord, wordList):
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

        wordList = set(wordList)  # Convert to set for faster lookup
        queue = deque([(beginWord, 1)])  # Initialize queue with (word, level)
        visited = {beginWord}  # Keep track of visited words

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + char + word[i+1:]

                    if new_word in wordList and new_word not in visited:
                        queue.append((new_word, level + 1))
                        visited.add(new_word)

        return 0  # No transformation sequence found

    return ladderLength

# Test cases
def test_solution():
    ladderLength = solution()

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected1 = 5
    actual1 = ladderLength(beginWord1, endWord1, wordList1)
    assert actual1 == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {actual1}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    expected2 = 0
    actual2 = ladderLength(beginWord2, endWord2, wordList2)
    assert actual2 == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {actual2}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]
    expected3 = 2
    actual3 = ladderLength(beginWord3, endWord3, wordList3)
    assert actual3 == 2, f"Test Case 3 Failed: Expected {expected3}, Got {actual3}"

    # Test case 4 (beginWord already equals endWord)
    beginWord4 = "hot"
    endWord4 = "hot"
    wordList4 = ["hot","dot","dog"]
    expected4 = 1
    actual4 = ladderLength(beginWord4, endWord4, wordList4)
    assert actual4 == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {actual4}"

    # Test case 5 (longer list)
    beginWord5 = "sand"
    endWord5 = "acne"
    wordList5 = ["sand","acnd","acne","mand","pond","sane","send","dand","mend","wand"]
    expected5 = 0
    actual5 = ladderLength(beginWord5, endWord5, wordList5)
    assert actual5 == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {actual5}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()