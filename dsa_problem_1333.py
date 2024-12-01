# DSA Problem generated on 2024-12-02

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a list of strings, find the longest common suffix (LCS) among all the strings in the list. A suffix is a contiguous sequence of characters at the end of a string. For example, the longest common suffix among the strings ["ABCDEF", "GHIDEF", "KLMNDEF"] is "DEF".

**Solution Code:**
```python
def longest_common_suffix(strings):
    if not strings:
        return ""

    min_len = min(len(s) for s in strings)
    common_suffix = ""

    for i in range(1, min_len + 1):
        suffix = strings[0][-i:]
        if all(s.endswith(suffix) for s in strings):
            common_suffix = suffix
        else:
            break

    return common_suffix
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n*m), where n is the number of strings in the input list and m is the minimum length of the strings.

Here's a breakdown of the time complexity:

* The `min` function takes O(n) time to find the minimum length of the strings.
* The loop iterates at most m times, where m is the minimum length of the strings.
* Inside the loop, we check if all strings end with the current suffix using the `all` function, which takes O(n) time.
* Since we're checking for the longest common suffix, we only need to consider the last m characters of each string, which reduces the time complexity.

Overall, the time complexity is O(n*m), which is relatively efficient for large input lists.

**Example Usage:**
```python
strings = ["ABCDEF", "GHIDEF", "KLMNDEF"]
print(longest_common_suffix(strings))  # Output: "DEF"

strings = ["HELLO", "WORLD", "FOLLO"]
print(longest_common_suffix(strings))  # Output: "LO"
```
Note that this solution assumes that the input list contains at least one string. If the input list is empty, the function returns an empty string.