# Python Question: Find the Maximum Sum of Non-Adjacent Elements in an Array
'''
Given an array of integers (positive, negative, or zero), find the maximum sum of a subsequence with the constraint that no two numbers in the subsequence are adjacent in the array.

Example:
Input: [5, 5, 10, 100, 10, 5]
Output: 110 (5 + 100 + 5)

Input: [1, 2, 3]
Output: 4 (1 + 3)

Input: [1, 20, 3]
Output: 20
'''

# Solution
def solution():
    def max_sum_non_adjacent(arr):
        """
        Calculates the maximum sum of non-adjacent elements in an array.

        Args:
            arr: A list of integers.

        Returns:
            The maximum sum of non-adjacent elements.
        """

        if not arr:
            return 0

        if len(arr) == 1:
            return arr[0]

        # Initialize two variables:
        # include: Maximum sum including the current element.
        # exclude: Maximum sum excluding the current element.
        include = arr[0]
        exclude = 0

        # Iterate through the array starting from the second element.
        for i in range(1, len(arr)):
            # The new 'include' will be the previous 'exclude' plus the current element.
            new_include = exclude + arr[i]

            # The new 'exclude' will be the maximum of the previous 'include' and 'exclude'.
            new_exclude = max(include, exclude)

            # Update 'include' and 'exclude' for the next iteration.
            include = new_include
            exclude = new_exclude

        # The final result is the maximum of the last 'include' and 'exclude'.
        return max(include, exclude)

    return max_sum_non_adjacent

# Test cases
def test_solution():
    func = solution()

    # Test case 1
    arr1 = [5, 5, 10, 100, 10, 5]
    expected1 = 110
    assert func(arr1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {func(arr1)}"

    # Test case 2
    arr2 = [1, 2, 3]
    expected2 = 4
    assert func(arr2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {func(arr2)}"

    # Test case 3
    arr3 = [1, 20, 3]
    expected3 = 20
    assert func(arr3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {func(arr3)}"

    # Test case 4
    arr4 = [1, 2, 3, 4, 5]
    expected4 = 9
    assert func(arr4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {func(arr4)}"

    # Test case 5: Empty array
    arr5 = []
    expected5 = 0
    assert func(arr5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {func(arr5)}"

    # Test case 6: Single element array
    arr6 = [5]
    expected6 = 5
    assert func(arr6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {func(arr6)}"

    # Test case 7: All negative numbers
    arr7 = [-1, -2, -3]
    expected7 = -1
    assert func(arr7) == -1, f"Test Case 7 Failed: Expected {expected7}, Got {func(arr7)}"

    # Test case 8: Mixed positive and negative
    arr8 = [5, -1, -2, 6]
    expected8 = 11
    assert func(arr8) == 11, f"Test Case 8 Failed: Expected {expected8}, Got {func(arr8)}"
    
    # Test case 9: Array with zeros
    arr9 = [0, 0, 0]
    expected9 = 0
    assert func(arr9) == 0, f"Test Case 9 Failed: Expected {expected9}, Got {func(arr9)}"
    
    # Test case 10: Array with zeros and positives
    arr10 = [0, 1, 0, 2]
    expected10 = 2
    assert func(arr10) == 2, f"Test Case 10 Failed: Expected {expected10}, Got {func(arr10)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()