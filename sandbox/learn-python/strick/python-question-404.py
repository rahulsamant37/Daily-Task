# Python Question: Word Ladder

'''
Given two words, beginWord and endWord, and a dictionary wordList, find the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the wordList.

Return 0 if no such transformation sequence exists.

Example:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

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
        endWord (str): The ending word.
        wordList (list): A list of words in the dictionary.

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
    wordList4 = ["hot","dog","cog","pot","dot"]
    assert solution(beginWord4, endWord4, wordList4) == 3

    beginWord5 = "leet"
    endWord5 = "code"
    wordList5 = ["lest","leet","lose","code","lode","robe","lost"]
    assert solution(beginWord5, endWord5, wordList5) == 0
    
    beginWord6 = "sand"
    endWord6 = "acne"
    wordList6 = ["sand","acnd","acns","acln","acle","sand","sand","acne","sand"]
    assert solution(beginWord6, endWord6, wordList6) == 0

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()