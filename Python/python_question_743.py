# Python Question: Longest Increasing Subsequence with Specific Sum
'''
Given an array of positive integers `nums` and a target sum `target`, find the length of the longest increasing subsequence (LIS) in `nums` that sums up to the `target`. If no such subsequence exists, return 0.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 9
Output: 4
Explanation: The subsequence [1, 2, 3, 3] is not increasing.  The longest increasing subsequence that sums to 9 is [1, 2, 3, 3]. The longest *increasing* subsequence that sums to 9 is [2,3,4], which has length 3. But the problem statement implies that [1, 2, 3, 3] should not be considered increasing, even if the numbers are non-decreasing. The correct increasing subsequence summing to 9 is [2,3,4], which has length 3.

Input: nums = [4, 3, 2, 1], target = 10
Output: 0
Explanation: No increasing subsequence sums up to 10.

Input: nums = [1, 3, 2, 4, 5], target = 7
Output: 3
Explanation: The longest increasing subsequence that sums to 7 is [1, 2, 4], which has length 3.
'''

# Solution
def longest_increasing_subsequence_sum_target(nums, target):
    """
    Finds the length of the longest increasing subsequence in nums that sums up to the target.

    Args:
        nums: A list of positive integers.
        target: The target sum.

    Returns:
        The length of the longest increasing subsequence that sums up to the target.
    """

    n = len(nums)
    # dp[i][j] stores the length of the longest increasing subsequence ending at index i with a sum of j.
    dp = {}  # Dictionary to store (index, sum): length

    def solve(index, current_sum, last_element):
        """
        Recursive helper function to find the LIS length.

        Args:
            index: The current index in the nums array.
            current_sum: The current sum of the subsequence.
            last_element: The last element added to the subsequence (used to maintain increasing order).

        Returns:
            The length of the longest increasing subsequence.
        """

        # Base cases
        if current_sum == target:
            return 0  # Found a valid subsequence, return 0 to add length of the current one.
        if index == n:
            return float('-inf')  # Reached the end of the array, no valid subsequence found.
        if current_sum > target:
            return float('-inf')  # Sum exceeded the target, no valid subsequence found.

        # Memoization
        if (index, current_sum, last_element) in dp: #Added last_element to the key
            return dp[(index, current_sum, last_element)]

        # Two options: either include the current element or exclude it.
        # Option 1: Exclude the current element
        exclude = solve(index + 1, current_sum, last_element)

        # Option 2: Include the current element if it's greater than the last element in the subsequence
        include = float('-inf')
        if nums[index] > last_element:
            include = 1 + solve(index + 1, current_sum + nums[index], nums[index])

        # Store the result in the memoization table
        dp[(index, current_sum, last_element)] = max(include, exclude)
        return dp[(index, current_sum, last_element)]

    # Start the recursion with index 0, current sum 0, and a last element of negative infinity (to allow any element to be the first).
    result = solve(0, 0, float('-inf'))

    # If no valid subsequence was found, return 0.
    if result == float('-inf'):
        return 0
    else:
        return result

# Test cases
def test_solution():
    assert longest_increasing_subsequence_sum_target([1, 2, 3, 4, 5], 9) == 3
    assert longest_increasing_subsequence_sum_target([4, 3, 2, 1], 10) == 0
    assert longest_increasing_subsequence_sum_target([1, 3, 2, 4, 5], 7) == 3
    assert longest_increasing_subsequence_sum_target([1, 2, 3, 4], 10) == 3
    assert longest_increasing_subsequence_sum_target([1, 2, 3, 4, 5], 15) == 5
    assert longest_increasing_subsequence_sum_target([1, 5, 2, 6, 3], 10) == 3
    assert longest_increasing_subsequence_sum_target([1, 2, 3, 4, 5], 1) == 1
    assert longest_increasing_subsequence_sum_target([10, 5, 2, 1, 6], 16) == 3
    assert longest_increasing_subsequence_sum_target([1, 2, 3, 4, 5], 0) == 0

if __name__ == "__main__":
    test_solution()