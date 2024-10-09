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
'''

# Solution
from collections import deque

def solution():
    def word_ladder(beginWord, endWord, wordList):
        """
        Finds the length of the shortest transformation sequence from beginWord to endWord.

        Args:
            beginWord: The starting word.
            endWord: The ending word.
            wordList: A list of valid words.

        Returns:
            The length of the shortest transformation sequence, or 0 if no such sequence exists.
        """

        if endWord not in wordList:
            return 0

        wordSet = set(wordList)  # Convert wordList to a set for faster lookup
        queue = deque([(beginWord, 1)])  # Initialize queue with (word, level)
        visited = {beginWord}  # Keep track of visited words

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char_code in range(ord('a'), ord('z') + 1):
                    new_char = chr(char_code)
                    new_word = word[:i] + new_char + word[i+1:]

                    if new_word in wordSet and new_word not in visited:
                        queue.append((new_word, level + 1))
                        visited.add(new_word)

        return 0  # No transformation sequence found

    return word_ladder

# Test cases
def test_solution():
    word_ladder = solution()

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

    # Test case 4
    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","cog","pot","dot"]
    expected4 = 3
    assert word_ladder(beginWord4, endWord4, wordList4) == 3, f"Test Case 4 Failed: Expected {3}, Got {word_ladder(beginWord4, endWord4, wordList4)}"

    # Test case 5
    beginWord5 = "qa"
    endWord5 = "sq"
    wordList5 = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","ca","ir","ma","mi","la","pi","tp","oh","kk","pa","to","eo","sf","lr","ib","dr","zb","sh","st","er","mt","co","ga","ro","rc","zb","fh","bk","pg","ca","sk","mr","ai","rn","bg","sr","wn","mr","or","ud","io","rf","gd","zn","ch","hu","md","jo","hg","zt","ye","ly","jj","zw","wc","zi","lb","mb","lm","lt","ld","fu","hm","lc","yy","rb","pc","da","tj","kt","jo","se","sm","fp","yy","tl","dm","pt","ky","pg","pr","at","dt","hc","hp","kw","vr","rd","dl","tl","mc","ot","er","tp","gp","lc","ln","ar","sb","rq","pc","mg","jr","fo","ds","jt","rg","hk","jl","dm","an","fn","hr","em","lg","dr","mt","mo","av","pc","io","if","hc","tm","wm","si","kg","fo","ha","or","se","lc","eh","lr","ar","se","db","th","wg","sk","nu","if","sz","ca","kr","sm","jt","hy","ga","fm","lt","ib","tm","wm","da","rq","ts","vr","jr","lb","hk","vt","se","hc","sz","ch","sq","ph","ca","jr","mt","si","kb","qr","tp","kt","dt","lb","si","kg","ot","uh","dr","mt","se","cm","ph","ib","dr","oh","rg","lt","hc","ky","nu","ln","fo","jr","lb","to","se","fn","hk","ts","jr","lb","kg","nu","tl","hk","yt","nu","sm","se","lb","pc","ky","yt","nu","se","lb","tl","ca","yt","nu","se","lb","hk","yt","nu","dr","se","lb","mb","pc","nu","lb","to","se","yt","nu","dr","hk","se","lb","pc","nu","to","se","yt","nu","dr","lb","mb"]
    expected5 = 5
    assert word_ladder(beginWord5, endWord5, wordList5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {word_ladder(beginWord5, endWord5, wordList5)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()