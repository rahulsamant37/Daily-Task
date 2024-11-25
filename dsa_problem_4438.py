# DSA Problem generated on 2024-11-26

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` containing only lowercase English letters, find the maximum number of unique characters that can be formed by rearranging the characters in `s` such that the resulting string is a palindrome.

**Example:**

Input: `s = "aabbcc"`
Output: 3 (The maximum number of unique characters that can be formed is 3, which is "abc")

Input: `s = "abccba"`
Output: 3 (The resulting palindrome string is "abcba" with 3 unique characters)

**Solution Code:**
```python
from collections import Counter

def max_unique_palindrome_chars(s):
    char_count = Counter(s)
    odd_count = 0
    unique_chars = 0

    for count in char_count.values():
        if count % 2 == 0:
            unique_chars += count // 2
        else:
            unique_chars += count // 2
            odd_count += 1

    if odd_count > 0:
        unique_chars += 1

    return unique_chars
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n), where n is the length of the input string `s`.

Here's a breakdown of the time complexity:

1. `Counter(s)`: Creating a `Counter` object from the input string takes O(n) time.
2. Iterating over the `Counter` values: This takes O(n) time, where n is the number of unique characters in the input string.
3. Calculating `unique_chars`: This takes O(1) time for each iteration, so the total time complexity is O(n).
4. Returning `unique_chars`: This takes O(1) time.

Since the dominant operation is creating the `Counter` object and iterating over its values, the overall time complexity is O(n).

**Explanation:**

The solution uses a `Counter` object to count the frequency of each character in the input string. Then, it iterates over the `Counter` values to calculate the maximum number of unique characters that can be formed.

For each character, if its count is even, we can form half of that count as unique characters. If the count is odd, we can form half of that count minus one as unique characters, and the remaining one character can be used as the middle character of the palindrome.

Finally, if there are any odd counts, we increment the `unique_chars` count by one to account for the middle character of the palindrome.

The solution takes advantage of the fact that a palindrome can have at most one character with an odd count.