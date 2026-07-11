# Python Question: Word Ladder
'''
Given two words, beginWord and endWord, and a dictionary wordList, find the length of the shortest transformation sequence from beginWord to endWord, such that:

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

    beginWord4 = "qa"
    endWord4 = "sq"
    wordList4 = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","ca","ir","ho","cy","mx","nq","ly","rn","eu","br","io","sk","ce","di","oz","dm","ma","wz","sy","mm","np","jm","mc","jr","ai","rn","mg","cd","mo","sw","sz","ts","ok","me","at","if","kt","co","gd","tp","cv","ca","pm","ed","md","eq","sh","rc","ab","ac","aw","rs","zl","cj","mz","oi","pp","op","pa","yz","hm","qy","fi","la","gm","sq","fo","cc","ea","to","au","sn","lw","hc","le","ac","tl","eh","dt","er","ns","el","sm","ns","cr","oa","tc","sz","hc","mm","st","co","lr","ap","lw","db","me","ho","cd","md","av","qa","yr","ai","lt","pc","wa","za","st","dm","ql","br","po","tm","rb","mr","pa","gm","lm","nu","ea","cm","au","tr","md","lp","mn","ow"]
    assert solution(beginWord4, endWord4, wordList4) == 5

    beginWord5 = "hot"
    endWord5 = "dog"
    wordList5 = ["hot","dog"]
    assert solution(beginWord5, endWord5, wordList5) == 0

    beginWord6 = "hot"
    endWord6 = "dog"
    wordList6 = ["hot","dot","dog"]
    assert solution(beginWord6, endWord6, wordList6) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()