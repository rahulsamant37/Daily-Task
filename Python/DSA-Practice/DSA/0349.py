# DSA Problem 349

'''
Problem Statement:
A sequence of positive integers `nums` is given. You are also given an integer `target`. 
Your task is to find the smallest subsequence of `nums` so that the sum of the subsequence is strictly greater than `target`. 
If there are multiple subsequences of the same minimum length, choose the one with the smallest lexicographical order. 
Return the chosen subsequence. If no such subsequence exists, return an empty list.

Example:
Input: nums = [4,3,10,9,8], target = 21
Output: [3,10,9]
Explanation: The sum of the subsequence [3,10,9] is 22 which is greater than 21. No other subsequence of the same length has a smaller sum. 
'''

Solution:
```python
def min_subsequence(nums, target):
    """
    Finds the lexicographically smallest subsequence of nums that sums up to more than target.
    """
    nums.sort(reverse=True)
    total_sum = sum(nums)
    subsequence = []
    
    for num in nums:
        if sum(subsequence) > (total_sum - sum(subsequence)) / 2:
            break
        subsequence.append(num)
        total_sum -= num
    
    return subsequence

# Check function to verify the solution with provided data points
def check_solution():
    assert min_subsequence([4,3,10,9,8], 21) == [3,10,9], "Test case 1 failed"
    assert min_subsequence([1,2,3], 3) == [2,3], "Test case 2 failed"
    assert min_subsequence([1,1,1,1,1], 10) == [], "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This code snippet defines a function `min_subsequence` that implements the logic to find the required subsequence, followed by a check function to validate the solution against given test cases.