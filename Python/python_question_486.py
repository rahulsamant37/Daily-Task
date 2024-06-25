# Python Question: Longest Increasing Subsequence with a Twist
'''
Given an array of integers `nums`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at most `k`.

Example:
Input: nums = [1, 3, 2, 4, 5], k = 1
Output: 4
Explanation: The longest increasing subsequence with a difference of at most 1 is [1, 2, 3, 4] or [2, 3, 4, 5], both of length 4.

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 3
Explanation: The longest increasing subsequence with a difference of at most 2 is [1, 2, 3] or [1, 2, 4] or [1, 3, 4], all of length 3.
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_k_difference(nums, k):
        """
        Finds the length of the longest increasing subsequence with a difference of at most k.

        Args:
            nums: A list of integers.
            k: The maximum difference allowed between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence with a difference of at most k.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
        dp = [1] * n

        # Iterate through the array to build the dp table
        for i in range(1, n):
            for j in range(i):
                # If nums[i] is greater than nums[j] and the difference is at most k,
                # update dp[i] if including nums[i] in the subsequence ending at nums[j]
                # gives a longer subsequence.
                if nums[i] > nums[j] and nums[i] - nums[j] <= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in the dp table is the length of the longest increasing subsequence
        return max(dp)

    return longest_increasing_subsequence_with_k_difference

# Test cases
def test_solution():
    lis_with_k_diff = solution()

    # Test case 1
    nums1 = [1, 3, 2, 4, 5]
    k1 = 1
    expected1 = 4
    assert lis_with_k_diff(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {lis_with_k_diff(nums1, k1)}"

    # Test case 2
    nums2 = [1, 5, 2, 4, 3]
    k2 = 2
    expected2 = 3
    assert lis_with_k_diff(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {lis_with_k_diff(nums2, k2)}"

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = 0
    expected3 = 1
    assert lis_with_k_diff(nums3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {lis_with_k_diff(nums3, k3)}"

    # Test case 4
    nums4 = [5, 4, 3, 2, 1]
    k4 = 1
    expected4 = 1
    assert lis_with_k_diff(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {lis_with_k_diff(nums4, k4)}"

    # Test case 5
    nums5 = [1, 1, 1, 1, 1]
    k5 = 1
    expected5 = 1
    assert lis_with_k_diff(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {lis_with_k_diff(nums5, k5)}"

    # Test case 6
    nums6 = []
    k6 = 1
    expected6 = 0
    assert lis_with_k_diff(nums6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {lis_with_k_diff(nums6, k6)}"

    # Test case 7
    nums7 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    k7 = 10
    expected7 = 6
    assert lis_with_k_diff(nums7, k7) == 6, f"Test Case 7 Failed: Expected {expected7}, got {lis_with_k_diff(nums7, k7)}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()