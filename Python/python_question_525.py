# Python Question: Word Ladder
'''
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of the shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

Note:
* Return 0 if there is no such transformation sequence.
* All words have the same length.
* All words contain only lowercase alphabetic characters.
* You may assume no duplicates in the word list.
* You may assume beginWord and endWord are non-empty and are not the same.

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

'''

# Solution
from collections import deque

def solution(beginWord, endWord, wordList):
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


# Test cases
def test_solution():
    assert solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert solution("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert solution("a", "c", ["a","b","c"]) == 2
    assert solution("hot", "dog", ["hot","dog","cog","pot","dot"]) == 3
    assert solution("sand", "acne", ["slit","bunk","wars","ping","viva","vice","rave","gizs","riot","pugs","wynn","rhea","rove","hear","awry","east","lynx","huzz","tref","kats","trip","apts","qlip","pang","dewy","zigz","mrsd","quil","jive","rhon","qwav","zjig","mulu","lock","mirs","moil","myth","wore","kirn","rock","sayn","fogs","eggi","shim","auts","warn","hugs","wear","guts","huff","epee","iamb","tugs","coco","owner","wake","vider","jays","moil","puffs","kill","swat","toyv","gien"," Ward","aisle","erie","meta","tins","zizz","roth","seam","chin","kiew","juif","coxe","jamb","jaws","duos","dare","mews","czar","bows","warn","whim","tion","load","taff","pals","glop","arms","cree","nate","imia","rawl","rows","sans","nary","have","jaro","boyo","yore","more","verd","rude","roes","gyps","comp","jabs","teen","prevent","close","size","dade","dare","gigz","glen","ding","koala","lusd","areg","norn","shawl","than","site","eave","sear","craw","thee","ston","dove","doll","body","tows","nows","wine","tops","numb","lime","weep","agon","gray","tram","myre","seen","dead","ilks","pens","wiry","noyd","wite","pink","nets","ogre","lore","kirk","troy","hunt","rand","miso","dopy","aarr","imps","worm","nest","noon","tush","tuss","rowl","hews","snip","lips","fogs","shun","calo","rely","keep","gaze","wack","dupe","dale","spin","ming","chip","near","nize","foil","less","olov","tune","path","ourn","amic"]) == 0
    assert solution("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","tm","sq","si","ge","ml","am","zo","ep","sq","cm","sb","kr","ln","lt","er","mt","da","rf","la","st","sh","mt","ca","ir","io","ac","rq","ly","rb","if"]) == -1

if __name__ == "__main__":
    test_solution()