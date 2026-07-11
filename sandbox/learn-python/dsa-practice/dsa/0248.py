# DSA Problem 248

'''
Problem Statement:
Alice has a list of integers and wants to rearrange it so that every even-indexed element is even and every odd-indexed element is odd. She can perform the following operations any number of times:
- Swap any two elements at even indices.
- Swap any two elements at odd indices.

Given a list of integers `nums`, return `True` if Alice can rearrange the list to meet the above conditions, otherwise return `False`.

Example:
Input: nums = [4, 2, 5, 3]
Output: True
Explanation: The list already satisfies the condition, as 4 and 5 are at even indices and 2 and 3 are at odd indices.
'''

Solution:
def canRearrange(nums):
    """
    Checks if the given list can be rearranged so that every even-indexed element is even and every odd-indexed element is odd.
    """
    even_misplaced = 0
    odd_misplaced = 0
    for i in range(len(nums)):
        if i % 2 == 0 and nums[i] % 2 != 0:
            even_misplaced += 1
        elif i % 2 != 0 and nums[i] % 2 == 0:
            odd_misplaced += 1
    return even_misplaced == odd_misplaced

# Test the function with an example
nums = [4, 2, 5, 3]
print(canRearrange(nums))  # Output: True

# Additional check function to verify the correctness of the solution
def check_solution():
    test_cases = [
        ([4, 2, 5, 3], True),
        ([1, 3, 5, 7], False),
        ([2, 1, 6, 5], True)
    ]
    for nums, expected in test_cases:
        assert canRearrange(nums) == expected, f"Failed for {nums}"
    print("All test cases passed!")

check_solution()