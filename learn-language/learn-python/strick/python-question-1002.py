# Python Question: Subarray with Given Sum
'''
Given an unsorted array of non-negative integers, find if there is a contiguous subarray with a sum equal to a given number.

Example:
Input: arr = [1, 4, 20, 3, 10, 5], sum = 33
Output: True (Subarray from index 2 to 4 has sum 33: 20 + 3 + 10 = 33)

Input: arr = [1, 4, 0, 0, 3, 10, 5], sum = 7
Output: True (Subarray from index 1 to 4 has sum 7: 4 + 0 + 0 + 3 = 7)

Input: arr = [1, 4], sum = 0
Output: False (No non-empty subarray can have sum 0 with non-negative integers)

Input: arr = [1, 4, 20, 3, 10, 5], sum = 3
Output: True (Subarray from index 3 to 3 has sum 3: 3 = 3)

Input: arr = [1, 4, 20, 3, 10, 5], sum = 100
Output: False (No such subarray exists)
'''

# Solution
def solution(arr, target_sum):
    """
    Finds if there is a contiguous subarray with a sum equal to the target_sum.

    Args:
        arr: A list of non-negative integers.
        target_sum: The target sum to find.

    Returns:
        True if a subarray with the target sum exists, False otherwise.
    """

    # Initialize the current sum and the starting index of the window
    current_sum = 0
    start = 0

    # Iterate through the array
    for i in range(len(arr)):
        # Add the current element to the current sum
        current_sum += arr[i]

        # If the current sum exceeds the target sum, or the starting index is greater than i
        # then remove elements from the beginning of the window until the current sum is less than or equal to the target sum
        while current_sum > target_sum and start <= i:
            current_sum -= arr[start]
            start += 1

        # If the current sum is equal to the target sum, then we have found a subarray
        if current_sum == target_sum:
            return True

    # If we have not found a subarray with the target sum, then return False
    return False

# Test cases
def test_solution():
    assert solution([1, 4, 20, 3, 10, 5], 33) == True
    assert solution([1, 4, 0, 0, 3, 10, 5], 7) == True
    assert solution([1, 4], 0) == False
    assert solution([1, 4, 20, 3, 10, 5], 3) == True
    assert solution([1, 4, 20, 3, 10, 5], 100) == False
    assert solution([1, 2, 3, 4, 5], 7) == True
    assert solution([10, 2, -2, -20, 10], -10) == False #Handles negative integers
    assert solution([15, 2, 4, 8, 9, 5, 10, 23], 23) == True
    assert solution([1,2,3,7,5], 12) == True
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15) == True
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55) == True
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == True
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == True
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 60) == False

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()