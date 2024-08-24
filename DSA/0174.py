# DSA Problem 174

'''
Problem Statement:
A sequence of integers, `nums`, is given. You are required to find the longest subsequence where the absolute difference between any two consecutive elements in the subsequence is at most 1. A subsequence is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. Return the length of the longest such subsequence.

For example, if nums = [4, 2, 5, 3], one of the longest subsequences where the absolute difference between consecutive elements is at most 1 is [2, 3] or [4, 5], so the function should return 2.
'''

Solution:
```python
def longest_subsequence(nums):
    if not nums:
        return 0

    # Dictionary to keep track of the longest subsequence ending with each number
    longest_subseq = {}
    max_length = 1  # At least one element can always be a subsequence

    for num in nums:
        # The longest subsequence ending with num is at least 1 (the num itself)
        # It could be increased by 1 if there's a subsequence ending with num-1 or num+1
        longest_subseq[num] = 1 + max(longest_subseq.get(num - 1, 0), longest_subseq.get(num + 1, 0))
        max_length = max(max_length, longest_subseq[num])
    
    return max_length

# Example check:
# nums = [1, 3, 5, 4, 2]
# Should return 3 because the longest subsequence where the difference is at most 1 is [3, 4, 5] or [1, 2, 3]
print(longest_subsequence([1, 3, 5, 4, 2]))
```

This Python solution uses a hash map to track the maximum length of subsequences ending at each number. It iterates through the input list, updating the maximum length of subsequences that can be formed ending with the current number, by checking the lengths of subsequences that can be formed with the previous and next numbers (if they exist).