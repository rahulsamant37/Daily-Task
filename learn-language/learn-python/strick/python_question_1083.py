# Python Question: Largest Sum Contiguous Subarray (Kadane's Algorithm)
'''
Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.
'''

# Solution
def solution():
    def max_subarray_sum(arr):
        """
        Finds the largest sum of a contiguous subarray using Kadane's Algorithm.

        Args:
            arr: A list of integers.

        Returns:
            The largest sum of any contiguous subarray within the input array.
        """
        max_so_far = float('-inf')  # Initialize the maximum sum found so far to negative infinity
        current_max = 0  # Initialize the current maximum sum to 0

        for i in range(len(arr)):
            current_max += arr[i]  # Add the current element to the current maximum sum

            if current_max > max_so_far:
                max_so_far = current_max  # Update the maximum sum found so far if the current sum is larger

            if current_max < 0:
                current_max = 0  # Reset the current sum to 0 if it becomes negative,
                                  # as a negative sum will only decrease subsequent subarray sums

        return max_so_far  # Return the largest sum found

    return max_subarray_sum

# Test cases
def test_solution():
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert solution()(arr1) == 6, "Test Case 1 Failed"

    arr2 = [1, 2, 3, 4, 5]
    assert solution()(arr2) == 15, "Test Case 2 Failed"

    arr3 = [-1, -2, -3, -4, -5]
    assert solution()(arr3) == -1, "Test Case 3 Failed"

    arr4 = [-2, -3, 4, -1, -2, 1, 5, -3]
    assert solution()(arr4) == 7, "Test Case 4 Failed"

    arr5 = [5, 4, -1, 7, 8]
    assert solution()(arr5) == 23, "Test Case 5 Failed"

    arr6 = [-10]
    assert solution()(arr6) == -10, "Test Case 6 Failed"

    arr7 = [0]
    assert solution()(arr7) == 0, "Test Case 7 Failed"

    arr8 = [-1, 0, -2]
    assert solution()(arr8) == 0, "Test Case 8 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()