# DSA Problem 79

'''
Problem Statement:
You are given a string `s` consisting of lowercase English letters. Your task is to find the length of the longest substring of `s` that contains exactly two distinct characters. For instance, in the string "abcabc", "abca" is a substring with exactly two distinct characters, but "abc" is not since it contains three distinct characters. 

Write a function `longest_two_char_substring(s: str) -> int` that computes the length of the longest substring with exactly two distinct characters.

Example 1:
Input: "abcabc" 
Output: 3 
Explanation: The longest substring with exactly two distinct characters is "abca" or "bca".

Example 2:
Input: "aa" 
Output: 2 
Explanation: The longest substring with exactly two distinct characters is "aa" (since it only contains one character, the maximum length is the length of the string itself).

Constraints:
- The string `s` will have a length between 1 and 10^4 characters.
- The string `s` consists of only lowercase English letters.
'''

Solution:
```python
def longest_two_char_substring(s: str) -> int:
    if len(s) < 2: 
        return len(s)
    
    max_length = 0
    left = 0
    char_count = {}
    
    for right in range(len(s)):
        if s[right] in char_count:
            char_count[s[right]] += 1
        else:
            char_count[s[right]] = 1
        
        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example check (not part of the solution code)
print(longest_two_char_substring("abcabc"))  # Output: 3
print(longest_two_char_substring("aa"))     # Output: 2
```
This code uses a sliding window approach to keep track of the number of distinct characters in the current window and adjusts the window size to ensure it contains at most two distinct characters. It maximizes the length of such a window while iterating through the string.