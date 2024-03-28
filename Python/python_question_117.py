# Python Question: Word Ladder
'''
Given two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

Return 0 if no such transformation sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

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
        wordList (list[str]): A list of valid words to use for transformations.

    Returns:
        int: The length of the shortest transformation sequence, or 0 if no such sequence exists.
    """

    if endWord not in wordList:
        return 0

    wordList = set(wordList)  # Convert to set for faster lookups
    queue = deque([(beginWord, 1)])  # Initialize queue with starting word and initial length
    visited = {beginWord}  # Keep track of visited words to avoid cycles

    while queue:
        word, length = queue.popleft()

        if word == endWord:
            return length

        for i in range(len(word)):
            for char_code in range(ord('a'), ord('z') + 1):
                new_char = chr(char_code)
                new_word = word[:i] + new_char + word[i+1:]

                if new_word in wordList and new_word not in visited:
                    queue.append((new_word, length + 1))
                    visited.add(new_word)

    return 0  # No transformation sequence found

# Test cases
def test_solution():
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    assert solution(beginWord1, endWord1, wordList1) == 5

    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    assert solution(beginWord2, endWord2, wordList2) == 0

    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    assert solution(beginWord3, endWord3, wordList3) == 2

    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog"]
    assert solution(beginWord4, endWord4, wordList4) == 0

    beginWord5 = "red"
    endWord5 = "tax"
    wordList5 = ["ted","tex","red","tax","tad","den","rex","pee"]
    assert solution(beginWord5, endWord5, wordList5) == 4

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()