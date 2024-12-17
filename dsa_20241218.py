# DSA Problem for 2024-12-18

Here is a novel DSA problem with a Python solution for 2024-12-18:

**Problem Statement:**

**"Festival of Lights"**

The Festival of Lights is a popular winter celebration in a small town, where residents decorate their houses with colorful lights. The town has `n` houses, numbered from 1 to `n`, each with a unique light pattern. The light pattern of each house is represented as a string of '0's and '1's, where '0' indicates a turned-off light and '1' indicates a turned-on light.

The festival organizers want to create a special light show where the light patterns of adjacent houses are synchronized. Specifically, they want to find the longest contiguous sequence of houses where the light patterns are identical.

Given an array `lights` of length `n`, where `lights[i]` represents the light pattern of the `i`-th house, find the length of the longest contiguous sequence of houses with identical light patterns.

**Example:**

`lights = ["101", "101", "010", "010", "101", "101", "101"]`

**Output:** `4` (the longest contiguous sequence of houses with identical light patterns is from house 1 to house 4)

**Optimal Solution:**

Here is a Python solution using a single pass through the array:
```python
def longest_identical_light_sequence(lights):
    n = len(lights)
    max_length = 0
    current_length = 1
    for i in range(1, n):
        if lights[i] == lights[i-1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    return max(max_length, current_length)
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the `lights` array. We iterate through the array once, comparing each element with its previous one.

**Space Complexity Analysis:**

The space complexity of this solution is O(1), as we only use a few extra variables to keep track of the current and maximum lengths of identical light sequences.

**Explanation:**

The solution uses a simple single-pass approach to find the longest contiguous sequence of houses with identical light patterns. We maintain two variables: `current_length` to keep track of the length of the current sequence of identical light patterns, and `max_length` to keep track of the maximum length of such sequences seen so far.

As we iterate through the array, we compare each element with its previous one. If they are identical, we increment `current_length`. If they are not, we update `max_length` with the maximum of the current `max_length` and `current_length`, and reset `current_length` to 1.

Finally, we return the maximum of `max_length` and `current_length` to account for the possibility that the longest sequence ends at the end of the array.

I hope you enjoy this problem!