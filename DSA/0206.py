# DSA Problem 206

'''
Problem Statement:
You are tasked with organizing a list of words based on their last character. Given a list of strings, sort the list such that the strings are ordered by the alphabetical order of their last character. If two strings have the same last character, maintain their original order in the list.

For example, if given the list ["cat", "dog", "elephant", "apple"], the function should return ["dog", "cat", "apple", "elephant"] because 'g' < 't' < 'e' < 't', and "apple" comes before "elephant" in the original list despite having the same last character.

Constraints:
- The length of the list will be between 1 and 1000.
- Each string in the list will have a length between 1 and 100.
- All characters in the strings are lowercase English letters.
'''

Solution:
```python
def sort_by_last_char(words):
    return sorted(words, key=lambda x: (x[-1], words.index(x)))

# Test the function
words = ["cat", "dog", "elephant", "apple"]
print(sort_by_last_char(words))  # Output: ['dog', 'cat', 'apple', 'elephant']
```

Explanation:
The solution uses Python's built-in `sorted` function with a custom sorting key. The key is a tuple where the first element is the last character of the string (for primary sorting) and the second element is the original index of the string in the list (to maintain order among elements with the same last character if needed). This ensures that the strings are sorted primarily by the last character alphabetically and secondarily by their original index to preserve the relative order of strings with the same last character.