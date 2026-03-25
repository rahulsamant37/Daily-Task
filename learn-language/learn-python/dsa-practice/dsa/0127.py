# DSA Problem 127

'''
Problem Statement:
A sequence of integers is called "balanced" if for every distinct pair of integers (x, y) in the sequence, the number of occurrences of x is not equal to the number of occurrences of y. Given a list of integers `nums`, determine if the list is balanced. If it is not balanced, find the minimum number of elements that need to be removed to make it balanced. Return the minimum number of removals required.

Example:
Input: nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
Output: 3
Explanation: To make the list balanced, you can remove three 4's, making the counts of each number unique.
'''

Solution:
```python
from collections import Counter

def min_removals_to_balance(nums):
    """
    Finds the minimum number of elements to remove to make the list balanced.
    """
    count = Counter(nums)
    freq_count = Counter(count.values())
    freqs = list(freq_count.items())
    freqs.sort()
    
    removals = 0
    for i in range(len(freqs)):
        if i == len(freqs) - 1:
            removals += freqs[i][1] * freqs[i][0]
            break
        if freqs[i][1] == 1 and freqs[i][0] + 1 == freqs[i + 1][0]:
            continue
        extra = freqs[i][1] - 1
        removals += extra * freqs[i][0]
        freqs[i + 1] = (freqs[i + 1][0], freqs[i + 1][1] + extra)
    
    return removals

# Check function to verify the solution with provided data points
def check_solution():
    assert min_removals_to_balance([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 3
    assert min_removals_to_balance([1, 1, 2, 2, 2, 3, 3, 3, 3]) == 1
    assert min_removals_to_balance([5, 5, 5, 5, 5]) == 4
    assert min_removals_to_balance([1, 2, 3, 4, 5]) == 0
    print("All tests passed!")

check_solution()
```

This Python solution defines a function `min_removals_to_balance()` that calculates the minimum number of removals required to make the input list "balanced" according to the problem statement. A helper function `check_solution()` is used to verify the correctness of the solution with given test cases.