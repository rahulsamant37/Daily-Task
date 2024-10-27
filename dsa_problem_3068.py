# DSA Problem generated on 2024-10-28

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a list of strings, where each string represents a word, and a character 'c', find the maximum length of a word that can be formed using the characters of the given list of words, such that the word does not contain the character 'c'.

For example, if the input list of words is ["cat", "dog", "tac", "god", "good"] and the character 'c', the output will be 4, because the maximum length of a word that can be formed without the character 'c' is "good".

**Solution Code:**
```python
def max_word_length(words, c):
    max_len = 0
    for word in words:
        if c not in word:
            max_len = max(max_len, len(word))
    return max_len
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n*m), where n is the number of words in the input list and m is the average length of each word.

Here's a breakdown of the time complexity:

* The outer loop iterates over each word in the input list, which takes O(n) time.
* For each word, we check if the character 'c' is present in the word using the `in` operator, which takes O(m) time in the worst case, where m is the length of the word.
* If the character 'c' is not present, we update the maximum length using the `max` function, which takes O(1) time.

Since the inner loop has a maximum of m iterations, the total time complexity is O(n*m).

**Space Complexity Analysis:**

The space complexity of this solution is O(1), since we only use a single variable to store the maximum length, which does not depend on the input size.

Note: This solution assumes that the input list of words is a list of strings, and the character 'c' is a single character.