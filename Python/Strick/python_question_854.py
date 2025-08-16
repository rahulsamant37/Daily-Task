# Python Question: Find the Maximum Sum of Non-Adjacent Elements in an Array
'''
Given an array of integers, find the maximum sum of non-adjacent elements.
You are not allowed to select adjacent elements.

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
        Finds the maximum sum of non-adjacent elements in an array.

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
        # include: max sum including the current element
        # exclude: max sum excluding the current element
        include = arr[0]
        exclude = 0

        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            # The new 'include' will be the previous 'exclude' plus the current element.
            # We can only include the current element if we excluded the previous one.
            new_include = exclude + arr[i]

            # The new 'exclude' will be the maximum of the previous 'include' and 'exclude'.
            # We exclude the current element, so we take the maximum of the previous
            # 'include' and 'exclude' because we want the best result so far.
            new_exclude = max(include, exclude)

            # Update 'include' and 'exclude' for the next iteration.
            include = new_include
            exclude = new_exclude

        # Finally, return the maximum of the last 'include' and 'exclude'.
        # This will give us the maximum sum of non-adjacent elements.
        return max(include, exclude)

    return max_sum_non_adjacent

# Test cases
def test_solution():
    max_sum_non_adjacent = solution()

    assert max_sum_non_adjacent([5, 5, 10, 100, 10, 5]) == 110, "Test Case 1 Failed"
    assert max_sum_non_adjacent([1, 2, 3]) == 4, "Test Case 2 Failed"
    assert max_sum_non_adjacent([1, 20, 3]) == 20, "Test Case 3 Failed"
    assert max_sum_non_adjacent([1, 2, 3, 4, 5]) == 9, "Test Case 4 Failed"
    assert max_sum_non_adjacent([5, 1, 1, 5]) == 10, "Test Case 5 Failed"
    assert max_sum_non_adjacent([]) == 0, "Test Case 6 Failed"
    assert max_sum_non_adjacent([1]) == 1, "Test Case 7 Failed"
    assert max_sum_non_adjacent([1, 2]) == 2, "Test Case 8 Failed"
    assert max_sum_non_adjacent([-1, -2, -3]) == 0, "Test Case 9 Failed" #Handles negative numbers correctly
    assert max_sum_non_adjacent([-1, 2, -3]) == 2, "Test Case 10 Failed" #Handles negative numbers correctly
    assert max_sum_non_adjacent([-1, 2, 3]) == 3, "Test Case 11 Failed"
    assert max_sum_non_adjacent([2, 1, 4, 5, 3]) == 9, "Test Case 12 Failed"
    assert max_sum_non_adjacent([10, 5, 20, 4, 50]) == 80, "Test Case 13 Failed"
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()