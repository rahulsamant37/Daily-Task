# Python Question: Longest Increasing Subsequence with Constraints
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) in `nums` such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence with a maximum difference of 1 is [1, 2, 3, 4] or [2,3,4,5].

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence with a maximum difference of 2 is [1, 2, 3] or [2, 4].

Input: nums = [1, 5, 2, 4, 3], k = 0
Output: 1
Explanation: The longest increasing subsequence with a maximum difference of 0 is [1], [5], [2], [4], or [3].
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_constraints(nums, k):
        """
        Finds the length of the longest increasing subsequence in nums such that the
        difference between consecutive elements in the subsequence is at most k.

        Args:
            nums: A list of integers.
            k: The maximum allowed difference between consecutive elements.

        Returns:
            The length of the longest increasing subsequence with the given constraint.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
        dp = [1] * n

        # Iterate through the array to build the dp table
        for i in range(1, n):
            for j in range(i):
                # If nums[i] > nums[j] and the difference is within the constraint,
                # update dp[i] if a longer subsequence is found
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in dp is the length of the LIS
        return max(dp)

    return longest_increasing_subsequence_with_constraints


# Test cases
def test_solution():
    func = solution()
    assert func([1, 3, 2, 4, 5], 1) == 4
    assert func([1, 5, 2, 4, 3], 2) == 3
    assert func([1, 5, 2, 4, 3], 0) == 1
    assert func([1, 2, 3, 4, 5], 1) == 5
    assert func([5, 4, 3, 2, 1], 1) == 1
    assert func([1, 1, 1, 1, 1], 0) == 1
    assert func([1, 2, 3, 5, 7, 9], 2) == 3
    assert func([10, 22, 9, 33, 21, 50, 41, 60, 80], 10) == 6
    assert func([], 5) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()