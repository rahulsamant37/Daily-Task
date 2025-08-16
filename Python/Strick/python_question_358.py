# Python Question: Largest Subarray with Equal Number of 0s and 1s
'''
Given an array containing only 0s and 1s, find the length of the largest contiguous subarray with an equal number of 0s and 1s.

Example:
Input: [0, 1, 0, 0, 1, 1, 0]
Output: 6
Explanation: The subarray [0, 1, 0, 0, 1, 1] has an equal number of 0s and 1s (3 zeros and 3 ones) and is the largest such subarray.

Input: [1, 0, 1, 1, 0, 0]
Output: 6
Explanation: The entire array [1, 0, 1, 1, 0, 0] has equal number of 0s and 1s (3 zeros and 3 ones).

Input: [1, 1, 1, 1]
Output: 0
Explanation: There is no subarray with equal number of 0s and 1s.
'''

# Solution
def solution(arr):
    """
    Finds the length of the largest subarray with an equal number of 0s and 1s.

    Args:
        arr: A list of integers containing only 0s and 1s.

    Returns:
        The length of the largest subarray with an equal number of 0s and 1s.
    """

    # Replace 0s with -1 to simplify the calculation.
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1

    # Use a dictionary to store the cumulative sum and its first occurrence index.
    sum_index = {}
    curr_sum = 0
    max_len = 0

    # Initialize the dictionary with a sum of 0 at index -1.
    sum_index[0] = -1

    # Iterate through the array and calculate the cumulative sum.
    for i in range(len(arr)):
        curr_sum += arr[i]

        # If the current sum is 0, update the maximum length.
        if curr_sum == 0:
            max_len = i + 1

        # If the current sum is already in the dictionary,
        # it means we have found a subarray with an equal number of 0s and 1s.
        if curr_sum in sum_index:
            max_len = max(max_len, i - sum_index[curr_sum])
        else:
            # If the current sum is not in the dictionary, add it along with its index.
            sum_index[curr_sum] = i

    # Return the maximum length.
    return max_len

# Test cases
def test_solution():
    assert solution([0, 1, 0, 0, 1, 1, 0]) == 6
    assert solution([1, 0, 1, 1, 0, 0]) == 6
    assert solution([1, 1, 1, 1]) == 0
    assert solution([0, 0, 0, 0]) == 0
    assert solution([0, 1]) == 2
    assert solution([1, 0]) == 2
    assert solution([0, 1, 1, 0, 1, 1, 1, 0, 0]) == 8
    assert solution([]) == 0
    assert solution([1]) == 0
    assert solution([0]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()