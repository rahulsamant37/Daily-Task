# Python Question: Word Ladder
'''
Given two words, `beginWord` and `endWord`, and a word list `wordList`, return the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:

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
    def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
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

        wordSet = set(wordList)  # Convert wordList to a set for faster lookup
        queue = deque([(beginWord, 1)])  # Initialize queue with (word, level)
        visited = {beginWord}  # Keep track of visited words to avoid cycles

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char_code in range(ord('a'), ord('z') + 1):
                    new_word = word[:i] + chr(char_code) + word[i+1:]  # Generate all possible one-letter variations

                    if new_word in wordSet and new_word not in visited:
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
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    expected1 = 5
    assert ladderLength(beginWord1, endWord1, wordList1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {ladderLength(beginWord1, endWord1, wordList1)}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    expected2 = 0
    assert ladderLength(beginWord2, endWord2, wordList2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {ladderLength(beginWord2, endWord2, wordList2)}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    expected3 = 2
    assert ladderLength(beginWord3, endWord3, wordList3) == 2, f"Test Case 3 Failed: Expected 2, got {ladderLength(beginWord3, endWord3, wordList3)}"

    # Test case 4
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","dot"]
    expected4 = 3
    assert ladderLength(beginWord4, endWord4, wordList4) == 3, f"Test Case 4 Failed: Expected 3, got {ladderLength(beginWord4, endWord4, wordList4)}"

    # Test case 5
    beginWord5 = "red"
    endWord5 = "tax"
    wordList5 = ["ted","tex","red","tax","tad","den","rex","pee"]
    expected5 = 4
    assert ladderLength(beginWord5, endWord5, wordList5) == 4, f"Test Case 5 Failed: Expected 4, got {ladderLength(beginWord5, endWord5, wordList5)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()