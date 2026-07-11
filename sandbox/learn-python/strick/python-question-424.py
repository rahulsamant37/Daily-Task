# Python Question: Find the Largest Non-Adjacent Sum
'''
Given a list of integers, find the largest sum of non-adjacent numbers. Numbers at indices i and i+1 cannot both be included in the sum.

For example:
Input: [2, 4, 6, 2, 5]
Output: 13 (2 + 6 + 5)

Input: [5, 1, 1, 5]
Output: 10 (5 + 5)

Constraint: You cannot use built-in functions like max() with iterables.
'''

# Solution
def solution():
    def largest_non_adjacent_sum(nums):
        """
        Calculates the largest sum of non-adjacent numbers in a list.

        Args:
            nums: A list of integers.

        Returns:
            The largest sum of non-adjacent numbers.
        """

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # Initialize two variables:
        #   - incl: The maximum sum including the current element.
        #   - excl: The maximum sum excluding the current element.
        incl = nums[0]
        excl = 0

        # Iterate through the remaining elements of the list.
        for i in range(1, len(nums)):
            # The new 'incl' will be the old 'excl' plus the current element.
            # We take the old 'excl' because we cannot include the adjacent element.
            new_incl = excl + nums[i]

            # The new 'excl' will be the maximum of the old 'incl' and 'excl'.
            # This is because we can either include the previous element or not.
            new_excl = incl if incl > excl else excl # No built-in max() usage

            # Update 'incl' and 'excl' for the next iteration.
            incl = new_incl
            excl = new_excl

        # The final result is the maximum of 'incl' and 'excl',
        # representing whether we included the last element or not.
        return incl if incl > excl else excl # No built-in max() usage
    return largest_non_adjacent_sum

# Test cases
def test_solution():
    largest_non_adjacent_sum = solution()
    assert largest_non_adjacent_sum([]) == 0
    assert largest_non_adjacent_sum([1]) == 1
    assert largest_non_adjacent_sum([2, 4, 6, 2, 5]) == 13
    assert largest_non_adjacent_sum([5, 1, 1, 5]) == 10
    assert largest_non_adjacent_sum([5, 5, 10, 100, 10, 5]) == 110
    assert largest_non_adjacent_sum([1, 2, 3]) == 4
    assert largest_non_adjacent_sum([1, 20, 3, 40]) == 60
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()