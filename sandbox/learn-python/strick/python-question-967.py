# Python Question: Word Ladder
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
        beginWord: The starting word.
        endWord: The ending word.
        wordList: A list of valid words.

    Returns:
        The length of the shortest transformation sequence, or 0 if no such sequence exists.
    """

    if endWord not in wordList:
        return 0

    wordSet = set(wordList)  # Convert wordList to a set for faster lookup
    queue = deque([(beginWord, 1)])  # Initialize a queue with the starting word and initial length of 1
    visited = {beginWord}  # Keep track of visited words to avoid cycles

    while queue:
        currentWord, length = queue.popleft()

        if currentWord == endWord:
            return length

        for i in range(len(currentWord)):
            # Iterate through each character of the current word
            for char_code in range(ord('a'), ord('z') + 1):
                # Try replacing each character with all possible letters
                newWord = currentWord[:i] + chr(char_code) + currentWord[i+1:]

                if newWord in wordSet and newWord not in visited:
                    # If the new word is in the word list and hasn't been visited
                    queue.append((newWord, length + 1))  # Add it to the queue with increased length
                    visited.add(newWord)  # Mark it as visited

    return 0  # If the endWord is not reachable, return 0

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

    beginWord4 = "red"
    endWord4 = "tax"
    wordList4 = ["ted","tex","red","tax","tad","den","rex","pee"]
    assert solution(beginWord4, endWord4, wordList4) == 4

    beginWord5 = "leet"
    endWord5 = "code"
    wordList5 = ["lest","leet","lose","code","lode","robe","lost"]
    assert solution(beginWord5, endWord5, wordList5) == 0

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()