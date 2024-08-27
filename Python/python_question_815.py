# Python Question: Word Ladder Transformation
'''
Given two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

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

def solution(beginWord, endWord, wordList):
    """
    Finds the length of the shortest transformation sequence from beginWord to endWord.

    Args:
        beginWord (str): The starting word.
        endWord (str): The target word.
        wordList (list[str]): A list of valid words.

    Returns:
        int: The length of the shortest transformation sequence, or 0 if no such sequence exists.
    """

    if endWord not in wordList:
        return 0

    wordSet = set(wordList)  # Convert wordList to a set for faster lookup
    queue = deque([(beginWord, 1)])  # Store (word, level) pairs
    visited = {beginWord}  # Keep track of visited words to avoid cycles

    while queue:
        currentWord, level = queue.popleft()

        if currentWord == endWord:
            return level

        for i in range(len(currentWord)):
            for char_code in range(ord('a'), ord('z') + 1):
                newChar = chr(char_code)
                newWord = currentWord[:i] + newChar + currentWord[i+1:]

                if newWord in wordSet and newWord not in visited:
                    queue.append((newWord, level + 1))
                    visited.add(newWord)

    return 0  # No transformation sequence found


# Test cases
def test_solution():
    assert solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert solution("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert solution("a", "c", ["a","b","c"]) == 2
    assert solution("hot", "dog", ["hot","dog","dot"]) == 3
    assert solution("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]) == 4
    assert solution("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()