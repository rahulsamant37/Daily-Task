# Python Question: Longest Increasing Subsequence with Specific Sum
'''
Given an array of positive integers `nums` and a target sum `target`, find the length of the longest increasing subsequence (LIS) of `nums` such that the sum of the elements in the LIS equals the `target`. If no such LIS exists, return 0.

An increasing subsequence is a sequence of elements from the array `nums` that are in increasing order but not necessarily contiguous.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 9
Output: 3
Explanation: The longest increasing subsequence with a sum of 9 is [1, 3, 5] or [2, 3, 4], both of length 3.

Input: nums = [4, 3, 2, 1], target = 10
Output: 0
Explanation: No increasing subsequence exists with a sum of 10.

Input: nums = [1, 5, 2, 8, 3, 9, 4, 10], target = 14
Output: 3
Explanation: The longest increasing subsequence with a sum of 14 is [1, 5, 8] or [2, 3, 9] or [5, 9], etc.
'''

# Solution
def longest_increasing_subsequence_with_sum(nums, target):
    """
    Finds the length of the longest increasing subsequence of `nums` with sum `target`.

    Args:
        nums: A list of positive integers.
        target: The target sum.

    Returns:
        The length of the longest increasing subsequence with sum `target`, or 0 if none exists.
    """

    n = len(nums)
    dp = {}  # dp[index, sum, last_val] = length of LIS ending at index with given sum and last value

    def solve(index, current_sum, last_val):
        """
        Recursive helper function to find the length of the LIS.

        Args:
            index: The current index being considered.
            current_sum: The current sum of the subsequence.
            last_val: The last value added to the subsequence.

        Returns:
            The length of the longest increasing subsequence.
        """

        if (index, current_sum, last_val) in dp:
            return dp[(index, current_sum, last_val)]

        if current_sum == target:
            return 0  # Base case: Target sum reached, return 0 as we don't need to add anything more

        if index == n:
            return float('-inf')  # Base case: Reached the end of the array, return -inf as target not reached.

        # Option 1: Exclude the current element
        exclude = solve(index + 1, current_sum, last_val)

        # Option 2: Include the current element if it's greater than the last value and the sum doesn't exceed target
        include = float('-inf')
        if nums[index] > last_val and current_sum + nums[index] <= target:
            include = 1 + solve(index + 1, current_sum + nums[index], nums[index])

        dp[(index, current_sum, last_val)] = max(exclude, include)
        return dp[(index, current_sum, last_val)]

    result = solve(0, 0, float('-inf'))  # Start from index 0, sum 0, last_val -inf
    return max(0, result)  # Return 0 if no solution exists (result is -inf)


# Test cases
def test_solution():
    """
    Tests the longest_increasing_subsequence_with_sum function.
    """
    assert longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 9) == 3
    assert longest_increasing_subsequence_with_sum([4, 3, 2, 1], 10) == 0
    assert longest_increasing_subsequence_with_sum([1, 5, 2, 8, 3, 9, 4, 10], 14) == 3
    assert longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 15) == 5
    assert longest_increasing_subsequence_with_sum([10, 5, 2, 8, 3, 9, 4, 1], 15) == 0
    assert longest_increasing_subsequence_with_sum([1, 3, 5], 9) == 0
    assert longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 1) == 1
    assert longest_increasing_subsequence_with_sum([1, 1, 1, 1, 1], 5) == 0
    assert longest_increasing_subsequence_with_sum([2,4,6,8,10], 20) == 3
    assert longest_increasing_subsequence_with_sum([1,2,3,4,5,6,7,8,9,10], 30) == 5

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()