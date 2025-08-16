# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest strictly increasing subsequence such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4] or [2, 3, 4, 5], both with length 4.

Input: nums = [1, 5, 2, 6, 3, 7, 4], k = 2
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 2 is [1, 2, 3, 4], with length 4.  Another possible solution is [5, 6, 7] with length 3.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_k_difference(nums, k):
        """
        Finds the length of the longest strictly increasing subsequence such that the
        difference between consecutive elements in the subsequence is at most k.

        Args:
            nums: A list of integers.
            k: The maximum allowed difference between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence with the specified difference constraint.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i].
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] > nums[j] and the difference is at most k.
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    # If so, update dp[i] if adding nums[i] to the subsequence ending at nums[j]
                    # results in a longer subsequence.
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in dp is the length of the longest increasing subsequence.
        return max(dp)

    return longest_increasing_subsequence_with_k_difference


# Test cases
def test_solution():
    lis_k = solution()
    assert lis_k([1, 3, 2, 4, 5], 1) == 4
    assert lis_k([1, 5, 2, 6, 3, 7, 4], 2) == 4
    assert lis_k([1, 2, 3, 4, 5], 0) == 1
    assert lis_k([5, 4, 3, 2, 1], 1) == 1
    assert lis_k([1, 2, 3, 4, 5], 2) == 5
    assert lis_k([10, 22, 9, 33, 21, 50, 41, 60, 80], 3) == 6
    assert lis_k([1, 1, 1, 1, 1], 1) == 1
    assert lis_k([], 5) == 0
    assert lis_k([1], 5) == 1
    assert lis_k([1, 3, 5, 2, 4], 2) == 3
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()