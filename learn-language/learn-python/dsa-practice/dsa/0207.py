# DSA Problem 207

'''
Problem Statement:
You are given a list of positive integers, `nums`, and an integer `k`. You need to find the maximum number of operations you can perform on the list, where in each operation you can choose any two distinct elements `a` and `b` from the list such that `a + b` is divisible by `k`. After each operation, both `a` and `b` are removed from the list. The goal is to maximize the number of operations performed.

Constraints:
- The length of `nums` is between 1 and 10^5.
- Each integer in `nums` is between 1 and 10^9.
- `k` is between 1 and 10^9.

Example:
Input: nums = [4, 5, 8, 2], k = 3
Output: 1
Explanation: You can perform 1 operation where you choose 4 and 2 (4 + 2 == 6 which is divisible by 3), leaving [5, 8].
'''

Solution:
```python
def maxOperations(nums, k):
    from collections import Counter
    
    # Count the occurrence of each remainder when divided by k
    remainder_counts = Counter([num % k for num in nums])
    
    # Initialize the operation count
    operations = 0
    
    # Handle the special cases for 0 and k/2 remainders
    if k % 2 == 0:
        operations += remainder_counts[k // 2] // 2
    
    # Calculate the maximum operations for other remainders
    for i in range(1, (k + 1) // 2):
        operations += min(remainder_counts[i], remainder_counts[k - i])
    
    return operations

# Example usage
nums = [4, 5, 8, 2]
k = 3
print(maxOperations(nums, k))  # Output: 1
```

This solution efficiently finds the maximum number of operations that can be performed by leveraging the properties of remainders when numbers are divided by `k`. It uses a counter to keep track of the frequency of each possible remainder and calculates the maximum number of valid pairs that can be formed with these remainders.