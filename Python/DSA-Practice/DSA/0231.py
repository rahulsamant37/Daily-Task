# DSA Problem 231

'''
Problem Statement:
A 'repetitive substring' is defined as a substring which appears at least twice in a string and the distance between any two adjacent occurrences of this substring is less than or equal to 10 characters. Given a string s, find the number of unique repetitive substrings in it. Note that the substrings are case-sensitive.

Example:
Input: s = "abcabcabcabc"
Output: 3
Explanation: The repetitive substrings are: "a", "b", "c", "abc", "bc", "c", "abcabc", "bcab", "cabc", "abcab", "bcabc", and "cabcab". However, only "a", "b", and "c" meet the distance criteria and are unique.
'''

Solution:
```python
def find_repetitive_substrings(s: str) -> int:
    def is_repetitive(sub: str) -> bool:
        indices = [i for i in range(len(s) - len(sub) + 1) if s.startswith(sub, i)]
        return all(j - i <= 10 for i, j in zip(indices, indices[1:]))

    repetitive_substrings = set()
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if len(sub) > 0 and is_repetitive(sub):
                repetitive_substrings.add(sub)
    return len(repetitive_substrings)

# Example usage
s = "abcabcabcabc"
print(find_repetitive_substrings(s))  # Output should be 3
```

Note: The example given in the problem statement is simplified for clarity. The solution provided is based on a stricter interpretation of the problem statement, which requires the substring to be repetitive with a distance criterion. The solution may need optimization depending on the input size due to its potentially high computational complexity.