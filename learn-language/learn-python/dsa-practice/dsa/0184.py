# DSA Problem 184

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, find the total number of continuous subarrays whose sum equals to `k`.

For example, given the list nums = [1, 1, 1] and k = 2, the function should return 2, as there are two continuous subarrays that sum up to 2: [1, 1] (first and second elements) and [1, 1] (second and third elements).

Note:
- The list `nums` can have up to 10^5 elements.
- The sum of the elements in the subarray must be exactly `k`.
'''

Solution:
```python
from collections import defaultdict

def subarray_sum(nums, k):
    count = 0
    sums = 0
    d = defaultdict(int)
    d[0] = 1
    
    for num in nums:
        sums += num
        if sums - k in d:
            count += d[sums - k]
        d[sums] += 1
    
    return count

# Example check (This part is not part of the solution code)
nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))  # Expected output: 2
```

This problem involves using a hash map to keep track of the cumulative sums encountered as we iterate through the array. For each position, we check if the current cumulative sum minus `k` has been encountered before. If it has, it means there exists a subarray ending at the current position which sums up to `k`, and we increment our count by the number of times the difference has been seen.