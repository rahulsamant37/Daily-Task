# DSA Problem 125

'''
Problem Statement:
You are given a list of integers, `nums`, and an integer `k`. Your task is to find the maximum number of unique integers you can have in any subsequence of length `k` from `nums`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. Return the maximum number of unique integers possible in any subsequence of length `k`.

For example, if nums = [1, 2, 1, 3, 4, 3] and k = 3, one possible subsequence is [1, 3, 4], which has 3 unique integers.
'''

Solution:
```python
from collections import Counter

def max_unique_subsequence(nums, k):
    # Count the frequency of each number in nums
    freq = Counter(nums)
    # Sort the numbers by their frequency, and by their appearance order if the frequency is the same
    sorted_nums = sorted(freq.keys(), key=lambda x: (freq[x], nums.index(x)), reverse=True)
    # The maximum number of unique integers in any subsequence of length k
    return min(len(sorted_nums), k)

# Example check function
def check_solution():
    assert max_unique_subsequence([1, 2, 1, 3, 4, 3], 3) == 3
    assert max_unique_subsequence([1, 2, 3, 4, 5], 2) == 2
    assert max_unique_subsequence([5, 5, 5, 5, 5], 4) == 1
    assert max_unique_subsequence([1, 2, 3, 4, 5, 6, 7, 8], 5) == 5
    print("All test cases passed.")

check_solution()
```

This solution constructs a function `max_unique_subsequence` that takes a list of integers and an integer `k` as input and returns the maximum number of unique integers possible in any subsequence of length `k` from the given list. The solution utilizes the `Counter` from the `collections` module to count the frequency of each integer in the list and then sorts these integers based on their frequency and their first appearance in the list to determine the maximum number of unique integers in any subsequence of length `k`.