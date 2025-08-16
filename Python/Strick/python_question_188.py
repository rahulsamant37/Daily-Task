# Python Question: Word Ladder
'''
Given two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the wordList.

Return 0 if no such transformation sequence exists.

Example:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length.

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
    queue = deque([(beginWord, 1)])  # Store word and its level
    visited = {beginWord}  # Keep track of visited words

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

    beginWord5 = "sand"
    endWord5 = "acne"
    wordList5 = ["slit","bunk","wars","ping","viva","wynn","wows","irks","ward","cops","nibs","owns","kopp","tame","drub","kara","hoof","show","jab","gray","grim","java","kirk","teds","trip","dogs","punt","robs","duff","rick","oafs","opus","hogh","ging","simp","rope","gash","ping","rugs","rand","gabs","vats","ohms","reps","hand","dyke","nibz","dome","zaps","keir","silk","goad","labs","wabs","hohs","bohs","pose","wops","ruts","lakh","umps","toss","rays","psst","sows","adpt","wuft","lnes","baby","dlps","grab","visa","drab","sand","tite","baps","spyt","rums","wogs","yjef","visa","pads","unas","rims","tups","apos","olab","clone","plew","hope","nets","lang","tews","clan","lyre","yuks","taco","nibs","lyre","jnjo","hawk","taco","mugs","alee","esop","pots","nuws","bawd","cake","naif","jong","fuzz","sigs","weka","bail","wows","dips","tups","huts","newt","mako","rups","tatw","curt","rune","jams","pong","tows","taco","poms","pays","neps","hugs","wows","pats","hugs","rues","rift","jams","pons","tows","tups"]
    assert solution(beginWord5, endWord5, wordList5) == 0

if __name__ == "__main__":
    test_solution()