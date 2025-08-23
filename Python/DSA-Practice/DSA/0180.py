# DSA Problem 180

'''
Problem Statement:
You are given a list of integers and a target sum. Your task is to determine if there are any two distinct numbers in the list that add up to the target sum. If such a pair exists, return the pair in ascending order. If no such pair exists, return None.

For example, given the list [4, 2, -1, 5, 8] and the target sum 7, the function should return [-1, 8] because -1 + 8 = 7. Note that the order of the pair returned does not matter, as long as the numbers are returned in ascending order.

Input:
- A list of integers, `nums`, where 2 <= len(nums) <= 10^4 and -10^9 <= nums[i] <= 10^9.
- An integer, `target`, representing the target sum, where -10^9 <= target <= 10^9.

Output:
- A list containing the two numbers if a pair with the target sum exists, otherwise None.
'''

Solution:
```python
def find_pair_with_sum(nums, target):
    seen = set()
    for number in nums:
        complement = target - number
        if complement in seen:
            return sorted([number, complement])
        seen.add(number)
    return None

# Example check function
def check_solution():
    assert find_pair_with_sum([4, 2, -1, 5, 8], 7) == [-1, 8], "Test case failed!"
    assert find_pair_with_sum([1, 2, 3, 4], 8) is None, "Test case failed!"
    assert find_pair_with_sum([-1, -2, -3, -4], -6) == [-4, -2], "Test case failed!"
    print("All tests passed!")

check_solution()
```

This solution uses a set to keep track of the numbers we have seen so far. For each number in the list, it calculates the complement (i.e., the number that, when added to the current number, would equal the target sum). If the complement is in the set, it means we have found a pair that sums up to the target, and we return the pair sorted in ascending order. If no such pair is found after iterating through the list, the function returns None.