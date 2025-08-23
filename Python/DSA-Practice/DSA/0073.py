# DSA Problem 73

'''
Problem Statement:
A sequence of integers is called a zigzag sequence if each element is either strictly greater than both of its neighbors or strictly less than both of its neighbors. Given an array `arr` of integers, determine the length of the longest zigzag subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, in the array [1, 7, 4, 9, 2, 5], one zigzag subsequence could be [1, 7, 4, 9, 2] or [7, 4, 9, 2].
'''

Solution:
```python
def longest_zigzag_subsequence(arr):
    n = len(arr)
    if n < 2:
        return n

    # increase[i] stores the length of the longest zigzag subsequence ending at i with a positive difference
    # decrease[i] stores the length of the longest zigzag subsequence ending at i with a negative difference
    increase = [0] * n
    decrease = [0] * n
    increase[0] = decrease[0] = 1

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                increase[i] = max(increase[i], decrease[j] + 1)
            elif arr[i] < arr[j]:
                decrease[i] = max(decrease[i], increase[j] + 1)
        if increase[i] == 0 and decrease[i] == 0:
            increase[i] = decrease[i] = 1

    return max(max(increase), max(decrease))

# Test the function
arr = [1, 7, 4, 9, 2, 5]
print("Length of the longest zigzag subsequence:", longest_zigzag_subsequence(arr))
```

This Python code defines a function `longest_zigzag_subsequence` that calculates the length of the longest zigzag subsequence in a given array `arr`. It uses dynamic programming to keep track of the longest subsequences that end with an increase or decrease at each index. The function is tested with an example array, and it prints the length of the longest zigzag subsequence found.