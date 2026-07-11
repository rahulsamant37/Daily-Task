# Python Question: Largest Sum Contiguous Subarray
'''
Given an array of integers, find the contiguous subarray with the largest sum.

Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.
'''

# Solution
def largest_sum_contiguous_subarray(arr):
    """
    Finds the contiguous subarray with the largest sum in a given array.

    Args:
        arr: A list of integers.

    Returns:
        The largest sum of any contiguous subarray in the input array.
    """
    # Initialize max_so_far to the smallest possible integer value to ensure that even arrays with all negative numbers are handled correctly.
    max_so_far = float('-inf')
    current_max = 0

    # Iterate through the array
    for i in range(len(arr)):
        # Update current_max by adding the current element
        current_max += arr[i]

        # If current_max is greater than max_so_far, update max_so_far
        if current_max > max_so_far:
            max_so_far = current_max

        # If current_max becomes negative, reset it to 0, as a negative sum cannot contribute to a larger overall sum
        if current_max < 0:
            current_max = 0

    return max_so_far

# Test cases
def test_largest_sum_contiguous_subarray():
    """
    Tests the largest_sum_contiguous_subarray function with various test cases.
    """
    # Test case 1: Basic test case
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected1 = 6
    assert largest_sum_contiguous_subarray(arr1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {largest_sum_contiguous_subarray(arr1)}"

    # Test case 2: Array with all negative numbers
    arr2 = [-1, -2, -3, -4]
    expected2 = -1
    assert largest_sum_contiguous_subarray(arr2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {largest_sum_contiguous_subarray(arr2)}"

    # Test case 3: Array with all positive numbers
    arr3 = [1, 2, 3, 4]
    expected3 = 10
    assert largest_sum_contiguous_subarray(arr3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {largest_sum_contiguous_subarray(arr3)}"

    # Test case 4: Array with a single element
    arr4 = [5]
    expected4 = 5
    assert largest_sum_contiguous_subarray(arr4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {largest_sum_contiguous_subarray(arr4)}"

    # Test case 5: Array with a single negative element
    arr5 = [-5]
    expected5 = -5
    assert largest_sum_contiguous_subarray(arr5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {largest_sum_contiguous_subarray(arr5)}"

    # Test case 6: Array with zero
    arr6 = [0]
    expected6 = 0
    assert largest_sum_contiguous_subarray(arr6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {largest_sum_contiguous_subarray(arr6)}"

    # Test case 7: Array with zero and some negative and positive numbers
    arr7 = [-1, 0, -2, 3, -1]
    expected7 = 3
    assert largest_sum_contiguous_subarray(arr7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {largest_sum_contiguous_subarray(arr7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_largest_sum_contiguous_subarray()