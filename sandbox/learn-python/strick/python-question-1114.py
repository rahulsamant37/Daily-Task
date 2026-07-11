# Python Question: Longest Increasing Subsequence with Gap
'''
Given an array of integers `nums` and an integer `k`, find the length of the longest increasing subsequence (LIS) such that the difference between consecutive elements in the subsequence is at least `k`.

Example:
Input: nums = [3, 10, 2, 1, 20], k = 3
Output: 3
Explanation: The longest increasing subsequence with a gap of at least 3 is [3, 10, 20] or [1, 10, 20].

Input: nums = [1, 5, 2, 4, 3], k = 2
Output: 2
Explanation: The longest increasing subsequence with a gap of at least 2 is [1, 3] or [1, 4] or [2, 4] or [3,5]
'''

# Solution
def solution():
    def longest_increasing_subsequence_with_gap(nums, k):
        """
        Finds the length of the longest increasing subsequence with a gap of at least k.

        Args:
            nums: A list of integers.
            k: The minimum difference between consecutive elements in the subsequence.

        Returns:
            The length of the longest increasing subsequence with a gap of at least k.
        """

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the length of the longest increasing subsequence ending at nums[i]
        dp = [1] * n

        # Iterate through the nums array
        for i in range(1, n):
            # Iterate through the elements before nums[i]
            for j in range(i):
                # If nums[i] is greater than nums[j] and the difference is at least k,
                # update dp[i] if including nums[i] in the subsequence ending at nums[j]
                # results in a longer subsequence.
                if nums[i] > nums[j] and nums[i] - nums[j] >= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum value in dp array is the length of the LIS with gap k
        return max(dp)

    return longest_increasing_subsequence_with_gap

# Test cases
def test_solution():
    longest_increasing_subsequence_with_gap = solution()

    # Test case 1
    nums1 = [3, 10, 2, 1, 20]
    k1 = 3
    expected1 = 3
    assert longest_increasing_subsequence_with_gap(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {longest_increasing_subsequence_with_gap(nums1, k1)}"

    # Test case 2
    nums2 = [1, 5, 2, 4, 3]
    k2 = 2
    expected2 = 2
    assert longest_increasing_subsequence_with_gap(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {longest_increasing_subsequence_with_gap(nums2, k2)}"

    # Test case 3: Empty array
    nums3 = []
    k3 = 5
    expected3 = 0
    assert longest_increasing_subsequence_with_gap(nums3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {longest_increasing_subsequence_with_gap(nums3, k3)}"

    # Test case 4: No increasing subsequence with gap
    nums4 = [1, 2, 3, 4, 5]
    k4 = 5
    expected4 = 1
    assert longest_increasing_subsequence_with_gap(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {longest_increasing_subsequence_with_gap(nums4, k4)}"

    # Test case 5: k = 0 (standard LIS)
    nums5 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    k5 = 0
    expected5 = 6
    assert longest_increasing_subsequence_with_gap(nums5, k5) == 6, f"Test Case 5 Failed: Expected {expected5}, Got {longest_increasing_subsequence_with_gap(nums5, k5)}"

    # Test case 6: All same numbers
    nums6 = [5,5,5,5,5]
    k6 = 1
    expected6 = 1
    assert longest_increasing_subsequence_with_gap(nums6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {longest_increasing_subsequence_with_gap(nums6, k6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()