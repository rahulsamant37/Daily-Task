# Python Question: Word Ladder II
'''
Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, find all the shortest transformation sequence(s) from `beginWord` to `endWord`, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the `wordList`.

Return an empty list if there is no such transformation sequence.

Note:

*   Return all such transformation sequence(s) in the form of a list of lists of strings.
*   All words have the same length.
*   All words contain only lowercase alphabetic characters.
*   The `beginWord` is not required to be in the `wordList`.
*   The `endWord` must be in the `wordList`.

Example:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output:
[]

'''

# Solution
from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    wordLen = len(beginWord)
    adj = defaultdict(list)

    # Build the adjacency list
    wordSet.add(beginWord)
    for word in wordSet:
        for i in range(wordLen):
            pattern = word[:i] + "*" + word[i+1:]
            adj[pattern].append(word)

    # BFS to find the shortest paths
    queue = deque([(beginWord, [beginWord])])
    visited = {beginWord}
    result = []
    minLen = float('inf')

    while queue:
        word, path = queue.popleft()

        if len(path) > minLen:
            continue

        if word == endWord:
            minLen = len(path)
            result.append(path)
            continue

        for i in range(wordLen):
            pattern = word[:i] + "*" + word[i+1:]
            for neighbor in adj[pattern]:
                if neighbor not in visited:
                    newPath = path + [neighbor]
                    queue.append((neighbor, newPath))

        visited.add(word) # Mark the word as visited *after* exploring its neighbors at the current level

    # Filter out paths longer than minLen (if any were found)
    if result:
        filtered_result = [path for path in result if len(path) == minLen]
        return filtered_result
    else:
        return []

# Test cases
def test_solution():
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected1 = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
    assert findLadders(beginWord1, endWord1, wordList1) == expected1

    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    expected2 = []
    assert findLadders(beginWord2, endWord2, wordList2) == expected2

    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]
    expected3 = [["a", "c"]]
    assert findLadders(beginWord3, endWord3, wordList3) == expected3

    beginWord4 = "hot"
    endWord4 = "dog"
    wordList4 = ["hot","dog","cog","pot","dot"]
    expected4 = [["hot","dot","dog"], ["hot","dog","cog"]]
    assert sorted(findLadders(beginWord4, endWord4, wordList4)) == sorted(expected4)

    beginWord5 = "red"
    endWord5 = "tax"
    wordList5 = ["ted","tex","red","tax","tad","den","rex","pee"]
    expected5 = [["red","ted","tad","tax"],["red","rex","tex","tax"]]
    assert sorted(findLadders(beginWord5, endWord5, wordList5)) == sorted(expected5)

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()