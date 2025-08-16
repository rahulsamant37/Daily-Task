# Python Question: Longest Increasing Subsequence with Limited Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is less than or equal to `diff`.

Example:
Input: nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], diff = 2
Output: 4
Explanation: One possible LIS with difference <= 2 is [1, 2, 3, 5].  Another is [1, 1, 2, 3]. The length is 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_difference(nums, diff):
        """
        Finds the length of the longest increasing subsequence with a limited difference.

        Args:
            nums: A list of integers.
            diff: The maximum allowed difference between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence with the specified difference constraint.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
        dp = [1] * n

        # Iterate through the array to build the dp table
        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] > nums[j] and the difference is within the limit
                if nums[i] > nums[j] and nums[i] - nums[j] <= diff:
                    # Update dp[i] if a longer subsequence is found
                    dp[i] = max(dp[i], dp[j] + 1)

        # Return the maximum value in the dp table
        return max(dp)

    return longest_increasing_subsequence_with_difference
    # Test cases
def test_solution():
    lis_with_diff = solution()
    assert lis_with_diff([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 2) == 4
    assert lis_with_diff([1, 2, 3, 4, 5], 1) == 2
    assert lis_with_diff([5, 4, 3, 2, 1], 1) == 1
    assert lis_with_diff([1, 5, 2, 4, 3], 2) == 3
    assert lis_with_diff([1, 5, 2, 4, 3], 1) == 2
    assert lis_with_diff([], 2) == 0
    assert lis_with_diff([1], 2) == 1
    assert lis_with_diff([1, 1, 1, 1, 1], 0) == 1
    assert lis_with_diff([1, 2, 3, 4, 5], 0) == 1
    assert lis_with_diff([1, 3, 5, 2, 4, 6], 2) == 4
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()