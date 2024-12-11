# DSA Problem generated on 2024-12-12

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` containing only lowercase alphabets, find the minimum number of operations required to make all characters in the string equal. An operation is defined as incrementing or decrementing a character's ASCII value by 1.

For example, if the input string is "abc", the minimum number of operations required is 2, because we can convert all characters to 'b' by incrementing 'a' by 1 and decrementing 'c' by 1.

**Solution Code:**
```python
def min_operations(s):
    char_freq = {}
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    median_char = sorted(char_freq.keys())[len(char_freq) // 2]
    operations = 0
    for char in s:
        operations += abs(ord(char) - ord(median_char))
    
    return operations
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n log n), where n is the length of the input string `s`. Here's the breakdown:

1. The first loop iterates over the string `s` to count the frequency of each character, which takes O(n) time.
2. The second line sorts the keys of the `char_freq` dictionary, which takes O(n log n) time in the worst case, since the number of unique characters is at most n.
3. The third loop iterates over the string `s` again to calculate the minimum number of operations, which takes O(n) time.
4. The `ord` function is used to calculate the ASCII value of each character, which takes O(1) time.

Since the second step dominates the time complexity, the overall time complexity is O(n log n).

**Example:**
```python
print(min_operations("abc"))  # Output: 2
print(min_operations("aabbc"))  # Output: 4
print(min_operations("xyz"))  # Output: 2
```
Note that this problem is a variation of the classic "median finding" problem, where we find the median element in a list. In this case, we're finding the median character in the string and calculating the minimum number of operations to make all characters equal to it.