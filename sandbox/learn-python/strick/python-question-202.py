# Python Question: Find the Maximum Sum of Non-Adjacent Elements in an Array
'''
Given an array of integers, find the maximum sum of non-adjacent elements. You are not allowed to pick adjacent elements.

Example:
Input: [5, 5, 10, 100, 10, 5]
Output: 110 (5 + 100 + 5)

Input: [1, 2, 3]
Output: 4 (1 + 3)

Input: [1, 20, 3]
Output: 20

Input: [5, 1, 1, 5]
Output: 10 (5 + 5)
'''

# Solution
def solution():
    def max_non_adjacent_sum(arr):
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
        # incl: Maximum sum including the current element
        # excl: Maximum sum excluding the current element
        incl = arr[0]
        excl = 0

        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            # New excl will be the maximum of the previous incl and excl
            new_excl = max(incl, excl)

            # New incl will be the previous excl plus the current element
            incl = excl + arr[i]
            excl = new_excl

        # Return the maximum of the final incl and excl
        return max(incl, excl)
    
    return max_non_adjacent_sum


# Test cases
def test_solution():
    def assert_equal(actual, expected, message=""):
        if actual != expected:
            print(f"Assertion failed: {message}")
            print(f"Expected: {expected}, Actual: {actual}")
            assert actual == expected

    max_non_adjacent_sum = solution()

    assert_equal(max_non_adjacent_sum([]), 0, "Empty array")
    assert_equal(max_non_adjacent_sum([1]), 1, "Single element array")
    assert_equal(max_non_adjacent_sum([1, 2]), 2, "Two element array")
    assert_equal(max_non_adjacent_sum([1, 2, 3]), 4, "Three element array")
    assert_equal(max_non_adjacent_sum([5, 5, 10, 100, 10, 5]), 110, "Example 1")
    assert_equal(max_non_adjacent_sum([1, 20, 3]), 20, "Example 2")
    assert_equal(max_non_adjacent_sum([5, 1, 1, 5]), 10, "Example 3")
    assert_equal(max_non_adjacent_sum([1, 0, 3, 9, 2]), 11, "Test case 1")
    assert_equal(max_non_adjacent_sum([1, 2, 3, 4, 5]), 9, "Test case 2")
    assert_equal(max_non_adjacent_sum([5, 1, 1, 5, 2, 10]), 15, "Test case 3")

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()