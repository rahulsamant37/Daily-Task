# Python Question: Word Ladder
'''
Given two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the wordList.

Return 0 if no such transformation sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

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
        endWord: The target word.
        wordList: A list of valid words.

    Returns:
        The length of the shortest transformation sequence, or 0 if no such sequence exists.
    """

    if endWord not in wordList:
        return 0

    wordList = set(wordList)  # Convert to set for faster lookup
    queue = deque([(beginWord, 1)])  # Store (word, distance)
    visited = {beginWord}

    while queue:
        word, distance = queue.popleft()

        if word == endWord:
            return distance

        for i in range(len(word)):
            for char_code in range(ord('a'), ord('z') + 1):
                new_char = chr(char_code)
                new_word = word[:i] + new_char + word[i+1:]

                if new_word in wordList and new_word not in visited:
                    queue.append((new_word, distance + 1))
                    visited.add(new_word)

    return 0  # No transformation sequence found

# Test cases
def test_solution():
    assert solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert solution("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert solution("a", "c", ["a","b","c"]) == 2
    assert solution("hot", "dog", ["hot","dog","cog","pot","dot"]) == 3
    assert solution("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]) == 4
    assert solution("leetcode", "codeleet", ["lest","leet","lose","code","lode","lede","leep","lots","lase","lose","codes","lacs","lede","lame","mole","lame","lode","keel","codeleet","leetcode","lose","lote","laze","lede","lase"]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()