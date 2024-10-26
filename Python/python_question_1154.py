# Python Question: Largest Sum Contiguous Subarray (Kadane's Algorithm)
'''
Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.

Input: [1]
Output: 1

Input: [-1, -2, -3]
Output: -1
'''

# Solution
def solution(nums):
    """
    Finds the largest sum contiguous subarray using Kadane's Algorithm.

    Kadane's Algorithm:
    1. Initialize max_so_far and current_max to the first element of the array.
    2. Iterate through the array from the second element.
    3. For each element, update current_max by taking the maximum of the current element and the sum of current_max and the current element.
    4. Update max_so_far by taking the maximum of max_so_far and current_max.
    5. Return max_so_far.

    Args:
        nums: A list of integers.

    Returns:
        The largest sum of any contiguous subarray in the input array.
    """
    if not nums:
        return 0

    max_so_far = nums[0]  # Initialize max_so_far with the first element
    current_max = nums[0] # Initialize current_max with the first element

    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i]) # Decide whether to start a new subarray from current element or extend the previous one
        max_so_far = max(max_so_far, current_max)       # Update max_so_far if current_max is greater

    return max_so_far


# Test cases
def test_solution():
    assert solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solution([1]) == 1
    assert solution([-1, -2, -3]) == -1
    assert solution([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
    assert solution([5, 4, -1, 7, 8]) == 23
    assert solution([]) == 0
    assert solution([-1]) == -1
    assert solution([0]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()