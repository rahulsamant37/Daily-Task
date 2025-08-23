# DSA Problem 150

'''
Problem Statement:
In a unique town, there's a special kind of lottery where participants choose a sequence of numbers. The lottery organizers, however, have a peculiar rule: they only accept sequences where the sum of the first half of the numbers equals the sum of the second half. Moreover, the sequence must contain an even number of elements.

Given a list of integers, your task is to determine if it's possible to rearrange these integers to form a valid sequence for the lottery. If it's possible, return True; otherwise, return False.

Example:
Input: [1, 2, 3, 3]
Output: True
Explanation: The sequence can be rearranged into [1, 3, 3, 2] where the sum of the first half (1+3) equals the sum of the second half (3+2).
'''

Solution:
def is_valid_lottery_sequence(arr):
    from itertools import permutations
    
    # Check if the array length is even
    if len(arr) % 2 != 0:
        return False
    
    # Try all permutations of the array
    for perm in permutations(arr):
        mid = len(arr) // 2
        if sum(perm[:mid]) == sum(perm[mid:]):
            return True
    return False

# Test cases to verify the correctness
def check_function():
    assert is_valid_lottery_sequence([1, 2, 3, 3]) == True, "Test case 1 failed"
    assert is_valid_lottery_sequence([1, 2, 3, 4]) == False, "Test case 2 failed"
    assert is_valid_lottery_sequence([3, 3, 3, 3]) == True, "Test case 3 failed"
    assert is_valid_lottery_sequence([1, 2, 3, 4, 5, 5]) == True, "Test case 4 failed"
    print("All test cases passed!")

check_function()