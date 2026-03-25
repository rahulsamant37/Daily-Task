# DSA Problem 31

'''
Problem Statement:
Given a list of integers, find the longest strictly increasing subsequence that can be formed by removing exactly one element from the list. If removing any single element does not result in a strictly increasing sequence, return -1. A strictly increasing sequence is one in which each element is greater than the preceding one.

Example:
For input_list = [3, 5, 6, 4, 7], the output should be [3, 5, 6, 7] as removing the element '4' results in the longest strictly increasing subsequence.
For input_list = [1, 2, 3, 9, 4, 5, 6], removing '9' gives the longest strictly increasing subsequence [1, 2, 3, 4, 5, 6].
'''

Solution:
```python
def longest_increasing_subseq_after_removal(arr):
    def is_increasing(subseq):
        return all(subseq[i] < subseq[i + 1] for i in range(len(subseq) - 1))
    
    max_length = -1
    best_subseq = []
    for i in range(len(arr)):
        new_seq = arr[:i] + arr[i+1:]
        if is_increasing(new_seq) and len(new_seq) > max_length:
            max_length = len(new_seq)
            best_subseq = new_seq
    return best_subseq if max_length != -1 else -1

# Example usage
print(longest_increasing_subseq_after_removal([3, 5, 6, 4, 7]))  # Output: [3, 5, 6, 7]
print(longest_increasing_subseq_after_removal([1, 2, 3, 9, 4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
```

This solution iterates through all possibilities of removing each element once and checks if the resulting sequence is strictly increasing. It keeps track of the longest sequence found that meets the criteria. If no such sequence is found, it returns `-1`.