# Python Question: Maximum Non-Adjacent Sum
'''
Given a list of integers, find the maximum sum of non-adjacent elements. You cannot include adjacent numbers in the sum.

Example:
Input: [5, 5, 10, 100, 10, 5]
Output: 110 (5 + 100 + 5)

Input: [3, 2, 7, 10]
Output: 13 (3 + 10)

Input: [3, 2, 5, 10, 7]
Output: 15 (3 + 5 + 7) or (2 + 10 + 3)
'''

# Solution
def solution():
    def max_non_adjacent_sum(nums):
        """
        Calculates the maximum sum of non-adjacent elements in a list.

        Args:
            nums: A list of integers.

        Returns:
            The maximum sum of non-adjacent elements.
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # Initialize two variables:
        # include: Maximum sum including the current element
        # exclude: Maximum sum excluding the current element
        include = nums[0]
        exclude = 0

        # Iterate through the remaining elements
        for i in range(1, len(nums)):
            # The new 'include' is the previous 'exclude' plus the current element
            new_include = exclude + nums[i]

            # The new 'exclude' is the maximum of the previous 'include' and 'exclude'
            new_exclude = max(include, exclude)

            # Update include and exclude for the next iteration
            include = new_include
            exclude = new_exclude

        # The final result is the maximum of the last 'include' and 'exclude'
        return max(include, exclude)

    return max_non_adjacent_sum


# Test cases
def test_solution():
    max_non_adjacent_sum = solution()
    assert max_non_adjacent_sum([]) == 0
    assert max_non_adjacent_sum([1]) == 1
    assert max_non_adjacent_sum([1, 2]) == 2
    assert max_non_adjacent_sum([5, 5, 10, 100, 10, 5]) == 110
    assert max_non_adjacent_sum([3, 2, 7, 10]) == 13
    assert max_non_adjacent_sum([3, 2, 5, 10, 7]) == 15
    assert max_non_adjacent_sum([1, 2, 3, 1]) == 4
    assert max_non_adjacent_sum([1, 20, 3, 10, 1]) == 31
    assert max_non_adjacent_sum([-1, -2, -3, -1]) == 0 # Handle all negative numbers
    assert max_non_adjacent_sum([-1, 2, -3, 4, -5]) == 6
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()