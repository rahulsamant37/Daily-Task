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

def solution():
    def word_ladder(beginWord, endWord, wordList):
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

        wordList = set(wordList)  # Convert to set for faster lookup
        queue = deque([(beginWord, 1)])  # Initialize queue with (word, level)
        visited = {beginWord}  # Keep track of visited words to avoid cycles

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char_code in range(ord('a'), ord('z') + 1):
                    new_word = word[:i] + chr(char_code) + word[i+1:]

                    if new_word in wordList and new_word not in visited:
                        queue.append((new_word, level + 1))
                        visited.add(new_word)

        return 0  # No transformation sequence found

    return word_ladder


# Test cases
def test_solution():
    word_ladder = solution()  # Get the word_ladder function

    # Test case 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected1 = 5
    assert word_ladder(beginWord1, endWord1, wordList1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {word_ladder(beginWord1, endWord1, wordList1)}"

    # Test case 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    expected2 = 0
    assert word_ladder(beginWord2, endWord2, wordList2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {word_ladder(beginWord2, endWord2, wordList2)}"

    # Test case 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]
    expected3 = 2
    assert word_ladder(beginWord3, endWord3, wordList3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {word_ladder(beginWord3, endWord3, wordList3)}"

    # Test case 4 (longer list)
    beginWord4 = "sand"
    endWord4 = "acne"
    wordList4 = ["sand","acnd","acne","mand","sand","sand"]
    expected4 = 0
    assert word_ladder(beginWord4, endWord4, wordList4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {word_ladder(beginWord4, endWord4, wordList4)}"

    # Test case 5 (same start and end)
    beginWord5 = "a"
    endWord5 = "a"
    wordList5 = ["a"]
    expected5 = 1
    assert word_ladder(beginWord5, endWord5, wordList5) == 1, f"Test Case 5 Failed: Expected {1}, Got {word_ladder(beginWord5, endWord5, wordList5)}"
    
    # Test case 6 (from LeetCode)
    beginWord6 = "qa"
    endWord6 = "sq"
    wordList6 = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ca","sr","pc","it","tq","co","ke","ha","er","hm","og","fi","la","ti","go","ky","eh","tc","dm","pm","sr","lp","tx","pr","sa","tp","qa","op","ai","mt","ep","ap","st","ci","ml","lb","pt","io","eq","dr","qy","rf","to","mg","rm","ly","md","mo","vb","lc","nm","sq","ph","og","td","zz","gr","ri","pc","tr","cm","ea","in","ca","sk","ba","st","er","og","sy","hr","ai","rb","mr"]
    expected6 = 5
    assert word_ladder(beginWord6, endWord6, wordList6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {word_ladder(beginWord6, endWord6, wordList6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()