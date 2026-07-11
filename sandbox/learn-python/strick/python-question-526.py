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
def word_ladder(beginWord, endWord, wordList):
    """
    Finds the length of the shortest transformation sequence from beginWord to endWord using BFS.

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
    queue = [(beginWord, 1)]  # Initialize queue with (word, level)
    visited = {beginWord}  # Keep track of visited words

    while queue:
        word, level = queue.pop(0)

        if word == endWord:
            return level

        for i in range(len(word)):
            for char_code in range(ord('a'), ord('z') + 1):
                new_word = word[:i] + chr(char_code) + word[i + 1:]

                if new_word in wordList and new_word not in visited:
                    queue.append((new_word, level + 1))
                    visited.add(new_word)

    return 0  # No transformation sequence found


# Test cases
def test_word_ladder():
    assert word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert word_ladder("a", "c", ["a", "b", "c"]) == 2
    assert word_ladder("hot", "dog", ["hot", "dog"]) == 0
    assert word_ladder("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]) == 0
    assert word_ladder("a", "c", ["a","b","c"]) == 2
    assert word_ladder("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]) == 4
    assert word_ladder("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ca","sr","pc","it","tq","co","ke","rp","ns","hi","ht","qi","he","ta","to","sq","rf","kt","oe","of","oa","pf","oj","jm","rl","jm","da","sa","hm","yz","lb","tf","rv","ui","ko","me","ve","lc","wi","zw","ky","mn","hm","ld","tb","lp","js","nu","mr","ai","rn","dx","dt","dl","hc","cp","th","jp","nu","kk","cm","dm","jg","hq","yz","zt","dr","pp","qk","pc","gm","kl","kg","qq","dg","vo","mo","an","mt","fj","hm","se","sq","mr","ai","rn","dx","dt","dl","hc","cp","th","jp","nu","kk","cm","dm","jg","hq","yz","zt","dr","pp","qk","pc","gm","kl","kg","qq","dg","vo","mo","an","mt","fj","hm","se"]) == 0



if __name__ == "__main__":
    test_word_ladder()