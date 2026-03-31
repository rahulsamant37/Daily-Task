# Python Question: Find the largest number that can be divided by each number from 2 to n without any remainder

"""
For example, consider the following numbers: 6, 8, 9.

Input: List of numbers [6, 8, 9]
Output: 6 (as 6 is the largest number that can be divided without any remainder by 2, 3, and 4)
"""

def largest_divisible_by(nums):
    """
    Returns the largest number from the given list that can be divided by each number from 2 to n without any remainder.
    """
    largest = nums[0]
    for num in nums[1:]:
        if largest % num == 0:
            largest = max(largest, num)
    return largest

def test_largest_divisible_by():
    """
    Test the largest_divisible_by function with various input lists.
    """
    assert largest_divisible_by([6, 8, 9]) == 6
    assert largest_divisible_by([10, 15, 20]) == 10
    assert largest_divisible_by([1, 2, 3, 4]) == 1
    assert largest_divisible_by([3, 6, 9]) == 3

if __name__ == "__main__":
    test_largest_divisible_by()