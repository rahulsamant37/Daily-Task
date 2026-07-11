# DSA Problem 148

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, write a function `find_pairs` to find the number of unique pairs of elements (i, j) in `nums` such that their absolute difference is exactly `k`. Note that the order of elements in a pair does not matter, meaning (i, j) is considered the same as (j, i), and no element can be used more than once in a pair.

Example:
Input: nums = [1, 5, 3, 4, 2], k = 2
Output: 3
Explanation: The unique pairs that satisfy the condition are (1, 3), (2, 4), and (3, 5).
'''

Solution:
```python
def find_pairs(nums, k):
    if k < 0:
        return 0  # Since we are looking for absolute difference, negative k doesn't make sense.
    nums_set = set(nums)
    count = 0
    for num in nums_set:
        if k == 0:
            if nums.count(num) > 1:
                count += 1
        else:
            if num + k in nums_set:
                count += 1
    return count

# Test the function
nums = [1, 5, 3, 4, 2]
k = 2
print(find_pairs(nums, k))  # Expected output: 3
```
This Python solution uses a set to eliminate duplicates and then checks for each number if its complement (num + k) exists in the set. The function counts each unique pair only once. If `k` is 0, it checks for duplicates within the list and counts them if there are more than one instance of the number.