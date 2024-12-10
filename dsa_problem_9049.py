# DSA Problem generated on 2024-12-11

Here is a unique DSA problem in Python with a solution, time complexity analysis, and a problem statement:

**Problem Statement:**

Given a string `s` consisting of lowercase English letters, find the length of the longest substring without repeating characters and containing at least one occurrence of each of the vowels 'a', 'e', 'i', 'o', and 'u'. If no such substring exists, return -1.

**Example 1:**

Input: s = "aeiou"
Output: 5
Explanation: The longest substring is "aeiou" itself, which contains all vowels and has no repeating characters.

**Example 2:**

Input: s = "abcde"
Output: -1
Explanation: There is no substring containing all vowels.

**Solution Code:**

```
def longest_vowel_substring(s):
    vowels = set('aeiou')
    max_len = -1
    left = 0
    vowel_count = 0
    char_count = {}
    
    for right in range(len(s)):
        if s[right] in vowels:
            vowel_count += 1
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        while char_count[s[right]] > 1:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
            
        if vowel_count == 5:
            max_len = max(max_len, right - left + 1)
    
    return max_len
```

**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. This is because we are traversing the string once using the sliding window approach.

Here's a breakdown of the time complexity:

* The outer loop iterates `n` times.
* The inner while loop can iterate at most `n` times in total, since each character is removed from the window at most once.
* The set and dictionary operations (insertion, deletion, and lookup) take constant time.

Therefore, the overall time complexity is O(n).

**Space Complexity Analysis:**

The space complexity of this solution is O(1), since we are using a constant amount of space to store the vowels, character counts, and window boundaries. The space used does not grow with the size of the input string `s`.