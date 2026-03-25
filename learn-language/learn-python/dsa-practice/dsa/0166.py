# DSA Problem 166

'''
Problem Statement:
A sequence of positive integers `nums` is given. We define a function `f(i)` for each `i` (0 ≤ i < len(nums)) as follows:
- If `nums[i]` is even, `f(i) = nums[i] // 2`.
- If `nums[i]` is odd, `f(i) = 3 * nums[i] + 1`.

The sequence is considered "happy" if, for every index `i`, the sequence `nums[i], f(nums[i]), f(f(nums[i])), ...` eventually reaches 1.

Your task is to find and return the starting index of the first "happy" sequence in `nums` or -1 if no such sequence exists. If multiple "happy" sequences start at different indices, return the smallest starting index.

For example, given `nums = [2, 3, 4, 5]`, the function should return `0` because the sequence starting at index 0 (with value 2) is "happy" as it reaches 1.
'''

Solution:
```python
def find_happy_sequence_start(nums):
    def is_happy(n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
        return n == 1

    for i, num in enumerate(nums):
        if is_happy(num):
            return i
    return -1

# Example check
nums = [2, 3, 4, 5]
print(find_happy_sequence_start(nums))  # Output should be 0
```

This solution defines a helper function `is_happy` to check if a number leads to a "happy" sequence according to the problem's definition. It then iterates over the given list of numbers, using the helper function to check each number. If a "happy" sequence is found, it returns the current index. If no "happy" sequence is found throughout the list, it returns -1.