# DSA Problem generated on 2024-12-06

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` containing only uppercase and lowercase letters, find the minimum number of operations required to convert all characters in the string to uppercase or lowercase, such that all characters in the string are of the same case.

An operation is defined as changing the case of a single character (i.e., converting uppercase to lowercase or vice versa).

Example: If `s = "ABCdEf"`, the minimum number of operations required is 2, as we can convert the characters 'd' and 'E' to uppercase to make the entire string uppercase.

**Solution Code:**
```python
def min_operations(s):
    uppercase_count = sum(1 for c in s if c.isupper())
    lowercase_count = len(s) - uppercase_count
    return min(uppercase_count, lowercase_count)
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. This is because we iterate through the string only once to count the number of uppercase and lowercase characters.

Here's a breakdown of the time complexity:

* The `sum` function has a time complexity of O(n), as it iterates through the entire string.
* The `len` function has a time complexity of O(1), as it simply returns the length of the string.
* The `min` function has a time complexity of O(1), as it takes two constants and returns the minimum value.

Since the dominant operation is the iteration through the string, the overall time complexity is O(n).

**Space Complexity Analysis:**

The space complexity of this solution is O(1), as we only use a few extra variables to store the counts of uppercase and lowercase characters. These variables do not depend on the size of the input string, so the space complexity is constant.