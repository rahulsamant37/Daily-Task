# Python Question: Word Ladder
'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

Note:

*   Return 0 if there is no such transformation sequence.
*   All words have the same length.
*   All words contain only lowercase alphabetic characters.
*   You may assume no duplicates in the word list.
*   You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

# Solution
from collections import deque

def solution():
    def word_ladder(beginWord, endWord, wordList):
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
        queue = deque([(beginWord, 1)])  # Store (word, level)
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char_code in range(ord('a'), ord('z') + 1):
                    char = chr(char_code)
                    next_word = word[:i] + char + word[i+1:]

                    if next_word in wordList and next_word not in visited:
                        queue.append((next_word, level + 1))
                        visited.add(next_word)

        return 0

    return word_ladder

# Test cases
def test_solution():
    word_ladder = solution()

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    expected1 = 5
    assert word_ladder(beginWord1, endWord1, wordList1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {word_ladder(beginWord1, endWord1, wordList1)}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot","dot","dog","lot","log"]
    expected2 = 0
    assert word_ladder(beginWord2, endWord2, wordList2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {word_ladder(beginWord2, endWord2, wordList2)}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a","b","c"]
    expected3 = 2
    assert word_ladder(beginWord3, endWord3, wordList3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {word_ladder(beginWord3, endWord3, wordList3)}"

    # Test case 4
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","cog","pot","dot"]
    expected4 = 3
    assert word_ladder(beginWord4, endWord4, wordList4) == 3, f"Test Case 4 Failed: Expected 3, Got {word_ladder(beginWord4, endWord4, wordList4)}"

    # Test case 5: No transformation possible even with valid words
    beginWord5 = "sand"
    endWord5 = "acne"
    wordList5 = ["slit","bunk","wars","ping","viva","wynn","wows","irks","ward","cord","rage","gele","wired","gown","rove","hens","deed","roof","lure","rave","weak","vamp","grid","robs","gore","worn","bawd","bawl","vows","magi","rove","hist","ogre","omic","wise","hare","wiggy","rope","rove","zing","home","lathe","rings","whiff","snip","soci","weave","flaky","jaunt","tonic","yaws","wooed","freer","vise","baby","ruth","heck","gaze","rook","rove","wicked","zape","maid","deep","almost","toed","mile","reap","rect","wore","rude","rove","weep","lacks","impy","yoke","live","mote","rail","rake","rove","reds","rove","unow","rave","robs","nary","sate","rave","roof","rove","weak","void","rove","wire","rave","rove","wick","ware","wing","wons","rove","wack","rove","wail","rove","cats","rove","sand","rove","wine","rove","mare","rove","rove","rove","wave","move","wave","rave","rove","wary","rove","weave","wowser","rove","sand","rove"]
    expected5 = 0
    assert word_ladder(beginWord5, endWord5, wordList5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {word_ladder(beginWord5, endWord5, wordList5)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()