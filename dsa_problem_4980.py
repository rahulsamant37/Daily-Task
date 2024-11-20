# DSA Problem generated on 2024-11-21

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string S and an integer K, find the longest substring of S that contains at most K distinct characters. If there are multiple such substrings, return any one of them.

**Example:**

Input: S = "araaci", K = 2
Output: "araa"

**Solution Code:**
```
def longest_substring_with_k_distinct_chars(S, K):
    if K == 0:
        return ""
    
    char_count = {}
    left = 0
    max_len = 0
    max_substr = ""
    
    for right, char in enumerate(S):
        char_count[char] = char_count.get(char, 0) + 1
        
        while len(char_count) > K:
            char_count[S[left]] -= 1
            if char_count[S[left]] == 0:
                del char_count[S[left]]
            left += 1
        
        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_substr = S[left:right+1]
    
    return max_substr
```
**Time Complexity Analysis:**

The time complexity of this solution is O(N), where N is the length of the input string S. Here's a breakdown of the time complexity:

* The outer loop iterates over the entire string S, which takes O(N) time.
* The inner while loop iterates at most K times, since we only remove characters from the `char_count` dictionary when the number of distinct characters exceeds K. This adds an O(K) factor to the time complexity.
* The dictionary operations (insertion, deletion, and lookup) take O(1) time on average, since we're using a hash table.
* The string slicing operations (e.g., `S[left:right+1]`) take O(N) time, but this is done only once for the maximum substring, so it doesn't affect the overall time complexity.

Since K is a constant, the overall time complexity is O(N). The space complexity is O(K), since we're storing at most K characters in the `char_count` dictionary.

Note that this problem is a variation of the "Longest Substring with At Most K Distinct Characters" problem, which is a classic problem in the field of algorithms and data structures.