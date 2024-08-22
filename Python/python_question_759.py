# Python Question: Longest Increasing Subsequence with Specific Difference
'''
Given an array of integers `nums` and an integer `diff`, find the length of the longest increasing subsequence (LIS) where the difference between consecutive elements in the subsequence is exactly `diff`.

Example:
Input: nums = [3, 0, 3, 4, 5, 6], diff = 3
Output: 4
Explanation: The longest increasing subsequence with a difference of 3 is [0, 3, 6], so the length is 3. Another one is [3, 6], so the length is 2.
Input: nums = [1, 5, 7, 8, 5, 3, 4, 2, 1], diff = -2
Output: 4
Explanation: The longest increasing subsequence with a difference of -2 is [7, 5, 3, 1], so the length is 4.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_diff(nums, diff):
        """
        Finds the length of the longest increasing subsequence (LIS) where the difference
        between consecutive elements in the subsequence is exactly `diff`.

        Args:
            nums: A list of integers.
            diff: The required difference between consecutive elements in the LIS.

        Returns:
            The length of the longest increasing subsequence with the specified difference.
        """

        # Create a dictionary to store the length of the LIS ending at each number.
        # The keys are the numbers in the input array, and the values are the lengths
        # of the LIS ending with that number.
        dp = {}

        # Iterate over the numbers in the input array.
        for num in nums:
            # If the number minus the difference is already in the dictionary,
            # it means we can extend an existing LIS.
            if num - diff in dp:
                # The length of the LIS ending at the current number is one more than
                # the length of the LIS ending at the number minus the difference.
                dp[num] = dp[num - diff] + 1
            else:
                # If the number minus the difference is not in the dictionary, it means
                # we are starting a new LIS.  The length of the LIS ending at the
                # current number is 1.
                dp[num] = 1

        # The length of the longest increasing subsequence is the maximum value in the
        # dictionary.
        if not dp:
            return 0
        return max(dp.values())

    return longest_increasing_subsequence_with_diff

# Test cases
def test_solution():
    lis_with_diff = solution()
    assert lis_with_diff([3, 0, 3, 4, 5, 6], 3) == 4
    assert lis_with_diff([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
    assert lis_with_diff([1, 2, 3, 4, 5], 1) == 5
    assert lis_with_diff([1, 2, 3, 4, 5], 0) == 1
    assert lis_with_diff([1, 3, 5, 7, 9], 2) == 5
    assert lis_with_diff([5, 4, 3, 2, 1], -1) == 5
    assert lis_with_diff([5, 4, 3, 2, 1], 1) == 1
    assert lis_with_diff([1, 1, 1, 1, 1], 0) == 5
    assert lis_with_diff([1, 1, 1, 1, 1], 1) == 1
    assert lis_with_diff([], 1) == 0
    assert lis_with_diff([7, 4, 10, 4, 8, 8, 3, 0, 5, 1, 8, 6, 9], 1) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()