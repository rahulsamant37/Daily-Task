# DSA Problem generated on 2024-11-07

Here is a unique DSA problem in Python with solution:

**Problem Statement:**

Given a string S and a dictionary of words Dict, find all possible ways to segment the string into words from the dictionary. The result should be a list of lists, where each inner list represents a possible segmentation of the string.

Example:

S = "catsanddog"
Dict = ["cat", "cats", "and", "sand", "dog"]

Output: [["cat", "sand", "dog"], ["cats", "and", "dog"]]

**Solution Code:**
```
def word_break(S, Dict):
    def backtrack(start, path):
        if start == len(S):
            result.append(path[:])
            return
        for end in range(start, len(S)):
            word = S[start:end+1]
            if word in Dict:
                path.append(word)
                backtrack(end+1, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result

S = "catsanddog"
Dict = ["cat", "cats", "and", "sand", "dog"]
print(word_break(S, Dict))  # Output: [["cat", "sand", "dog"], ["cats", "and", "dog"]]
```
**Time Complexity Analysis:**

The time complexity of this solution is O(N * 2^N), where N is the length of the input string S.

Here's a breakdown of the time complexity:

* The outer loop iterates over the string S, so it has a complexity of O(N).
* For each iteration of the outer loop, the inner loop iterates over the remaining characters of the string, so it has a complexity of O(N) as well.
* Inside the inner loop, we recursively call the backtrack function, which has a complexity of O(2^N) because it explores all possible segmentations of the remaining string.
* Since the outer loop and inner loop have complexities of O(N) each, and the recursive call has a complexity of O(2^N), the overall time complexity is O(N * 2^N).

Note that this is an exponential time complexity, which means the algorithm may take a long time to run for large input strings. However, it is a classic example of a problem that can be solved using backtracking, and it is often used as a teaching example in dynamic programming and algorithm courses.