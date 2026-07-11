# Python Question: Longest Increasing Subsequence with Specific Sum
'''
Given an array of positive integers `nums` and a target sum `target`, find the length of the longest increasing subsequence (LIS) of `nums` whose elements sum up to `target`.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 7
Output: 3
Explanation: The longest increasing subsequence that sums to 7 is [1, 2, 4] which has length 3. Another valid subsequence is [2, 5] which has length 2.  [3,4] is also a valid subsequence of length 2.

Input: nums = [4, 3, 2, 1], target = 7
Output: 0
Explanation: There is no increasing subsequence that sums to 7.

Input: nums = [2, 4, 6, 8, 10], target = 12
Output: 2
Explanation: The longest increasing subsequence that sums to 12 is [2, 10] or [4,8], which has length 2.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_sum(nums, target):
        """
        Finds the length of the longest increasing subsequence (LIS) of `nums` whose elements sum up to `target`.

        Args:
            nums: A list of positive integers.
            target: The target sum.

        Returns:
            The length of the longest increasing subsequence that sums to `target`.
            Returns 0 if no such subsequence exists.
        """

        n = len(nums)
        # dp[i][j] stores the length of the longest increasing subsequence ending at index i with sum j.
        dp = [[0] * (target + 1) for _ in range(n)]

        for i in range(n):
            # If the current number is less than or equal to the target, we can consider it as the first element
            # of a potential LIS.
            if nums[i] <= target:
                dp[i][nums[i]] = 1

            # Iterate through all previous elements to find potential LIS endings.
            for j in range(i):
                # Iterate through all possible sums.
                for k in range(1, target + 1):
                    # If there's a LIS ending at index j with sum k and nums[i] is greater than nums[j],
                    # we can extend the LIS by adding nums[i] to it.
                    if dp[j][k] > 0 and nums[i] > nums[j] and k + nums[i] <= target:
                        dp[i][k + nums[i]] = max(dp[i][k + nums[i]], dp[j][k] + 1)

        # Find the maximum length of LIS with sum equal to the target.
        max_len = 0
        for i in range(n):
            max_len = max(max_len, dp[i][target])

        return max_len

    return longest_increasing_subsequence_with_sum
    

# Test cases
def test_solution():
    longest_increasing_subsequence_with_sum = solution()

    assert longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 7) == 3
    assert longest_increasing_subsequence_with_sum([4, 3, 2, 1], 7) == 0
    assert longest_increasing_subsequence_with_sum([2, 4, 6, 8, 10], 12) == 2
    assert longest_increasing_subsequence_with_sum([1, 3, 5, 7, 9], 16) == 3
    assert longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 1) == 1
    assert longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 0) == 0
    assert longest_increasing_subsequence_with_sum([10, 20, 30, 40, 50], 100) == 0
    assert longest_increasing_subsequence_with_sum([1, 5, 2, 4, 3], 7) == 2
    assert longest_increasing_subsequence_with_sum([1, 2, 3, 4, 5], 15) == 5
    assert longest_increasing_subsequence_with_sum([2, 3, 5, 7, 11], 17) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()