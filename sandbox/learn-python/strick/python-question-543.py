# Python Question: Word Ladder
'''
Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the `wordList`.

Return 0 if no such transformation sequence exists.

Note:

*   Return the length of the shortest transformation sequence, not the sequence itself.
*   All words have the same length.
*   All words contain only lowercase alphabetic characters.
*   You may assume no duplicates in the wordList.
*   `beginWord` and `endWord` are not the same.

Example:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log"]

Output: 0

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

        wordList = set(wordList)  # Convert to set for faster lookup
        queue = deque([(beginWord, 1)])  # (word, level)
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char_code in range(ord('a'), ord('z') + 1):
                    new_char = chr(char_code)
                    new_word = word[:i] + new_char + word[i+1:]

                    if new_word in wordList and new_word not in visited:
                        queue.append((new_word, level + 1))
                        visited.add(new_word)

        return 0

    return word_ladder
    
# Test cases
def test_solution():
    word_ladder = solution()
    assert word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert word_ladder("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert word_ladder("a", "c", ["a","b","c"]) == 2
    assert word_ladder("a", "c", ["a","b"]) == 0
    assert word_ladder("hot", "dog", ["hot","dog","cog","pot","dot"]) == 3
    assert word_ladder("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]) == 4
    print("All test cases passed!")
    

if __name__ == "__main__":
    test_solution()