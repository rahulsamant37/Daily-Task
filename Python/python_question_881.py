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
        beginWord (str): The starting word.
        endWord (str): The ending word.
        wordList (list[str]): A list of valid words.

    Returns:
        int: The length of the shortest transformation sequence, or 0 if no such sequence exists.
    """

    if endWord not in wordList:
        return 0

    wordSet = set(wordList)  # Convert wordList to a set for faster lookup
    queue = deque([(beginWord, 1)])  # Initialize a queue with the beginWord and its initial length (1)
    visited = {beginWord}  # Keep track of visited words to avoid cycles

    while queue:
        word, length = queue.popleft()  # Get the next word and its current length

        if word == endWord:
            return length  # If we've reached the endWord, return the length

        for i in range(len(word)):  # Iterate through each character in the word
            for char_code in range(ord('a'), ord('z') + 1):  # Iterate through all possible lowercase letters
                new_char = chr(char_code)
                new_word = word[:i] + new_char + word[i+1:]  # Create a new word by replacing the i-th character

                if new_word in wordSet and new_word not in visited:  # Check if the new word is valid and unvisited
                    queue.append((new_word, length + 1))  # Add the new word to the queue with an incremented length
                    visited.add(new_word)  # Mark the new word as visited

    return 0  # If we've exhausted all possibilities without finding the endWord, return 0


# Test cases
def test_solution():
    assert solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert solution("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert solution("a", "c", ["a","b","c"]) == 2
    assert solution("hot", "dog", ["hot","dog","cog","pot","dot"]) == 3
    assert solution("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]) == 0
    assert solution("aaaa", "bbbb", ["aaaa","aaab","aabb","abbb","bbbb"]) == 5

if __name__ == "__main__":
    test_solution()