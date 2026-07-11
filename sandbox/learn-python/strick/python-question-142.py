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
        beginWord (str): The starting word.
        endWord (str): The ending word.
        wordList (list): A list of valid words.

    Returns:
        int: The length of the shortest transformation sequence, or 0 if no such sequence exists.
    """

    if endWord not in wordList:
        return 0

    wordList = set(wordList)  # Convert to set for faster lookup
    queue = deque([(beginWord, 1)])  # Store word and its level (distance from beginWord)
    visited = {beginWord}  # Keep track of visited words to avoid cycles

    while queue:
        word, level = queue.popleft()

        if word == endWord:
            return level

        for i in range(len(word)):
            # Try changing each character in the word
            for char_code in range(ord('a'), ord('z') + 1):
                new_word = word[:i] + chr(char_code) + word[i+1:]

                if new_word in wordList and new_word not in visited:
                    queue.append((new_word, level + 1))
                    visited.add(new_word)  # Mark the new word as visited

    return 0  # No transformation sequence found

# Test cases
def test_solution():
    assert solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert solution("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert solution("a", "c", ["a","b","c"]) == 2
    assert solution("a", "c", ["a","b"]) == 0
    assert solution("hot", "dog", ["hot","dog","cog","pot","dot"]) == 3
    assert solution("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]) == 0
    assert solution("sand", "acne", ["sand","acne","tand","cane","tend"]) == 0
    assert solution("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","qg","pc","dm","ts","er","md","st","lm","ql","tc","eh","lb","pt","gc","aq","dr","co","ca","sr","bs","tz","ss","mo","sz","op","pf","to","ge","lc","sj","mk","fo","ko","me","qt","rg","fu","hm","lc","ea","sk","lt","nm","bn","mt","co","ga","vp","mc","mn","nf","id","jv","lp","sq","ar"]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()