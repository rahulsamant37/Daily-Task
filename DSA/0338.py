# DSA Problem 338

'''
Problem Statement:
A sequence of integers A is given. You are to partition the sequence into non-empty contiguous sub-sequences such that the sum of each sub-sequence is the same. Find the maximum number of such partitions, and if no such partition is possible, return 0.

For example, if the sequence is [1, 2, 3, 4, 4], one possible partition is [1, 2], [3], [4, 4] with a sum of 3 for each sub-sequence. Hence, the maximum number of partitions is 3.

Input:
The input is a single argument, an integer array A.

Output:
Return an integer representing the maximum number of partitions.

Constraints:
- The length of array A is between 1 and 10^4.
- Each element in A is between -10^5 and 10^5.

Examples:
1. max_partitions([1, 2, 3, 4, 4]) returns 3
2. max_partitions([1, 2, 3, 4]) returns 0
'''

Solution:
```python
def max_partitions(A):
    total_sum = sum(A)
    if total_sum == 0:
        return 0
    # Possible partition sum can only be a divisor of total_sum
    possible_sums = set()
    for i in range(1, int(total_sum**0.5) + 1):
        if total_sum % i == 0:
            possible_sums.add(i)
            possible_sums.add(total_sum // i)
    
    max_partitions = 0
    for target_sum in possible_sums:
        partitions = 0
        current_sum = 0
        for num in A:
            current_sum += num
            if current_sum == target_sum:
                partitions += 1
                current_sum = 0
            elif current_sum > target_sum:
                break
        else:
            if current_sum == 0:  # Ensure the last segment also meets the requirement
                max_partitions = max(max_partitions, partitions)
                
    return max_partitions

# Example check (You can run these to test your solution)
print(max_partitions([1, 2, 3, 4, 4]))  # Expected output: 3
print(max_partitions([1, 2, 3, 4]))    # Expected output: 0
```
The provided function `max_partitions` finds the maximum number of partitions of the array `A` such that the sum of each partition is equal. It checks all possible sums that can divide the total sum of the array and returns the maximum number of valid partitions found.