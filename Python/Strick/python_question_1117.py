# Python Question: Subarray with Given Sum (Sliding Window)
'''
Given an array of positive integers `arr` and a target sum `target`, find a contiguous subarray in `arr` that adds up to `target`. Return the starting and ending indices (inclusive) of the subarray if it exists. If multiple such subarrays exist, return the leftmost one. If no such subarray exists, return [-1].

Example:
Input: arr = [1, 4, 20, 3, 10, 5], target = 33
Output: [2, 4]

Input: arr = [1, 4, 0, 0, 3, 10, 5], target = 7
Output: [1, 4]

Input: arr = [1, 4], target = 0
Output: [-1]

Input: arr = [10, 2, -2, -20, 10], target = -10
Output: [-1] # Only positive integers are allowed

Input: arr = [1, 2, 3, 4, 5], target = 15
Output: [0, 4]

Input: arr = [1, 2, 3, 7, 5], target = 12
Output: [1, 3]
'''

# Solution
def solution(arr, target):
    """
    Finds a contiguous subarray in arr that sums to target using the sliding window technique.

    Args:
        arr: A list of positive integers.
        target: The target sum.

    Returns:
        A list containing the starting and ending indices (inclusive) of the subarray if it exists.
        Returns [-1] if no such subarray exists.
    """

    if not all(x > 0 for x in arr):
        return [-1]

    window_start = 0
    window_end = 0
    current_sum = 0

    while window_end < len(arr):
        current_sum += arr[window_end]

        while current_sum > target:
            current_sum -= arr[window_start]
            window_start += 1

        if current_sum == target:
            return [window_start, window_end]

        window_end += 1

    return [-1]

# Test cases
def test_solution():
    assert solution([1, 4, 20, 3, 10, 5], 33) == [2, 4]
    assert solution([1, 4, 0, 0, 3, 10, 5], 7) == [-1] #Contains zeros, but only positive integers are allowed.
    assert solution([1, 4], 0) == [-1]
    assert solution([10, 2, -2, -20, 10], -10) == [-1] #Contains negative integers
    assert solution([1, 2, 3, 4, 5], 15) == [0, 4]
    assert solution([1, 2, 3, 7, 5], 12) == [1, 3]
    assert solution([1, 2, 1, 3], 4) == [0, 2]
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15) == [0, 4]
    assert solution([1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10], 15) == [-1]
    assert solution([1, 2, 3, 4, 5], 1) == [0, 0]
    assert solution([1], 1) == [0, 0]
    assert solution([1], 2) == [-1]
    assert solution([], 5) == [-1]

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()