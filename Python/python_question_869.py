# Python Question: Maximum Non-Adjacent Subset Sum
'''
Given an array of integers, find the maximum sum of a subset of the array such that no two numbers in the subset are adjacent in the array.

Example:
Input: [5, 5, 10, 100, 10, 5]
Output: 110 (5 + 100 + 5)
'''

# Solution
def solution():
    def max_non_adjacent_subset_sum(arr):
        """
        Calculates the maximum sum of a non-adjacent subset.

        Args:
            arr: A list of integers.

        Returns:
            The maximum sum of a non-adjacent subset.
        """
        if not arr:
            return 0

        if len(arr) == 1:
            return arr[0]

        # Initialize two variables:
        # include: The maximum sum including the current element.
        # exclude: The maximum sum excluding the current element.
        include = arr[0]
        exclude = 0

        # Iterate through the array starting from the second element.
        for i in range(1, len(arr)):
            # The new 'include' value will be the previous 'exclude' value plus the current element.
            # This is because if we include the current element, we cannot include the previous one.
            new_include = exclude + arr[i]

            # The new 'exclude' value will be the maximum of the previous 'include' and 'exclude' values.
            # This is because if we exclude the current element, we can either include or exclude the previous one,
            # so we choose the option that gives us the maximum sum.
            new_exclude = max(include, exclude)

            # Update 'include' and 'exclude' for the next iteration.
            include = new_include
            exclude = new_exclude

        # The final result will be the maximum of the last 'include' and 'exclude' values.
        return max(include, exclude)
    return max_non_adjacent_subset_sum
    # Test cases
def test_solution():
    def assert_equal(actual, expected, message=""):
        if actual != expected:
            print(f"Assertion failed: {message}")
            print(f"Expected: {expected}")
            print(f"Actual: {actual}")
            raise AssertionError

    max_non_adjacent_subset_sum = solution()

    # Test case 1
    arr1 = [5, 5, 10, 100, 10, 5]
    expected1 = 110
    assert_equal(max_non_adjacent_subset_sum(arr1), expected1, "Test Case 1 Failed")

    # Test case 2
    arr2 = [1, 2, 3]
    expected2 = 4
    assert_equal(max_non_adjacent_subset_sum(arr2), expected2, "Test Case 2 Failed")

    # Test case 3
    arr3 = [1, 20, 3]
    expected3 = 20
    assert_equal(max_non_adjacent_subset_sum(arr3), expected3, "Test Case 3 Failed")

    # Test case 4
    arr4 = [5, 1, 1, 5]
    expected4 = 10
    assert_equal(max_non_adjacent_subset_sum(arr4), expected4, "Test Case 4 Failed")

    # Test case 5
    arr5 = []
    expected5 = 0
    assert_equal(max_non_adjacent_subset_sum(arr5), expected5, "Test Case 5 Failed")

    # Test case 6
    arr6 = [1]
    expected6 = 1
    assert_equal(max_non_adjacent_subset_sum(arr6), expected6, "Test Case 6 Failed")

    # Test case 7
    arr7 = [1, 2]
    expected7 = 2
    assert_equal(max_non_adjacent_subset_sum(arr7), expected7, "Test Case 7 Failed")

    # Test case 8
    arr8 = [2, 1]
    expected8 = 2
    assert_equal(max_non_adjacent_subset_sum(arr8), expected8, "Test Case 8 Failed")

    # Test case 9
    arr9 = [10, 2, 3, 20, 5, 10]
    expected9 = 40
    assert_equal(max_non_adjacent_subset_sum(arr9), expected9, "Test Case 9 Failed")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()