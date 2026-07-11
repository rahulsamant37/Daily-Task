# Python Question: Word Ladder
'''
Given two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the wordList.

Return 0 if no such transformation sequence exists.

Example:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

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
        wordList (List[str]): A list of valid words.

    Returns:
        int: The length of the shortest transformation sequence, or 0 if none exists.
    """

    if endWord not in wordList:
        return 0

    wordList = set(wordList)  # Convert to set for faster lookup
    queue = deque([(beginWord, 1)])  # Initialize queue with starting word and its level (1)
    visited = {beginWord}  # Keep track of visited words to avoid cycles

    while queue:
        word, level = queue.popleft()  # Dequeue the next word and its level

        if word == endWord:
            return level  # Found the endWord, return the level

        for i in range(len(word)):  # Iterate through each character in the word
            for char_code in range(ord('a'), ord('z') + 1):  # Iterate through all possible characters
                new_char = chr(char_code)  # Convert character code to character
                new_word = word[:i] + new_char + word[i+1:]  # Create a new word by changing one letter

                if new_word in wordList and new_word not in visited:  # Check if the new word is valid and not visited
                    queue.append((new_word, level + 1))  # Enqueue the new word and its level
                    visited.add(new_word)  # Mark the new word as visited

    return 0  # No transformation sequence found

# Test cases
def test_solution():
    assert solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert solution("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert solution("a", "c", ["a","b","c"]) == 2
    assert solution("a", "c", ["a","b","c","d"]) == 2
    assert solution("hot", "dog", ["hot","dog"]) == 0
    assert solution("hot", "dog", ["hot","dog","dot"]) == 3
    assert solution("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]) == 0
    assert solution("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","qw","mo","ko","me","ki","pc","tr","rw","er","md","st","lm","nu","mg","ly","yr","rd","lb","og","rg","lt","nm","az","io","rp","gc","aq","tr","mr","sn","ca","ir","io","ao","sr","tc","lc","mv","mc","ax","zt","qm","sq","fo","cc","bn","ax","mt","ac","qy","hc","lr","xx","ye","ct","ea","nf","hm","ye","ul","mo","qy","mx","mt","id","nr","lt","qm","si","mm","nd","po","dt","to","hc","rr","ou","hm","ca","md","wr","mv","hc","cd","bn","er","mt","ou","ad","st","cs","cn","ap","az","st","ex","co","sq","mt","gm","ai","ub","mn","lc","ub","pc","gm","md","ai","qy","yr","ai","gm","hc","tm","md","yr","qy","pc","hc","lr","ai","ub","zy","sq","mt","ca","az","ai"]) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()