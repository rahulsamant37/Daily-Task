# Python Question: Word Ladder
'''
Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the `wordList`.

Return 0 if no such transformation sequence exists.

Note:
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the wordList.
- You may assume beginWord and endWord are non-empty and are not the same.

Example:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

'''

# Solution
def solution():
    def wordLadder(beginWord, endWord, wordList):
        """
        Finds the length of the shortest transformation sequence from beginWord to endWord.

        Args:
            beginWord: The starting word.
            endWord: The target word.
            wordList: A list of valid words.

        Returns:
            The length of the shortest transformation sequence, or 0 if no such sequence exists.
        """

        wordSet = set(wordList)  # Convert wordList to a set for faster lookups
        if endWord not in wordSet:
            return 0

        queue = [(beginWord, 1)]  # Queue of (word, level) pairs
        visited = {beginWord}  # Keep track of visited words to avoid cycles

        while queue:
            word, level = queue.pop(0)  # Dequeue the next word and its level

            if word == endWord:
                return level  # Found the endWord, return the level

            for i in range(len(word)):  # Iterate through each character in the word
                for char_code in range(ord('a'), ord('z') + 1):  # Iterate through all lowercase letters
                    new_char = chr(char_code)
                    new_word = word[:i] + new_char + word[i+1:]  # Create a new word by changing one letter

                    if new_word in wordSet and new_word not in visited:
                        queue.append((new_word, level + 1))  # Add the new word to the queue with the next level
                        visited.add(new_word)  # Mark the new word as visited

        return 0  # No transformation sequence found

    return wordLadder
    # Test cases
def test_solution():
    wordLadder = solution()

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    expected1 = 5
    assert wordLadder(beginWord1, endWord1, wordList1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {wordLadder(beginWord1, endWord1, wordList1)}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    expected2 = 0
    assert wordLadder(beginWord2, endWord2, wordList2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {wordLadder(beginWord2, endWord2, wordList2)}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    expected3 = 2
    assert wordLadder(beginWord3, endWord3, wordList3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {wordLadder(beginWord3, endWord3, wordList3)}"

    # Test case 4
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","cog","pot","dot"]
    expected4 = 3
    assert wordLadder(beginWord4, endWord4, wordList4) == 3, f"Test Case 4 Failed: Expected {3}, Got {wordLadder(beginWord4, endWord4, wordList4)}"

    # Test case 5
    beginWord5 = "sand"
    endWord5 = "acne"
    wordList5 = ["sand","acne","and","cand","san"]
    expected5 = 0
    assert wordLadder(beginWord5, endWord5, wordList5) == 0, f"Test Case 5 Failed: Expected {0}, Got {wordLadder(beginWord5, endWord5, wordList5)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()