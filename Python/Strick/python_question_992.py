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
    Finds the length of the shortest transformation sequence from beginWord to endWord using words from wordList.

    Args:
        beginWord (str): The starting word.
        endWord (str): The target word.
        wordList (list): A list of valid words.

    Returns:
        int: The length of the shortest transformation sequence, or 0 if no such sequence exists.
    """

    if endWord not in wordList:
        return 0

    wordSet = set(wordList)  # Convert wordList to a set for faster lookup
    queue = deque([(beginWord, 1)])  # Use a queue for BFS (word, level)
    visited = {beginWord}

    while queue:
        word, level = queue.popleft()

        if word == endWord:
            return level

        for i in range(len(word)):
            for char_code in range(ord('a'), ord('z') + 1):  # Iterate through all possible characters
                new_char = chr(char_code)
                new_word = word[:i] + new_char + word[i+1:]

                if new_word in wordSet and new_word not in visited:
                    queue.append((new_word, level + 1))
                    visited.add(new_word)  # Mark as visited to avoid cycles

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
    wordList5 = ["sand","acnd","acne","mand","cand","sand","mand","acnd","cmnd","acns","acln","mand","sand"]
    assert solution(beginWord5, endWord5, wordList5) == 0

    beginWord6 = "qa"
    endWord6 = "sq"
    wordList6 = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","lw","rw","sf","ka","qr","er","mt","da","rf","la","tl","bg","fo","mo","ek","sq","cc","rb","pc","dm","pm","gn","av","rs","cn","ap","pf","ye","po","sh","ma","tp","io","ac","dy","hm","hr","em","st","ss","tc","wi","vr","pr","rp","nd","vo","es","ca","vs","lc","wi","nu","mf","kw","se","nn","kw","di","md","mc","ta","tb","bb","mr","pa","sg","vn","kw","ie","ca","md","mo","sh","ne","yy","fo","ta","ck","ha","eu","vb","ko","tc","jl","nm","pg","hc","sq","cf","fg","cb","gd","tp","ms","la","qq","ss","ca","rf","ho","vp","nd","nu","le"]
    assert solution(beginWord6, endWord6, wordList6) == 0

if __name__ == "__main__":
    test_solution()